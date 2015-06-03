# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


import hashlib
import codecs


def bytestoint(data):
    return int(codecs.encode(data, 'hex'), 16)


def file_obj(obj, offset=0, hash_algorithm=hashlib.sha256):
    hasher = hash_algorithm()
    if offset:
        obj.seek(offset)
    buf = obj.read()
    hasher.update(buf)
    digest = hasher.hexdigest()
    return digest

    # TODO startindex = bytestoint(seed) % (filesize - lenght) if seed else 0


def file_path(path, offset=0, hash_algorithm=hashlib.sha256):
    with open(path, 'rb') as obj:
        return file_obj(obj, offset=offset, hash_algorithm=hash_algorithm)
