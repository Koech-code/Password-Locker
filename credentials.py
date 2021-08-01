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








    






