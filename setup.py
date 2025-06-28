from setuptools import find_packages , setup
from typing import List

def get_requirements()->List[str]:
    """
    Reads a requirements file and returns a list of requirements.
    """

    requirements_list = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
        for line in lines:
            # Strip whitespace and remove comments
            line = line.strip()
            if line and line != '-e .':
                requirements_list.append(line)
    except Exception as e:
        print(f"Error reading requirements.txt: {e}")
    return requirements_list


setup(
    name='Networksecurity',
    version='0.1.0',
    author='Sahu pithiya',
    packages=find_packages(),
    install_requires=get_requirements(),
)