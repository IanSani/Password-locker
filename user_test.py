def test_save_user(self):
    """
    test_save_user test case to test if the user object is saved into
    the user user list
    """
    self.new_user.save_user() #saving the new contact
    self.asserEqual(len(user.user_list),1)

    if _name_ == '_main_':
        unittest.main()
