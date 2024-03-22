# user.py

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, user_id):
        user = User(name, user_id)
        self.users.append(user)

    def update_user(self, user_id, name=None):
        for user in self.users:
            if user.user_id == user_id:
                if name:
                    user.name = name
                return True
        return False

    def delete_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                return True
        return False

    def list_users(self):
        if not self.users:
            print("No users available.")
        else:
            for user in self.users:
                print(f"Name: {user.name}, User ID: {user.user_id}")

    def search_user_by_name(self, name):
        found_users = [user for user in self.users if user.name.lower() == name.lower()]
        return found_users

    def search_user_by_id(self, user_id):
        found_users = [user for user in self.users if user.user_id == user_id]
        return found_users
