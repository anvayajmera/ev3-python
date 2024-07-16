class PythonFundamentals:
    def __init__(self):
        self.run_all()

    def run_all(self):
        self.hello_world()
        self.variables()
        self.data_types()
        self.lists()
        self.tuples()
        self.dictionaries()
        self.conditionals()
        self.loops()
        self.functions()
        self.classes_objects()
        self.file_io()
        self.modules()
        self.exceptions()
        self.final_project()

    def hello_world(self):
        print("Hello, World!")

    def variables(self):
        x = 5
        y = 10
        name = "Python"
        is_fun = True
        print(x, y, name, is_fun)

    def data_types(self):
        a = 10
        b = 20.5
        c = "Hello"
        d = [1, 2, 3]
        e = (4, 5, 6)
        f = {"name": "Alice", "age": 25}
        g = True
        print(a, b, c, d, e, f, g)

    def lists(self):
        fruits = ["apple", "banana", "cherry"]
        fruits.append("orange")
        fruits.remove("banana")
        print(fruits)
        for fruit in fruits:
            print(fruit)

    def tuples(self):
        colors = ("red", "green", "blue")
        print(colors[0])
        for color in colors:
            print(color)

    def dictionaries(self):
        person = {"name": "John", "age": 30, "city": "New York"}
        print(person["name"])
        person["email"] = "john@example.com"
        del person["age"]
        for key, value in person.items():
            print(key, value)

    def conditionals(self):
        x = 10
        if x < 10:
            print("Less than 10")
        elif x == 10:
            print("Equal to 10")
        else:
            print("Greater than 10")

    def loops(self):
        for i in range(5):
            print(i)
        i = 0
        while i < 5:
            print(i)
            i += 1

    def functions(self):
        def greet(name):
            return f"Hello, {name}!"

        print(greet("Alice"))
        print(greet("Bob"))

    def classes_objects(self):
        class Dog:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            def bark(self):
                return "Woof!"

        dog1 = Dog("Rex", 5)
        dog2 = Dog("Buddy", 3)
        print(dog1.name, dog1.age, dog1.bark())
        print(dog2.name, dog2.age, dog2.bark())

    def file_io(self):
        with open("test.txt", "w") as file:
            file.write("Hello, file!")
        with open("test.txt", "r") as file:
            content = file.read()
            print(content)

    def modules(self):
        import math
        print(math.sqrt(16))
        print(math.pi)

    def exceptions(self):
        try:
            x = 10 / 0
        except ZeroDivisionError:
            print("Cannot divide by zero")
        finally:
            print("Done")

    def final_project(self):
        def calculator():
            while True:
                operation = input("Enter operation (+, -, *, /) or 'quit': ")
                if operation == 'quit':
                    break
                if operation in ('+', '-', '*', '/'):
                    x = float(input("Enter first number: "))
                    y = float(input("Enter second number: "))
                    if operation == '+':
                        print(x + y)
                    elif operation == '-':
                        print(x - y)
                    elif operation == '*':
                        print(x * y)
                    elif operation == '/':
                        if y != 0:
                            print(x / y)
                        else:
                            print("Cannot divide by zero")
                else:
                    print("Invalid operation")

        calculator()

if __name__ == "__main__":
    PythonFundamentals()
