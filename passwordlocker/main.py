#!/usr/bin/env python3.9

from random import randint
import random
import string
from password_locker import User     #Importing user from password Locker file
from password_locker import Credentials   #Importing Credentials class from Password Locker file

def create_user( username,password):     #Creating instances for user input
    '''
    create a new user
    '''
    new_user= User(username,password)
    return new_user

def save_user(User):
    '''
    Function to save users
    '''
    User.save_user()

def delete_user(User):
     '''
     Function to delete user
     '''
     User.delete_user()

def find_user(number):
    '''
    Function to find users
    '''
    return User.find_by_number(number)

def check_existing_user(number):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return User.user_exist(number)

def display_user() :
    '''
    Function to display users
    '''
    return User.display_user()


def create_account( accountusername,accountname,accountpassword):     #Creating instances for user Credentials
    new_account = Credentials(accountusername,accountname,accountpassword)
    return new_account
    
def save_account(User):
    '''
    Function to save Credentials
    '''
    User.save_account()

def delete_account(User):
    '''
    Function to delete credentials
    '''
    User.delete_account()

def find_account(number):
    '''
    Function to find Credentials
    '''
    return Credentials.find_by_number(number)

def display_account():
    '''
    Function to display Credentials
    '''
    return Credentials.display_account()   



def main():
    '''
    Main Function
    '''
    while True:
        print("\n")
        print(f"Welcome to Sir Felix Password Hub.")
        print("Use the following short codes to navigate through the application::: \n \n 'na' to create New Account if you dont have an existing account::  \n 'dc' to Display Your Details:: \n 'fc' to search for existing user account and delete it if you want::: \n 'lg' to login to your existing account::: \n 'ex' to exit:::")
        print("************************************************************************************")
        choice = input().lower()
        if choice =="na":
            print("\n")
            print("Create New Account:")
            print("--------------------")
            print("\n")
            print("Enter Your Name: ")
            Username= input()
            print("Enter Your Password: ")
            password= input()
            save_user(create_user(Username,password))
            print("\n")
            print("CONGRADULATION!!!!! \n Your acount was successfully Created, here are your account details:")
            print("---------------------------------------------------------------------------------")
            print(f" Username:: {Username} \n Password:: {password}" )
            print("\n")
            print("Use the above details to LOGIN in Your Account:::")
            print("---------------------------------------------------")
        elif choice == 'dc':
            if display_user():
             print('\n')
             print("Here is a list of all your contacts")
            
             for user in display_user():
              print(f" Username:: {user.username} \n Password:: {user.password}")
              print('\n')
            else:
             print('\n')
             print("You dont have any account saved yet")
             print('\n')
        elif choice == 'fc':
             print("Enter the PASSWORD for the account you want to search for SECURITY reasons!!!!")
             number = input()
             if check_existing_user(number):
              search_user = find_user(number)
              print('-' * 20)
              print(f"Username::: {search_user.username}")
              print(f"Password::: {search_user.password}")
              print("\n")
              print(f"Do you want to delete this account from your account List ?????? \n \n Username::: {search_user.username} \n Password::: {search_user.password} \n ")
              print("if YES select 'y' and 'n' for NO :::::")
              decisionInput = input().lower()
              if decisionInput == 'y':
                 delete_user(search_user)
                 print(f"You have successfully deleted {search_user.username} {search_user.password} from your account list.")
                 print("\n")
              elif decisionInput == 'n':
                 print("You have not deleted any account, try again later::::")
              else:
                 print("Sorry I didn't get that")
             else:
                 print("That User does not exist")
       
        elif choice == "lg":
            print("Login in to Your Existing Account at Sir Felix Hub:")
            print("----------------------------------------------------")
            print("Enter Your Username:")
            loginUsername = input()
            print("Enter Your Password:")
            loginPassword = input()
            if find_user(loginPassword):
                print("\n")
                print("You can create Multiple Accounts(AC) and check there status (CS):")
                print("-----------------------------------------------------------------")
                print("Use 'AC' for creating multiple Account or 'CS' for checking the existing accounts:::")
                option = input().upper()
                print("\n")
                if option == "AC":
                    print("Add Your Account::")
                    print("-------------------")
                    accountusername = loginUsername
                    print("\n")
                    print("Account Name:")
                    accountname =input()
                    print("\n")
                    print("To Use Automated Password: SELECT 'AP' or Create your Own Password: SELECT 'CP'.")
                    print("---------------------------------------------------------------------------------")
                    print("\n")
                    decision = input().upper()
                    if decision == "AP":
                        characterspassword = string.ascii_letters + string.digits + string.ascii_lowercase
                        accountpassword =" ".join(random.choice(characterspassword)for x in range(randint(8,16)))
                        print(f"password: {accountpassword}")

                    elif decision == "CP":
                        print("Enter Your Password::")
                        accountpassword = input()
                    else:
                        print("Kindly, Enter a VALID Choice!!!!")
                    save_account(create_account(accountusername,accountname, accountpassword))
                    print("\n")
                    print("CONGRATULATIONS!!!!!!!!!!! Here are your Account Details.")
                    print("----------------------------------------------------------")
                    print("\n")
                    print(f" Username::: {accountusername} \n Account Name::: {accountname} \n Password::: {accountpassword}")

                elif option=="CS":
                    if find_account(accountusername):
                        print("\n")
                        print("Here is the List of your Created Accounts::")
                        print("---------------------------------------------")
                        for User in display_account():
                            print(f"Account Name:: {User.accountname} \n Password:: {User.accountpassword}")
                            print("\n")
                            print("\n")
                    else:
                        print("Your Credentials were INVALID!!!!")

                else:   
                    print("FAILED!!!!!!!! Please Try Again Later.")   
                    print("\n")
            
            else:
                print("FAILED!!!!!  Your information were incorrect,try again. \n THANK YOU")
                print("\n")
        
        elif choice == "ex":
             print("Hope You enjoyed. Thank You!!!! \n GoodBye!!")
             print("\n")
             break

        else:
            print("Kindly, Choose a valid option and try again!!")
            print("\n")

if __name__ == '__main__':
          main()