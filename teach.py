print("Welcome to Python Programming!")

name = input("Enter your name: ")
print("Hello, " + name + "!")

age = int(input("Enter your age: "))
print("In five years, you'll be " + str(age + 5))

x = 10
y = 20
sum = x + y
product = x * y
print("Sum:", sum)
print("Product:", product)

if age < 13:
    print("You're a child.")
elif 13 <= age < 20:
    print("You're a teenager.")
else:
    print("You're an adult.")

for i in range(1, 11):
    print(i * i)

def greet(person):
    return "Hello, " + person + "!"

print(greet(name))

colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print(color)

even_numbers = [2, 4, 6, 8, 10]
odd_numbers = [1, 3, 5, 7, 9]
all_numbers = even_numbers + odd_numbers
print(all_numbers)

numbers_dict = {"one": 1, "two": 2, "three": 3}
for key in numbers_dict:
    print(key, ":", numbers_dict[key])

def square(number):
    return number * number

print("Square of 4 is", square(4))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 6 is", factorial(6))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

p = Person(name, age)
p.display()

try:
    file = open("nonexistentfile.txt", "r")
except FileNotFoundError:
    print("File not found!")

with open("example.txt", "w") as file:
    file.write("This is an example file.")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

def multiply(a, b):
    return a * b

print("6 * 7 =", multiply(6, 7))

import math
print("Value of Pi is", math.pi)
print("Cosine of 45 degrees is", math.cos(math.radians(45)))

def countdown(n):
    if n <= 0:
        print("Blast off!")
    else:
        print(n)
        countdown(n-1)

countdown(5)

import random
print("Random number between 1 and 100:", random.randint(1, 100))

def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n - 1)

print("Sum of first 10 numbers is", recursive_sum(10))

def is_palindrome(word):
    return word == word[::-1]

print("Is 'level' a palindrome?", is_palindrome("level"))

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fibs = [0, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

print("First 15 Fibonacci numbers:", fibonacci(15))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)

from datetime import datetime
now = datetime.now()
print("Current date and time:", now)

name_lengths = [len(name) for name in ["Alice", "Bob", "Charlie"]]
print("Name lengths:", name_lengths)

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    else:
        return a / b

print("10 / 2 =", divide(10, 2))
print("10 / 0 =", divide(10, 0))

def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found!"

print(read_file("example.txt"))
print(read_file("nonexistent.txt"))

animals = ["cat", "dog", "rabbit"]
for animal in animals:
    if animal == "dog":
        continue
    print(animal)

number = 5
while number > 0:
    print(number)
    number -= 1

def cube(n):
    return n ** 3

cubes = [cube(i) for i in range(1, 6)]
print("Cubes from 1 to 5:", cubes)

grades = {"Alice": 85, "Bob": 90, "Charlie": 78}
for student in grades:
    print(student, "scored", grades[student])

# Nested dictionary example
students = {
    "Alice": {"age": 20, "major": "Physics"},
    "Bob": {"age": 22, "major": "Mathematics"},
    "Charlie": {"age": 21, "major": "Chemistry"}
}
for student in students:
    print(student, ":", students[student])

import time
print("Current time:", time.ctime())
print("Sleeping for 2 seconds...")
time.sleep(2)
print("Awake now!")

from collections import Counter
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = Counter(words)
print("Word count:", word_count)

def merge_lists(list1, list2):
    return list1 + list2

print("Merged list:", merge_lists([1, 2, 3], [4, 5, 6]))

def prime_numbers(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
           
