import re
def checkPassword(password:str)->str:

    if (len(password)<=16):
        return "Weak Password. Password Should be Greater Than 15 Characters"
    elif not re.search("[a-z]", password):
        return "Weak Password. Try using Small Letters."
    elif not re.search("[A-Z]", password):
        return "Weak Password. Try using Capital Letters."
    elif not re.search("[0-9]", password):
        return "Weak Password. Try adding Digits."
    elif not re.search("[_@$]" , password):
        return "Weak Password, Try using Special Characters."
    
    else:
        return "Strong Password"