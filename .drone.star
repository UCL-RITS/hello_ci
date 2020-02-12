def main(ctx):
    return [
        pipeline("linux", "amd64", "3.6"),
        pipeline("linux", "amd64", "3.7")
    ]


def pipeline(os, arch, python_version):
    return {
        "kind": "pipeline",
        "name": os + " - " + arch + " - Python " + python_version,
        "steps": [
            {
                "name": "build",
                "image": "python:" + python_version,
                "commands": [
                    "pip install .[dev]",
                    "pytest",
                    "python -c 'from hello_ci import HelloCI; HelloCI().greet()'"
                ]
            }
        ]
    }
