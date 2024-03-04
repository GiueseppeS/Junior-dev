import os

class User:
    """Simple User class to manage users and methods"""
    
    def __init__(self, _username = "", _password = "") -> None:
        self.username = _username
        self.password = _password



    def authenticate(self):
        """Method that authenticate the user at the beginning of the software"""
        logged_in = False
        username_check = False
        while not logged_in:
            users = self.get_register_user_from_file()
            print("LOGIN")
            curr_user = input("Username: ").strip()
            curr_pass = input("Password: ").strip()
            for user in users:
                if curr_user != user.username:
                    continue
                elif curr_pass != user.password:
                    print("Wrong password!")
                else:
                    logged_in = True
                    print("Login succesful")
            if username_check is False:
                print("User does not exist")
        return User(curr_user, curr_pass)


    def reg_user(self):
        """Register a new user and write it in the user.txt"""
        new_username = input("New Username: ")


        # - Request input of password confirmation.
        #confirm_password = input("Confirm Password: ")
        users_list = self.get_register_user_from_file()

        user_info_dict = {}
        for user in users_list:
            user_info_dict = {user.username : user.password}

        if new_username in user_info_dict:
            print("The user already exist in the database")
        else:
            while True:
                # - Request input of a new password
                new_password = input("New Password: ").strip()
                # - Request input of password confirmation.
                confirm_password = input("Confirm Password: ").strip()


                if new_password == confirm_password:
                    self.username = new_username
                    self.password = new_password
                    with open("user.txt", "a", encoding="utf-8") as out_file:
                        user_data = f"{self.username};{self.password}"
                        out_file.write("\n" + user_data)
                        break
                # - Otherwise you present a relevant message.
                else:
                    print("Passwords do no match")


    def get_register_user_from_file(self) -> list:
        '''Create a list from the user.txt and return a dictionary username : password
        this function is used across the scripts'''
        users = []
        if not os.path.exists("user.txt"):
            with open("user.txt", "w", encoding="utf-8") as default_file:
                default_file.write("admin;password")

        with open("user.txt", 'r', encoding="utf=8") as user_file:
            user_data = user_file.read().split("\n")
            for user in user_data:
                if user:
                    user_info = user.split(';')
                    new_user = User(*user_info)
                    users.append(new_user)
            return users