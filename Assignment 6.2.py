class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print("Name:", self.name)
        print("Age:", self.age)

    def get_info(self):
        print("Coat Color:", self.coat_color)

class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def special_ability(self):
        print("Special Ability: Jack Russell Terriers are known for their high energy and agility.")

class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def special_ability(self):
        print("Special Ability: Bulldogs are known for their gentle and friendly nature.")

# Create objects and implement the functionalities
dog1 = JackRussellTerrier("Buddy", 5, "White and Brown")
dog1.description()
dog1.get_info()
dog1.special_ability()
print()

dog2 = Bulldog("Max", 3, "Fawn")
dog2.description()
dog2.get_info()
dog2
