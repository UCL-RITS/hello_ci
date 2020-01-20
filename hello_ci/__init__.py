import os


class HelloCI:
    def __init__(self):
        if os.getenv("TRAVIS") == "true":
            self.name = "Travis"
        elif os.getenv("CIRCLECI") == "true":
            self.name = "Circle"
        else:
            self.name = "World"

    def greet(self):
        print(f"Hello {self.name}")
