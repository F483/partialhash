#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from __future__ import print_function
from __future__ import unicode_literals
import binascii
import json
import unittest
import partialhash


fixtures = json.load(open("tests/fixtures.json"))


def h2b(h):
    return binascii.unhexlify(h.encode("ascii"))


class TestHash(unittest.TestCase):

    def test_full(self):
        path = fixtures["full"]["path"]
        expected = h2b(fixtures["full"]["sha256"])
        digest = partialhash.compute(path)
        self.assertEqual(digest, expected)

    def test_partial(self):
        path = fixtures["partial"]["path"]
        length = fixtures["partial"]["length"]
        offset = fixtures["partial"]["offset"]
        expected = h2b(fixtures["partial"]["sha256"])
        digest = partialhash.compute(path, length=length, offset=offset)
        self.assertEqual(digest, expected)

    def test_from_obj(self):
        path = fixtures["full"]["path"]
        with open(path, 'rb') as obj:
            expected = h2b(fixtures["full"]["sha256"])
            digest = partialhash.compute(obj)
            self.assertEqual(digest, expected)


class TestLength(unittest.TestCase):

    def test_length(self):
        path = fixtures["length"]["path"]
        length = fixtures["length"]["length"]
        expected = h2b(fixtures["length"]["sha256"])
        digest = partialhash.compute(path, length=length)
        self.assertEqual(digest, expected)


class TestOffset(unittest.TestCase):

    def test_offset(self):
        path = fixtures["offset"]["path"]
        offset = fixtures["offset"]["offset"]
        expected = h2b(fixtures["offset"]["sha256"])
        digest = partialhash.compute(path, offset=offset)
        self.assertEqual(digest, expected)


class TestSeed(unittest.TestCase):

    def test_seed(self):
        seed_path = fixtures["seed"]["seed_path"]
        file_path = fixtures["seed"]["file_path"]
        expected = h2b(fixtures["seed"]["sha256"])
        with open(seed_path, 'rb') as seed_file:
            seed_data = seed_file.read()
            digest = partialhash.compute(file_path, seed=seed_data)
            self.assertEqual(digest, expected)


class TestSample(unittest.TestCase):

    def test_sample_full(self):
        path = fixtures["sample"]["full"]["path"]
        sample_size = fixtures["sample"]["full"]["sample_size"]
        expected = h2b(fixtures["sample"]["full"]["sha256"])
        digest = partialhash.sample(path, sample_size)
        self.assertEqual(digest, expected)

    def test_sample_half_no_seed(self):
        path = fixtures["sample"]["half_no_seed"]["path"]
        sample_size = fixtures["sample"]["half_no_seed"]["sample_size"]
        expected = h2b(fixtures["sample"]["half_no_seed"]["sha256"])
        digest = partialhash.sample(path, sample_size)
        self.assertEqual(digest, expected)

    def test_sample_seed(self):
        path = fixtures["sample"]["seed"]["path"]
        seed_path = fixtures["sample"]["seed"]["seed_path"]
        sample_size = fixtures["sample"]["seed"]["sample_size"]
        expected = h2b(fixtures["sample"]["seed"]["sha256"])
        with open(seed_path, 'rb') as seed_file:
            seed_data = seed_file.read()
            digest = partialhash.sample(path, sample_size, seed=seed_data)
            self.assertEqual(digest, expected)

    def test_multisample_obj(self):
        path = fixtures["sample"]["multisample_obj"]["path"]
        sample_size = fixtures["sample"]["multisample_obj"]["sample_size"]
        sample_count = fixtures["sample"]["multisample_obj"]["sample_count"]
        with open(path, 'rb') as obj:
            partialhash.sample(obj, sample_size, sample_count=sample_count)

    def test_oversample_obj(self):
        path = fixtures["sample"]["oversample_obj"]["path"]
        sample_size = fixtures["sample"]["oversample_obj"]["sample_size"]
        sample_count = fixtures["sample"]["oversample_obj"]["sample_count"]
        with open(path, 'rb') as obj:
            partialhash.sample(obj, sample_size, sample_count=sample_count)


if __name__ == '__main__':
    unittest.main()
