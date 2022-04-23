#!/usr/bin/env python3.9

from ast import While
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

def find_by_username(accountusername):
    return Credentials.find_by_username(accountusername)

def display_account():
    return Credentials.display_account()   



def main():
    while True:
        print("\n")
        name = input("Enter Your Name: ")
        print(f"Hello {name}, Welcome to Sir Felix Password Hub.")
        print("\n")
        print("Use 'na' to create New Account if you dont have an existing account: \n or 'lg' to login to your existing account:")




if __name__ == '__main__':

    main()