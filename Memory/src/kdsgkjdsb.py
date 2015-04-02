'''
Created on Jun 15, 2012

@author: Meredith
'''
'''
Created on Jun 11, 2012
@author: jambran
'''
import pygame
import random
import sys
import os
import gradients

#Sound + Fonts check
if not pygame.font:
    print ('Warning, fonts disabled')
if not pygame.mixer:
    print ('Warning, sound disabled')

NUM_CARDS = 16
SCREEN_WIDTH = None
SCREEN_HEIGHT = None
score = 0

#Loading sounds
def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    try:
        sound = pygame.mixer.Sound(name)
    except pygame.error:
        print ('Cannot load sound:', name)
        sys.exit()
    return sound

class CardConfig(object):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.total_pairs = rows * cols // 2
        self.cardset = []
        self.card_indexes = []
        for i in range(1, NUM_CARDS + 1):
            self.cardset.append(Card(i))
            self.card_indexes.append(i - 1)

        self.image_width = self.cardset[0].rect.width
        self.image_height = self.cardset[0].rect.height
        self.top_margin = 30
        self.padding = 10
        global SCREEN_WIDTH, SCREEN_HEIGHT
        SCREEN_WIDTH = cols * self.image_width + (cols + 1) * self.padding
        SCREEN_HEIGHT = self.top_margin + rows * self.image_height + (rows + 1) * self.padding
        self.reset()

    def reset(self):
        self.cards = []
        random.shuffle(self.card_indexes)
        for i in range(self.total_pairs):
            self.cards.append(self.cardset[i].clone())
            self.cards.append(self.cardset[i].clone())
        random.shuffle(self.cards)

        pos, row, col = 0, 0, 0
        for card in self.cards:
            card.set_position(col * self.image_width + (col + 1) * self.padding, \
                              row * self.image_height + (row + 1) * self.padding + self.top_margin)
            pos += 1
            col = (col + 1) % self.cols
            if pos % self.cols == 0:
                row += 1
        self.num_flipped = 0
        self.flipped = [-1, -1]

    def get_index_of_clicked_card(self, x, y):
        '''Returns the index of the card that has been clicked and -1 if the
        (x, y) coordinate does not correspond to any card.'''
        
        index = 0

        for i in self.cards:
            if x in range(i.rect[0], i.rect[0] + i.rect[2]) and y in range(i.rect[1], i.rect[1] + i.rect[3]): 
                return index
            else:
                index += 1
        return -1
    
    def flip_card(self, index):
        '''Flips the card at the given index.'''
        if self.num_flipped == 0 or self.num_flipped == 1 and index != self.flipped[0]:
            self.flipped[self.num_flipped] = index
            self.num_flipped += 1
            self.cards[index].flip()

    def is_match(self):
        '''Returns True if there are two unique flipped cards that have the same
        image_number; False otherwise.'''
        if self.cards[self.flipped[0]].image_number == self.cards[self.flipped[1]].image_number:
            return True
        else:
            return False


    def clear_flippings(self):
        '''Resets the num_flipped counter, flips the pair of flipped cards over
        again, and resets the indexes of the flipped cards to -1.''' 
        for i in self.cards:
            if i.status == Card.IMAGE_SHOWN:
                i.status = Card.BACK_SHOWN
            self.flipped = [-1, -1]
            self.num_flipped = 0

    def hide_flippings(self):
        '''Resets the num_flipped counter, hides the pair of flipped cards, and
        resets the indexes of the flipped cards to -1.''' 
        self.num_flipped = 0
        self.cards[self.flipped[0]].hide()
        self.cards[self.flipped[1]].hide()
        self.flipped = [-1, -1]

    def paint(self, screen):
        '''Paints each of the cards in the collection on the screen.'''
        for card in self.cards:
            card.paint(screen)

class Card(pygame.sprite.Sprite):
    BACK_SHOWN = 0
    IMAGE_SHOWN = 1
    HIDDEN = 2

    def __init__(self, image_number):
        pygame.sprite.Sprite.__init__(self)
        self.image_number = image_number
        filename = "images\monster{0:d}.png".format(image_number)
        back_image = "images\cardback.png"
        self.image = pygame.image.load(filename)
        self.cardback = pygame.image.load(back_image)
        self.rect = self.image.get_rect()
        self.status = Card.BACK_SHOWN

    def set_position(self, x, y):
        '''Sets the left and top attributes of self.rect to x and y,
        respectively.'''
        self.rect.top = y
        self.rect.left = x

    def clone(self):
        '''Returns a copy of the Card object.''' 
        return Card(self.image_number)

    def flip(self):
        '''Toggles self.status between showing the back of the card and the
        actual image.'''
        if self.status != Card.HIDDEN:
            if self.status == Card.BACK_SHOWN:
                self.status = Card.IMAGE_SHOWN
            else:
                self.status = Card.BACK_SHOWN
            

    def contains(self, x, y):
        '''Returns True if the card is not hidden and the (x, y) coordinate is
        located within self.rect; returns False otherwise.'''
        
        if self.rect.left + self.rect.width <= x and self.rect.left >= x:
            return True
        
        if self.rect.top + self.rect.height <= y and self.rect.top >= y:
            return True
        
        else:
            return False

    def hide(self):
        '''Changes the status of the card to reflect that it is hidden.'''
        self.status = Card.HIDDEN

    def paint(self, screen):
        '''Paints the appropriate side of the card, if the card is not
        hidden.''' 
        if self.status == Card.BACK_SHOWN:
            screen.blit(self.cardback, (self.rect[0], self.rect[1]))
        elif self.status == Card.IMAGE_SHOWN:
            screen.blit(self.image, (self.rect[0], self.rect[1]))

class Game(object):
    GREEN = (0, 50, 0, 255)
    DARK_GREEN = (0, 100, 0, 255)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    OVER = 0
    RUNNING = 1
    GAME_OVER_MESSAGE = "CONGRATULATIONS!"
    GAME_OVER_DIRECTIONS = "Press S to start a new game."

    def __init__(self, rows=3, cols=6):
        product = rows * cols
        if product % 2 != 0:
            raise ValueError("Product of rows and columns must be divisible by 2.")
        if product > NUM_CARDS * 2:
            raise ValueError("Product of rows and columns must not exceed {0:d}.".format(NUM_CARDS * 2))
        self.rows = rows
        self.cols = cols
        self.card_config = CardConfig(self.rows, self.cols)
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Memory Game")
        self.clock = pygame.time.Clock()
        self.background = \
            gradients.vertical((SCREEN_WIDTH, SCREEN_HEIGHT), Game.DARK_GREEN, Game.GREEN)
        self.fade_rect = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.fade_rect.set_alpha(96)
        self.fade_rect.fill((0, 0, 0))
        self.small_font = pygame.font.Font(None, 20)
        self.large_font = pygame.font.Font(None, 64)
        self.medium_font = pygame.font.Font(None, 28)
        self.game_over_msg_image = self.large_font.render(Game.GAME_OVER_MESSAGE, True, Game.YELLOW).convert_alpha()
        self.game_over_dir_image = self.medium_font.render(Game.GAME_OVER_DIRECTIONS, True, Game.WHITE).convert_alpha()
        self.reset()
        # Sound
        self.click_sound = load_sound("sounds\clickerx.wav")
        self.match_sound = load_sound("sounds\sparkle.wav")
        self.startup = load_sound("sounds\startup.wav")
        self.shutdown = load_sound("sounds\shutdown.wav")
        self.onsound = False
        self.offsound = False
        

    def reset(self):
        self.offsound = False
        self.card_config.reset()
        self.match_detected = False
        self.is_stalling = False
        self.stalled_seconds = 0
        self.elapsed_time = 0
        self.time_image = self.small_font.render("Elapsed time (s): 0.000", True, Game.WHITE).convert_alpha()
        self.attempts = 0
        self.attempts_image = self.small_font.render("Attempts: 0", True, Game.WHITE).convert_alpha()
        self.hits = 0
        self.hits_image = self.small_font.render("Hits: 0", True, Game.WHITE).convert_alpha()
        global score
        score = 0
        self.score_image = self.small_font.render("Score: 0", True, Game.WHITE).convert_alpha()
        self.status = Game.RUNNING        

    def update(self, seconds):
        if self.is_stalling:
            self.stalled_seconds += seconds
            if self.stalled_seconds >= 1:
                self.stalled_seconds = 0
                self.is_stalling = False
                if self.match_detected:
                    self.card_config.hide_flippings()
                else:
                    self.card_config.clear_flippings()
                if self.hits == self.card_config.total_pairs:
                    self.status = Game.OVER

        # Code to reset the game if the user presses the 's' key.
        
        if self.status == Game.OVER:
            
            if self.offsound == False:
                self.shutdown.play()
            self.offsound = True
            
            for event in pygame.event.get():
                if event.type == pygame. QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    self.startup.play()
                    self.reset()
        
        # End reset code
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN and self.status == Game.RUNNING and \
            not self.is_stalling:
                # Get the (x, y) position of the mouse click.
                position = pygame.mouse.get_pos()
                
                # Make click sound
                self.click_sound.play()

                index = self.card_config.get_index_of_clicked_card(position[0], position[1])
                if index != -1:
                    self.card_config.flip_card(index)
                    if self.card_config.num_flipped == 2:
                        self.is_stalling = True
                        self.attempts += 1
                        if self.card_config.is_match():
                            self.hits += 1
                            global score
                            # Create your own formula for scoring.
                            # score += ?
                            # End formula.
                            score += int(500 // self.elapsed_time)
                            self.match_detected = True
                            self.match_sound.play()
                        else:
                            self.match_detected = False

        if self.status == Game.RUNNING:
            self.elapsed_time += seconds
            time_text = "Elapsed time (s): {0:0.3f}".format(self.elapsed_time)
            self.time_image = self.small_font.render(time_text, True, Game.WHITE).convert_alpha()
            attempts_text = "Attempts: {0:d}".format(self.attempts)
            self.attempts_image = self.small_font.render(attempts_text, True, Game.WHITE).convert_alpha()
            hits_text = "Hits: {0:d}".format(self.hits)
            self.hits_image = self.small_font.render(hits_text, True, Game.WHITE).convert_alpha()
            score_text = "Score: {0:d}".format(score)
            self.score_image = self.small_font.render(score_text, True, Game.WHITE).convert_alpha()

    def render(self):
        self.screen.blit(self.background, (0, 0))

        # Display the number of attempts, hits, score, and elapsed time.

        self.screen.blit(self.time_image, (450, 15))
        self.screen.blit(self.attempts_image, (60, 15))
        self.screen.blit(self.hits_image, (220, 15))
        self.screen.blit(self.score_image, (330, 15))

        # Display the card configuration.
        
        self.card_config.paint(self.screen)

        if self.status == Game.OVER:
            self.screen.blit(self.fade_rect, (0, 0))
            (text_width, text_height) = self.large_font.size(Game.GAME_OVER_MESSAGE)
            x = (SCREEN_WIDTH - text_width) // 2
            y = (SCREEN_HEIGHT - text_height) // 2
            self.screen.blit(self.game_over_msg_image, (x, y - 20))
            (text_width, text_height) = self.medium_font.size(Game.GAME_OVER_DIRECTIONS)
            x = (SCREEN_WIDTH - text_width) // 2
            self.screen.blit(self.game_over_dir_image, (x, y + 30))
        pygame.display.update()

    def run(self):
        while True:
            
            if self.onsound == False:
                self.startup.play()
            self.onsound = True
            
            time_ms = self.clock.tick(30)
            if time_ms < 100:
                self.update(time_ms / 1000)
                self.render()

if __name__ == '__main__':
    argc = len(sys.argv)
    if argc != 1 and argc != 3:
        print("Error: memory expects either 0 or 2 arguments.")
        sys.exit(1)
    if argc == 3:
        try:
            rows = int(sys.argv[1])
        except ValueError:
            print("Error: Bad value '%s' for number of rows." % sys.argv[1])
            sys.exit(1)
        try:
            cols = int(sys.argv[2])
            if cols < 5:
                print("Error: Minimum number of columns is 5.")
                sys.exit(1)
        except ValueError:
            print("Error: Bad value '%s' for number of columns." % sys.argv[2])
            sys.exit(1)
        try:
            game = Game(rows, cols)
        except ValueError as error:
            print("Error: %s" % error)
            sys.exit(1)
    else:
        game = Game()
    game.run()
