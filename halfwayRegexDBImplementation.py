#!/usr/bin/python
import MySQLdb
from playerClass import player
import random



db = MySQLdb.connect("127.0.0.1", "root", "root", "regexQuestions")
cur = db.cursor()
questionList =[]
answerList = []




def questionRead():
	for dbread in cur.fetchone():
		questionList.append(dbread)
		
def answerRead():
	for answerread in cur.fetchone():
		answerList.append(answerread)
		
		
def fillQuestionList():
	cur.execute("SELECT question FROM questions")
	row = cur.fetchone()
	while row is not None:
		questionList.append(row)
		row = cur.fetchone()
	print questionList[3]
	return 1
	
def fillAnswerList():
	cur.execute("SELECT answer FROM answers")
	row = cur.fetchone()
	while row is not None:
		answerList.append(row)
		row = cur.fetchone()
	return 1



def gameDeclaration():
	testPlayer = player()
	control = "Yes"
	questionIndex = 0
	answerIndex = 0
	fillQuestionList()
	fillAnswerList()
	
	
	while(control == "Yes"):
		print "The question is: "
		print questionList[questionIndex]
		checkInput = input("Enter the corresponding regex statement: ")
		
		if(checkInput == answerList[answerIndex]): #check first expression 
			print "You have entered the correct expression!"
			testPlayer.addScore()
			testPlayer.printScore()
			contPlay = input("Would you like to play again? Type 'Yes' to continue, type 'No' to quit\n")
			if(contPlay == "No"):
				return 1
			if(contPlay == "Yes"):
				control = "Yes"
				questionIndex = questionIndex + 1
				answerIndex = answerIndex + 1
		else:
			print "False! Try again please"
			
			
gameDeclaration()
