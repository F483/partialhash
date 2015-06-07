#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from __future__ import print_function
from __future__ import unicode_literals
import os
import tempfile
from timeit import timeit


def make_test_file(path, size):
    # TODO use dd instead for speed?
    with open(path, 'wb') as fo:
        for i in range(size):
            fo.write(b'b' * (1024 * 1024))


def profile_partialhash(path):
    execstr = "partialhash.compute('%s')" % path
    return timeit(execstr, setup="import partialhash", number=5)


def profile_sha256sum(path):
    execstr = "os.system('sha256sum %s > /dev/null')" % path
    return timeit(execstr, setup="import os", number=5)


def profile(size):
    path = tempfile.mktemp()  # make tempfile
    make_test_file(path, size)  # make tempdata
    sha256sum_time = profile_sha256sum(path)
    partialhash_time = profile_partialhash(path)
    os.remove(path)  # remove tempfile
    return {
        "partialhash": partialhash_time, 
        "sha256sum": sha256sum_time,
        "difference" : "%f%%" % ((sha256sum_time / partialhash_time) * 100.0)
    }


if __name__ == '__main__':
    print("fullhash 1M:", profile(1))
    print("fullhash 5M:", profile(5))
    print("fullhash 10M:", profile(10))
    print("fullhash 50M:", profile(50))
    print("fullhash 100M:", profile(100))
    print("fullhash 500M:", profile(500))
    print("fullhash 1000M:", profile(1000))
    print("fullhash 5000M:", profile(5000))
    print("fullhash 10000M:", profile(10000))
