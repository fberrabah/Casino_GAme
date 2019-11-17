from math import ceil #add ceil for win with same color
from random import randrange  #add randrange for random number
import sys #for quit program with sys.exit()

print("---------------------------------")
print("Bienvenue au jeu de la roulette.") #visual information game 
print("---------------------------------")

choice = 0
bet = 0
money = 50 #player wallet
while int(money) > 0 : # firt loop when money as > at 0
        bet=input("Veuillez entrer votre mise : ")
        try:
            bet=int(bet)     
        except ValueError:
            print("vous n'avez pas saisi de nombre")
            bet = -1
            continue
        if money > 0 : 
            
            if bet < 1 or bet > money :         
                bet=input("Veuillez entrer une mise possible : ") #if answer not possible 
        if bet <= money :
            choice=input("choisisser votre numero entre 1 et 50 : ") #add input with choice for number
            try :
                choice = int(choice)
            except ValueError:
                print("vous n'avez pas saisi de nombre entre 1 et 50 :")
                choice = -1
                continue

            if choice < 1 or choice > 50 : #if choise is not in range 1 at 50
                choice=int(input("Attention, il faut choisir un numero entre 1 et 50 : ")) 

            computer = randrange(1,50) # Add random range for choise a number between 1 and 50
            print ("Faite vos jeu! rien ne va plus!!")
            print ("Et la roue s'arrete sur sur sur .... le numéro", computer) #display random number

            if computer == choice : # if same number between computer and choise winner!
                print("Bravo vous avez gagné !!",bet * 3, "$") #display how he win
                money += bet * 3  #calculation of gain

            elif computer%2 == choice%2 : #if number are even and odd 
                bet = ceil(bet * 0.5) 
                print ("Vous avez joué la bonne couleur!!")
                print ("Vous avez donc gagné la moitié de votre mise soit",bet,"$") #display how he win
                money += bet

            else : #if player loose 
                print("Perdue...")
                money -= bet
            if money <= 0: # if player dont have money the games if finish
                print("Désolé mais la maison ne fait pas credit! je vous accompagne à la sortie.")
            
            else: 
                print("Vous avez désormais",money,"$") #when the game is finish i display money
                while True : # condition for player if want replay
                    replay=input("Voulez-vous rejouer? oui/non ").lower() #.lower for translate upper in lower
                    if replay == "oui": #if say yes 
                        print("Voici votre pot",money,"$") #display money 
                        break #break the while for restart the game at first while 
                    elif replay == "non":
                        print("Vous repartez avec",money,"$") #display money again
                        print("A bientôt.")
                        sys.exit() #for exit program 
                    else:
                        print("C'est oui ou non!!") #if answer are not oui ou non 