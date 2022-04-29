class Costumers:
    def __init__(self, name, beverage, food, total):
        self.name = name
        self.beverage = beverage
        self.food = food
        self.total = total

    greeting = "Welcome to Coffee Palace"


c_1 = Costumers("Nate", "Espresso", "Pastrami on rye", 220)
c_2 = Costumers("Elaine", "Strawberry frappuccino", "Tuna wrap", 270)
c_3 = Costumers("Samirah", "Iced caffe latte", "Cinnamon roll", 225)
c_4 = Costumers("Jerry", "Caramel macchiato", "Glazed doughnut", 230)
c_5 = Costumers("Paz", "Iced tea", "Blueberry pancakes", 315)

print(Costumers.greeting)
print(c_2.name)
print(c_2.beverage)
print(c_2.food)
print(c_2.total)
print(c_4.name)
print(c_4.beverage)
print(c_4.food)
print(c_4.total)