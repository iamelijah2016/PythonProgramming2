# Inheritance

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def display1(self):
        print("(parent class/User) Username:", self.username, "password:", self.password)


class Admin(User):
    def display2(self):
        print("(subclass/Admin) Username:", self.username, "password:", self.password)


a_1 = Admin("leslie2001", "password1234")
u_45 = User("pretty_jun25", "otherpassword287")

u_45.display1()
a_1.display2()
