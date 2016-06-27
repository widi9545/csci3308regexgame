#!/usr/bin/python
import MySQLdb
from playerClass import player
import random

##@package FinalImplementation
#This is the final implementation for the terminal version of our game. We have
#implemented our 'hardness-selection' functionality, we pull in from our database of questions
#and we are able to create a player and track their score.




##@var db
#This is the DB that we connect to, it holds all of our questions.
db = MySQLdb.connect("127.0.0.1", "root", "root", "regexQuestions") 
cur = db.cursor()
##@var questionList
#This is the list that we append all of our questions to. It's a simple python list
questionList =[]
##@var answerList
#This is the list we append all of our answers to. It's also a simple python list.
answerList = []

"""@package docstring
"""

##These are the functions for our "easy" mode, using basic questions. We pull a single
	#question/answer from the database at a time using a continuous for loop.
	#We then append the lists with questions/answers"""
		
def fillQuestionListBasic():
	
	cur.execute("SELECT question FROM questions")
	row = cur.fetchone()
	while row is not None:
		questionList.append(row)
		row = cur.fetchone()
	return 1
	
	
##These are the functions for our "easy" mode, using basic questions. We pull a single
#question/answer from the database at a time using a continuous for loop.
#We then append the lists with questions/answers
def fillAnswerListBasic():

	cur.execute("SELECT answer FROM answers")
	row = cur.fetchone()
	while row is not None:
		answerList.append(row)
		row = cur.fetchone()
	return 1

##Here is the function for our difficulty selector. It follows the same principle as above,
#except it has a input string check for Hard/Medium settings

def fillQuestionListDifficulty(difficultyString):

	
	if(difficultyString == "Hard"):
		cur.execute("select questions.question from questions, answers where questions.qid = answers.aid and questions.difficulty ='3'")
		row = cur.fetchone()
		while row is not None:
			questionList.append(row)
			row = cur.fetchone()
		return 1
	if(difficultyString == "Medium"):
		cur.execute("select questions.question from questions, answers where questions.qid = answers.aid and questions.difficulty = '2'")
		row = cur.fetchone()
		while row is not None:
			questionList.append(row)
			row = cur.fetchone()
		return 1
        return 0
##Here is the function for our difficulty selector. It follows the same principle as above,
#except it has a input string check for Hard/Medium settings. This fills the Answer List that we have
		
def fillAnswerListDifficulty(difficultyString):
	
	
	if(difficultyString == "Hard"):
		cur.execute("select answers.answer from questions, answers where questions.qid = answers.aid and questions.difficulty ='3'")
		row = cur.fetchone()
		while row is not None:
			answerList.append(row)
			row = cur.fetchone()
		return 1
	if(difficultyString == "Medium"):
		cur.execute("select answers.answer from questions, answers where questions.qid = answers.aid and questions.difficulty ='2'")
		row = cur.fetchone()
		while row is not None:
			answerList.append(row)
			row = cur.fetchone()
		return 1
        return 0		
     
		
##We declare an instance of the "player" class that we have declared
#

def gameDeclaration():
	
	
	testPlayer = player()
	##@var control
	#This is the control for our game. Depending on what the player types in,
	#it switches from easy questions, to medium questions, to hard questions.
	control = input("Type 'Yes' if you want to play a game with basic questions, type 'Medium' or 'Hard' if you want to play a game with Medium or Hard Questions ")
	#@var questionIndex
	#This is the index for our questionList
	questionIndex = 0
	#@var answerIndex 
	#this is the index for our answerList
	answerIndex = 0
	
	
	if(control == "Yes"):
		fillQuestionListBasic()
		fillAnswerListBasic()
	if(control == "Hard"):
		fillQuestionListDifficulty(control)
		fillAnswerListDifficulty(control)
	if(control == "Medium"):
		fillQuestionListDifficulty(control)
		fillAnswerListDifficulty(control)
	
	
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
		
	while(control == "Hard"):
		print "The question is: "
		print questionList[questionIndex]
		checkInput = input("Enter the corresponding regex statement: ")
		
		if(checkInput == answerList[answerIndex]): #check first expression 
			print "You have entered the correct expression!"
			testPlayer.addScore()
			testPlayer.printScore()
			contPlay = input("Would you like to play again? Type 'Hard' to continue, type 'No' to quit\n")
			if(contPlay == "No"):
				return 1
			if(contPlay == "Hard"):
				control = "Hard"
				questionIndex = questionIndex + 1
				answerIndex = answerIndex + 1
		else:
			print "False! Try again please"
			
	while(control == "Medium"):
		print "The question is: "
		print questionList[questionIndex]
		checkInput = input("Enter the corresponding regex statement: ")
		
		if(checkInput == answerList[answerIndex]): #check first expression 
			print "You have entered the correct expression!"
			testPlayer.addScore()
			testPlayer.printScore()
			contPlay = input("Would you like to play again? Type 'Medium' to continue, type 'No' to quit\n")
			if(contPlay == "No"):
				return 1
			if(contPlay == "Medium"):
				control = "Medium"
				questionIndex = questionIndex + 1
				answerIndex = answerIndex + 1
		else:
			print "False! Try again please"
		
			
			
gameDeclaration()
