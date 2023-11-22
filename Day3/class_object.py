# name = "john deo"
# email = "john.deo@example.com"
# age = "20"
# password = "passwd"

class User:
    def __init__(self, name, email, age, passwd):
        self.name = name
        self.email = email
        self.age = age
        self.password = passwd
    
    def change_passwd(self, new_passwd):
        self.password = new_passwd

    def change_age(self, new_age):
        self.age = new_age

    def print_value(self):
        print(f"Name: {self.name}, Email: {self.email}, Age: {self.age}, Password: {self.password}")

user = User("john deo", "john.deo@example.com", "20", "passwd")
user.print_value()
user.change_age("50")
user.print_value()