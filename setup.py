import os
from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(
    name="potluck_project",
    version="0.0.1",
    description="potluck project of batch #1181",
    packages=find_packages(),
    install_requires=requirements,
    test_suite="tests",
    # include_package_data: to install data from MANIFEST.in
    include_package_data=True,
    # scripts=['scripts/packagename-run'],
    zip_safe=False,
)
