###########
partialhash
###########


[![Build Status](https://travis-ci.org/Storj/partialhash.svg)](https://travis-ci.org/Storj/partialhash)
[![Coverage Status](https://coveralls.io/repos/Storj/partialhash/badge.svg)](https://coveralls.io/r/Storj/partialhash)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/storj/partialhash/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/storj/partialhash.svg)](https://github.com/storj/partialhash/issues)


Library to partialy hash files.


============
Installation
============

::

  pip install partialhash


=====
Usage
=====

.. code:: python

    import binascii
    import partialhash


    path = "examples/random.data"


    # sha256 hash of full file
    digest = partialhash.compute(path)
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
