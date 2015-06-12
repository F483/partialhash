###########
partialhash
###########


|BuildLink|_ |CoverageLink|_ |LicenseLink|_ |IssuesLink|_


.. |BuildLink| image:: https://travis-ci.org/Storj/partialhash.svg
.. _BuildLink: https://travis-ci.org/Storj/partialhash

.. |CoverageLink| image:: https://coveralls.io/repos/Storj/partialhash/badge.svg
.. _CoverageLink: https://coveralls.io/r/Storj/partialhash

.. |LicenseLink| image:: https://img.shields.io/badge/license-MIT-blue.svg
.. _LicenseLink: https://raw.githubusercontent.com/F483/partialhash/master/LICENSE

.. |IssuesLink| image:: https://img.shields.io/github/issues/F483/partialhash.svg
.. _IssuesLink: https://github.com/F483/partialhash/issues


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

    # from examples/usage.py
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

    # sha256 hash of 256 byte sample with given seed
    # which data is sampled depends on given seed
    digest = partialhash.sample(path, 256, seed=b'seeddata')
    print(binascii.hexlify(digest))

    # sha256 hash of three 256 byte samples with given seed
    # sample data will not overlap until sample size exceeds file size
    digest = partialhash.sample(path, 256, sample_count=3, seed=b'seeddata')
    print(binascii.hexlify(digest))
