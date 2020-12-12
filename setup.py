# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:31:40 2020

@author: Daniel
"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mp-tools",
    version="1.0.0",
    author="kinderhead",
    description="multiprocessing tools",
    packages=setuptools.find_packages(),
    python_requires='>=3.6'
    )