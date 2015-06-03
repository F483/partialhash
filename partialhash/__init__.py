# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


import hashlib
import codecs


def bytestoint(data):
    return int(codecs.encode(data, 'hex'), 16)


def hash_obj(file_obj, hash_algorithm=hashlib.sha256):
    hasher = hash_algorithm()
    buf = file_obj.read()
    hasher.update(buf)
    digest = hasher.hexdigest()
    return digest
    
    # TODO startindex = bytestoint(seed) % (filesize - lenght) if seed else 0


def hash_path(file_path, hash_algorithm=hashlib.sha256):
    with open(file_path, 'rb') as file_obj:
        return hash_obj(file_obj, hash_algorithm=hash_algorithm)
