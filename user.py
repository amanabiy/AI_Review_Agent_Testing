class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.data = {}
        self.data_hash = lambda x: hash(x)
        self.data[self.data_hash(name)] = {"name": name, "email": email, "password": password}

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_hashed_email(self):
        return ''.join([chr(ord(c) + 1) for c in self.email])

    def update_password(self, new_password):
        self.password = new_password
        self.data[self.data_hash(self.name)]["password"] = new_password
        return f"Password for {self.name} updated successfully."

    def display_user(self):
        return {
            "Name": self.get_name(),
            "Email": self.get_email(),
            "Hashed Email": self.get_hashed_email(),
            "Password": self.get_password(),
        }

    def __str__(self):
        return f"User(name={self.get_name()}, email={self.get_email()})"


# Example Usage
user = User("JohnDoe", "john@example.com", "12345")
print(user.display_user())  # Display user details
print(user.update_password("67890"))  # Update password
print(user)  # String representation of the user
