print("Hello, World!")

name = input("What's your name? ")
print("Nice to meet you, " + name + "!")
age = int(input("How old are you? "))
print("You will be " + str(age + 1) + " next year.")

x = 5
y = 10
z = x + y
print("The sum of x and y is", z)

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")

for i in range(5):
    print(i)

def greet_person(person):
    print("Hello, " + person + "!")

greet_person(name)

numbers = [1, 2, 3, 4, 5]
print(numbers)

for num in numbers:
    print(num)

squares = [n * n for n in numbers]
print(squares)

person = {"name": name, "age": age}
print(person["name"], "is", person["age"], "years old.")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("Factorial of 5 is", factorial(5))

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says hello!"

dog = Animal("Dog")
print(dog.speak())

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

with open("test.txt", "w") as file:
    file.write("Hello, World!")

with open("test.txt", "r") as file:
    print(file.read())

def add(a, b):
    return a + b

print("3 + 5 =", add(3, 5))

import math
print("Square root of 16 is", math.sqrt(16))

def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Liftoff!")

countdown(5)
