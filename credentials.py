import pyperclip
import string
import random
from user import User
class Credential:
    """
    Class taht holds and saves user login details,social media a/c credentials,password
    """
    # class variables
    credentials_list =[]

    @classmethod
    def confirm_user(cls,first_name,password):
        active_user = 'ksl'
        for user in User.users_list:
          if (user.first_name == user.password == password):
              active_user = user.first_name
        return active_user

    def __init__(self,user_name,social_media,account_name,password):
        """
        Method defining the properties each object will hold
        """
        self.user_name =user_name
        self.social_media = social_media
        self.account_name = account_name
        self.password = password

    def generate_password():
        """
        Function to generate random passwords for social media accounts
        """
        pwchar = string.printable
        length = int(input("Enter password length needed:"))
        gen_pwd=''
        for char in range(length):
            gen_pwd += random.choice(pwchar)
        return gen_pwd

    @classmethod
    def display_credentials(cls):
        """
        Class method to display the list of saved credentials
        """
        return cls.credentials_list

    @classmethod
    def search_social_media(cls,social_media):
        """
        Method that accepts social media name and returns credentials matching
        """
        for credential in cls.credentials_list:
            if credential.social_media == social_media:
                return True
            return False
    # @classmethod
    # def save_credentials(cls,number):


    # @classmethod
    # def copy_password(cls,social_media):
    #     """
    #     Class method that copies a credential`s password of a specific social media site after the credential`s is entered
    #     """
    #     collect_pass = Credential.search_social_media(search_social_media)
    #     return pyperclip.copy(collect_pass.password)
