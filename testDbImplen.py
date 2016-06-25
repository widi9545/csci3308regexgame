#!/usr/bin/python
import MySQLdb
from playerClass import player
import random
db=MySQLdb.connect()


db = MySQLdb.connect("localhost", "regexMemoryGame", "root", "questions")
cur = db.cursor()
questions =[]




def dbRead():
	for dbread in cur.fetchone():
		questions.append(dbread)
		



def gameDeclaration():
	testPlayer = player()
	#Questions go in as ('a',) what can we do about this?
	control = "Yes"
	listRead = 0
	
	
	while(control == "Yes"):
		checkInput = input("Enter what the first expression is")
		cur.execute("SELECT Question FROM easy")
		dbRead()
		
		
		if(checkInput == questions[listRead]): #check first expression 
			print "You have entered the correct expression!"
			testPlayer.addScore()
			testPlayer.printScore()
			contPlay = input("Would you like to play again? Type 'Yes' to continue, type 'No' to quit\n")
			if(contPlay == "No"):
				return 1
			if(contPlay == "Yes"):
				control = "Yes"
				listRead = listRead + 1
				dbRead()
		else:
			print "False! Try again please"
gameDeclaration()
