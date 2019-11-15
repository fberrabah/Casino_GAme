from math import ceil #add ceil for win with same color
from random import randrange  #add randrange for random number
import sys #for quit program with sys.exit()

print("---------------------------------")
print("Bienvenue au jeu de la roulette.") #visual information game 
print("---------------------------------")

money = 50 #player wallet
while int(money) > 0 : # firt loop when money as > at 0
        if money > 0 : 
            bet=int(input("Veuillez entrer votre mise : "))     
            if bet < 1 or bet > money :         
                bet=int(input("Veuillez entrer une mise possible : ")) #if answer not possible 
        if bet <= money :
            choice=int(input("choisisser votre numero entre 1 et 50 : ")) #add input with choice for number
            if choice < 1 or choice > 50 : #if choise is not in range 1 at 50
                choice=int(input("Attention, il faut choisir un numero entre 1 et 50 : "))
        