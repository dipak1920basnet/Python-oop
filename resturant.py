class Resturant:
    def __init__(self, resturant, cusine_type, number_served=0):
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
        self.number_served += 1


resturant = Resturant("Java_Coffee", "Serves Coffee")
print(resturant.resturant_name)
print(resturant.cusine_type)
print(resturant.number_served)
# resturant.addCustomer()
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


class User:
    def __init__(
        self, name, surname, email, phone_number, resturant: Resturant, login_attempt=0
    ):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone_number = phone_number
        self.resturant = resturant
        self.login_attempt = login_attempt

    def describe_user(self):
        return f"Hi my name is {self.name} {self.surname} and my email is {self.email} and here is my phone number {self.phone_number}"

    def greet_user(self):
        return f"Hello {self.name} {self.surname} welcome to our resturant {self.resturant.resturant_name}"

    def increment_login_attempts(self):
        self.login_attempt += 1

    def reset_login_attempt(self):
        self.login_attempt = 0


user_one = User(
    name="Dipak", surname="Basnet", email="dipak@gmail.com", phone_number=984632146, resturant=resturant
)

user_one.increment_login_attempts()
user_one.increment_login_attempts()
user_one.increment_login_attempts()
print(user_one.login_attempt)
user_one.reset_login_attempt()
print(user_one.login_attempt)