import os



class UserLogin:
    """Class that manage the login of the users"""
    def __init__(self, filename="user.txt"):
        self.filename = filename
        self.username_passowrd = {}
        self.logged_in = False
        self.read_in_user_data()


    def read_in_user_data(self):
        # If no user.txt file, write one with a default account
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as default_file:
                default_file.write("admin;password")

        # Read in user_data
        with open(self.filename, 'r') as user_file:
            user_data = user_file.read().split("\n")
            return user_data

        