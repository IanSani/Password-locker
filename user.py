class user:
    """
    class that generates new instances of users
    """

    users_list =[] #Empty user list

    def _init_(self,first_name,last_name,password):
        """
        Method to define the properties of the object
        """

        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        """
        save user details method into users_list
        """
        user.users_list.append(self)
