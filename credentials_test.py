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

    def test_save_credentials(self):
        """
        Test and confrim that the new credential information is being saved
        """
        self.new_credential.save_credentials()
        self.assertEqual(len(Credential.credentials_list),1)

    def tearDown(self):
        """
        tearDown method that executes a set of instructions after  every test
        """
        User.users_list =[]
        Credential.credentials_list = []

    def test_display_credentials(self):
        """
        Test to confirm user can view the correct credential details
        """
        self.new_credential.save_credentials()
        facebook = Credential('Ian','facebook','Iansani','sani254')
        facebook.save_credentials()
        self.asserEqual(Credential.display_credentials(),Credential.credential_list)

    def test_search_social_media(self):
        """
        Test to confirm if the method returns the correct social media credential
        """
        self.new_credential.save_credentials()
        facebook = Credential('Ian','facebook','Iansani','sani254')
        facebook.save_credentials()
        credential_exist = Credential.search_social_media('Facebook')
        self.assertEqual(credential_exists,facebook)
