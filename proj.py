#!/usr/bin/python
import pygame
import sys
from pygame.locals import *
pygame.init()
#import MySQLdb
#from playerClass import player
#import random

white = (255,255,255)
black = (0,0,0)
blue=(0,0,255)

              
class cards(object): 
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 25)
        pygame.display.set_caption('Box Test')
        self.screen = pygame.display.set_mode((1000,1000))
        self.screen.fill((white))
        pygame.display.update()

	
    def addRect(self, x, y):
	
		pygame.draw.rect(self.screen,blue,(x,y,150,75),1)
		pygame.display.flip()
		

    def addText(self):
        self.screen.blit(self.font.render('REGEX Game', True, (255,0,0)), (200, 100))
        pygame.display.update()
        
    def userpush(self):
		while True:
			for event in pygame.event.get():
				
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					pos= pygame.mouse.get_pos()
					if b.collidepoint(pos):
						print("Yup")
		
	

if __name__ == '__main__':
 Cardsb=cards()


 #Pan3.addRect()
 x=150
 y=75
done = False
for z in range(1,5):
 for m in range(3,7):
	Cardsb.addRect(z*x,m*y);

while not done:
 for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
             Cardsb.addText()

pygame.display.quit()

