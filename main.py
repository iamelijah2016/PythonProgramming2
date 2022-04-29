# Overriding method

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def display1(self):
        print("Parent class/User")
        print("Username:", self.username)
        print("Password", self.password)


class Admin(User):
    # overriding the init of class User
    def __init__(self, username, password, code):
        self.code = code
        User.__init__(self, username, password)

    def display3(self):
        print("Subclass/Admin")
        print("Username:", self.username)
        print("Password:", self.password)
        print("Code:", self.code)


u_45 = User("pretty_jun25", "otherpassword287")
a_1 = Admin("leslie2001", "password 1234", "2468")

u_45.display1()
a_1.display3()