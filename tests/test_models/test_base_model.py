#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        # This method will run before each test case
        pass

    def tearDown(self):
        # This method will run after each test case
        pass

    def test_base_model_creation(self):
        # Write test cases to ensure that BaseModel creation works as expected
        pass

    def test_base_model_serialization(self):
        # Write test cases to ensure that serialization of BaseModel instances works correctly
        pass

    # Add more test methods for other functionalities of BaseModel
    def test_base_model_creation(self):
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        # Add more assertions as needed


if __name__ == "__main__":
    unittest.main()
