#!/usr/bin/env python3

#This script take a given email adress and output the username and the domain

email = input("Enter your email adress: ").strip()

username = email[:email.index('@')]

domain = email[email.index('@') + 1:]

print(f"Your username is {username} and the domain is {domain} ")

