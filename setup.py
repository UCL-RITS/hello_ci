import setuptools

setuptools.setup(
    name="HelloCI",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description="A small example package",
    long_description_content_type="text/markdown",
    url="https://github.com/UCL-RITS/rsdg-ci-reboot",
    packages=setuptools.find_packages(),
    license="MIT",
    license_file="LICENSE",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    extras_require={
        "dev": ["pytest"],
    }
)
