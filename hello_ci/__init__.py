import os


class HelloCI:
    def __init__(self):
        if os.getenv("TRAVIS") == "true":
            self.name = "Travis"
        elif os.getenv("CIRCLECI") == "true":
            self.name = "Circle"
        elif os.getenv("DRONE") == "true":
            self.name = "Drone"
        elif os.getenv("GITHUB_ACTIONS") == "true":
            self.name = "GitHub Actions"
        elif os.getenv("GITLAB_CI") == "true":
            self.name = "GitLab Pipelines"
        elif os.environ.get("GO_PIPELINE_NAME"):
            # There isn't an environment variable with a fixed value.
            self.name = "GoCD"
        elif os.getenv("BUILD_BUILDNUMBER") == "true":
            # Somewhat surprisingly, Azure Pipelins doesn't seem to have an
            # environment variable that unequivocally tells that we are using
            # this CI service.  Environment variables are also not documented
            # anywhere.
            self.name = "Azure Pipelines"
        else:
            self.name = "World"

    def greet(self):
        print(f"Hello {self.name}")
