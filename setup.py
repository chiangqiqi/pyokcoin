#!/usr/bin/env python

from  setuptools import setup, find_packages

install_requires = ['pymongo']

setup(
        name='pyokcoin',
        author='Qiqi Jiang',
        version='0.0.1',
        description='get trade info from okcoin and try to analysis',
        packages=find_packages(),
        install_requires=install_requires
)

