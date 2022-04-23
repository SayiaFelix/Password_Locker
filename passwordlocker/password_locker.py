from requests import delete


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

