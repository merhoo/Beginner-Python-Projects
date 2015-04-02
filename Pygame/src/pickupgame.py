'''
Created on May 30, 2012

@author: jasontuhy
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
CYAN = (138,43,226)
PURPLE = (0,255,255)
ORANGE = (255,165,0)
WHITE = (255,255,255,255)
BLACK = (0,0,0,255)
PINK = (255,20,147,255)
YELLOW = (255, 255, 0,255)
BROWN = (139,69,19,255)
pause = False
COLORS_CHANGE = True
squaresMove = False
RED = (255,0,0,255)

class Character(object):
    
    def __init__(self,rect):
        self.x = rect[0]
        self.y = rect[1]
        self.length = rect[2]
        self.height = rect[3]
        self.rect = rect
        self.speed = 2
    def move_right(self):
        if self.x +self.length< SCREEN_WIDTH:
            self.rect = (self.rect[0] +2, self.rect[1],self.rect[2],self.rect[3])
            self.x+=self.speed
            
    def move_left(self):
        if self.x > 0:
            self.rect = (self.rect[0] -2, self.rect[1],self.rect[2],self.rect[3])
            self.x-=self.speed
            
    def move_up(self):
        if self.y - 1 > 0:
            self.rect = (self.rect[0], self.rect[1]-2,self.rect[2],self.rect[3])
            self.y-=self.speed
            
    def move_down(self):
        if self.y+self.height < SCREEN_HEIGHT:
            self.rect = (self.rect[0], self.rect[1]+2,self.rect[2],self.rect[3])
            self.y+=self.speed
            
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
        self.pause = False
        self.win = False
        self.score = 0
        self.colorList = []
        self.moveList = []
        self.time_ms = 0
        self.clock = pygame.time.Clock()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.game_font = pygame.font.Font(None,20)
        self.win_text = pygame.font.Font(None,100)
        self.win_description_text = pygame.font.Font(None,40)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Sets height and width
        pygame.display.set_caption(Game.TEXT)
        self.background = \
            gradients.radial((SCREEN_WIDTH, SCREEN_HEIGHT), BLUE, BLACK)
        self.character = Character((10,10,25,25))
        self.items = Items(20)
        self.colorDecider()
        self.num = 0
        self.moveTime = 0
        self.fps = 0
        self.fps_time = 0
        self.last_update = 0
        self.make_random_list(self.items.numOfItems, 1, 4, self.moveList)
    def render(self):
        self.screen.blit(self.background, (0,0))
        pygame.draw.ellipse(self.screen, RED, self.character.rect)
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
            if squaresMove:
                if self.moveList[i//2] == 1:
                    if self.items.lstOfCoords[i+1] - 11 > 0:
                        self.items.lstOfCoords[i+1] -= 10
                elif self.moveList[i//2] == 2:
                    if self.items.lstOfCoords[i+1]+20 < SCREEN_HEIGHT:
                        self.items.lstOfCoords[i+1] += 10
                elif self.moveList[i//2] == 3:
                    if self.items.lstOfCoords[i] +20< SCREEN_WIDTH:
                        self.items.lstOfCoords[i] += 10
                else:
                    if self.items.lstOfCoords[i] - 10> 0:
                        self.items.lstOfCoords[i] -=10
                    
        time_text = "Seconds: " + str(self.time) + " "* 24 +"Score: " + str(self.score) + " " * 24 +"Items Left: "+ \
            str(len(self.items.lstOfCoords)//2) + " "*24+ "Items Gathered: " + str(self.score)
        self.time_image = self.game_font.render(time_text, True, WHITE).convert_alpha()
        self.screen.blit(self.time_image, (10, SCREEN_HEIGHT - 20))
        self.screen.blit(self.fps_image, (SCREEN_WIDTH - 80, 10))
        if len(self.items.lstOfCoords) == 0:
            self.win = True
        pygame.display.update()
        
    def update(self,time_seconds):
        self.fps_time += time_seconds
        if  self.fps_time >  0.25 and  squaresMove:
            self.make_random_list(self.items.numOfItems, 1, 4, self.moveList)
            
        if self.fps_time >= 1 or self.fps == 0:
            self.fps = self.clock.get_fps()
            fps_text = "FPS: {0:0.1f}".format(self.fps)
            self.fps_image = self.game_font.render(fps_text, True, WHITE).convert_alpha()
            self.fps_time = 0
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
                if not(COLORS_CHANGE):
                    self.colorList.pop(i)
                    self.colorList.pop(i)
                self.score+=1
                break
    def colorDecider(self):
        for _ in range(0,len(self.items.lstOfCoords)):
            self.colorList.append(random.randint(1,6))
    def make_random_list(self,lst_len,a,b,lst):
        self.moveList = []
        for _ in range(lst_len+1):
            self.moveList.append(random.randint(a,b))
            
    def win_render(self):
        
        self.display_text = "YOU WIN!"
        self.description_text = ("With a score of %d in %d seconds!  "% (self.score, self.time))
        self.second_line = ("That is %.2f per second!" % (self.score/self.time))
        self.win_image = self.win_text.render(self.display_text, True, WHITE).convert_alpha()
        self.description_image = self.win_description_text.render(self.description_text, True, WHITE).convert_alpha()
        self.second_image = self.win_description_text.render(self.second_line, True, WHITE).convert_alpha()
        (self.display_text_length,self.display_text_width) = self.win_text.size(self.display_text)
        (self.description_text_length,self.description_text_width) = self.win_description_text.size(self.description_text)
        (self.second_text_length,self.second_text_width) = self.win_description_text.size(self.second_line)
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.win_image, ((SCREEN_WIDTH- self.display_text_length//2)- self.display_text_length ,0))
        self.screen.blit(self.description_image,((SCREEN_WIDTH//2) - (self.description_text_width+180) ,70))
        self.screen.blit(self.second_image, ((SCREEN_WIDTH- self.second_text_length//2) - self.second_text_length,115))
        pygame.display.update()
        
    def run(self):
        while True:
            if self.win:
                while True:
                    self.win_render()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit(0)
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                sys.exit(1)
            if not(self.pause):
                self.tempMS = self.clock.tick()
                time_mis = self.tempMS
                
                self.time_ms += self.tempMS
                self.moveTime+= time_mis//1000 
                self.time = self.time_ms//1000
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit(1)
                    if event.key == K_p:
                        self.pause = True
                if event.type == KEYUP:
                    if event.key == K_p:
                        self.pause =False
            if not(self.pause):
                self.check_for_collisions()
                self.update(time_mis/1000)
                self.render()
            
if __name__ == "__main__":
    game = Game()
    game.run()