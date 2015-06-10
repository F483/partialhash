# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from __future__ import print_function
from __future__ import unicode_literals
import hashlib


class BoundsError(Exception):

    def __init__(self, size, length, offset):
        msg = ("Bounds error! length (%s), offset (%s) must be >= 0"
               " and length + offset (%s) <= size (%s).")
        args = (length, offset, length + offset, size)
        Exception.__init__(self, msg % args)


def compute_from_obj(obj, offset=0, length=0, seed=b"",
                     hash_algorithm=hashlib.sha256):

    # bounds check
    obj.seek(0, 2)
    size = obj.tell()
    length = length if length else size - offset
    if length < 0 or offset < 0 or length + offset > size:
        raise BoundsError(size, length, offset)

    # start reading from offset
    obj.seek(offset)

    # add seed if given
    hasher = hash_algorithm()
    if seed:
        hasher.update(seed)

    # hash data
    chunklimit = 1024 * 1024 * 100  # 100mb
    chunks = [chunklimit] * (length // chunklimit) + [length % chunklimit]
    for chunksize in chunks:
        buf = obj.read(chunksize)
        hasher.update(buf)
    return hasher.digest()


def compute_from_path(path, *args, **kwargs):
    with open(path, 'rb') as obj:
        return compute_from_obj(obj, *args, **kwargs)


def compute(f, *args, **kwargs):
    if type(f) in [type(b'bytes'), type('str'), type(u'unicode')]:
        return compute_from_path(f, *args, **kwargs)
    return compute_from_obj(f, *args, **kwargs)


#def sample_from_obj(obj, size, count, seed=b"",
#                    hash_algorithm=hashlib.sha256):
#    pass
#
#
#def sample_from_path(path, *args, **kwargs):
#    with open(path, 'rb') as obj:
#        return sample_from_obj(obj, *args, **kwargs)
#
#
#def sample(f, *args, **kwargs):
#    if type(f) in [type(b'bytes'), type('str'), type(u'unicode')]:
#        return sample_from_path(f, *args, **kwargs)
#    return sample_from_obj(f, *args, **kwargs)
