import pygame
import time

PIXEL_WIDTH = 1000
PIXEL_HEIGHT = 1000
CARD_WIDTH = 150
CARD_HEIGHT = 75
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
class Card(pygame.sprite.Sprite):
    def __init__(self,color,x,y, message):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([x, y])
        self.image.fill(color)
        self.message=message
        #self.grid_x=x
        #self.grid_y=y
        self.rect=self.image.get_rect()
    
        


def main():
    print "hello world"
    pygame.init()
    pygame.display.set_caption("Regex Memory Game")
    screen = pygame.display.set_mode((PIXEL_WIDTH, PIXEL_HEIGHT))
    done = False
    card_group=pygame.sprite.Group()
    card_turned_group=pygame.sprite.Group()
    clock=pygame.time.Clock()
    card_words=["number1","second","three","Four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen"]
    k=0
    card_turned=0
    for z in range(1,5):
        for m in range(3,7):
            card=Card(WHITE,CARD_WIDTH,CARD_HEIGHT, card_words[k])
            card_group.add(card)
            screen.blit(card.image, [CARD_WIDTH*z+z,CARD_HEIGHT*m+m])
            card.rect.x=CARD_WIDTH*z+z
            card.rect.y=CARD_HEIGHT*m+m
            print "Card created"
            k+=1

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                #for x in card_group:
                   # if x.rect.collidepoint(pos):
                      #  print "Card Pressed"
                clicked_sprites=[x for x in card_group if x.rect.collidepoint(pos)]
                for i in clicked_sprites:
                    if card_turned <2:
                        font = pygame.font.Font(None, 36)
                        text = font.render(i.message, 1, (10, 10, 10))
                        textpos = text.get_rect()
                        textpos.centerx = i.image.get_rect().centerx
                        i.image.blit(text, textpos)
                        card_turned_group.add(i)
                        card_turned+=1
                    else:
                        for i in card_turned_group:
                            i.image.fill(WHITE)
                            card_turned_group.remove(i)
                            card_turned=0
        screen.fill(BLACK)
        #card = Card(WHITE,100,100)
        #card_group=pygame.sprite.Group()
        #card_group.add(card)
        card_group.draw(screen)
        card_group.update()
        pygame.display.update()
        pygame.display.flip()
        clock.tick(5)


main()

pygame.quit()
