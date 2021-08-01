import random
import pyperclip
import string

class Credentials:
    '''
    This is a credentials class that creates new instances credentials
    '''

    credentials_list=[]

    @classmethod
    def check_user(self, userName, userPassword):
        '''
        This is a method that first checks if the user is already in the user_list or not
        '''

        first_user=""
        for user in User.user_list:
            if (user.userName==userName and user.userPassword==userPassword):
                first_user=userName

        return first_user

    def __init__(self,account,userName, password):
        '''
        A method that defines user credentials to be stored
        '''    
        self.account=account
        self.userName=userName
        self.password=password

    def save_credential(self):
        '''
        A method that will help us save new credential details into the credentials_list
        '''   
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        This is a method that deletes the saved credentials in the credentials_list
        '''    

        Credentials.credentials_list.remove(self)
    
    @classmethod
    def find_credentials(cls, account):
        '''
        This is a method that helps a user search for saved credentials using the account name
        '''

        for credential in cls.credentials_list:
            if credential.account==account:
                return credential

    @classmethod
    def copy_credentials(cls, account):
        '''
        A method that copies my credentials to the clipboard
        '''

        found_credentials=Credentials.find_credentials(account)
        pyperclip.copy(found_credentials.account)
        pyperclip.copy(found_credentials.userName)
        pyperclip.copy(found_credentials.password)

    @classmethod
    def display_credentials(cls):
        '''
        This is a method that displays all credentials in the credential_list
        '''
        
        return cls.credential_list

    def systemGeneratedPassword(passwordLength=10):
        '''
        Allows the system to generate a random password for you. A password that has has numerals, alphabets and special characters
        '''

        password=string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%^&*"

        return ''.join(random.choice(password) for i in range (passwordLength))











    






