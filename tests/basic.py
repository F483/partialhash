#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from __future__ import print_function
from __future__ import unicode_literals
import json
import unittest
import partialhash


fixtures = json.load(open("tests/fixtures.json"))


class TestPartialHash(unittest.TestCase):

    def test_fullfile(self):
        path = fixtures["alpha"]["path"]
        expected = fixtures["alpha"]["sha256"]
        digest = partialhash.file_path(path)
        self.assertEqual(digest, expected)

    def test_offset(self):
        offset = fixtures["betaalpha"]["offset"]
        path = fixtures["betaalpha"]["path"]
        expected = fixtures["betaalpha"]["sha256"]
        digest = partialhash.file_path(path, offset=offset)
        self.assertEqual(digest, expected)

if __name__ == '__main__':
    unittest.main()
