"""guidelines

length - input

case sensitivity

numbers

punctuiation 

"""

'''generatePass( [int length, bool case sensitive, bool numbers, bool punctuation])'''

import random
import math

#def case():
    


#def numb():


#def punct():

lst1 = "abcdefghijklmnopqrstuvwxyz"

lst2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lst3 = "0123456789"

lst4 = "!@#$%^&*"


length = int(input("How long do you want your password to be?: "))

lst = [length,lst2+lst3+lst1+lst4] 


def genPass(lst):

    i = 0

    ret = ""

    while i < lst[0]:
        i += 1

        pass1 = random.random()
        
        pass1 = len(lst[1]) * pass1
        
        passW = math.floor(pass1)
        
        ltrs = lst[1][passW]



        ret += ltrs
    

    return ret

'''genPass(lst)
print(genPass(lst))

while True:
    passacc = input("do you like your password? (Yes to continue, No to get another): ")
    if passacc == "No":
        genPass(lst)
        print(genPass(lst))
    elif passacc == "Yes":
        break'''



