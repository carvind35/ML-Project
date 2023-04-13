from setuptools import find_packages, setup
from typing import List




Hypen_dot ='-e .'
def get_requirement(file_path =str)->List[str]:

    ''' 
    This function will return the list of requirement
    
    '''
    requirement =[]
    with open('requirement.txt') as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace('\n','')for req in requirement ]
        if Hypen_dot in requirement:
            requirement.remove(Hypen_dot)

    return requirement




setup(
name = 'ML-Project',
version ='0.0.1',
author ='Arvind',
author_email ='carvind35@gmail.com',
packages = find_packages(),
insatll_require = get_requirement('requirement.txt')


)