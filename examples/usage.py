#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from __future__ import print_function
from __future__ import unicode_literals
import binascii
import partialhash


path = "examples/random.data"


# sha256 hash of full file
digest = partialhash.compute(path)  # file path or file like object
print(binascii.hexlify(digest))


# sha256 hash of first 1024 bytes
digest = partialhash.compute(path, length=1024)
print(binascii.hexlify(digest))


# sha256 hash, skipping the first 512 bytes
digest = partialhash.compute(path, offset=512)
print(binascii.hexlify(digest))


# sha256 hash of seed + file data
digest = partialhash.compute(path, seed=b'seeddata')
print(binascii.hexlify(digest))


# recursivly compute sha256 hash until scatter reaches zero
# uses digest to deterministically get next offset and seed value
digest = partialhash.compute(path, length=1024, scatter=4)
print(binascii.hexlify(digest))
