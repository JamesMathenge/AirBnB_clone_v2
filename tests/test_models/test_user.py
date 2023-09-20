#!/usr/bin/python3
"""Module for testing the User class"""

import os
import unittest
from models.user import User
from tests.test_models.test_base_model import TestBaseModel


class TestUser(TestBaseModel):
    """Test class for User"""

    def setUp(self):
        """Set up test instances for User"""
        self.model = User()
        self.model.first_name = "John"
        self.model.last_name = "Doe"
        self.model.email = "johndoe@example.com"
        self.model.password = "password123"

        def test_first_name_attr(self):
            """Test the first_name attribute of User"""
            self.assertEqual(type(self.model.first_name), str)

            def test_last_name_attr(self):
                """Test the last_name attribute of User"""
                self.assertEqual(type(self.model.last_name), str)

                def test_email_attr(self):
                    """Test the email attribute of User"""
                    self.assertEqual(type(self.model.email), str)

                    def test_password_attr(self):
                        """Test the password attribute of User"""
                        self.assertEqual(type(self.model.password), str)

                        # Add more test cases as needed

                        if __name__ == "__main__":
                            unittest.main()
