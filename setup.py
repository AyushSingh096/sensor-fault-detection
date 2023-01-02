from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return a list of requirements
    """
    requirement_list:List[str] = []

    """
    Write code to read requirements.txt file and append each requirements requirement_list variable.
    """
    return requirement_list

setup(

    name = "sensor",
    version = "0.0.1",
    author = "ayush",
    author_email = "ayushsingh00112233@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),#["pymongo==4.2.0"],
    
)