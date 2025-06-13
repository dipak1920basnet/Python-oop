class Resturant:
    def __init__(self, resturant, cusine_type, number_served = 0):
        self.resturant_name = resturant
        self.cusine_type = cusine_type
        self.number_served = number_served

    def describe_resturant(self):
        print(f"{self.resturant_name} is of {self.cusine_type} type")

    def open_resturant(self):
        print(f"This resturant is open")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self):
        self.number_served +=1


resturant = Resturant("Java_Coffee", "Serves Coffee")
print(resturant.resturant_name)
print(resturant.cusine_type)
print(resturant.number_served)
resturant.addCustomer()
print(resturant.number_served)
# resturant.describe_resturant()
# resturant.open_resturant()
# print()
# print()
# resturant_two = Resturant("Sherpa khaza Ghar", "Serves Mongol Food")
# print(resturant_two.resturant_name)
# print(resturant_two.cusine_type)
# resturant_two.describe_resturant()
# resturant_two.open_resturant()


# class User():
#     def __init__(self, name, surname, email, phone_number, resturant:Resturant):
#         self.name = name
#         self.surname = surname
#         self.email = email
#         self.phone_number = phone_number
#         self.resturant = resturant

#     def describe_user(self):
#         return f"Hi my name is {self.name} {self.surname} and my email is {self.email} and here is my phone number {self.phone_number}"

#     def greet_user(self):
#         return f"Hello {self.name} {self.surname} welcome to our resturant {self.resturant.resturant_name}"
