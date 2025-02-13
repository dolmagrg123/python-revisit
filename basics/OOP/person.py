
# class Person():
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age =age
# p1 = Person("Dolma", 25)
# print(p1.name, p1.age)  # Output: Dolma 25

class Car():
    def __init__(self, name, model):
        self.name = name
        self.model = model
        
    def display_info(self):
        return f"{self.name} {self.model}"

car_model = Car("mercedez", "c560")
print(car_model.display_info())