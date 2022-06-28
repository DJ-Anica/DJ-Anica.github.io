# -*- coding: utf-8 -*-

#Created on Tue May 10 12:32:54 2022

#@author: David Anica

name = input("Hello! \nWhat is your name? ")
print(f"\nHello, {name.title()}, nice to meet you.")

year = input("\nWhat year were you born? ")
age = 2022 - int(year)
print("\nHm...")
print(f"According to my calculations, you are {age} years old.")

job = input("\nWhat do you want to be when you grow up? ")
print("\nThat's fantastic!")
print(f"As long as you work hard in school, you can be {job} or anything else you want.")


input("\nWhat's your favorite subject in school? ")

print("\nLook at you, smarty pants.")

input("\nDo you like music, yes or no? ")

band = input("\nWho is your favorite band of all time? ")

print(f"\nI know them! I love {band}, too! Jon Mess and Tilian are my favorite singers of all time.")
print("I love their new songs Synergy and Pop Off!")

input("\nDid you know... Your mom and dad love you very, very much? ")


print("\nGood. Never forget that.")
print("\nIt was nice meeting you.")
print(f"Have a nice day, {name.title()}, aka future {job[2:]}, and I hope you have fun listening to {band}'s new album, Jackpot Juicer, with your mom and dad.")

