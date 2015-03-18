#!/usr/bin/env python
from __future__ import unicode_literals
from setuptools import setup, find_packages

install_requires = [
    "redis",
]

setup(
    name='redeye',
    version='0.0.2',
    description='A library to watch Redis',
    author='Steve Pulec',
    author_email='spulec@gmail',
    url='https://github.com/spulec/redeye',
    entry_points={
        'console_scripts': [
            'redeye = redeye.main:main',
        ],
    },
    packages=find_packages(exclude=("tests", "tests.*")),
    install_requires=install_requires,
    license="Apache",
    test_suite="tests",
)
