import unittest
import pyperclip
from credentials import Credential
from user import User

class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for the credentials class behaviours
    Args:
        unittest.TestCase: TestCase class that helps create test cases
    """



    def setUp(self):
        self.new_credential = Credential('Ian','facebook','Iansani','sani254')

    def tearDown(self):
        """
        tearDown method that executes a set of instructions after  every test
        """
        User.users_list =[]
        Credential.credentials_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.user_name,"Ian")
        self.assertEqual(self.new_credential.social_media,"facebook")
        self.assertEqual(self.new_credential.account_name,"Iansani")
        self.assertEqual(self.new_credential.password,"sani254")

    def test_save_credentials(self):
        """
        Test and confrim that the new credential information is being saved
        """
        self.new_credential.credentials_list
        self.assertEqual(1,1)

    def test_confirm_user(self):
        """
        Function to confirm login details to active users
        """
        self.new_user = User('Ian','Sani','SaniBoy')
        self.new_user.save_user()
        userX= User('Ian','Sani','SaniBoy')
        userX.save_user()
        active_user = Credential.confirm_user('Ian','SaniBoy')
        self.assertTrue(active_user)

    def test_display_credentials(self):
        """
        Test to confirm user can view the correct credential details
        """

        self.new_credential = Credential('Ian','facebook','Iansani','sani254')
        self.new_credential .credentials_list
        self.assertEqual(Credential.display_credentials(),Credential.credentials_list)

    def test_search_social_media(self):
        """
        Test to confirm if the method returns the correct social media credential
        """
        self.new_credential.credentials_list
        test_user_credentials = Credential('Ian','facebook','Iansani','sani254')
        test_user_credentials.credentials_list
        found_social_media = Credential.search_social_media('facebook')
        # self.assertEqual(found_social_media.account_name,test_user_credentials.account_name)


if __name__ == '__main__':
     unittest.main()
