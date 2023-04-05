# Setup.py file helps in packageing the project for deployment and for pypi, as it installs form requirment.txt file

from setuptools import find_packages,setup
from typing import List # for returning as a list



# Inputs a file path and return a list
HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirments
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        # HyphenEDot should not be ready by python
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)


#this is the metadata of the project
setup(
    name='mlproject',
    version='0.0.1',
    author='Joseph',
    author_email='kbjoseph2@gmail.com',
    packages=find_packages(),
    instll_requires=get_requirements('requirements.txt'),
)