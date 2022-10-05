# this one below is parent class
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def infoDetails (self):
        print(f"My name is {self.name} \n")
        print(f"My age {self.age}")

class Contact(Person):
    def __init__(self, name, age,numberPhone,address):
        self.numberPhone=numberPhone
        self.address=address

        # invoking init of parent class
        Person.__init__(self,name,age)

    def infoDetails(self):
        print(f"My name is {self.name} \n")
        print(f"My age {self.age}")
        print(f"My number phone is {self.numberPhone}")
        print(f"My address is {self.address}")


if __name__ == "__main__":
    person1= Contact("Syarif", 22, "0812234556","Kuningan jabar")
    person1.infoDetails()