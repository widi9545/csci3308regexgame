#!/usr/bin/python
import MySQLdb
from playerClass import player
import random



db = MySQLdb.connect("127.0.0.1", "root", "root", "regexQuestions")
cur = db.cursor()
questionList =[]
answerList = []

		
		
def fillQuestionListBasic():
	cur.execute("SELECT question FROM questions")
	row = cur.fetchone()
	while row is not None:
		questionList.append(row)
		row = cur.fetchone()
	print questionList[3]
	return 1
	
def fillAnswerListBasic():
	cur.execute("SELECT answer FROM answers")
	row = cur.fetchone()
	while row is not None:
		answerList.append(row)
		row = cur.fetchone()
	return 1

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
		
		


def gameDeclaration():
	testPlayer = player()
	control = input("Type 'Yes' if you want to play a game with basic questions, type 'Medium' or 'Hard' if you want to play a game with Medium or Hard Questions ")
	questionIndex = 0
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
