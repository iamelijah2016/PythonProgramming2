# super() method

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def display1(self):
        print("Username:", self.username)
        print("Password", self.password)


class Admin(User):
    # overriding the init of class User
    def __init__(self, username, password, code):
        self.code = code
        # super() returns an object of the class User
        super().__init__(username, password)

    def display3(self):
        super().display1()
        print("Code:", self.code)


a_1 = Admin("leslie2001", "password 1234", "2468")
a_1.display3()
