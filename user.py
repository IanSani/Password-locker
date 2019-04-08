class user:
    """
    class that generates new instances of users
    """

    user_list =[] #Empty user list

    def _init_(self,first_name,last_name,password):
        """
        Method to define the properties of the object
        """

        self.first_name = first_name
        self.last_name = last_name
        self.password = password
