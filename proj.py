#!/usr/bin/python
import pygame
import sys
from pygame.locals import *
#import MySQLdb
#from playerClass import player
#import random

white = (255,255,255)
black = (0,0,0)
blue=(0,0,255)

              
class Pane(object): 
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
		#done = False				
		#while not done:
		  #for event in pygame.event.get():
				#if event.type == pygame.QUIT:
					#done = True

    def addText(self):
        self.screen.blit(self.font.render('REGEX Game', True, (255,0,0)), (200, 100))
        pygame.display.update()
        #done = False				
		#while not done:
			#for event in pygame.event.get():
				#if event.type == pygame.QUIT:
					#done = True
    #def userpush():
		#while True:
			#for event in pygame.event.get():
				#if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					#pos = pygame.mouse.get_pos()
					#if b.collidepoint(pos):
		
	

if __name__ == '__main__':
 Pan3=Pane()
 Pan3.addText()
 #Pan3.addRect()
 x=150
 y=75
 done = False
 for z in range(1,5):
     for m in range(3,7):
         Pan3.addRect(z*x,m*y);
 while not done:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             done = True 
