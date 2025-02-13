class Animal():
    def __init__(self, name):
        self.name = name

class Dog(Animal):

    def __init__(self,name):
        super().__init__(name)

    def bark(self):
        print(f"{self.name} barks BOW WOW")

dog1 = Dog("Noah")
dog1.bark()