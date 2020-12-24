#!/usr/bin/env python
# coding: utf-8

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hhfetcher", # Replace with your own username
    version="0.0.1",
    author="huangzeyu",
    author_email="zeyu_huang@163.com",
    description="hhfetcher is used for fetching common resources in directory.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shellhue/hhfetcher",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)