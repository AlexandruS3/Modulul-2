
                                    #SignUp

import re

username = input("write new username: ")
email = input("Your email address: ")
password = input ("write new password: ")

def signUp(username, email, password):
    if type(username) and type(email) and type(password) == str:
        if len(username) >= 5 or len(username) <= 12:
            if check_alphanumeric(username) == True:
                if "a" and "." in email:
                    if len(password)>8:
                        result = {('username', username), ('email', email), ('password', password)}
                        return print(result)
                    else:
                        print ("the password must contain at least 8 characters")
                else:
                    print ("invalid format")
            else:
                print("username must contain latin letters and numbers")
        else:
            print("the user name must contain at least 5 and at most 12 characters")
    else:
        print ("ivalid format")  
    
                # checking if username contain latin letters and digits
def check_alphanumeric(username):
    return bool(re.match(r'^[a-zA-Z0-9]+$', username))

signUp(username,email,password)
