from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="TestProject",
    version="0.0.1",
    author="Matias Borghi",
    author_email="borghi.matias@gmail.com",
    description="Just a testing project where I try things",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mattborghi/moduleStructure",
    license='MIT',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
