local Pipeline(os, arch, python_version) = {
    kind: "pipeline",
    name: os+" - "+arch+" - Python "+python_version,
    platform: {
	os: os,
	arch: arch
    },
    steps: [
	{
	    name: "build",
	    image: "python:"+python_version,
	    commands: [
              "pip install .[dev]",
              "pytest",
	      "python -c 'from hello_ci import HelloCI; HelloCI().greet()'"
	    ]
	}
    ]
};

[
    Pipeline("linux", "amd64", "3.6"),
    Pipeline("linux", "amd64", "3.7"),
]
