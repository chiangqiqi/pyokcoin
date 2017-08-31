#!/usr/bin/env python

from  setuptools import setup, find_packages

install_requires = ['requests']

setup(
        name='pyokcoin',
        author='Alex Jiang',
        version='0.0.2',
        description='okcoin simple restful api',
        packages=find_packages(),
        install_requires=install_requires
)

