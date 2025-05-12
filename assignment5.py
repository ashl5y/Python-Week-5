class Food:
    def __init__(self, name, texture):
        self.name = name
        self.texture = texture
    def about(self):
        print(f"{self.name} is edible and is {self.texture}")

class Carbohydrate(Food):
    def __init__ (self, name, texture, type):
        super().__init__(name, texture)
        self.type = type
    def about(self):
        print(f"{self.name} is {self.texture},is edible and is a {self.type}")

meal = Carbohydrate("Maize", "hard", "cereal")
meal.about()