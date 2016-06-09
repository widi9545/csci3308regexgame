import os, pygame.mixer
import random
pygame.mixer.init(22050,8,1,2048)

songList=list()#creates a empty list
print("Welcome to the zoo.")
print("1. Play a sound.")
print("2. Quit")
mainmenu=raw_input("Select 1 or 2: ")

			
if mainmenu == "2":
	quit()	
if mainmenu != "1":
	mainmenu = raw_input("I did not understand please enter 1 or 2.")
			
def songSelection(randomN):
	
	sg=(songList[randomN][1])
	sg=sg.rstrip("\n")
	
	print(sg)
	return sg
def startup(randomN):
	if randomN == 0:
		a=os.path.join('data','cat.wav')
		pygame.mixer.music.load(a)
		pygame.mixer.music.play()
	if randomN ==1:
		b=os.path.join('data','chickens.wav')
		pygame.mixer.music.load(b)
		pygame.mixer.music.play()
		
	if randomN ==2:
		c=os.path.join('data','duck.wav')
		pygame.mixer.music.load(c)
		pygame.mixer.music.play()
	if randomN == 3:
		d=os.path.join('data','gorilla.wav')
		pygame.mixer.music.load(d)
		pygame.mixer.music.play()
	if randomN == 4:
		e=os.path.join('data','horse.wav')
		pygame.mixer.music.load(e)
		pygame.mixer.music.play()
	if randomN == 5:
		f=os.path.join('data','pig.wav')
		pygame.mixer.music.load(f)
		pygame.mixer.music.play()
	if randomN == 6:
		g=os.path.join('data','tiger.wav')
		pygame.mixer.music.load(g)
		pygame.mixer.music.play()
def options(menu):	
	print("The sound belongs to which animal?")
	print("Cat")
	print("Chickens")
	print("Duck")
	print("Gorilla")
	print("Horse")
	print("Pig")
	print("Tiger")

def guessUser(guess,song):
		
	
		if guess==song:
			print("Guess right.")
			choice=raw_input("Would you like to play again? Yes or No?")
			if choice == "Yes":
				main()
			elif choice == "No":
				quit()
			else:
				choice = raw_input("I did not understand choose : Yes or No. Press Enter")
			
			
		
		else:
			print("Wrong guess.")
			while guess != song:
				
				choice=raw_input("1.Would you like to try again? 2.or skip the song? 3.or quit?:")
				if choice == "1":
					guess=raw_input("Enter another guess:")
					if guess == song:
						print("Guess right.")
						choice2=raw_input("Would you like to play again Yes or No?")
						if choice2=="Yes":
							main()
				elif choice == "2":
					main()
				elif choice =="3": 
					quit()
				else:
					choice = raw_input("I did not understand choose : 1. or 2. or 3.Press Enter")
				
		
def main():
			menu=str()
			randomN=random.randint(0,7)
			
			startup(randomN)
			Songfile=open("Song.csv",'r')
			for x in Songfile:
				row = x.split(",")
				songList.append(row)
			
			song=songSelection(randomN)
			options(menu)
			guess=raw_input("Enter your guess:")
			guessUser(guess,song)
			
			
			
main()
		
			
			
