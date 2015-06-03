# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from __future__ import print_function
from __future__ import unicode_literals
import hashlib
import codecs


class BoundsError(Exception):

    def __init__(self, size, length, offset):
        msg = ("Bounds error! length (%s), offset (%s) must be >= 0"
               " and length + offset (%s) <= size (%s).")
        args = (length, offset, length + offset, size)
        Exception.__init__(self, msg % args)


def bytestoint(data):
    return int(codecs.encode(data, 'hex'), 16)


def compute_from_obj(obj, offset=0, length=0, seed=b"", scatter=0,
             hash_algorithm=hashlib.sha256):

    # bounds check
    obj.seek(0, 2)
    size = obj.tell()
    if length < 0 or offset < 0 or length + offset > size:
        raise BoundsError(size, length, offset)

    # start reading from offset
    obj.seek(offset)

    # add seed if given
    hasher = hash_algorithm()
    if seed:
        hasher.update(seed)

    # hash data
    buf = obj.read(length) if length else obj.read()
    hasher.update(buf)
    digest = hasher.digest()

    # scatter if given
    if scatter:
        offset = bytestoint(digest) % (size - length)
        return compute_from_obj(obj, offset=offset, length=length,
                                seed=digest, scatter=(scatter - 1),
                                hash_algorithm=hash_algorithm)
    return digest


def compute_from_path(path, *args, **kwargs):
    with open(path, 'rb') as obj:
        return compute_from_obj(obj, *args, **kwargs)


def compute(f, *args, **kwargs):
    if type(f) in [type('str'), type(u'unicode')]:
        return compute_from_path(f, *args, **kwargs)
    return file_obj(f, *args, **kwargs)
