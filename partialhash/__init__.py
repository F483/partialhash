# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from __future__ import print_function
from __future__ import unicode_literals
import sys
import hashlib
import codecs


class PartialHash(object):

    class BoundsError(Exception):

        def __init__(self, size, length, offset):
            msg = ("Bounds error! length (%s), offset (%s) must be >= 0"
                   " and length + offset (%s) <= size (%s).")
            args = (length, offset, length + offset, size)
            Exception.__init__(self, msg % args)

    def bytestoint(self, data):
        return int(codecs.encode(data, 'hex'), 16)

    def file_obj(self, obj, offset=0, length=0, hash_algorithm=hashlib.sha256):
        hasher = hash_algorithm()

        # bounds check
        obj.seek(0,2)
        size = obj.tell()
        if length < 0 or offset < 0 or length + offset > size:
            raise self.BoundsError(size, length, offset)

        # start reading from offset
        obj.seek(offset)

        # hash data
        buf = obj.read(length) if length else obj.read()
        hasher.update(buf)
        digest = hasher.hexdigest()

        return digest

        # TODO nextseed = digest
        # TODO nextoffset = self.bytestoint(digest) % (size - lenght)

    def file_path(self, path, *args, **kwargs):
        with open(path, 'rb') as obj:
            return self.file_obj(obj, *args, **kwargs)

    def __call__(self, f, *args, **kwargs):
        if type(f) in [type('str'), type(u'unicode')]:
            return self.file_path(f, *args, **kwargs)
        return self.file_obj(f, *args, **kwargs)


sys.modules[__name__] = PartialHash()
