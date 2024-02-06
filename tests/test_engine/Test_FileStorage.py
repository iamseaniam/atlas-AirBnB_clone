#!/usr/bin/python3
"""Tests unittesting for file storage"""
import unittest 
from models import models.base_model
from models import storage
import os



class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up the test environment"""
        self.storage = FileStorage()
        self.storage.new(BaseModel())
        self.storage.new(User())
        self.storage.new(State())
        self.storage.new(City())
        self.storage.new(Amenity())
        self.storage.new(Place())
        self.storage.new(Review())

        def teardown(self):
             """Clean up the test environment"""
             self.storage = None
             if os.path.exists('file.json'):
                 os.remove('file.json')

        def test_new(self):
            """Test the new method of FileStorage"""
            self.assertEqual(len(self.storage.all()),  7)

        def test_save(self):
            """Test the save method of FileStorage"""
            self.storage.save()
            with open('file.json', 'r') as f:
                data = json.load(f)
            self.assertEqual(len(data),  7)

        def test_reload(self):
            """Test the reload method of FileStorage"""
            self.storage.save()
            self.storage = FileStorage()
            self.storage.reload()
            self.assertEqual(len(self.storage.all()),  7)

        def test_all(self):
            """Test the all method of FileStorage"""
            self.assertEqual(len(self.storage.all()),  7)
