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

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        ''' 

        User.user_list=[]
    
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

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        ''' 

        Credentials.credentials_list=[]

    def test_init(self):
        '''
        A test case that checks if the new credential objects have been initialized correctly
        '''    
        
        self.assertEqual(self.new_credential.account,"nixonkipkorir01@gmail.com")
        self.assertEqual(self.new_credential.userName,"Nixon Kipkorir")
        self.assertEqual(self.new_credential.password,"12345")


    def test_save_credential(self):
        '''
        A test case to check if we can save a new user credentials
        '''

        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list),1)

   
    def test_save_multiple_accounts(self):
        '''
        This is a test case that tests if we can save more than one account to the credentials_list
        '''

        self.new_credential.save_credential()
        test_credential=Credentials("Twitter","nickyJuniour01","54321")
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list),2)

    

    def test_delete_credentials(self):
        '''
        This is a test case that checks if we can delete saved credentials in the credentials_list
        '''    

        self.new_credential.save_credential()
        test_credential=Credentials("Twitter","nickyJuniour01","54321")
        test_credential.save_credential()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    
    def test_find_credentials(self):
        '''
        This is a test case to check if we can find saved credentials in the credential_list using the account name
        '''

        self.new_credential.save_credential()
        test_credential=Credentials("Twitter","nickyJuniour01","54321")
        test_credential.save_credential()

        search_credential=Credentials.find_credentials("Twitter")
        self.assertEqual(search_credential.account, test_credential.account)

    def test_credential_exist(self):
        '''
        Test to check if we can return a true or false based on whether we find or miss the credential.
        '''
        self.new_credential.save_credential()
        test_credential=Credentials("Twitter","nickyJuniour01","54321")
        test_credential.save_credential()

        credential_is_found = Credential.credential_exist("Twitter")
        self.assertTrue(credential_is_found)

    def test_dispaly_credentials(self):
        '''
        Test case that checks if we can display all saved credentials from the credentials_list
        '''

        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)


if __name__ == '__main__':
    unittest.main()           




