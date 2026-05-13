from User_Modules import User
from admin_priveleges import Priveleges
from admin_priveleges import Admin



ken = Admin('ken', 'ken', 'kken', 'administrator')
ken.describe_user()
ken.priveleges.show_priveleges()
ken_priveleges = ['add users', 
                  'remove users', 
                  'update passwords']
ken.priveleges.priveleges = ken_priveleges

ken.priveleges.show_priveleges()