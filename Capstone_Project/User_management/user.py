import os

class User:
    """Simple User class to manage users and methods"""
    def __init__(self) -> None:
        self.username = ""
        self.password = ""

    def authenticate(self, _curr_user, _curr_password) -> bool:
        """Method that authenticate the user at the beginning of the software"""
        username_password = self.get_register_user()
        if _curr_user not in username_password:
            print("User does not exist")
            return False
        elif username_password[_curr_user] != _curr_password:
            print("Wrong password!")
            return False
        else:
            self.username = _curr_user
            self.password = _curr_password
            print("Login succesful")
            return True


    def reg_user(self):
        """Register a new user and write it in the user.txt"""
        new_username = input("New Username: ")

        # - Request input of a new password
        new_password = input("New Password: ")

        # - Request input of password confirmation.
        confirm_password = input("Confirm Password: ")
        users_list = self.get_register_user()

        if new_username in users_list:
            print("The user already exist in the database")
        else:
            if new_password == confirm_password:
                self.username = new_username
                self.password = new_password
                with open("user.txt", "a", encoding="utf-8") as out_file:
                    user_data = f"{self.username};{self.password}"
                    out_file.write("\n" + user_data)

                # - Otherwise you present a relevant message.
            else:
                print("Passwords do no match")


    def get_register_user(self) -> list:
        '''Create a list from the user.txt and return a dictionary username : password
        this function is used across the scripts'''
        if not os.path.exists("user.txt"):
            with open("user.txt", "w", encoding="utf-8") as default_file:
                default_file.write("admin;password")
        with open("user.txt", 'r', encoding="utf=8") as user_file:
            user_data = user_file.read().split("\n")

        # Convert to a dictionary
        username_password = {}
        for user in user_data:
            username, password = user.split(';')
            username_password[username] = password
        return username_password
    