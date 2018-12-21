# import the pygame module, so you can use it
# -*-coding:utf-8-*-

import pygame
import os
import codecs
import time
import datetime
import math
import sys
import random

# define colors
SLATEGRAY1 = (198,226,255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# define screensize
SCREEN_HEIGHT = 300
SCREEN_WIDTH = 600
SCREENSIZE = [SCREEN_WIDTH,SCREEN_HEIGHT]

class FlashCards(object):
    """
    Attributes:
        filepath: Path of csv or text file that contains the flashcard information
    """
    def __init__(self, filepath=None):
        super(FlashCards, self).__init__()
        #self.arg = arg
        #self.filepath = filepath
        self.cards = self._load_flashcards(filepath)
        #self.dir_path = os.path.dirname
        #self.cards = {}
        self.init_cards = self.cards
        self.unmemorized_cards = {}
        self.history = []

    def _load_flashcards(self,filepath):
        card_list = {}
        infile = codecs.open(filepath, encoding = 'utf-8')
        for line in infile.readlines():
            key = line.split(",")[0]
            value = line.split(",")[1].strip()
            card_list[key]=value
        infile.close()
        return card_list

    def add_unmemorized_card(self, card_pair):
        self.unmemorized_cards.update(card_pair)

    def write_unmemorized_card_to_file(self):
        if len(self.unmemorized_cards) is not 0:  # if the unmemorized cards is not empty
            datestr = datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d-%H-%M-%S")
            outfile = "unmemorized-cards-" + datestr
            print outfile
            with open(outfile,'wb') as data:
                for k, v in self.unmemorized_cards.items():
                    #print k
                    data.write(k.encode("UTF-8") + ',' + v.encode("UTF-8") + '\n')


def draw_background():
    screen.fill(WHITE)
    # define the size and location of the button
    BUTTON_HEIGHT = 30
    BUTTON_WIDTH = 170
    MARGIN_WIDTH = 20
    DIST_TO_BOTTOM = 50

    # button initialize as rect object
    answer_button = pygame.Rect(MARGIN_WIDTH, SCREEN_HEIGHT-DIST_TO_BOTTOM, BUTTON_WIDTH, BUTTON_HEIGHT)
    remembered_button = pygame.Rect(math.ceil(SCREEN_WIDTH/2-BUTTON_WIDTH/2), SCREEN_HEIGHT-DIST_TO_BOTTOM, BUTTON_WIDTH, BUTTON_HEIGHT)
    notRemembered_button = pygame.Rect(SCREEN_WIDTH-BUTTON_WIDTH-MARGIN_WIDTH, SCREEN_HEIGHT-DIST_TO_BOTTOM, BUTTON_WIDTH, BUTTON_HEIGHT)

    # Set text fond and render text in the center of the button
    font = pygame.font.SysFont("comicsansms",30)
    answer_text = font.render("Answer", True, (0, 128, 0))
    answer_text_rect = answer_text.get_rect()
    answer_text_rect.center = answer_button.center

    remembered_text = font.render("Remembered", True, (0, 128, 0))
    remembered_text_rect = remembered_text.get_rect()
    remembered_text_rect.center = remembered_button.center

    notRemembered_text = font.render("Not Remembered", True, (0, 128, 0))
    notRemembered_text_rect = notRemembered_text.get_rect()
    notRemembered_text_rect.center = notRemembered_button.center

    # draw buttons and texts
    pygame.draw.rect(screen, SLATEGRAY1, answer_button)
    pygame.draw.rect(screen, SLATEGRAY1, remembered_button)
    pygame.draw.rect(screen, SLATEGRAY1, notRemembered_button)

    screen.blit(answer_text,answer_text_rect)
    screen.blit(remembered_text,remembered_text_rect)
    screen.blit(notRemembered_text,notRemembered_text_rect)


def init():
    draw_background()
    TESTCARDS.cards = TESTCARDS.init_cards
    return 'Stop'

def stop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q) :
            TESTCARDS.write_unmemorized_card_to_file()
            running = False
            pygame.quit()
            sys.exit()
        # keyboard actions
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and previous_event == 'Next_card':
            return 'Answer'

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return 'Next_card'

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            return 'Reset'

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            return 'Next_card'

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            return 'Previous_card'

        if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            return 'Remembered'

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            return 'NotRemembered'

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.button_down = True
            pygame.button_type = event.button

        if event.type == pygame.MOUSEBUTTONUP:
            pygame.button_down = False

    return 'Stop'

def next_card():
    key = random.choice(TESTCARDS.cards.keys())
    TESTCARDS.history.append(key)
    print key

    question_rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT-70)

    font = pygame.font.Font("KosugiMaru-Regular.ttf",60)
    card_text = font.render(key, True, BLACK)
    card_text_rect = card_text.get_rect()
    card_text_rect.center = question_rect.center
    pygame.draw.rect(screen, WHITE, question_rect)
    screen.blit(card_text,card_text_rect)

    return 'Stop'


def answer():
    try:
        key = TESTCARDS.history[-1]
    except:
        print "ERROR Finding card history in FUNC: check_answer()."

    answer = TESTCARDS.cards[key]
    print answer
    font = pygame.font.SysFont("motoyaLMaru", 40)

    question_rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT-70)

    font = pygame.font.Font("KosugiMaru-Regular.ttf",60)
    text = font.render(answer, True, BLACK)
    text_rect = text.get_rect()
    text_rect.center = question_rect.center
    pygame.draw.rect(screen, WHITE, question_rect)
    screen.blit(text,text_rect)

    return 'Stop'

def remembered():
    print len(TESTCARDS.history)
    if len(TESTCARDS.history) == 0:
        return 'Stop'
    else:
        TESTCARDS.cards.pop(TESTCARDS.history[-1], None)
        #print len(TESTCARDS.cards)
    return 'Stop'

def notRemembered():
    if len(TESTCARDS.history) == 0:
        return 'Stop'
    else:
        key = TESTCARDS.history[-1]
        value = TESTCARDS.init_cards[key]
        TESTCARDS.add_unmemorized_card({key:value})

        #print len(TESTCARDS.unmemorized_cards)
        #print TESTCARDS.unmemorized_cards

    return 'Stop'

if __name__=="__main__":
    # state machine:
    state_actions = {
        'Reset': init,
        'Stop': stop,
        'Next_card': next_card,
        'Answer': answer,
        'Remembered': remembered,
        'NotRemembered': notRemembered
    }
    state = 'Reset'
    previous_event = state
    # initialize the pygame module and set the game caption
    pygame.init()
    pygame.display.set_caption("Flashcards")

    # create a surface on screen that has the size of 600 x 300
    screen = pygame.display.set_mode(SCREENSIZE)

    # define a variable to control the main loop
    running = True

    # init flashcards with file name
    if len(sys.argv) == 1:
        TESTCARDS = FlashCards("cardlists/Hiragana")
    else:
        TESTCARDS = FlashCards(sys.argv[1])

    # main loop
    while running:
        state = state_actions[state]()
        if state is not 'Stop':
            previous_event = state
            print previous_event
        pygame.display.flip()
