import pygame
import time
import sys
import random
w = 800
h = 600
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
pygame.init()
gameDisplay = pygame.display.set_mode((w,h))
pygame.display.set_caption('Iron Cat')
clock = pygame.time.Clock()
menu=pygame.image.load('พื้นหลังหลัก.png')
start=pygame.image.load('start.gif')
fil =pygame.image.load('พื้นหลังเล่นเกม.jpg')
cat = pygame.image.load('saa.png')
enemy = pygame.image.load('ยาน.png')
enemy2 = pygame.image.load('ยาน2.png')
pygame.mixer.music.load("Nyan Cat.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
hscore=0
def score1(count):
    font=pygame.font.Font('New Super Mario Font U.ttf',25)
    text =font.render("Score : "+str(count),True,white)
    gameDisplay.blit(text,(10,10))
def score2(count):
    font=pygame.font.Font('New Super Mario Font U.ttf',25)
    text =font.render("HighScore : "+str(count),True,white)
    gameDisplay.blit(text,(10,50))


def text_ob(text,font):
    textsuf =font.render(text,True,black)
    print(textsuf.get_rect())
    return textsuf,textsuf.get_rect()
def message(text):
    lartext = pygame.font.Font('New Super Mario Font U.ttf',115)
    texts, textrect = text_ob(text,lartext)
    textrect.center = ((w/2),(h/2))
    gameDisplay.blit(texts,textrect)
    pygame.display.update()

    time.sleep(2)
    new()
def over():
    message('Game Over')

def iron (x,y):
    gameDisplay.blit(cat,(x,y))
def new():
    global hscore
    i = 0
    x = (100)
    y = (300)
    ty = random.randrange(100,500,100)
    ty2 = random.randrange(200, 500, 100)
    tx = 2000
    ts = 7
    tw = 80
    th = 80

    x_ch = 0
    y_ch = 0
    crashed = False
    score=0
    la = 7
    while not crashed :

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y_ch = la

                if event.key == pygame.K_UP:
                    y_ch = -la
                if event.key == pygame.K_LEFT:
                    x_ch = -la
                if event.key == pygame.K_RIGHT:
                    x_ch = la
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_ch = 0
                    y_ch = 0

        y += y_ch
        x += x_ch
        gameDisplay.blit(fil, (0, 0))
        gameDisplay.blit(enemy, (tx,ty))
        gameDisplay.blit(enemy2,(tx,ty2))
        tx -= ts
        iron(x,y)
        score1(score)
        score2(hscore)
        if x > w - 65 or x < -15 or y > h - 50 or y < -10:
            over()
        if tx < -200 :
            tx = 800 - tw
            ty = random.randrange(100,500,100)
            ty2 = random.randrange(100,500,100)
        score = i
        print( i)
        if ts<=15:
            if score%500==0:
                ts=ts+0.5
                la=la+0.5
                



        if  tx-15 < x < tx + tw or tx < x + 90 < tx-15 + tw  :

            if ty < y + 20 < ty + th or ty < y + 90 < ty + th or ty < int((y+y+90)/2) < ty +th :
                print('y cos')
                over()
            if ty2 < y + 20 < ty2 + th or ty2 < y + 90 < ty2 + th or ty2 < int((y+y+90)/2) < ty2 +th :
                print('y cos')
                over()
        if score > hscore:
            hscore = score
        i += 1
        pygame.display.update()
        clock.tick(70)

def game_intro():
    intro = True
    gameDisplay.blit(menu,(0,0))
    pygame.display.update()
    while intro:
        for event in pygame.event.get():
            if event.type ==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    intro = False
                    new()
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
game_intro()
new()
pygame.quit()
quit()