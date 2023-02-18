

def signin(username,password):
    register = [{"username":"john", "password":"travolta"},
                {"username":"boris", "password":"johnos"},
                {"username":"eva", "password":"mendez"}]
    for i in register:
        if i["username"] == username and i["password"] == password:
            return i
        else:
            return None




signin("john","travoljta")

