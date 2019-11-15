from math import ceil #add ceil for win with same color
from random import randrange  #add randrange for random number
import sys #for quit program with sys.exit()

print("---------------------------------")
print("Bienvenue au jeu de la roulette.") #visual information game 
print("---------------------------------")

money = 50 #player wallet
while int(money) > 0 : # firt loop when money as > at 0
        if money > 0 : 
        bet=int(input("Veuiller entrer votre mise : "))     
        if bet < 1 or bet > money :         
            bet=int(input("Veuillez entrer une mise possible : ")) #if answer not possible 