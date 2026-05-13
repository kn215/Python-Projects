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

# class Admin(User):

#     def __init__(self, first_name, last_name, username, job_title):
#         super().__init__(first_name, last_name, username, job_title)
#         #self.priveleges = ['modify users', 'add users', 'remove users', 'reset passwords']
#         self.priveleges = Priveleges()

# class Priveleges():
#     def __init__(self, priveleges=[]):
#         self.priveleges = priveleges         
        
#     def show_priveleges(self):
#         print(f"\nThe administrator role can perform the following functions")
#         if self.priveleges:
#             for privelege in self.priveleges:
#                 print(f"- {privelege}")
#         else:
#             print("- This user has no privileges")