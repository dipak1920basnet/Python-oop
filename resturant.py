class Resturant:
    def __init__(self,resturant,cusine_type):
        self.resturant_name = resturant
        self.cusine_type = cusine_type

    def describe_resturant(self):
        print(f"{self.resturant_name} is of {self.cusine_type} type")

    def open_resturant(self):
        print(f"This resturant is open")

resturant = Resturant("Java_Coffee","Serves Coffee")
print(resturant.resturant_name)
print(resturant.cusine_type)
resturant.describe_resturant()
resturant.open_resturant()
print()
print()
resturant_two = Resturant("Sherpa khaza Ghar","Serves Mongol Food")
print(resturant_two.resturant_name)
print(resturant_two.cusine_type)
resturant_two.describe_resturant()
resturant_two.open_resturant()