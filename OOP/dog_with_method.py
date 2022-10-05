class DogWithMethod:

    def __init__(self,name):
        self.name=name

    def speak(self):
        print(f'My name is {self.name}')


if __name__ == '__main__':
    roger=DogWithMethod('roger')
    roger.speak()