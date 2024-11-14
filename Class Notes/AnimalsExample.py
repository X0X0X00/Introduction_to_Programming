"""
mkp
Week 11 Live Coding Examples 1,2 Monday

"""

class Dog:
    def __init__(self,furColor, name, age):
        self.furColor = furColor
        self.name = name
        self.age = age

    def info(self):
        print('Dog named', self.name, '; fur color', self.furColor, ';age',self.age)

    def speak(self):
        print('Bark')

    def getfurColor(self):
        return self.furColor


class Cat:
    def __init__(self,furColor, name, age):
        self.furColor = furColor
        self.name = name
        self.age = age

    def info(self):
        print('Cat named', self.name, '; fur color', self.furColor, ';age',self.age)

    def speak(self):
        print('Meow')

    def getfurColor(self):
        return self.furColor

def main():
    felix = Dog('grey', 'Felix', 5)
    print(felix)
    felix.info()
    felix.speak()
    print(felix.getfurColor())
    doris = Cat('white', 'Doris', 3)
    doris.speak()

main()


