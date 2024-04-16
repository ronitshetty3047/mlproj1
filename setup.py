from setuptools import find_packages,setup
from typing import List

hypen_e_dot='-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return a list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    
    return requirements


setup(
name='machlearn1',
version='0.0.1',
author='Ron',
author_email='ronitshetty3047@gmail.com',
packages=find_packages(),
#install_requires=['pandas','numpy','seaborn']
install_requires=get_requirements('requirements.txt')
)