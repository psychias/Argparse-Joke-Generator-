#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# setup.py

# Authors: Luisa Wunderlin, Jean Kesselring, Sophia Carpentieri, Iris Zoder
# University of Zurich
# Department of Computational Linguistics


import setuptools

with open('README.md', 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name='jg',
    version='1.0.0',
    author='Luisa Wunderlin, Jean Kesselring, Sophia Carpentieri, Iris Zoder',
    description='Library and CLI to generate and print jokes',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.uzh.ch/pcl2-2022-assignments/exercise_3',
    packages=['jg'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'jg = jg.CLI_solution:main'
        ]
    },
    include_package_data=True,
    package_data={'jg': ['data/profanities.txt', 'data/reddit_dadjokes.csv']}
)
