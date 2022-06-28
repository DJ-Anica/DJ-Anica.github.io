# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 17:15:51 2022

@author: Mjolnir
"""

prompt = "\nEnter desired toppings "
prompt += "\nEnter 'done' when finished: "

topping = ""

while topping.lower() != "done":
    menu = ["cheese", "pepperoni", "onions", "meatballs", "mushrooms", "chicken", ]
    topping = input(prompt)
    reply = f"\nAdding {topping} to your pizza"
    
    if topping.lower() == "done":
        print("\n\nThank you, preparing your pizza now!")
        break
    if topping not in menu:
         print(f"\n{topping} is not a valid topping.")
    else:
        print(reply)