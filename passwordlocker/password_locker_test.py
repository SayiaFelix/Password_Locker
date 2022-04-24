import unittest                             # Importing the unittest module
import pyperclip                            # Importing the pyperclip module
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
        self.new_user.save_user()                  #For saving the user input
        self.assertEqual(len(User.user_list),1)


    def tearDown(self):
            '''
            tearDown method to clean up each test case after has run.
            '''
            User.user_list = []

    def test_save_multiple_users(self):
        '''
        To save multiple users in our list
        '''  
        self.new_user.save_user()
        test_user=User("Rensia","23455")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user details from our User list
            '''
            self.new_user.save_user()
            test_user = User("Rensia","23455")           # new contact
            test_user.save_user()
            self.new_user.delete_user()                   # Deleting a user object
            self.assertEqual(len(User.user_list),1)

    def test_find_user_by_number(self):
        '''
        test to check if we can find a user by username and display information
        '''

        self.new_user.save_user()
        test_user = User("Rensia","23455")               # new contact
        test_user.save_user()

        found_user = User.find_by_number("23455")
        self.assertEqual(found_user.username,test_user.username)


    def test_display_all_users(self):
        '''
        method that returns a list of all users input saved
        '''
        self.assertEqual(User.display_user(),User.user_list)
    

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_user.save_user()
        test_user = User("Rensia","23455") # new contact
        test_user.save_user()

        user_exists = User.user_exist("23455")

        self.assertTrue(user_exists)
    


if __name__=="__main__":
    unittest.main()
