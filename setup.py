# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in burgout/__init__.py
from burgout import __version__ as version

setup(
	name='burgout',
	version=version,
	description='Custom Burgout website',
	author='MostafaFekry',
	author_email='mostafa.fekry@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
