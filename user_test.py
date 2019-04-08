import unittest #Importing the unittest module
import pyperclip #Helps in copy and paste functions
from user import User # importing the user class

class Testuser(unittest.TestCase):
    """
    Test class that defines test cases for the users class behaviours
    Args:
        unittest.TestCase: TestCase class that helps create test cases
    """

    def setUp(self):
        """
        Function to help create user account details before each test
        """
        self.new_user = User('Ian','Sani','SaniBoy')

    def test_init_(self):
        """
        Test to check creation of new user instances
        """
        self.assertEqual(self.new_user.first_name,'Ian')
        self.assertEqual(self.new_user.last_name,'Sani')
        self.assertEqual(self.new_user.password,'SaniBoy')

    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into
        the user user list
        """
        self.new_user.save_user() #saving the new contact
        self.assertEqual(len(User.users_list),1)

if __name__ == '__main__':
    unittest.main()
