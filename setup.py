#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


import os
from setuptools import setup, find_packages


THISDIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(THISDIR)


VERSION = open("version.txt").readline().strip()
DOWNLOAD_BASEURL = "https://pypi.python.org/packages/source/a/partialhash/"
DOWNLOAD_URL = DOWNLOAD_BASEURL + "partialhash-%s.tar.gz" % VERSION


setup(
    name='partialhash',
    version=VERSION,
    description=('Library to partialy hash files.'),
    long_description=open("README.rst").read(),
    keywords=("sha256, partial, hash"),
    url='https://github.com/F483/partialhash/',
    author='Fabian Barkhau',
    author_email='fabian.barkhau@gmail.com',
    license='MIT',
    packages=find_packages(),
    download_url = DOWNLOAD_URL,
    test_suite="tests",
    install_requires=[
    ],
    tests_require=[
        #'ipython',
        #'pudb' # import pudb; pu.db # set break point
    ],
    zip_safe=False
)
