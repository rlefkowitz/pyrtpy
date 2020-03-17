import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-rlefkowitz",
    version="0.0.1",
    author="Ryan Lefkowitz",
    author_email="rml258@cornell.edu",
    description="A Ray Tracing Library for Python, Written in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rlefkowitz/pyrtpy-pkg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)