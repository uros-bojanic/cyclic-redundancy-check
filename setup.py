# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Uros Bojanic
# Created Date: 2022/03/14
# ---------------------------------------------------------------------------

# Python program to setup `crc_otr` package using PIP
import setuptools

# Read description from github repository
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Setup
setuptools.setup(
    name='crc_otr',
    version='1.0.1',
    author='Uros Bojanic',
    description='A Python library for cyclic redundancy check (CRC) using polynomial long division in GF(2).',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/urkeboy/cyclic-redundancy-check',
    project_urls={
        "Bug Tracker": "https://github.com/urkeboy/cyclic-redundancy-check/issues"
    },
    packages=['crc_otr'],
    install_requires=[]
)
