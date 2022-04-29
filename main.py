class ClubMembers:
    def __init__(self, name, birthday, age, favorite_food, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favorite_food = favorite_food
        self.goal = goal

    def display1(self):
        print("Name:", self.name)
        print("Birthday:", self.birthday)
        print("Age:", self.age)
        print("Favorite food:", self.favorite_food)
        print("Goal:", self.goal)


class ClubOfficers(ClubMembers):
    def __init__(self, name, birthday, age, favorite_food, goal, position):
        self.position = position
        # # my solution using super() method
        # super().__init__(name, birthday, age, favorite_food, goal)

        # the solution
        ClubMembers.__init__(self, name, birthday, age, favorite_food, goal)

    def display2(self):
        # # my solution using super() method
        # super().display1()
        # print("Position:", self.position)

        # the solution
        print("Name:", self.name)
        print("Birthday:", self.birthday)
        print("Age:", self.age)
        print("Favorite food:", self.favorite_food)
        print("Goal:", self.goal)
        print("Position:", self.position)


m_1 = ClubMembers("Tom", "January 16", "14", "Ice cream", "To be happy")
o_4 = ClubOfficers("Vera", "June 22", "16", "Beef stroganoff", "To be the world's greatest chef", "Treasurer")

m_1.display1()
o_4.display2()