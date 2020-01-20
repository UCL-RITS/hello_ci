import os


class HelloCI:
    def __init__(self):
        if os.getenv("TRAVIS") == "true":
            self.name = "Travis"
        elif os.getenv("CIRCLECI") == "true":
            self.name = "Circle"
        elif os.getenv("DRONE") == "true":
            self.name = "Drone"
        else:
            self.name = "World"

    def greet(self):
        print(f"Hello {self.name}")
