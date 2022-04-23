from requests import delete
import pyperclip                #Importing pyperclip

class User:
    '''
    Class that generate User Intances.
    '''
    user_list=[]                              #Empty user list to store/save our username and password
    
    def __init__(self, username, password):

        '''
        Function for intantiating the user input
        '''
         
        self.username=username
        self.password= password

    def save_user(self):     
        '''
        Function for saving username and password on the list
        '''
        User.user_list.append(self)

    
    def delete_user(self):
        '''
        Function for delete user input from user list
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
    def copy_password(cls,username):
        password_found = User.find_by_username(username)
        pyperclip.copy(password_found.password)

#End of class User

#Start of class Credential

class Credentials:
    '''
    Class that generate user credentials.
    '''    
    user_account=[]                             #Empty user list to store/save our username and password
    
    def __init__(self, accountusername, accountpassword):

        '''
        Function for intantiating the user input for our object
        '''
        self.accountusername= accountusername
        self.accountpassword= accountpassword


    def save_account(self):     
        '''
        Function for saving user account
        '''
        Credentials.user_account.append(self)

    def delete_account(self):
        '''
        Function for delete credential input from user list
        '''
        Credentials.user_account.remove(self)

    @classmethod
    def find_by_username(cls,accountusername):
            '''
            Method that takes in a username and returns a user input that matches that username.
            '''
            for account in cls.user_account:
                if account.accountusername == accountusername:
                    return account

    @classmethod
    def display_account(cls):
        '''
        method that returns the account imput list
        '''
        return cls.user_account


    @classmethod
    def copy_password(cls,accountpassword):
        password_found = Credentials.find_by_username(accountpassword)
        pyperclip.copy(password_found.password)

