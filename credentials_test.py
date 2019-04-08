import unittest
import pyperclip
from credentials import credentials

class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for the credentials class behaviours
    Args:
        unittest.TestCase: TestCase class that helps create test cases
    """

    def test_confirm_user(self):
        """
        Function to confirm login details to active users
        """
        self.new_user = User('Ian','Sani','SaniBoy')
        self.new_user.save_user()
        userX= User('Ian','Sani','SaniBoy')
        userX.save_user()
        active_user = Credential.confirm_user('Ian','SaniBoy')
        self.assertTRue(active_user)

    def setUp(self):
        """
        Function to create social media account credentials before each test
        """
        self.new_credential = Credential('Ian','facebook','Iansani','sani254')

        
