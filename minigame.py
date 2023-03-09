import pygame, sys, random, time

from pygame.locals import *
from pygame import mixer


WIDTH = 900
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
pygame.display.set_caption("DUA XE CA CUOC")
FPS = 60
fpsClock = pygame.time.Clock()
kx = 1.5
ky = 1.5


def transform(img, w, h):
    img = pygame.transform.scale(img, (int(w), int(h)))
    return img


bg = pygame.image.load("minigame\\bg.png")
gun = pygame.image.load("minigame\\gun.png")
gun = transform(gun, 80, 100)
target = pygame.image.load("minigame\\target.png")
huong_dan = pygame.image.load("minigame\\huong-dan.png")


def instructions():
    ###----SETUP-----
    global SCREEN
    running = True
    while running:
        SCREEN.blit(huong_dan, (0, 0))
        ###-----EVENT------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                running = False
            # if event.type == MOUSEBUTTONDOWN:
            #     running = False
        ###--------UPDATE---------
        pygame.display.update()
        fpsClock.tick(FPS)


def minigame(sound):
    ###----SETUP-----
    global SCREEN
    running = True
    start = time.time()
    dem = 1
    score = 0
    shooting_target = []
    shooting_target_x = []
    shooting_target_y = []
    shooting_target_change = []
    for i in range(5):
        shooting_target.append(pygame.image.load("minigame\\shooting-target.png"))
        shooting_target_x.append(random.randint(-500, 0))
        shooting_target_change.append(random.randint(5, 10))
        shooting_target_y.append(random.randint(0, 400))
    # target = transform(target, 40, 40)
    font = pygame.font.SysFont('Algerian', 40)
    c = shooting_target[0].get_width();
    instructions()
    while running:
        SCREEN.blit(bg, (0, 0))
        ###-----EVENT------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                gun_sound = mixer.Sound('gun_sound.wav')
                if sound:
                    gun_sound.play()
                for j in range(5):
                    mx, my = pygame.mouse.get_pos()
                    if (shooting_target_x[j] <= mx) and (mx <= shooting_target_x[j] + c) and my >= shooting_target_y[
                        j] and my <= shooting_target_y[j] + c:
                        shooting_target_x[j] = random.randint(-500, 0)
                        shooting_target_y[j] = random.randint(0, 400)
                        shooting_target_change[j] = random.randint(5, 10)
                        score += 1
                        break

        ###-------MOVE------
        mxt, myt = pygame.mouse.get_pos()
        mxt -= 16
        myt -= 16
        SCREEN.blit(target, (mxt, myt))
        SCREEN.blit(gun, (mxt, 500))
        for i in range(5):
            if shooting_target_x[i] > WIDTH * 1.4:
                shooting_target_x[i] = -300
                shooting_target_y[i] = random.randint(0, 400)
                shooting_target_change[i] = random.randint(5, 10)
            shooting_target_x[i] += shooting_target_change[i]
            SCREEN.blit(shooting_target[i], (shooting_target_x[i], shooting_target_y[i]))
        ###--------TEXT---------
        _time = 30 - dem
        end = time.time()
        if end - start > dem:
            dem += 1
        txtTime = font.render('Time: ' + str(_time), True, (255, 255, 255), )
        txtScore = font.render('Score: ' + str(score), True, (255, 255, 255), )
        SCREEN.blit(txtTime, (0, 0))
        SCREEN.blit(txtScore, (680, 0))
        if _time == 0:
            running = False
        ###--------UPDATE---------
        pygame.display.update()
        fpsClock.tick(FPS)
    EndGame(score)
    return score


def EndGame(score):
    ###----SETUP-----
    global SCREEN
    font = pygame.font.SysFont('Algerian', 30)
    running = True
    bg = pygame.image.load("minigame\\bg.png")
    res = pygame.image.load("minigame\\Result.png")
    font = pygame.font.SysFont(" consolas ", 25)
    text = font.render(" CLick right mouse to continue!",True,(64,64,64))
    while running:
        SCREEN.blit(bg, (0, 0))
        SCREEN.blit(res, (WIDTH / 2 - res.get_width() / 2, 200))
        SCREEN.blit(text, (230,450))
        ###-----EVENT------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 3:
                    running = False

        ###--------TEXT---------
        txtScore = font.render('Score: ' + str(score), True, (255, 255, 255))
        SCREEN.blit(txtScore, (WIDTH / 2 - txtScore.get_width() / 2, 270))
        ###--------UPDATE---------
        pygame.display.update()
        fpsClock.tick(FPS)
    return score