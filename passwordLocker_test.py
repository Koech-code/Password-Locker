import unittest
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):
    '''
    This is a sub-class that performs user tests
    '''
    def setUp(self):
        '''
        This is a method that runs before other methods in the user class runs
        '''

        self.new_user=User("Nixon Kipkorir","12345")

    def test_init(self):
        '''
        This is a test to check if an object has been instantiated correctly
        '''

        self.assertEqual(self.new_user.userName,"Nixon Kipkorir") 
        self.assertEqual(self.new_user.userPassword,"12345")
    
    def test_save_user(self):
        '''
        A test case to see if a new user has been saved into the user_list
        '''

        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):
    '''
    Created a sub-class that defines test cases for the Credential class
    '''
    def setUp(self):
        '''
        A method that runs before each credential tes methods run
        '''

        self.new_credential=Credentials("nixonkipkorir01@gmail.com","Nixon Kipkorir","12345")

    def test_init(self):
        '''
        A test case that checks if the new credential objects have been initialized correctly
        '''    
        
        self.assertEqual(self.new_credential.account,"nixonkipkorir01@gmail.com")
        self.assertEqual(self.new_credential.userName,"Nixon Kipkorir")
        self.assertEqual(self.new_credential.password,"12345")

        
if __name__ == '__main__':
    unittest.main()           




