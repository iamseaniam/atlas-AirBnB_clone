#!/usr/bin/python3
"""Testing for Base_Model"""
import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    
    def setUp(self):
        """Define the setUp method to initialize the BaseModel instance"""
        self.model = BaseModel()
        
    def test_create_instance(self):
        """Test if an instance of BaseModel is created with correct attributes"""
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))
        self.assertEqual(type(self.model, 'updated_at'))
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        
    def test_create_intance(self):
        """Test if the save method updates the updated_at attribute"""
        initial_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(initial_updated_at, self.model.updated_at)
        
    def test_to_dict_method(self):
        """Test if the to_dict method returns the correct dictionary"""
        dict_representation = self.model.to_dict()
        self.assertEqual(dict_representation['__class__'], 'BaseModel')
        self.assertEqual(dict_representation['id'], str(self.model.id))
        self.assertEqual(dict_representation['created_at'], self.model.created_at.isoformat())
        self.assertEqual(dict_representation['updated_at'], self.model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
