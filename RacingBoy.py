import pygame, sys, random, time, os
import importlib
import minigame
from pygame.locals import *
from pygame import mixer

pygame.init()

# screen
WIDTH = 900
HEIGHT = 600
amulet = [0, 0, 0, 0]
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
pygame.display.set_caption("DUA XE CA CUOC")
FPS = 60
bg1 = pygame.mixer.music
fpsClock = pygame.time.Clock()
kx = 1
ky = 1
tien = 0
store_speed = []
store_slow = []
speed_up = pygame.image.load("speed_up.png")
slow_down = pygame.image.load("slow_down.png")
xuat_phat = pygame.image.load("xuatphat.png")
ve_dich = pygame.image.load("vedich.png")


###


# image transformation
def transform(img, w, h):
    img = pygame.transform.scale(img, (int(w), int(h)))
    return img


def transform2(img, h):
    k = img.get_height() / h
    img = pygame.transform.scale(img, (int(img.get_width() / k), int(h)))
    return img


sound = True
# upload images
CAR = [[], [], [], [], [], []]
TRACK = pygame.surface.Surface((0, 0))
TRACK2 = pygame.surface.Surface((0, 0))


# finish = pygame.image.load("finish.png")


def game_images(set):
    global CAR, TRACK, TRACK2
    TRACK = pygame.image.load(set + "\\bg1.png")
    TRACK2 = pygame.image.load(set + "\\bg2.png")
    CAR = [[], [], [], [], [], []]
    for i in range(6):
        for j in range(10):
            CAR[i].append(pygame.image.load(set + "\\nv" + str(i + 1) + "\\" + str(j + 1) + ".png"))


# draw car
def _car(CAR, x, y):
    SCREEN.blit(CAR, (x, y))


# track
def _track(x):
    SCREEN.blit(TRACK, (- x, 0))
    SCREEN.blit(TRACK2, (TRACK.get_width() - x, 0))


# Met moi vc
def huydeptrai(kx, ky):
    global TRACK, TRACK2, CAR

    TRACK = transform(TRACK, TRACK.get_width() * kx, TRACK.get_height() * ky)
    TRACK2 = transform(TRACK2, TRACK2.get_width() * kx, TRACK2.get_height() * ky)
    for i in range(6):
        for j in range(10):
            CAR[i][j] = transform(CAR[i][j], CAR[i][j].get_width() * kx, CAR[i][j].get_height() * ky)


# def test2(set1, length, tien):
def test2(set1, length, tien, bua_store, sound1):
    ###----SETUP-----
    # bg1.play()
    global SCREEN, WIDTH, HEIGHT, kx, ky, TRACK, TRACK2, sound
    sound=sound1
    running = True
    # bg1.stop()
    set = 'set' + str(set1 + 1)
    game_images(set)
    car_y = []
    length = length / 2
    car_change = [0, 0, 0, 0, 0, 0]
    track_change = 0
    track_x = 0
    bua_images = []
    zbua = ["speed_up.png", "slow_down.png", "shit.png", "flash.png", "clock.png"]
    bua1 = [0.7, -0.35, -0.8, 50, -1.5]
    bua_trangthai = []
    bua_chucnang = []
    bua_x = []
    bua_y = []
    change = 1
    bua_sudung = []
    STORE = []
    print(store_slow)
    print(store_speed)
    for i in range(6):
        car_change[i] = random.randint(65, 100) / 100
        bua_trangthai.append(0)
        bua_sudung.append(0)
        bua_x.append(random.randint(1, 10 * (length + 1)) * 100)
        k = random.randint(0, 4)
        bua_images.append(pygame.image.load(zbua[k]))
        bua_images[i] = transform2(bua_images[i], HEIGHT / 13)
        bua_chucnang.append(bua1[k])
        car_y.append((i + 1) * HEIGHT / 8)
        bua_y.append(car_y[i])
    car_x2 = [0, 0, 0, 0, 0, 0]
    dem = 0
    rank = 0
    RANK = [0, 1, 2, 3, 4, 5]
    x = 0
    kt = False
    Choose = []
    TienCuoc = []
    Vitri = [2, 1.5, 1, 0.5, 0, 0]
    # --------------------
    TRACK = transform(TRACK, WIDTH, HEIGHT)
    TRACK2 = transform(TRACK2, WIDTH, HEIGHT)
    for i in range(6):
        for j in range(10):
            CAR[i][j] = transform2(CAR[i][j], HEIGHT / 10)
    CACUOC = cacuoc(car_y, tien, bua_store)
    for i in range(6):
        STORE.append(store_slow[i] + store_speed[i])
        if CACUOC[i] > 0:
            Choose.append(i)
            TienCuoc.append(CACUOC[i])
    TienCaCuoc = CACUOC[6]
    bg1.stop()
    Cho(car_y)
    start = time.time()
    bg = mixer.Sound('bg.mp3')
    if sound:
        bg.play(-1)
    while running:
        ###-----EVENT------

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == VIDEORESIZE:
                kx = (event.w / WIDTH)
                ky = (event.h / HEIGHT)
                WIDTH = event.w
                HEIGHT = event.h
                SCREEN = pygame.display.set_mode((event.w, event.h), RESIZABLE)
                huydeptrai(kx, ky)

        ###-------MOVE------
        end = time.time()

        if end - start > 4: track_change = 1 * kx
        _track(track_x)
        SCREEN.blit(xuat_phat, (WIDTH / 20 - track_x, HEIGHT / 2 - xuat_phat.get_height() / 2))
        SCREEN.blit(ve_dich, (
            int(WIDTH * (1 + length) - ve_dich.get_width() - track_x), int(HEIGHT / 2 - ve_dich.get_height() / 2) + 10))

        if track_x >= TRACK.get_width() * length: track_change = 0
        track_x += track_change
        for i in range(6):
            if end - start > 2: STORE[i] = 0
            bua_x[i] -= track_change
            if bua_x[i] < car_x2[i] + CAR[0][0].get_width():
                bua_trangthai[i] = 1
                bua_sudung[i] = time.time()
                bua_x[i] = 10000
            if bua_chucnang[i] == -1.5:
                if bua_trangthai[i] == 1 and end - bua_sudung[i] > 1:
                    bua_trangthai[i] = 0
            if bua_chucnang[i] == 50:
                if bua_trangthai[i] == 1 and end - bua_sudung[i] > 1 / 60:
                    bua_trangthai[i] = 0
            if bua_trangthai[i] == 1 and end - bua_sudung[i] > 2:
                bua_trangthai[i] = 0

                car_y[i] = ((i + 1) * HEIGHT / 8)
            bua_y[i] = car_y[i]
            SCREEN.blit(bua_images[i], (bua_x[i], bua_y[i]))
            if end - start > change * 2 and car_change[i] > 0:
                change += 1
                for j in range(6):
                    if car_change[j] > 0: car_change[j] = random.randint(65, 100) / 100
            if car_change[i] > 0:
                car_x2[i] = car_x2[i] + car_change[i] * kx - track_change + bua_trangthai[i] * bua_chucnang[i] + STORE[
                    i]
            if car_x2[i] > WIDTH - CAR[0][0].get_width():
                car_x2[i] = WIDTH - CAR[0][0].get_width()
                RANK[i] = rank
                rank += 1
                car_change[i] = 0
                print(i)
                if rank > 5: kt = True
            if car_x2[i] == WIDTH - CAR[0][0].get_width():
                _car(CAR[i][0], car_x2[i], car_y[i])
            else:
                _car(CAR[i][dem], car_x2[i], car_y[i])
            end = time.time()
            if end - start > x * 0.1:
                dem = dem + 1
                x += 1
            if dem > 9:
                dem = 0
        ###--------UPDATE---------
        pygame.display.update()
        fpsClock.tick(FPS)
        if kt:
            running = False
    TienThangCuoc = 0
    dem = 0
    for i in Choose:
        TienThangCuoc += int(Vitri[RANK[i]] * TienCuoc[dem])
        dem += 1
    bg.stop()
    if sound:
        bg1.play(-1)
    win(RANK, TienThangCuoc - TienCaCuoc, CACUOC)
    return (TienThangCuoc - TienCaCuoc)


def win(RANK, TienThangCuoc, CACUOC):
    ###----SETUP-----
    TienThangCuoc = int(TienThangCuoc)
    global SCREEN, WIDTH, HEIGHT, CAR
    # top= []
    Car_copy = []
    for i in range(6):
        Car_copy.append(CAR[i][0])
        Car_copy[i] = (transform2(Car_copy[i], 30))
    font = pygame.font.SysFont("Arial Black", 20)
    font1 = pygame.font.SysFont("Tahoma", 17)
    bg = pygame.image.load("bg_win.jpg")
    kx = bg.get_width() / WIDTH
    ky = bg.get_height() / HEIGHT
    buc = pygame.image.load("buc.png")
    bg = transform(bg, bg.get_width() / kx, bg.get_height() / ky)
    buc = transform(buc, buc.get_width() / kx, buc.get_height() / ky)
    btn = pygame.image.load("btn.png")
    running = True
    while running:
        SCREEN.blit(bg, (0, 0))
        SCREEN.blit(btn, (WIDTH - btn.get_width() - 5, HEIGHT - btn.get_height() - 5))
        SCREEN.blit(buc, (WIDTH / 2 - buc.get_width() / 2, HEIGHT * 0.5))
        tien = font1.render("Tiền thắng cược: " + str(TienThangCuoc) + "$", True, (0, 0, 0))
        SCREEN.blit(tien, (WIDTH / 2 - tien.get_width() / 2, HEIGHT * 525 / 600 - tien.get_height() / 2))
        for x1 in range(3):
            SCREEN.blit(Car_copy[x1], (655, 55 + 65 * x1))
            tien = font.render(str(CACUOC[x1]), True, (255, 255, 255))
            SCREEN.blit(tien, (710, 55 + 65 * x1))
            SCREEN.blit(Car_copy[x1 + 3], (780, 55 + 65 * x1))
            tien = font.render(str(CACUOC[x1 + 3]), True, (255, 255, 255))
            SCREEN.blit(tien, (835, 55 + 65 * x1))
        ###---------------------------
        ###-----EVENT------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                WIDTH = event.w
                HEIGHT = event.h
                kx = bg.get_width() / WIDTH
                ky = bg.get_height() / HEIGHT
                bg = transform(bg, bg.get_width() / kx, bg.get_height() / ky)
                buc = transform(buc, buc.get_width() / kx, buc.get_height() / ky)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if (mx >= WIDTH - btn.get_width() and my >= HEIGHT - btn.get_height()):
                    running = False
        ###-----------------
        for j in range(6):
            if RANK[j] == 0:
                SCREEN.blit(CAR[j][0],
                            (WIDTH / 2 - CAR[j][0].get_width() / 2, HEIGHT * 190 / 600 + CAR[j][0].get_height()))
            if RANK[j] == 1:
                SCREEN.blit(CAR[j][0], (
                    WIDTH / 2 - CAR[j][0].get_width() / 2 - WIDTH * 175 / 900,
                    HEIGHT * 235 / 600 + CAR[j][0].get_height()))
            if RANK[j] == 2:
                SCREEN.blit(CAR[j][0], (
                    WIDTH / 2 - CAR[j][0].get_width() / 2 + WIDTH * 175 / 900,
                    HEIGHT * 265 / 600 + CAR[j][0].get_height()))
            if RANK[j] == 3:
                txtTop = font.render("TOP 4:", True, (255, 255, 255))
                SCREEN.blit(txtTop, (0, 50))
                CAR_copy = transform2(CAR[j][0], 35)
                SCREEN.blit(CAR_copy, (80, 50))
            if RANK[j] == 4:
                txtTop = font.render("TOP 5:", True, (255, 255, 255))
                SCREEN.blit(txtTop, (0, 120))
                CAR_copy = transform2(CAR[j][0], 35)
                SCREEN.blit(CAR_copy, (80, 120))
            if RANK[j] == 5:
                txtTop = font.render("TOP 6:", True, (255, 255, 255))
                SCREEN.blit(txtTop, (0, 190))
                CAR_copy = transform2(CAR[j][0], 35)
                SCREEN.blit(CAR_copy, (80, 190))

        ###--------UPDATE---------
        pygame.display.update()
        fpsClock.tick(FPS)
    return (TienThangCuoc)


def DatCuoc(a, vitri, txtx, Tien, y):
    font = pygame.font.SysFont("Arial Black", 25)
    text = font.render(str(Tien[vitri]), True, (255, 255, 255))
    SCREEN.blit(text, (txtx - text.get_width() / 2 + a.get_width() / 2, y))


def click(a, x, y):
    mx, my = pygame.mouse.get_pos()
    if x <= mx <= x + a.get_width() and y <= my <= y + a.get_height(): return (True)
    return (False)


#
def cacuoc(car_y, tien, bua_store):
    ###----SETUP-----
    # _sound = mixer.Sound("soundtrack.mp3")
    # _sound.play()
    # tien = 1000
    tien1 = tien
    global SCREEN, kx, ky, WIDTH, HEIGHT, store_slow, store_speed
    store_speed = []
    store_slow = []
    coin = pygame.image.load("coin.png")
    font = pygame.font.SysFont("Algerian", 29)
    Font = pygame.font.SysFont("consolas", 20)
    speed_buff_images = []
    slow_buff_images = []
    TienCuoc = []
    vitri = []
    txt = []
    t = []
    bua_images = []
    bua_pos = [(650, 10), (710, 10), (770, 10), (830, 10)]
    bua_pos2 = [(665, 60), (725, 60), (785, 60), (845, 60)]
    tex = []
    d = []
    txtx = []
    txty = []
    tx = []
    ty = []
    dx = []
    dy = []
    tong = 0
    '''

    '''
    speed0 = pygame.image.load("speed_buff.png")
    speed0 = transform(speed0, 50, 50)
    speed1 = pygame.image.load("speed2.png")
    speed1 = transform(speed1, 50, 50)
    slow0 = pygame.image.load("slow_buff.png")
    slow0 = transform(slow0, 50, 50)
    slow1 = pygame.image.load("slow2.png")
    slow1 = transform(slow1, 50, 50)
    sp = []
    sl = []
    next = pygame.image.load("right_arrow.png")
    Tien = [0, 250, 500, 750, 1000]
    for i in range(4):
        bua_images.append(pygame.image.load("store\\" + str(i + 1) + ".png"))
        bua_images[i] = transform(bua_images[i], 50, 50)
        tex.append(Font.render('x' + str(bua_store[i]), True, (255, 255, 0)))

    for i in range(6):
        txt.append(pygame.image.load("txt.png"))
        t.append(pygame.image.load("t.png"))
        d.append(pygame.image.load("d.png"))
        sp.append(0)
        sl.append(0)
        speed_buff_images.append(speed0)
        slow_buff_images.append(slow0)
        speed_buff_images[i] = transform(speed_buff_images[i], 50, 50)
        slow_buff_images[i] = transform(slow_buff_images[i], 50, 50)
        vitri.append(0)
    for i in range(6):
        txtx.append(WIDTH / 2 - txt[0].get_width() / 2 - WIDTH / 10)
        txty.append(car_y[i] + HEIGHT / 40)
        tx.append(txtx[i] + txt[0].get_width() + 1)
        ty.append(txty[i])
        dx.append(txtx[i] + txt[0].get_width() + 1)
        dy.append(txty[i] + t[i].get_height())

    running = True
    while running:
        strTien = font.render(str(tien1), True, (255, 255, 0))
        SCREEN.blit(TRACK, (0, 0))
        SCREEN.blit(next, (WIDTH - next.get_width() * 1.5, car_y[5]))
        SCREEN.blit(xuat_phat, (WIDTH / 20, HEIGHT / 2 - xuat_phat.get_height() / 2))
        SCREEN.blit(coin, (WIDTH * 0.75, car_y[1]))
        SCREEN.blit(strTien, (WIDTH * 0.75 + coin.get_width() / 1.5 - strTien.get_width() / 2,
                              car_y[1] + coin.get_height() / 2 - strTien.get_height() / 2))
        ###-----EVENT------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                WIDTH = event.w
                HEIGHT = event.h
            if event.type == pygame.MOUSEBUTTONDOWN:
                for j in range(6):
                    if click(t[j], tx[j], ty[j]) and tien1 >= 250:
                        vitri[j] += 1
                        tong += 250
                        tien1 -= 250
                        click_sound = mixer.Sound('click2.wav')
                        if sound == True:
                            click_sound.play()
                        if vitri[j] > 4:
                            vitri[j] = 4
                            tong -= 250
                            tien1 += 250
                    if click(d[j], dx[j], dy[j]):
                        click_sound = mixer.Sound('click2.wav')
                        if sound:
                            click_sound.play()
                        vitri[j] -= 1
                        tong -= 250
                        tien1 += 250
                        if vitri[j] < 0:
                            vitri[j] = 0
                            tong += 250
                            tien1 -= 250
                    if click(slow_buff_images[j], WIDTH / 2 + 60, txty[j]):
                        if sl[j] == 0 and bua_store[1] >= 1:
                            sl[j] = 1
                            bua_store[1] -= 1
                            slow_buff_images[j] = slow1
                        elif sl[j] == 1:
                            bua_store[1] += 1
                            sl[j] = 0
                            slow_buff_images[j] = slow0
                    if click(speed_buff_images[j], WIDTH / 2, txty[j]):
                        if sp[j] == 0 and bua_store[0] >= 1:
                            sp[j] = 1
                            bua_store[0] -= 1
                            speed_buff_images[j] = speed1
                        elif sp[j] == 1:
                            sp[j] = 0
                            bua_store[0] += 1
                            speed_buff_images[j] = speed0
                if click(next, WIDTH - next.get_width() * 1.5, car_y[5]):
                    running = False
                    click_sound = mixer.Sound('click2.wav')
                    if sound:
                        click_sound.play()

        ###-----------------
        for i in range(4):
            SCREEN.blit(bua_images[i], bua_pos[i])
            tex[i] = (Font.render('x' + str(bua_store[i]), True, (255, 255, 0)))
            SCREEN.blit(tex[i], bua_pos2[i])
        for i in range(6):
            _car(CAR[i][0], 0, car_y[i])
            SCREEN.blit(txt[i], (txtx[i], txty[i]))
            SCREEN.blit(speed_buff_images[i], (WIDTH / 2, txty[i]))
            SCREEN.blit(slow_buff_images[i], (WIDTH / 2 + 60, txty[i]))
            SCREEN.blit(t[i], (tx[i], ty[i]))
            SCREEN.blit(d[i], (dx[i], dy[i]))
            DatCuoc(txt[0], vitri[i], txtx[i], Tien, txty[i])
        ###----------------------
        ###--------UPDATE---------
        pygame.display.update()
        fpsClock.tick(FPS)
    res = []
    for i in range(6):
        res.append(Tien[vitri[i]])
        store_speed.append(0.7 * sp[i])
        store_slow.append(-0.35 * sl[i])
    res.append(tong)
    # _sound.stop()
    return res


def Cho(car_y):
    ###----SETUP-----
    global SCREEN
    start = time.time()
    dem = 1
    font = pygame.font.SysFont("Tahoma", 150)
    text = font.render(str(4 - dem), True, (255, 255, 255))
    running = True
    count_down = mixer.Sound('countdown.wav')
    if sound:
        count_down.play()
    while running:
        SCREEN.blit(TRACK, (0, 0))
        SCREEN.blit(xuat_phat, (WIDTH / 20, HEIGHT / 2 - xuat_phat.get_height() / 2))
        ###-----EVENT------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        ###--------------------
        for i in range(6):
            _car(CAR[i][0], 0, car_y[i])
        ###--------TEXT---------
        end = time.time()
        if end - start > dem - 1:
            text = font.render(str(4 - dem), True, (255, 255, 255))
            if 4 - dem == 0: break
            dem += 1

        SCREEN.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
        ###--------UPDATE---------
        pygame.display.update()
        fpsClock.tick(FPS)

# minigame()
# minigame.minigame()
# test()
