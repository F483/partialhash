###########
partialhash
###########

A library to read/write data to bitcoin transactions as nulldata outputs.


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
