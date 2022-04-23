#!/usr/bin/env python3.9

from ast import While
from random import randint
import string
from tkinter.tix import Select

from cupshelpers import Printer
from password_locker import User     #Importing user from password Locker file
from password_locker import Credentials   #Importing Credentials class from Password Locker file

def create_user( username,password):     #Creating instances for user input
    new_user= User(username,password)
    return new_user

def save_user(User):
    User.save_user()

def delete_user(User):
    User.delete_user()

def find_by_username(username):
    return User.find_by_username(username)

def display_user() :
    return User.display_user()


def create_account( accountusername,accountpassword):     #Creating instances for user Credentials
    new_account = Credentials(accountusername,accountpassword)
    return new_account
    
def save_account(Credentials):
    Credentials.save.account()

def delete_account(Credentials):
    Credentials.delete_account()

def find_by_username(number):
    return Credentials.find_by_username(number)

def display_account():
    return Credentials.display_account()   



def main():
    while True:
        print("\n")
        name = input("Enter Your Name: ")
        print(f"Hello {name}, Welcome to Sir Felix Password Hub.")
        print("\n")
        print("Use 'na' to create New Account if you dont have an existing account: \n or 'lg' to login to your existing account:")
        print("\n")
        print("**********************************************************")
        print("\n")


        choice = input().lower
        if choice =="na":
            print("\n")
            print("Create New Account:")
            print("-------------------------------------------------------")
            print("\n")
            print("Enter Your Name: ")
            Username= input()
            print("\n")
            print("Enter Your Password: ")
            password= input()

            save_user(create_user(Username,password))
            print("\n")
            print("CONGRADULATION!!!!! Your acount was successfully Created. \n Here are your account details:")
            print("----------------------------------------------------------")
            print("\n")
            print(f"Name: {Username} \n Password:{password}" )
            print("\n")
            print("Use this Details to login in Your Account:")
            print("\n")
            print("\n")

        elif choice == "lg":
            print("Login in to Your Existing Account at Sir Felix Hub:")
            print("-------------------------------------------------------------")
            print("\n")
            print("Enter Your Username:")
            loginusername= input()
            print("Enter Your Password:")
            loginpassword= input()

            if find_by_username(loginpassword):
                print("\n")
                print("You can create Multiple Accounts(AC) and check there status (CS):")
                print("------------------------------------------------------------")
                print("\n")
                print("Select 'AC' or 'CS' :")

                option = input().upper
                print("\n")
                if option == "AC":
                    print("Add Your Account::")
                    print("-------------------------------------------------------")
                    accountusername = loginusername
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







if __name__ == '__main__':

    main()