#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from __future__ import print_function
from __future__ import unicode_literals
import unittest
import partialhash


file_path = "tests/random.data"
filesha256 = "28c5a49c7ca7bfe152055ccf7c0c05527232e8a5bf7e805daad0e5ec02099cb0"


class TestPartialHash(unittest.TestCase):

    def test_fullfile(self):
        # equivalant to 
        # sha256sum tests/random.data
        digest = partialhash.hash_path(file_path)
        self.assertEqual(digest, filesha256)


if __name__ == '__main__':
    unittest.main()
