import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="characterbert", # Replace with your own username
    package_dir={"": "src"},
    packages=setuptools.find_packages("src"),
)
