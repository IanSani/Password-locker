import pyperclip
import string
import random

class Credential:
    """
    Class taht holds and saves user login details,social media a/c credentials,password
    """
    # class variables
    credentials_list =[]

    @classmethod
    def confirm_user(cls,first_name,password):
        """
          Method that checks if the name and password entered match entries in the users_list
          """
          active_user = ''
          for user in User.users_list:
              if (user.first_name == user.password == password):
                  active_user = user.first_name
          return active_user
