#  a model of a dog highlighting it attributes and behaviors   Speak - "Woof",  Walk, Run,  Eat

class Dog:
    def __init__(self, name, age, color):
       self.name = name
       self.age = age
       self.color = color

    # A method for Speaking
    def speak(self):
        return "Woof!"

    def walk(self):
        return "Walking!"

    def eat(self):
        return "Eating!"
    
    def run(self):
        return "Running!"



# A model of a dog
police_dog = Dog("Lion", 7, "Black")

print(police_dog.color)
print(police_dog.age)
print(police_dog.name)

print(f"The dog is barking {police_dog.speak()}")

print(police_dog.eat())
print(police_dog.walk())



   
