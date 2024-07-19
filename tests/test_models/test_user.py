#!/usr/bin/python3
"""
Unit Test for User Class
"""
import unittest
from datetime import datetime
import models
import json
import os

User = models.user.User
BaseModel = models.base_model.BaseModel
storage_type = os.environ.get('HBNB_TYPE_STORAGE')

class TestUserDocs(unittest.TestCase):
    """Class for testing documentation of User Class"""

    @classmethod
    def setUpClass(cls):
        """Set up for documentation tests"""
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('........   User  Class   ........')
        print('.................................\n\n')

    def test_doc_file(self):
        """Test documentation for the file"""
        expected = '\nUser Class from Models Module\n'
        actual = models.user.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """Test documentation for the User class"""
        expected = 'User class handles all application users'
        actual = User.__doc__
        self.assertEqual(expected, actual)

class TestUserInstances(unittest.TestCase):
    """Testing User class instances"""

    @classmethod
    def setUpClass(cls):
        """Set up for instance tests"""
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.........  User  Class  .........')
        print('.................................\n\n')

    def setUp(self):
        """Initialize a new User instance for testing"""
        self.user = User()

    def test_instantiation(self):
        """Test if User is properly instantiated"""
        self.assertIsInstance(self.user, User)

    @unittest.skipIf(storage_type == 'db', 'skip if environment is db')
    def test_to_string(self):
        """Test if User is properly casted to string"""
        my_str = str(self.user)
        my_list = ['User', 'id', 'created_at']
        actual = sum(sub_str in my_str for sub_str in my_list)
        self.assertTrue(actual == 3)

    @unittest.skipIf(storage_type == 'db', 'skip if environment is db')
    def test_instantiation_no_updated(self):
        """Test User instance should not have 'updated_at' attribute initially"""
        my_str = str(self.user)
        self.assertNotIn('updated_at', my_str)

    @unittest.skipIf(storage_type == 'db', 'skip if environment is db')
    def test_updated_at(self):
        """Test save function should update 'updated_at' attribute"""
        old_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(old_updated_at, self.user.updated_at)

    @unittest.skipIf(storage_type == 'db', 'skip if environment is db')
    def test_to_json(self):
        """Test to_json should return a serializable dict object"""
        user_json = self.user.to_json()
        try:
            json.dumps(user_json)
            serializable = True
        except (TypeError, OverflowError):
            serializable = False
        self.assertTrue(serializable)

    @unittest.skipIf(storage_type == 'db', 'skip if environment is db')
    def test_json_class(self):
        """Test to_json should include a class key with value User"""
        user_json = self.user.to_json()
        self.assertIn('__class__', user_json)
        self.assertEqual(user_json['__class__'], 'User')

