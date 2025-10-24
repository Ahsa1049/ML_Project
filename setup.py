from setuptools import setup,find_packages
from typing import List
hypon_e_dot = "-e ."
def get_requirements(file_path:str)->list[str]:
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if hypon_e_dot in requirements:
            requirements.remove(hypon_e_dot)
    return requirements
setup(
    name = "ML_project",
    version = "0.01",
    author = "Ahsan",
    author_email = "abadatalia@gmail.com",
    packages = find_packages(),
    install_require = get_requirements("requirements.txt")
)