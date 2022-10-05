class Dog:
    # class attribut
    atribut = "Mammal"

    #instance attribut
    def __init__(self,name):
        self.name= name

# Object instantiation
Rodger=Dog("Rodger")

# Accessing instance attributes
print(Rodger.name)

#Accessing class attribute
print("Rodger is a {}".format(Rodger.atribut))