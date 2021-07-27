import random 
import string

def options():
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chars1 = 'abcdefghijklmnopqrstuvwxyz'
    chars2 = '0123456789'
    chars3 = '!@#$%^&*()?<>:.'

    combined_list = chars + chars1 + chars2 + chars3

    ret = ""
    length = int(input("Password Length: "))

    upperCase = input("Would you like uppercase letters? Y/N")
    if upperCase == "Y": 
        ret += chars 

    lowerCase = input("Would you like lowercase letters? Y/N")
    if lowerCase == "Y": 
        ret += chars1

    numbers = input("Would you like numbers? Y/N")
    if numbers == "Y": 
        ret += chars2

    SpecialCharacters = input("Would you like to include any special characters? Y/N ")
    if SpecialCharacters == "Y": 
        ret += chars3 
    
    return [length,ret]






