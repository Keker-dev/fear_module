#!/usr/bin/env python

from io import open
from setuptools import setup

"""
:authors: Keker
:copyright: (c) 2025 Keker
"""

version = '0.9'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='fear_module',
    version=version,

    author='Keker',
    author_email='timaiv112008@gmail.com',

    description=(
        u'Python module for making fear apps '
        u'Fear Application'
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/Keker-dev/fear_module',
    download_url='https://github.com/Keker-dev/fear_module',

    license = "",

    packages=['fear_module'],
    install_requires=['aiohttp', 'aiofiles'],

    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)
