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

        




