from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="basepy",
    version="0.0.1",
    description="Opinionated layout for Python 3 CLI projects",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Guido Lena Cota",
    url="https://github.com/glenacota/basepy",
    license=license,
    install_requires=["click"],
    packages=find_packages(exclude=("tests", "docs")),
)
