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

@app.route('/')
def home():
	session.clear()
	return render_template('index.html')

@app.route('/create_account', methods = ['GET', 'POST'])
def create_account():
	if request.method == 'POST':
		cursor = mysql.connection.cursor()
		uname = request.form.get('uname')
		cursor.execute("SELECT * FROM register WHERE uname = %s", [uname])
		if cursor.fetchone() is not None:
			flash("That username is already taken...", "error")
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
			description = request.form.get('fname')
			password = request.form.get('password')
			password = pwd_context.hash(password)
			profpic = request.files['profpic']
		
		

		sql_insert_blob_query = """ INSERT INTO register(uname, fname, mname, lname,phone, email, dob, address, sex, city, state, password, profpic, descr) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
		cursor.execute(sql_insert_blob_query,(uname, fname, mname, lname,phone, email, dob, address, gender, city, state, password, profpic, description))
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
        cursor = mysql.connection.cursor()
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
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
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

    return render_template('candidatedashboard.html', students=edudata, tskills=skdata)

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
    result3 = cursorlnk.execute("SELECT * FROM links WHERE uname = %s", [uname])
    lnkdata = cursorlnk.fetchall()
    cursorskl.close()
    return render_template('candidatedashboard.html', scroll='educationtag', students=edudata, tskills=skdata, ldata=lnkdata)

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
    result3 = cursorlnk.execute("SELECT * FROM links WHERE uname = %s", [uname])
    lnkdata = cursorlnk.fetchall()
    cursorskl.close()
    return render_template('candidatedashboard.html', scroll='linktag', students=edudata, tskills=skdata, ldata=lnkdata)

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
    result3 = cursorlnk.execute("SELECT * FROM links WHERE uname = %s", [uname])
    lnkdata = cursorlnk.fetchall()
    cursorskl.close()
    return render_template('candidatedashboard.html', scroll='skilltag', students=edudata, tskills=skdata, ldata=lnkdata)


@app.route('/candidatedetails')
def candidatedetails():
	return render_template('candidatedetails.html')

@app.route('/candidatelist')
def candidatelist():
	return render_template('candidatelist.html')

@app.route('/companylist')
def companylist():
	return render_template('companylist.html')

@app.route('/joblist')
def joblist():
	return render_template('joblist.html')

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

#****************************link operations start****************************


@app.route('/updatelink',methods=['POST','GET'])
def updatelink():

    if request.method == 'POST':
        fblink = request.form['fblink']
        llink = request.form['llink']
        insta = request.form['insta']
        dribble = request.form['dlink']
        uname = session['username'] 
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE skills
               SET skname=%s, percent=%s
               WHERE uname=%s and skname=%s and percent=%s
            """, (skname, percent, uname, skname, percent,))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('cdashboardlink'))

#****************************link operations end****************************



if __name__ == '__main__':
	app.secret_key =  'mahesh'
	app.run(debug=True)
