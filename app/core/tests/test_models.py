"""
test for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
    """test models"""
    def test_create_user_email_with_successful(self):
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))