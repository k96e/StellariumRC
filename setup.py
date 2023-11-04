#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='StellariumRC',
    version='0.1',
    description=(
        'Control Stellarium by Python'
    ),
    long_description_content_type="markdown",
    long_description=open('README.md').read(),
    author='k96e',
    author_email='zy1835562526@gmail.com',
    license='MIT License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/k96e/StellariumRC',
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)