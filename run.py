#!/usr/bin/env python3.6

from user import User
from credentials import Credentials

def create_new_user(userName,userPassword):
    '''
    This is a function that creates a new user using a user name and a password
    '''
    
    new_user=User(userName,userPassword)
    return new_user

def save_user(user):
    '''
    A function that saves the new user
    '''  
    user.save_user() 

def display_users(self):
    '''
    Function to display all the saved users in the user_list
    '''
    return User.display_users()

def login_user(userName, userPassword):
    '''
    Function to login new user only. Checks if the user had been logged in earlier and logs in if not yet. 
    '''
    verify_user=Credentials.check_user(userName,userPassword)
    return verify_user

def create_new_credential(account,userName,userPassword):
    '''
    Function that creates new user credentials for a particular account
    '''
    new_credential=Credentials(account,userName,userPassword)
    return new_credential

def save_credentials(credentials):
    '''
    Function that saves the entered user account credentials
    '''
    credentials.save_credentials

def display_credential_details():
    '''
    A function that displays all the details in our credentials
    '''
    return Credentials.display_credentials

def delete_credential(credentials):
    '''
    A function that deletes particular selected credentials
    '''

    credentials.delete_credentials

def find_credential(account):
    '''
    A function that searches for a saved credential using the account name
    '''
    return Credentials.find_credential(account)

def check_credential(account):
    '''
    Function to check  credential already exist in the credential_list, returns a boolean
    '''
    return Credentials.credential_exist(account)

def generatePassword():
    '''
    Function that generates random passwords for the user account
    '''    
    auto_generate_password=Credentials.systemGeneratedPassword()
    return auto_generate_password

def copy_credential(account):
    '''
    A function that copies credentials using the pyperclip framework.
    We import the framework then declare a function that copies the credentials
    '''
    return Credentials.copy_credentials(account)


def passwordManager():
    print("I would like to know your name please.")
    user=input()
    print(f"Hello {user} I am happy to be your one place store for all your passwords")
    print("Use any of the following to proceed\n CA...Create New Account. \n LI...Login to your account.")
    short_code=input(" ").lower().strip()
    if short_code=="ca":
        print("Sign Up")
        print("*"*10)
        userName=input("user_name: ")
        
        while True:

            print("TP...To type your own password \n GP...If you want the system to generate a random password for you.")
            password_choice=input().lower().strip()
            if password_choice=="tp":
                password=input("Enter your password: ")
                break
            elif password_choice=="gp":
                password=generatePassword()
                break
            else:
                print("You must either input your own password or allow the system to generate it for you by just typing gp")

        save_user(create_new_user(userName,password))
        print("."*10)
        print(f"{userName}, your account has been created successfully!!! and {password} is the password that the system has generated for you.")
        print("."*10)

    elif short_code=="li":
        print("*"*10)
        print("Enter you user name and password to login: ")
        print("."*10)
        userName=input("Type your user name: ")
        password=input("Password: ")
        login=login_user(userName,password)
        if login_user == login:
            print(f"{userName} there you are! Welcome to your password locker manager")
    while True:
        print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A random password \n D - Delete credential \n EX - Exit the application \n")
        short_code = input().lower().strip()

        if short_code=="cc":
            print("Create New Credential")
            print(".."*5)
            print("Your account name...")
            account=input().lower()
            print("Your account user name")
            userName=input()
            while True:
                print(" TP - To type your own pasword if you already have an account:\n GP - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Your Password\n")
                    break
                elif password_Choice == 'gp':
                    password = generatePassword()
                    break
                else:
                    print("You must either enter your own password or gp to allow the system to create it for you.")
            save_credentials(create_new_credential(account,userName,password))
            print(f"The account credentials of {account} account, with {userName} and a password of {password} have been created successfully.")
        elif short_code=="dc":
            if  display_credential_details():
                print("Here is your list of account")
                print("-"*10)
                for account in display_credential_details():
                    print(f"Account:{account.account} \n user_name: {userName} \n password: {password}")
                    print("-"*10)
                
                else:
                    print("There are no credentials yet.")
        elif short_code=="fc":
            print("Enter the account name of the of the credentials you wish to search")
            search_account=input().lower()
            if find_credential(search_account):
                search_credential=find_credentials(search_account)
                print(f"Account Name : {search_credential.account}")
                print('-' * 10)
                print(f"")




                 


if __name__ == '__main__':

    passwordManager()                        
