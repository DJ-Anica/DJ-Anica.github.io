# -*- coding: utf-8 -*-

# Created on Wed May 11 09:44:02 2022

# @author: David Anica

"""
Simple weight converter
"""

# Script 1
"""
print("\nSimple Weight converter")

print("\n")
weight = input("Weight(number only): ")
unit = input("Kg or Lbs (type L or K only): ")

kg = float(weight) * 0.453592
lbs = float(weight) * 2.20462

if unit == "l":
    print(f"Weight in Kg: {kg}")
if unit == "L":
    print(f"Weight in Kg: {kg}")
if unit == "k":
    print(f"Weight in Lbs: {lbs}")
if unit == "K":
    print(f"Weight in Lbs: {lbs}")
    
"""

# Script 2

print("Simple Weight converter")

unit = input("\n(K)g or (L)bs: ")
weight = input("\nWeight #: ")

kg = float(weight) * 0.453592
lbs = float(weight) * 2.20462

if unit == "l" or unit == "L":
    print(f"\nWeight in Kg: {kg} kg")
if unit == "k" or unit == "K":
    print(f"\nWeight in Lbs: {lbs} lbs")
