import bcrypt
import logging
from datetime import datetime

logging.basicConfig(
    filename="login.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class AuthSystem:
    def __init__(self):
        self.user_database = {}

    def encrypt_password(self, password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode(), salt)
        return hashed

    def register_user(self, username, password):
        if username in self.user_database:
            print("Username already exists!")
            return
        self.user_database[username] = {
            "password": self.encrypt_password(password),
            "2fa_enabled": False,
            "2fa_method": None
        }
        print(f"User '{username}' registered successfully!")

    def login(self, username, password):
        if username not in self.user_database:
            print("User not found!")
            logging.warning(f"Login failed: user '{username}' not found.")
            return False

        stored_hash = self.user_database[username]["password"]
        if bcrypt.checkpw(password.encode(), stored_hash):
            print("Password is correct!")
            return True
        else:
            print("Incorrect password!")
            logging.warning(f"Login failed: incorrect password for user '{username}'.")
            return False

    def enable_2fa(self, username, method="sms"):
        if username not in self.user_database:
            print("User not found!")
            return
        self.user_database[username]["2fa_enabled"] = True
        self.user_database[username]["2fa_method"] = method
        print(f"2FA enabled for '{username}' using: {method.upper()}")

    def verify_2fa(self, username, code):
        user = self.user_database.get(username)
        if not user:
            print("User not found!")
            return False
        if not user["2fa_enabled"]:
            print("2FA is not enabled for this user.")
            return True

        method = user["2fa_method"]
        if method == "sms":
            correct_code = "123456"
        elif method == "app":
            correct_code = "654321"
        else:
            print("Invalid 2FA method!")
            return False

        if code == correct_code:
            print("2FA code is correct!")
            return True
        else:
            print("Incorrect 2FA code!")
            logging.warning(f"Login failed: incorrect 2FA code for user '{username}'.")
            return False

    def full_login(self, username, password, code=None):
        if not self.login(username, password):
            return False

        if self.user_database[username]["2fa_enabled"]:
            if code is None:
                print("2FA code required!")
                return False
            if not self.verify_2fa(username, code):
                return False

        print("Login successful!")
        logging.info(f"User '{username}' logged in successfully.")
        return True

    def menu(self):
        while True:
            print("\n Menu:")
            print("1 - Register")
            print("2 - Login")
            print("3 - Enable 2FA")
            print("4 - Exit")

            choice = input("> Choose: ")

            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                self.register_user(username, password)

            elif choice == "2":
                username = input("Username: ")
                password = input("Password: ")
                user = self.user_database.get(username)
                if user and user["2fa_enabled"]:
                    code = input("Enter 2FA code: ")
                    self.full_login(username, password, code)
                else:
                    self.full_login(username, password)

            elif choice == "3":
                username = input("Username: ")
                method = input("2FA method (sms/app): ").strip().lower()
                self.enable_2fa(username, method)

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid option.")

if __name__ == "__main__":
    app = AuthSystem()
    app.menu()
