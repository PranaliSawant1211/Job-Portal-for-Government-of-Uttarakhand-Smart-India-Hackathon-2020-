from flask import Flask, render_template, request,redirect, url_for,g,session
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
from flask import flash
from passlib.hash import sha256_crypt
from werkzeug.security import generate_password_hash, check_password_hash
from passlib.apps import custom_app_context as pwd_context
from functools import wraps


app = Flask(__name__)
app.config['MySQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sih'

mysql = MySQL(app)

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first","error")
            return redirect(url_for('login'))

    return wrap


def login_required_company(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first","error")
            return redirect(url_for('login'))

    return wrap

@app.route('/')
def home():
	session.clear()
	return render_template('index.html')

@app.route('/create_account', methods = ['GET', 'POST'])
def create_account():
    choice = request.form.get('role')
    if request.method == 'POST':
        if(choice == "candidate" ):
            cursor = mysql.connection.cursor()
            uname = request.form.get('uname')
            cursor.execute("SELECT * FROM register WHERE uname = %s", [uname])
            if cursor.fetchone() is not None:
                flash("The username is already taken...", "error")
                return render_template('create-account.html')
            else:
                fname = request.form.get('fname')
                mname = request.form.get('mname')
                lname = request.form.get('lname')
                email = request.form.get('email')
                dob = request.form.get('dob')
                phone = request.form.get('phone')
                address = request.form.get('address')
                state = request.form.get('state')
                city = request.form.get('city')
                gender = request.form.get('gender')
                description = request.form.get('description')
                password = request.form.get('password')
                password = pwd_context.hash(password)
                
   

                sql_insert_blob_query = """ INSERT INTO register(uname, fname, mname, lname,phone, email, dob, address, sex, city, state, password, descr) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                cursor.execute(sql_insert_blob_query,(uname, fname, mname, lname,phone, email, dob, address, gender, city, state, password, description))
                mysql.connection.commit()
                cursor.close()

                flash('You are now registered and can log in', 'success')
                return redirect(url_for('login'))

        elif(choice == "company"):
            cursor = mysql.connection.cursor()
            compid = request.form.get('compid')
            cursor.execute("SELECT * FROM company_register WHERE compid = %s", [compid])
            if cursor.fetchone() is not None:
                flash("The username is already taken...", "error")
                return render_template('create-account.html')
            else:
                compname = request.form.get('compname')
                estdate = request.form.get('estdate')
                compaddress = request.form.get('compaddress')
                compemail = request.form.get('compemail')
                compurl = request.form.get('compurl')
                compphone = request.form.get('compphone')
                compdescription = request.form.get('compdescription')
                comppassword = request.form.get('comppassword')
                comppassword = pwd_context.hash(comppassword)
        
                sql_insert_blob_query = """ INSERT INTO company_register(compid, compname, doe, compaddress, compemail, compurl, compphone, compdescription, comppassword) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                cursor.execute(sql_insert_blob_query,(compid, compname, estdate, compaddress, compemail, compurl, compphone, compdescription, comppassword))
                mysql.connection.commit()
                cursor.close()

                flash('You are now registered and can log in', 'success')
                return redirect(url_for('login'))

    return render_template('create-account.html')


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

@app.route('/login', methods = ['GET', 'POST'])
# @login_required
def login():
    if request.method == 'POST':
        session.pop('username', None)
        session.pop('comp_username', None)
        cursor = mysql.connection.cursor()
        choice = request.form.get('role')
        if(choice == "candidate"):
            uname = request.form.get('uname')
            password = request.form.get('password')
            result = cursor.execute("SELECT * FROM register WHERE uname = %s", [uname])
            if result > 0:
                data = cursor.fetchone()
                password_db = data[11]
                if (pwd_context.verify(password, password_db)):
                    session['logged_in'] = True
                    session['username'] = uname
                    flash('You are now logged in', 'success')
                    return redirect(url_for('cdashboard'))
                else:
                    flash('Invalid Login', 'error')
                    return render_template('login.html')
                cursor.close()
            else:
                flash('User not found', 'error')
                return render_template('login.html')

        elif(choice == "company"):
            uname = request.form.get('uname')
            password = request.form.get('password')
            result = cursor.execute("SELECT * FROM company_register WHERE compid = %s", [uname])
            if result > 0:
                data = cursor.fetchone()
                password_db = data[8]
                if (pwd_context.verify(password, password_db)):
                    session['logged_in'] = True
                    session['comp_username'] = uname
                    flash('You are now logged in', 'success')
                    return redirect(url_for('companydetails'))
                else:
                    flash('Invalid Login', 'error')
                    return render_template('login.html')
                cursor.close()
            else:
                flash('User not found', 'error')
                return render_template('login.html')

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

@app.route('/logout_company')
@login_required_company
def logout_company():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


@app.route('/cdashboard')
@login_required
def cdashboard():
    uname = session['username'] 
    cursoredu = mysql.connection.cursor()
    result1 = cursoredu.execute("SELECT * FROM edu WHERE uname = %s", [uname])
    edudata = cursoredu.fetchall()
    cursoredu.close()
    cursorskl = mysql.connection.cursor()
    result2 = cursorskl.execute("SELECT * FROM skills WHERE uname = %s", [uname])
    skdata = cursorskl.fetchall()
    cursorskl.close()

    cursorlnk = mysql.connection.cursor()
    result3 = cursorlnk.execute("SELECT * FROM link WHERE uname = %s", [uname])
    lnkdata = cursorlnk.fetchall()
    cursorskl.close()

    cursorlnk = mysql.connection.cursor()
    result4 = cursorlnk.execute("SELECT * FROM work WHERE uname = %s", [uname])
    workdata = cursorlnk.fetchall()
    cursorskl.close()

    cursorlnk = mysql.connection.cursor()
    result4 = cursorlnk.execute("SELECT * FROM register WHERE uname = %s", [uname])
    Mdata = cursorlnk.fetchall()
    cursorskl.close()
    return render_template('candidatedashboard.html', students=edudata,detail=Mdata, tlinks=lnkdata, tskills=skdata, twork=workdata)


@app.route('/cdashboardwork')
@login_required
def cdashboardwork():
    uname = session['username'] 
    cursoredu = mysql.connection.cursor()
    result1 = cursoredu.execute("SELECT * FROM edu WHERE uname = %s", [uname])
    edudata = cursoredu.fetchall()
    cursoredu.close()
    cursorskl = mysql.connection.cursor()
    result2 = cursorskl.execute("SELECT * FROM skills WHERE uname = %s", [uname])
    skdata = cursorskl.fetchall()
    cursorskl.close()
    cursorlnk = mysql.connection.cursor()
    result3 = cursorlnk.execute("SELECT * FROM link WHERE uname = %s", [uname])
    lnkdata = cursorlnk.fetchall()
    cursorskl.close()
    cursorlnk = mysql.connection.cursor()
    result4 = cursorlnk.execute("SELECT * FROM work WHERE uname = %s", [uname])
    workdata = cursorlnk.fetchall()
    cursorskl.close()

    cursorlnk = mysql.connection.cursor()
    result4 = cursorlnk.execute("SELECT * FROM register WHERE uname = %s", [uname])
    Mdata = cursorlnk.fetchall()
    cursorskl.close()
    print(Mdata)
    return render_template('candidatedashboard.html', scroll='worktag',detail=Mdata, students=edudata, twork=workdata, tlinks=lnkdata, tskills=skdata)



@app.route('/cdashboardedu')
@login_required
def cdashboardedu():
    uname = session['username'] 
    cursoredu = mysql.connection.cursor()
    result1 = cursoredu.execute("SELECT * FROM edu WHERE uname = %s", [uname])
    edudata = cursoredu.fetchall()
    cursoredu.close()
    cursorskl = mysql.connection.cursor()
    result2 = cursorskl.execute("SELECT * FROM skills WHERE uname = %s", [uname])
    skdata = cursorskl.fetchall()
    cursorskl.close()
    cursorlnk = mysql.connection.cursor()
    result3 = cursorlnk.execute("SELECT * FROM link WHERE uname = %s", [uname])
    lnkdata = cursorlnk.fetchall()
    cursorskl.close()
    cursorlnk = mysql.connection.cursor()
    result4 = cursorlnk.execute("SELECT * FROM work WHERE uname = %s", [uname])
    workdata = cursorlnk.fetchall()
    cursorskl.close()

    cursorlnk = mysql.connection.cursor()
    result4 = cursorlnk.execute("SELECT * FROM register WHERE uname = %s", [uname])
    Mdata = cursorlnk.fetchall()
    cursorskl.close()
    return render_template('candidatedashboard.html', scroll='educationtag',detail=Mdata, students=edudata, twork=workdata, tlinks=lnkdata, tskills=skdata)

@app.route('/cdashboardlink')
@login_required
def cdashboardlink():
    uname = session['username'] 
    cursoredu = mysql.connection.cursor()
    result1 = cursoredu.execute("SELECT * FROM edu WHERE uname = %s", [uname])
    edudata = cursoredu.fetchall()
    cursoredu.close()
    cursorskl = mysql.connection.cursor()
    result2 = cursorskl.execute("SELECT * FROM skills WHERE uname = %s", [uname])
    skdata = cursorskl.fetchall()
    cursorskl.close()
    cursorlnk = mysql.connection.cursor()
    result3 = cursorlnk.execute("SELECT * FROM link WHERE uname = %s", [uname])
    lnkdata = cursorlnk.fetchall()
    cursorskl.close()
    cursorlnk = mysql.connection.cursor()
    result4 = cursorlnk.execute("SELECT * FROM work WHERE uname = %s", [uname])
    workdata = cursorlnk.fetchall()
    cursorskl.close()
    print(lnkdata)

    cursorlnk = mysql.connection.cursor()
    result4 = cursorlnk.execute("SELECT * FROM register WHERE uname = %s", [uname])
    Mdata = cursorlnk.fetchall()
    cursorskl.close()
    return render_template('candidatedashboard.html', scroll='linktag',detail=Mdata, students=edudata, twork=workdata, tlinks=lnkdata, tskills=skdata)

@app.route('/cdashboardskill')
@login_required
def cdashboardskill():
    uname = session['username'] 
    cursoredu = mysql.connection.cursor()
    result1 = cursoredu.execute("SELECT * FROM edu WHERE uname = %s", [uname])
    edudata = cursoredu.fetchall()
    cursoredu.close()
    cursorskl = mysql.connection.cursor()
    result2 = cursorskl.execute("SELECT * FROM skills WHERE uname = %s", [uname])
    skdata = cursorskl.fetchall()
    cursorskl.close()
    cursorlnk = mysql.connection.cursor()
    result3 = cursorlnk.execute("SELECT * FROM link WHERE uname = %s", [uname])
    lnkdata = cursorlnk.fetchall()
    cursorskl.close()
    cursorlnk = mysql.connection.cursor()
    result4 = cursorlnk.execute("SELECT * FROM work WHERE uname = %s", [uname])
    workdata = cursorlnk.fetchall()
    cursorskl.close()
    cursorlnk = mysql.connection.cursor()
    result4 = cursorlnk.execute("SELECT * FROM register WHERE uname = %s", [uname])
    Mdata = cursorlnk.fetchall()
    cursorskl.close()
    
    return render_template('candidatedashboard.html', scroll='skilltag',detail=Mdata, students=edudata, twork=workdata, tlinks=lnkdata, tskills=skdata)
@app.route('/cdashboarddetail')
@login_required
def cdashboarddetail():
    uname = session['username'] 
    cursoredu = mysql.connection.cursor()
    result1 = cursoredu.execute("SELECT * FROM edu WHERE uname = %s", [uname])
    edudata = cursoredu.fetchall()
    cursoredu.close()
    cursorskl = mysql.connection.cursor()
    result2 = cursorskl.execute("SELECT * FROM skills WHERE uname = %s", [uname])
    skdata = cursorskl.fetchall()
    cursorskl.close()
    cursorlnk = mysql.connection.cursor()
    result3 = cursorlnk.execute("SELECT * FROM link WHERE uname = %s", [uname])
    lnkdata = cursorlnk.fetchall()
    cursorskl.close()
    cursorlnk = mysql.connection.cursor()
    result4 = cursorlnk.execute("SELECT * FROM work WHERE uname = %s", [uname])
    workdata = cursorlnk.fetchall()
    cursorskl.close()
    cursorlnk = mysql.connection.cursor()
    result4 = cursorlnk.execute("SELECT * FROM register WHERE uname = %s", [uname])
    Mdata = cursorlnk.fetchall()
    cursorskl.close()
    
    return render_template('candidatedashboard.html', scroll='detailtag',detail=Mdata, students=edudata, twork=workdata, tlinks=lnkdata, tskills=skdata)




@app.route('/candidatedetails')
def candidatedetails():
	
    uname = session['username'] 
    cursoredu = mysql.connection.cursor()
    result1 = cursoredu.execute("SELECT * FROM edu WHERE uname = %s", [uname])
    edudata = cursoredu.fetchall()
    cursoredu.close()
    cursorskl = mysql.connection.cursor()
    result2 = cursorskl.execute("SELECT * FROM skills WHERE uname = %s", [uname])
    skdata = cursorskl.fetchall()
    cursorskl.close()
    cursorlnk = mysql.connection.cursor()
    result3 = cursorlnk.execute("SELECT * FROM link WHERE uname = %s", [uname])
    lnkdata = cursorlnk.fetchall()
    cursorskl.close()
    cursorlnk = mysql.connection.cursor()
    result4 = cursorlnk.execute("SELECT * FROM work WHERE uname = %s", [uname])
    workdata = cursorlnk.fetchall()
    cursorskl.close()
    cursorlnk = mysql.connection.cursor()
    result4 = cursorlnk.execute("SELECT * FROM register WHERE uname = %s", [uname])
    Mdata = cursorlnk.fetchall()
    cursorskl.close()
    return render_template('candidatedetails.html',detail=Mdata, students=edudata, twork=workdata, tlinks=lnkdata, tskills=skdata)

@app.route('/candidatelist')
def candidatelist():
	return render_template('candidatelist.html')

@app.route('/companylist')
def companylist():
	return render_template('companylist.html')

@app.route('/joblist')
def joblist():
	return render_template('joblist.html')

#**************************** details operations start ****************************
@app.route('/updatedetails', methods = ['POST'])
def updatedetails():
    if request.method == "POST":
        fname = request.form.get('fname')
        mname = request.form.get('mname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        dob = request.form.get('dob')
        phone = request.form.get('phone')
        address = request.form.get('address')
        state = request.form.get('state')
        city = request.form.get('city')
        gender = request.form.get('gender')
        description = request.form.get('description')
        uname = session['username'] 
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE register
               SET fname=%s, mname=%s, lname=%s,phone=%s, email=%s, dob=%s, address=%s, sex=%s, city=%s, state=%s, descr=%s
               WHERE uname=%s
            """, (fname, mname, lname,phone, email, dob, address, gender, city, state, description,uname))
        mysql.connection.commit()
        return redirect(url_for('cdashboarddetail'))
        
                
#**************************** Details operations end****************************


#**************************** Education operations start ****************************
@app.route('/insertedu', methods = ['POST'])
def insertedu():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        Titleedu = request.form['Titleedu']
        degree = request.form['Degreeedu']
        inst = request.form['Instedu']
        year = request.form['Yearedu']
        uname = session['username'] 
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `edu` (`uname`, `title`, `degree`, `institute`, `year`) VALUES (%s, %s, %s, %s, %s)", (uname, Titleedu, degree, inst, year))
        mysql.connection.commit()
        return redirect(url_for('cdashboardedu'))





@app.route('/deleteedu/<string:id_data>', methods = ['GET'])
def deleteedu(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM edu WHERE srno=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('cdashboardedu'))





@app.route('/updateedu',methods=['POST','GET'])
def updateedu():

    if request.method == 'POST':
        Titleedu = request.form['Titleedu']
        degree = request.form['Degreeedu']
        inst = request.form['Instedu']
        year = request.form['Yearedu']
        srno = request.form['srno']
        uname = session['username'] 
        cur = mysql.connection.cursor()
        s=(Titleedu, degree, inst, year, srno)
        print(s)
        cur.execute("""
               UPDATE edu
               SET title=%s, degree=%s, institute=%s, year=%s
               WHERE srno=%s
            """, (Titleedu, degree, inst, year, srno))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('cdashboardedu'))
#**************************** Education operations end****************************


#****************************skill operations start****************************
@app.route('/insertskill', methods = ['POST'])
def insertskill():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        percent = request.form['prcnt']
        skname = request.form['skname']
        uname = session['username'] 
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `skills` (`uname`, `skname`, `percent`)VALUES (%s, %s, %s)", (uname, skname, percent))
        mysql.connection.commit()
        return redirect(url_for('cdashboardskill'))





@app.route('/deleteskill/<string:id_data>', methods = ['GET'])
def deleteskill(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM skills WHERE srno=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('cdashboardskill'))





@app.route('/updateskill',methods=['POST','GET'])
def updateskill():

    if request.method == 'POST':
        percent = request.form['prcnt']
        skname = request.form['skname']
        uname = session['username'] 
        srno = request.form['srno']
        cur = mysql.connection.cursor()
        print((skname, percent, uname))
        cur.execute("""
               UPDATE skills
               SET skname=%s, percent=%s
               WHERE srno=%s
            """, (skname, percent, srno))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('cdashboardskill'))

#****************************skill operations end****************************

#****************************Work operations end****************************
@app.route('/insertwork', methods = ['POST'])
def insertwork():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        jobtitle = request.form['jobtitle']
        org = request.form['org']
        duration = request.form['dur']
        yearwork = request.form['yearwork']
        uname = session['username'] 
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `work` (`uname`, `jobtitle`, `org`, `duration`, `year`) VALUES (%s, %s, %s, %s, %s)", (uname, jobtitle, org, duration, yearwork))
        mysql.connection.commit()
        return redirect(url_for('cdashboardwork'))





@app.route('/deletework/<string:id_data>', methods = ['GET'])
def deletework(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM work WHERE srno=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('cdashboardwork'))





@app.route('/updatework',methods=['POST','GET'])
def updatework():

    if request.method == 'POST':
        jobtitle = request.form['jobtitle']
        org = request.form['org']
        duration = request.form['dur']
        yearwork = request.form['yearwork']
        srno = request.form['srno']
        uname = session['username'] 
        cur = mysql.connection.cursor()
        print((jobtitle, org, duration, yearwork, srno))
        cur.execute("""
               UPDATE work
               SET jobtitle=%s, org=%s, duration=%s, year=%s
               WHERE srno=%s
            """, (jobtitle, org, duration, yearwork, srno))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('cdashboardwork'))
#**************************** Work operations end****************************



#****************************link operations start****************************

@app.route('/insertlink', methods = ['POST'])
def insertlink():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        value = request.form['value']
        link = request.form['link']
        uname = session['username'] 
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `link` (`link`, `value`, `uname`)VALUES (%s, %s, %s)", (link, value, uname))
        mysql.connection.commit()
        return redirect(url_for('cdashboardlink'))





@app.route('/deletelink/<string:id_data>', methods = ['GET'])
def deletelink(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM link WHERE srno=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('cdashboardlink'))





@app.route('/updatelink',methods=['POST','GET'])
def updatelink():

    if request.method == 'POST':
        value = request.form['value']
        link = request.form['link']
        uname = session['username'] 
        srno = request.form['srno']
        cur = mysql.connection.cursor()
        print((link, value, uname,srno))
        cur.execute("""
               UPDATE link
               SET link=%s, value=%s
               WHERE srno=%s
            """, (link, value, srno))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('cdashboardlink'))
#****************************link operations end****************************



@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contactform', methods=['GET','POST'])
def contactform():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form.get('name')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        msg_subject = request.form.get('msg_subject')
        message = request.form.get('message') 
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `contact` (`name`, `email`, `phone_number`, `msg_subject`, `message`) VALUES (%s, %s, %s, %s, %s)", (name, email, phone_number, msg_subject, message))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('contactform'))
    return render_template('contact.html') 


@app.route('/addblog', methods = ['GET', 'POST'])
def addblog():
    if request.method == 'POST':
        cursor = mysql.connection.cursor()

        pname = request.form.get('pname')
        email = request.form.get('email')
        dob = request.form.get('dob')
        phone = request.form.get('phone')
        blogg = request.form.get('blogg')

        sql_insert_blob_query = """ INSERT INTO blog(pname, email,dob,phone, blogg) VALUES (%s,%s,%s,%s,%s)"""
        cursor.execute(sql_insert_blob_query,(pname, email, dob, phone, blogg ))
        mysql.connection.commit()
        cursor.close()

    return render_template('addblog.html')

@app.route('/companydetails')
@login_required_company
def companydetails():
    return render_template('companydetails.html')

if __name__ == '__main__':
	app.secret_key =  'mahesh'
	app.run(debug=True)
