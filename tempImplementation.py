from playerClass import player
import random


def gameDeclaration():
	testPlayer = player()
	
	regFile = open('regex.txt', 'r')		#open the regex expression file
	exprList = regFile.read().splitlines()	#create a list from the regex expressions
	control = "Yes"
	listRead = 0
	
	while(control == "Yes"):
		checkInput = input("Enter what the first expression is")
		if(checkInput == exprList[listRead]): #check first expression 
			print("You have entered the correct expression!")
			testPlayer.addScore()
			testPlayer.printScore()
			contPlay = input("Would you like to play again? Type Yes to continue, type No to quit\n")
			if(contPlay == "No"):
				return 1
			if(contPlay == "Yes"):
				control = "Yes"
				listRead = listRead + 1
		else:
			print("False! Try again please")
		
	
gameDeclaration()
	
		
