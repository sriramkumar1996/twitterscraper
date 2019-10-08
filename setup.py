#!/usr/bin/env python3
from setuptools import setup, find_packages
import re
import os


def get_requirements():
    with open('requirements.txt') as requirements:
        required = requirements.read().splitlines()
        return required

def get_version():
    fn = os.path.join(os.path.dirname(__file__), "twitterscraper", "__init__.py")
    with open(fn) as f:
        return re.findall("__version__ = '([\d.\w]+)'", f.read())[0]

def get_long_description():
    readme = open('README.rst').read()
    return readme

setup(
    name='sriram-twitter-scraper',
    version=get_version(),
    author=['Ahmet Taspinar', 'Lasse Schuirmann', 'Sriram Kumar'],
    author_email='srirambsk1996@gmail.com',
    license='MIT',
    description='Tool for scraping Tweets',
    long_description=get_long_description(),
    url='https://github.com/sriramkumar1996/twitterscraper',
    packages=find_packages(exclude=["build.*", "tests", "tests.*"]),
    install_requires=get_requirements(),
    entry_points={
        "console_scripts": [
            "twitterscraper = twitterscraper.main:main"
        ]
    })
