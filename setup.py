from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name="lambdata-josemarquez89",
    version="0.4.2",
    author="Jose Marquez",
    author_email="jose_marquez89@outlook.com",
    description="Example package for lambda school DS Unit 3",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/jose-marquez89/lambdata-josemarquez89",
    keywords="lambda school",
    packages=find_packages() # ["my_lambdata"]
)
