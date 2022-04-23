
class User:
    '''
    Class that generate User Intances.
    '''
    user_list=[] #Empty user list to store/save our username and password
    
    def __init__(self, username, password):
        self.username=username
        self.password= password