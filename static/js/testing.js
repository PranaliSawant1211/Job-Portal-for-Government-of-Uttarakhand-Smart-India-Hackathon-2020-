function universal_validation(form){
    
    var choice = document.forms["registration"]["role"];
    if(choice ==="candidate")
    {
        return candidate_validation();
    }
    else(choice ==="company")
    {
        return company_validation();
    }
}

function candidate_validation(){
    var fname = document.forms["registration"]["fname"];
    var mname = document.forms["registration"]["mname"];
    var lname = document.forms["registration"]["lname"];               
    var email = document.forms["registration"]["email"];    
    var phone = document.forms["registration"]["phone"];  
    var dob =  document.forms["registration"]["dob"];  
    var uname = document.forms["registration"]["uname"];  
    var address = document.forms["registration"]["address"];
    var state = document.forms["registration"]["state"]; 
    var city = document.forms["registration"]["city"];
    var gender = document.forms["registration"]["gender"];
    var password = document.forms["registration"]["password"];
   
    if (fname.value === "")                                  
    { 
        window.alert("Please enter your first name."); 
        fname.focus(); 
        return false; 
    } 
    if (mname.value === "")                                  
    { 
        window.alert("Please enter your middle name."); 
        mname.focus(); 
        return false; 
    } 
    if (lname.value === "")                                  
    { 
        window.alert("Please enter your last name."); 
        lname.focus(); 
        return false; 
    } 
   
    if (email.value === "")                               
    { 
        window.alert("Please enter a valid e-mail address."); 
        email.focus(); 
        return false; 
    } 
       
    if (dob.value === "")                                   
    { 
        window.alert("Please enter your DOB ."); 
        dob.focus(); 
        return false; 
    } 
   
    if (phone.value === "")                           
    { 
        window.alert("Please enter your telephone number."); 
        phone.focus(); 
        return false; 
    } 
   
    if (password.value === "")                        
    { 
        window.alert("Please enter your password"); 
        password.focus(); 
        return false; 
    } 
   
    if (uname.value === "")                  
    { 
        alert("Please enter your username."); 
        uname.focus(); 
        return false; 
    } 

    if (address.value === "")                  
    { 
        alert("Please enter your address."); 
        address.focus(); 
        return false; 
    } 

    if (state.value === "")                  
    { 
        alert("Please select your state."); 
        state.focus(); 
        return false; 
    } 

    if (city.value === "")                  
    { 
        alert("Please enter your city."); 
        city.focus(); 
        return false; 
    } 

    if (gender.value === "")                  
    { 
        alert("Please select your gender."); 
        gender.focus(); 
        return false; 
    } 
    
    var atposition=email.indexOf("@");  
    var dotposition=email.lastIndexOf(".");  
    if (atposition<1 || dotposition<atposition+2 || dotposition+2>=email.length)
    {  
        alert("Please enter a valid e-mail address \n atpostion:"+atposition+"\n dotposition:"+dotposition);
        email.focus();  
        return false;  
    }

    if(password.length<6)
    {  
        alert("Password must be at least 6 characters long.");
        password.focus();  
        return false;
    } 

    if (isNaN(phone))
    {  
        alert("Enter Numeric value only"); 
        phone.focus(); 
        return false;
    } 

    return true;
}

function company_validation(){
    var compname = document.forms["registration"]["compname"];
    var compid = document.forms["registration"]["compid"];
    var estdate = document.forms["registration"]["estdate"];               
    var compemail = document.forms["registration"]["compemail"];    
    var compphone = document.forms["registration"]["compphone"];  
    var compurl =  document.forms["registration"]["compurl"];  
    var comppassword = document.forms["registration"]["comppassword"];  
    var compaddress = document.forms["registration"]["compaddress"];

    if (compid.value === "")                                  
    { 
        window.alert("Please enter your company id."); 
        compid.focus(); 
        return false; 
    }

    if (compname.value === "")                                  
    { 
        window.alert("Please enter your company name."); 
        compname.focus(); 
        return false; 
    }

    if (estdate.value === "")                                  
    { 
        window.alert("Please enter your establishment date."); 
        estdate.focus(); 
        return false; 
    }

    if (compemail.value === "")                                  
    { 
        window.alert("Please enter a valid e-mail address."); 
        compemail.focus(); 
        return false; 
    }

    if (compphone.value === "")                                  
    { 
        window.alert("Please enter your telephone number ."); 
        compphone.focus(); 
        return false; 
    }

    if (compurl.value === "")                                  
    { 
        window.alert("Please enter your company url."); 
        compurl.focus(); 
        return false; 
    }

    if (compaddress.value === "")                                  
    { 
        window.alert("Please enter your address."); 
        compaddress.focus(); 
        return false; 
    }

    if (comppassword.value === "")                                  
    { 
        window.alert("Please enter your password."); 
        compassword.focus(); 
        return false; 
    }

    var atposition=compemail.indexOf("@");  
    var dotposition=ccompemail.lastIndexOf(".");  
    if (atposition<1 || dotposition<atposition+2 || dotposition+2>=compemail.length)
    {  
        alert("Please enter a valid e-mail address \n atpostion:"+atposition+"\n dotposition:"+dotposition);
        compemail.focus();  
        return false;  
    }

    if(comppassword.length<6)
    {  
        alert("Password must be at least 6 characters long.");
        comppassword.focus();  
        return false;
    } 

    if (isNaN(compphone))
    {  
        alert("Enter Numeric value only"); 
        compphone.focus(); 
        return false;
    }

    return true;
}