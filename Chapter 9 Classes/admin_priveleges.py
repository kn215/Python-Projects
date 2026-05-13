from User_Modules import User
class Admin(User):

    def __init__(self, first_name, last_name, username, job_title):
        super().__init__(first_name, last_name, username, job_title)
        #self.priveleges = ['modify users', 'add users', 'remove users', 'reset passwords']
        self.priveleges = Priveleges()

class Priveleges():
    def __init__(self, priveleges=[]):
        self.priveleges = priveleges         
        
    def show_priveleges(self):
        print(f"\nThe administrator role can perform the following functions")
        if self.priveleges:
            for privelege in self.priveleges:
                print(f"- {privelege}")
        else:
            print("- This user has no privileges")