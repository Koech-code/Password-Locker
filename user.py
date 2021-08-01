class User:
    '''
    This is a user class that helps generate new instances of a user.
    '''
    
    user_list=[]

    def __init__(self,userName,userPassword):
        '''
        This is a method that will define the user properties.
        '''

        self.userName=userName
        self.userPassword=userPassword
    
    def save_user(self):
        '''
        This creates a method that saves each instance of a user into the user_list
        '''

        User.user_list.append(self)

    @classmethod
    def display_users(cls):
        return cls.user_list

    def delete_users(cls):
        '''
        This is a method that deletes saved contacts in a user_list
        '''
        User.user_list.remove(self)        
     

