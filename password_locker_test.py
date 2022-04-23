import unittest                             # Importing the unittest module
from password_locker import User            # Importing the User class from passwordlocker file

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the User class behaviours.
    '''

    def setUp(self):                      # Seting up method to run before test cases.
        
          self.new_user = User("Sir Felix","12345678",)  # create User instances

      
    def test_init(self):                                      #Testing if the object has been initialized properply.
        self.assertEqual(self.new_user.username,"Sir Felix")  
        self.assertEqual(self.new_user.password,"12345678")  
    
    def test_save_user(self):                      #To check if the user detatils has been saved correctly
        self.new_user.save_user()              #For saving the user input
        self.assertEqual(len(User.user_list),1)


if __name__=="__main__":
    unittest.main()
