from requests import delete
import pyperclip                #Importing pyperclip

class User:
    '''
    Class that generate User Intances.
    '''
    user_list=[] #Empty user list to store/save our username and password
    
    def __init__(self, username, password):

        '''
        Function for intantiating the user input
        '''
         
        self.username=username
        self.password= password

    def save_user(self):     
        '''
        Function for saving username and password
        '''
        User.user_list.append(self)

    
    def delete_user(self):
        '''
        Function for delete user input
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_username(cls,username):
            '''
            Method that takes in a username and returns a user input that matches that username.
            '''
            for user in cls.user_list:
                if user.username == username:
                    return user
   
    
    @classmethod
    def display_user(cls):
        '''
        method that returns the user imput list
        '''
        return cls.user_list
    @classmethod
    def copy_password(cls,password):
        password_found = Credential.find_by_username(password)
        pyperclip.copy(password_found.password)

#End of class User

#Start of class Credential

class Credential:
    '''
    Class that generate copy user credentials.
    '''    
    user_list=[]                             #Empty user list to store/save our username and password
    
    def __init__(self, username, password):

        '''
        Function for intantiating the user input for copying
        '''
        self.username= username
        self.password= password


    @classmethod
    def find_by_username(cls,username):
            '''
            Method that takes in a username and returns a user input that matches that username.
            '''
            for user in cls.user_list:
                if user.username == username:
                    return user

    @classmethod
    def copy_password(cls,password):
        password_found = Credential.find_by_username(password)
        pyperclip.copy(password_found.password)
