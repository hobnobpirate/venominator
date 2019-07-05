#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script"""

from setuptools import setup, find_packages

requirements = ["Click"]

setup(
    author="Hobnobpirate",
    author_email="hobnobpirate@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="This script provides a CLI driven menu for msfvenom in order to assist with the creation of shellcode or other msfvenom payloads.",
    entry_points={"console_scripts": ["venominator=venominator.cli:cli"]},
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    name="venominator",
    packages=find_packages(include=["venominator"]),
    url="https://github.com/hobnobpirate/venominator",
    version="0.2.0",
    zip_safe=False,
)
