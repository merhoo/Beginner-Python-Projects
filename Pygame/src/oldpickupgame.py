'''
Created on May 29, 2012

@author: Jason
'''
import pygame
import sys
import os
import random
import gradients
from pygame.locals import *
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLUE = (0,0,255,255)
GREEN = (34,139,34)
PURPLE = (138,43,226)
CYAN = (0,255,255)
ORANGE = (255,165,0)
WHITE = (255,255,255)
BLACK = (0,0,0,255)
PINK = (255,20,147)
YELLOW = (255, 255, 0)
RED = (255,0,0)

class Character(object):
    def __init__(self,rect):
        self.x = rect[0]
        self.y = rect[1]
        self.length = rect[2]
        self.height = rect[3]
        self.rect = rect
    def move_right(self):
        if self.x +10< SCREEN_WIDTH:
            self.rect = (self.rect[0] +1, self.rect[1],self.rect[2],self.rect[3])
            self.x+=1
    def move_left(self):
        if self.x > 0:
            self.rect = (self.rect[0] -1, self.rect[1],self.rect[2],self.rect[3])
            self.x-=1
    def move_up(self):
        if self.y - 1 > 0:
            self.rect = (self.rect[0], self.rect[1]-1,self.rect[2],self.rect[3])
            self.y-=1
    def move_down(self):
        if self.y+10 < SCREEN_HEIGHT:
            self.rect = (self.rect[0], self.rect[1]+1,self.rect[2],self.rect[3])
            self.y+=1
class Items(object):
    def __init__(self,numOfItems):
        self.numOfItems = numOfItems
        self.lstOfCoords = []
        keepGoing = True
        for _ in range(0,self.numOfItems-1):
            keepGoing = True
            while keepGoing:
                canChange = False
                tempX = random.randint(0,SCREEN_WIDTH-10)
                tempY = random.randint(0,SCREEN_HEIGHT-10)
                if len(self.lstOfCoords) != 0:
                    for x in self.lstOfCoords:
                        if x not in range(tempX, tempX + 20) and x not in range(tempY, tempY + 20):
                            canChange = True
                        else:
                            canChange = False
                            break
                else:
                    self.lstOfCoords.append(tempX)
                    self.lstOfCoords.append(tempY)
                if canChange:
                    self.lstOfCoords.append(tempX)
                    self.lstOfCoords.append(tempY)
                    keepGoing = False
        
class Game(object):
    TEXT = "Pick Up Game"
    def __init__(self):
        self.colorList = []
        self.clock = pygame.time.Clock()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Sets height and width
        pygame.display.set_caption(Game.TEXT)
        self.background = \
            gradients.radial((SCREEN_WIDTH, SCREEN_HEIGHT), BLUE, BLACK)
        self.character = Character((10,10,10,10))
        self.items = Items(20)
        
    def render(self):
        self.screen.blit(self.background, (0,0))
        pygame.draw.rect(self.screen, RED, self.character.rect)
        for i in range(0,len(self.items.lstOfCoords),2):
            if self.colorList[i] == 1:
                pygame.draw.rect(self.screen, GREEN, (self.items.lstOfCoords[i],self.items.lstOfCoords[i+1],10,10))
            elif self.colorList[i] == 2:
                pygame.draw.rect(self.screen, ORANGE, (self.items.lstOfCoords[i],self.items.lstOfCoords[i+1],10,10))
            elif self.colorList[i] == 3:
                pygame.draw.rect(self.screen, YELLOW, (self.items.lstOfCoords[i],self.items.lstOfCoords[i+1],10,10))
            elif self.colorList[i] == 4:
                pygame.draw.rect(self.screen, PINK, (self.items.lstOfCoords[i],self.items.lstOfCoords[i+1],10,10))
            elif self.colorList[i] == 5:
                pygame.draw.rect(self.screen, CYAN, (self.items.lstOfCoords[i],self.items.lstOfCoords[i+1],10,10))
            else:
                pygame.draw.rect(self.screen, PURPLE, (self.items.lstOfCoords[i],self.items.lstOfCoords[i+1],10,10))
        pygame.display.update()
        
    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_UP]:
            self.character.move_up()
        if pressed[K_DOWN]:
            self.character.move_down()
        if pressed[K_LEFT]:
            self.character.move_left()
        if pressed[K_RIGHT]:
            self.character.move_right()
            
    def check_for_collisions(self):
        for i in range(0,len(self.items.lstOfCoords),2):
            tempRect = pygame.Rect(self.items.lstOfCoords[i],self.items.lstOfCoords[i+1],10,10)
            if tempRect.colliderect(self.character.rect):
                self.items.lstOfCoords.remove(self.items.lstOfCoords[i])
                self.items.lstOfCoords.remove(self.items.lstOfCoords[i])
                break
    def colorDecider(self):
        
        for _ in range(0,len(self.items.lstOfCoords)):
            self.colorList.append(random.randint(1,6))
    def run(self):
        self.i = 0
        self.colorDecider()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit(1)
            self.check_for_collisions()
            self.update()
            self.render()
            self.i+=1
if __name__ == "__main__":
    game = Game()
    game.run()