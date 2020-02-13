from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
requires = [
    'ipython>=7.12.0',
    'pandas>=1.0.1',
    'scikit-learn>=0.22.1',
]   
    
setup(
    name="lambdata-josemarquez89",
    version="0.4.4",
    author="Jose Marquez",
    author_email="jose_marquez89@outlook.com",
    description="Example package for lambda school DS Unit 3",
    long_description=long_description,
    long_description_content_type="text/markdown", 
    license="MIT",
    url="https://github.com/jose-marquez89/lambdata-josemarquez89",
    keywords="lambda school",
    packages=find_packages(exclude=("test*")) # ["my_lambdata"]
)
