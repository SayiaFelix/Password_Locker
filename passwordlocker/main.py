#!/usr/bin/env python3.9

from random import randint
import string
from password_locker import User     #Importing user from password Locker file
from password_locker import Credentials   #Importing Credentials class from Password Locker file

def create_user( username,password):     #Creating instances for user input
    new_user= User(username,password)
    return new_user

def save_user(User):
    User.save_user()

def delete_user(User):
    User.delete_user()

def find_user(number):
    return User.find_by_username(number)

def display_user() :
    return User.display_user()


def create_account( accountusername,accountname,accountpassword):     #Creating instances for user Credentials
    new_account = Credentials(accountusername,accountname,accountpassword)
    return new_account
    
def save_account(Credentials):
    Credentials.save.account()

def delete_account(Credentials):
    Credentials.delete_account()

def find_account(number):
    return Credentials.find_by_username(number)

def display_account():
    return Credentials.display_account()   



def main():
    while True:
        print("\n")
        
        print(f"Welcome to Sir Felix Password Hub.")
        print("\n")
        print("Use 'na' to create New Account if you dont have an existing account or 'lg' to login to your existing account and 'ex' to exit. \n NB: use lower case characters:::")
        print("**********************************************************")
        choice = input()
        if choice =="na":
            print("\n")
            print("Create New Account:")
            print("--------------------------------------------------------------------------")
            print("\n")
            print("Enter Your Name: ")
            Username= input()
            print("Enter Your Password: ")
            password= input()
            save_user(create_user(Username,password))
            print("\n")
            print("CONGRADULATION!!!!! \n Your acount was successfully Created. \n Here are your account details:")
            print("--------------------------------------------------------------------------")
            print(f"Name: {Username} \n Password:{password}" )
            print("\n")
            print("Use this Details to login in Your Account:")
           
        
        elif choice == "lg":
            print("Login in to Your Existing Account at Sir Felix Hub:")
            print("------------------------------------------------------------------------")
            print("Enter Your Username:")
            loginUsername = input()
            print("Enter Your Password:")
            loginPassword = input()
            if find_user(loginPassword):
                print("\n")
                print("You can create Multiple Accounts(AC) and check there status (CS):")
                print("------------------------------------------------------------")
                print("\n")
                print("Select 'AC' or 'CS' : \n NB: Use Upper Case Characters ::")

                option = input()
                print("\n")
                if option == "AC":
                    print("Add Your Account::")
                    print("-------------------------------------------------------")
                    accountusername = loginUsername
                    print("\n")
                    print("Account Name:")
                    accountname =input()
                    print("\n")
                    print("To Use Automated Password: SELECT 'AP' or Create your Own Password: SELECT 'CP'.")
                    print("-------------------------------------------------------")
                    print("\n")
                    decision = input().upper
                    if decision == "AP":
                        characterspassword = string.ascii_letters + string.digits + string.ascii_lowercase
                        accountpassword ="".join(choice(characterspassword)for x in range(randint(8,16)))
                        print(f"password: {accountpassword}")

                    elif decision == "CP":
                        print("Enter Your Password::")
                        accountpassword = input()
                    
                    else:
                        print("Kindly, Enter a VALID Choice!!!!")

                    save_account(create_account(accountusername,accountname, accountpassword))
                    print("\n")
                    print("CONGRATULATIONS!!!!!!!!!!! Here are your Account Details.")
                    print("-------------------------------------------------------")
                    print("\n")
                    print(f"Username: {accountusername} \n Accountname: {accountname} \n Password: {accountpassword}")

                elif option=="CS":
                    if find_account(accountusername):
                        print("\n")
                        print("Here is the List of your Created Accounts::")
                        print("-------------------------------------------------------")
                        for User in display_account():
                            print(f"Account:: {User.accountname} \n Password:: {User.accountpassword}")
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
             print("Hope You enjoyed. Thank You!!!!")
             print("\n")
             break

        else:
            print("Kindly, Choose a valid option and try again!!")
            print("\n")


if __name__ == '__main__':

    main()