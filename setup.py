#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from setuptools import setup, find_packages


exec(open('partialhash/version.py').read())


DOWNLOAD_BASEURL = "https://pypi.python.org/packages/source/a/partialhash/"
DOWNLOAD_URL = DOWNLOAD_BASEURL + "partialhash-%s.tar.gz" % __version__  # NOQA


setup(
    name='partialhash',
    version=__version__,  # NOQA
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
    install_requires=[],
    tests_require=[
        'coverage',
        'coveralls',
    ],
    zip_safe=False,
    classifiers=[
        # "Development Status :: 1 - Planning",
        # "Development Status :: 2 - Pre-Alpha",
        # "Development Status :: 3 - Alpha",
        # "Development Status :: 4 - Beta",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
