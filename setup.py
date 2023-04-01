from setuptools import find_packages,setup
from typing import List


E_Dot="-e ."

def get_requirements(file_path:str)->List[str]:
    """
        This function will return the list of requirements
    """
    requirements=[]
    with open('requirements.txt') as obj:
        requirements=obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if E_Dot in requirements:
            requirements.remove(E_Dot)
    return requirements

setup(
    name="MlProject",
    version="0.1",
    author="Abhinav",
    email="abhinavabhi7575@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)