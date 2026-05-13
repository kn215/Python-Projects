class User:
    def __init__(self, first_name, last_name, username, job_title):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username.lower()
        self.job_title = job_title.title()

    def describe_user(self):
        print(f"\nFirst Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Job Title: {self.job_title}")

    def greet_user(self):
        print(f"\nHello {self.first_name} {self.last_name} welcome to the team!")
        
user_1 = User('steve', 'young', 'Syoung', 'project manager')
user_2 = User('Gordon', 'Bombay', 'GBOMBAY', 'director' )
user_3 = User('bob', 'ross', 'BrOsS', 'artist')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()