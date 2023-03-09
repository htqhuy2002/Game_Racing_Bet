import pygame
from pygame.locals import *
import RacingBoy
import minigame
import datetime

pygame.mixer.init()
Music = pygame.mixer.music
Music.load("soundtrack.mp3")
Music.play(-1, 0.0, 0)

pygame.init()

SIZE = (900, 600)
Screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Racing')
Pyimg = pygame.image
fps = pygame.time.Clock()

Choosepos = [[700, 320], [700, 374], [700, 428], [700, 482]]
Chooseimg = []
for i in range(1, 8, 2):
    Chooseimg.append([pygame.image.load("mnc\\" + str(i) + ".png"), pygame.image.load("mnc\\" + str(i + 1) + ".png")])
Choosesz = (130, 44)

quitimg = (Pyimg.load("undo.png"), Pyimg.load("undo1.png"))
quitpos = (30, 510)
quitsize = (quitimg[0].get_width(), quitimg[0].get_height())


def inarea(x, y, size, m):
    if x <= m[0] and y <= m[1] and x + size[0] >= m[0] and y + size[1] >= m[1]:
        return True
    return False


def click():
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                return True
    return False


def Button(posittion, img, size, command):
    _x, _y = pygame.mouse.get_pos()
    nowp = (_x, _y)
    if inarea(posittion[0], posittion[1], size, nowp):
        Screen.blit(img[1], (posittion[0] - 5, posittion[1] - 5))
        pygame.time.delay(20)
        if click():
            command()
            return True
    else:
        Screen.blit(img[0], posittion)



class Undobutton:
    def __init__(self):
        self.img = (Pyimg.load("undo.png"), Pyimg.load("undo1.png"))
        self.size = (self.img[0].get_width(), self.img[0].get_height())
        self.pos = (30, 510)
        self.run = False

    def undo(self):
        self.run = True

    def place(self):
        Button(self.pos, self.img, self.size, self.undo)

    def update(self):
        self.run = False
        self.pos = (30, 510)

class Player:
    def __init__(self):
        self.account = ''
        self.password = ''
        self.coin = 5000
        self.amulet = [0,0,0,0]
        self.history = []
        self.winlose = [0,0]
        self.tempalte = []
        self.gender = -1
        self.font = pygame.font.SysFont(" consolas ", 25)
        self.pos = (10, 10)
        self.img = pygame.image.load("user\\male.png")
        self.boximg = (Pyimg.load("user\\box.png"),Pyimg.load("user\\history.png"),
        Pyimg.load("user\\history1.png"),Pyimg.load("user\\logout.png"),Pyimg.load("user\\logout1.png"))
        self.boxpos = (5, 60)
        self.list = []
        self.logout = False
    def Logout(self):
        save(player.account)
        money.cost = 3000
        self.amulet = [0, 0, 0, 0]
        self.history = []
        self.winlose = [0, 0]
        self.tempalte = []
        self.logout = True
        self.run = False
    def uppdate(self):
        if self.gender == 0:
            self.img = pygame.image.load("user\\male.png")
        else:
            self.img = pygame.image.load("user\\female.png")
        self.name = self.font.render(self.account, True, (255, 255, 255))
        self.money = money.cost
        self.amulet = store.data
    def place(self):
        Button(self.pos, (self.img, self.img), (60, 60), self.showoffer)
        Screen.blit(self.name, (self.pos[0] + 80, self.pos[1] + 20))
    def showoffer(self):
        self.run = True
        while self.run:
            Event()
            Screen.blit(self.name, (self.pos[0] + 80, self.pos[1] + 20))

            Screen.blit(self.boximg[0],self.boxpos)
            Button((self.boxpos[0]+55,self.boxpos[1]+175),(self.boximg[1],self.boximg[2]),
               (110,140),self.showhistory)
            Button((self.boxpos[0]+255,self.boxpos[1]+175),(self.boximg[3],self.boximg[4]),(110,127),self.Logout)
            mx,my = pygame.mouse.get_pos()
            if not inarea(self.boxpos[0],self.boxpos[1],(438,323),(mx,my)):
                pygame.time.delay(20)
                if click():
                    self.run =False
            pygame.display.update()

    def showhistory(self):
        self.Font = pygame.font.SysFont('consolas',26)
        t = len(self.history)
        self.list = []
        for i in range(t):
            text1 = self.Font.render(self.history[i][0], True, (64, 64, 64))
            text2 = self.Font.render(self.history[i][1], True, (64, 64, 64))
            text3 = self.Font.render(self.history[i][2], True, (64, 64, 64))
            self.list.append([text1,text2,text3])
        text4 = self.Font.render("Activities", True ,(64, 64, 64))
        while not undobutton.run:
            Event()
            Screen.blit(Pyimg.load("historybg.png"),(0,0))
            undobutton.place()
            Screen.blit(text4,(300,180))
            for k in range(t):
                Screen.blit(self.list[k][0], (300, 180 + t* 40 - 40 * k))
                Screen.blit(self.list[k][1], (630, 180 + t* 40 - 40 * k))
                Screen.blit(self.list[k][2], (730, 180 + t* 40 - 40 * k))
            Screen.blit(self.img,(85,235))
            Screen.blit(self.name,(60,310))
            pygame.display.update()
        undobutton.update()
        self.run = False

def Textbox(_x, _y, n, c):
    clock = pygame.time.Clock()
    input_box = pygame.Rect(_x, _y, 301, 40)
    font = pygame.font.SysFont(" consolas  ", 18)
    box_inactive = pygame.image.load("textbox.png")
    box_active = pygame.image.load("textbox1.png")
    box = box_inactive
    text = ''
    txt_surface = font.render(text,True,(255,255,255))
    font1 = pygame.font.SysFont(" consolas ",26)
    if n == 1:
        text1 = font1.render(" Username ", True, (64, 64, 64))
    else:
        text1 = font1.render(" Password ", True,(64,64,64))
    img = (Pyimg.load("signup.png"),Pyimg.load("signup1.png"))
    pos = (300,350)

    active = False
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                box = box_active if active else box_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif txt_surface.get_width() < 280:
                        text += event.unicode
        Screen.blit(Pyimg.load("signbg.png"),(0,0))
        if c == 1:
            t = Button(pos, img, (100,40), signup)
            if t == 1:
                return 1
        txt_surface = font.render(text, True, (255, 255, 255))
        Screen.blit(text1, (160, 275))
        Screen.blit(box, (_x, _y))
        Screen.blit(txt_surface, (_x + 5, _y + 13))
        pygame.display.update()
        clock.tick(30)

def male():
    player.gender = 1

def female():
    player.gender = 0

def savename(username, password):
    f = open('saveaccount.txt','a')
    f.write('\n')
    f.write(username+'\n')
    f.writelines(str(password))
    f.close()

def signup():
    player.account = Textbox(300, 265, 1,0)
    player.password = Textbox(300, 265, 0,0)
    img1 = (Pyimg.load("male.png"),Pyimg.load("male1.png"))
    img2 = (Pyimg.load("female.png"),Pyimg.load("female1.png"))
    pos = (290,200)
    size = (102,45)
    while True:
        Screen.blit(Pyimg.load("signbg.png"),(0,0))
        Event()
        if Button(pos,img1,size,male):
            player.amulet = [0, 0, 0, 0]
            savename(player.account,player.password)
            save(player.account)
            return 1
        if Button((pos[0]+112,pos[1]),img2,size,female):
            player.amulet = [0,0,0,0]
            savename(player.account,player.password)
            save(player.account)
            return 1
        pygame.display.update()

def load(filename,password):
    f = open('saveaccount.txt','r')
    while True:
        temp = f.readline()
        temp1 = f.readline()
        if temp == '':
            return -1
        elif temp.replace('\n','') == filename and temp1.replace('\n','') == password:
            f.close()
            ff = open(filename+".txt",'r')
            player.account = filename
            player.gender = int(ff.readline())
            money.cost = int(ff.readline())
            for i in range(4):
                store.data[i] = int(ff.readline())
                print(store.data[i])
            t = ff.readline()
            while t != '':
                player.history.append([t.replace('\n',''),
                ff.readline().replace('\n',''),ff.readline().replace('\n','')])
                t = ff.readline()
            player.uppdate()
            ff.close()
            return 1

def save(filename):
    print(filename)
    f = open(filename+".txt",'w')
    f.write(str(player.gender)+'\n')
    f.write(str(money.cost)+'\n')
    for i in range(4):
        f.write(str(player.amulet[i])+'\n')
    for i in range(len(player.history)):
        f.write(player.history[i][0]+'\n')
        f.write(player.history[i][1] + '\n')
        f.write(player.history[i][2] + '\n')
    f.close()

def Signin():
    font = pygame.font.SysFont(' consolas ', 20)
    text = font.render(" Your username or password was wrong. Please try again or sign up new.", True, (64, 64, 64))
    temp1 = 0
    Screen.blit(pygame.image.load("mnbg\\bg1.png"), (0, 0))
    done = False
    while not done:
        Event()
        if temp1 == -1:
            while True:
                Event()
                Screen.blit(text, (60, 100))
                pygame.time.delay(20)
                if click():
                    break
                pygame.display.update()
                fps.tick()

        t1 = Textbox(300, 265,1,1)
        if t1 == 1:
            load(player.account,player.password)
            return 1
        t4 = Textbox(300, 265, 0,1)
        if t4 == 1:
            load(player.account,player.password)
            return 1
        temp1 = load(t1,t4)
        if temp1 == 1:
            return 1
        pygame.display.update()

def write(text1,text2,text3):
    if len(player.history) >= 8:
        player.history.pop(0)
    player.history.append([text1, text2, text3])

def convert(money):
    if money< 0:
        player.winlose[1]+=1
        return "LOSE"
    elif money > 0:
        player.winlose[0]-=1
        return "WIN"
    elif money == 0:
        return "DRAW"

def createhistory(money):
    result = convert(money)
    date = datetime.datetime.now()
    date = str(date)
    while len(date) > 19:
        date = date[:18]+date[19:]
    coin = str(money) + "$"
    write(date,result,coin)

class Sound:
    def __init__(self):
        self.img = (Pyimg.load("soundon.png"), Pyimg.load("soundoff.png"))
        self.pos = (800, 14)
        self.status = True
        self.statusimg = (self.img[0], self.img[0])
        self.size = (Pyimg.load("soundon.png").get_width(), Pyimg.load("soundon.png").get_height())

    def place(self):
        if self.status:
            self.statusimg = (self.img[1], self.img[1])
            Music.stop()
        else:
            self.statusimg = (self.img[0], self.img[0])
            Music.play(-1, 0.0, 0)
        self.status = not self.status


class money:
    def __init__(self):
        self.cost = 3000
        self.coinimg = Pyimg.load("coin.png")
        self.pos = (600, 20)
        self.font = pygame.font.SysFont('Algerian', 29)
        self.wimg = Pyimg.load("warning.png")
        self.quit = False

    def place(self):
        Screen.blit(self.coinimg, self.pos)
        self.mntext = self.font.render(str(self.cost), True, (255, 255, 0))
        Screen.blit(self.mntext, (self.pos[0] + 70, self.pos[1] + 22))

    def undo(self):
        self.quit = True

    def waring(self):
        self.quit = False
        while not self.quit:
            Event()
            Screen.blit(self.wimg, (200, 50))
            Button((630, 90), (Pyimg.load("store\\quitimg.png"), Pyimg.load("store\\quitimg.png")), (35, 35), self.undo)
            pygame.display.update()
        self.quit = True
    def update(self):
        self.mntext = self.font.render(str(self.cost), True, (255, 255, 0))

class Background:
    def __init__(self):
        self.bglist = []
        for i in range(1, 6, 1):
            self.bglist.append(Pyimg.load("mnbg\\bg" + str(i) + ".png"))
        self.titleimg = [Pyimg.load("mnbg\\title.png"), Pyimg.load("mnbg\\Text.png")]
        self.ttpos = (70, 110)
        self.txtpos = (70, 510)

    def place(self):
        self.bgimg = self.bglist[(pygame.time.get_ticks() // 5000) % 5]
        Screen.blit(self.bgimg, (0, 0))
        Screen.blit(self.titleimg[0], self.ttpos)
        Screen.blit(self.titleimg[1], self.txtpos)
        Screen.blit(Pyimg.load("mnbg\\flag.png"), (405, 90))


class Store:
    def __init__(self):
        self.icon = [Pyimg.load("store\\storeicon.png"), Pyimg.load("store\\storeicon1.png")]
        self.iconsize = (self.icon[0].get_width(), self.icon[0].get_height())
        self.amuimg = []
        for i in range(1, 5, 1):
            self.amuimg.append([Pyimg.load("store\\" + str(i) + ".png"),
                                Pyimg.load("store\\" + str(i) + ".1.png")])
        self.amupos = [(44, 220), (258, 220), (472, 220), (686, 220)]
        self.amupos1 = [(470, 300), (590, 300), (470, 410), (590, 410)]
        self.amupos2 = [(230, 460), (350, 460), (470, 460), (590, 460)]
        self.amucost = [250, 500, 300, 600]
        self.data = player.amulet
        self.bg = Pyimg.load("store\\storebg.png")

        self.font = pygame.font.SysFont(' Consolas ', 20)
        self.quit = False
        self.run = 0
        self.choose = -1

    def Undo(self):
        self.quit = True

    def pay(self):
        self.data[self.run] += 1
        money.cost = money.cost - self.amucost[self.run]
        if money.cost < 0:
            money.waring()
            self.data[self.run] -= 1
            money.cost = money.cost + self.amucost[self.run]

    def storeplay(self):
        money.pos = (700, 20)
        for i in range(1,9,1):
            img = Pyimg.load("store\\s"+str(9-i)+".png")
            pos = (260-2.5*i,38-2.5*i)
            pygame.time.delay(12)
            Screen.blit(Pyimg.load("store\\storebg.png"),(0,0))
            Screen.blit(img,pos)

            pygame.display.update()
        #pygame.time.delay(22222222)
        while not self.quit:
            Event()
            Screen.blit(self.bg, (0, 0))
            Button(quitpos, quitimg, quitsize, self.Undo)
            for self.run in range(4):
                Button(self.amupos[self.run], (self.amuimg[self.run][1],
                                               self.amuimg[self.run][1]), (170, 170), self.pay)
            for i in range(4):
                self.text = self.font.render("x" + str(self.data[i]), True, (255, 255, 0))
                Screen.blit(self.amuimg[i][0], self.amupos2[i])
                Screen.blit(self.text, (self.amupos2[i][0] + 82, self.amupos2[i][1] + 31))
            Button((790,90),(Pyimg.load("minigame\\game.png"),Pyimg.load("minigame\\game1.png")),(94,100),Minigame)
            money.place()
            pygame.display.update()
        self.quit = False
        money.pos = (600, 20)

    def place(self):
        Button((495, 10), self.icon, self.iconsize, self.storeplay)
        for i in range(4):
            self.text = self.font.render("x" + str(self.data[i]), True, (255, 255, 0))
            Screen.blit(self.amuimg[i][0], self.amupos1[i])
            Screen.blit(self.text, (self.amupos1[i][0] + 86, self.amupos1[i][1] + 26))

def help():
    img = Pyimg.load("helpbg.png")
    undobutton.pos = (20,20)
    while not undobutton.run:
        Event()
        Screen.blit(img,(0,0))
        undobutton.place()
        pygame.display.update()
    undobutton.update()
def about():
    img = Pyimg.load("aboutbg.png")
    while not undobutton.run:
        Event()
        Screen.blit(img,(0,0))
        undobutton.place()
        pygame.display.update()
    undobutton.update()

class Startgame:
    def __init__(self):
        self.j = 0
        self.bglist = []
        for i in range(1, 6, 1):
            self.bglist.append(Pyimg.load("mnbg\\bg" + str(i) + ".png"))
        self.arimg = (Pyimg.load("ar2.png"), Pyimg.load("ar1.png"))
        self.mapos = (60, 130)
        self.armpos = [(self.mapos[0] - 40, self.mapos[1] + 105), (self.mapos[0] + 310, self.mapos[1] + 105)]
        self.armsize = (self.arimg[1].get_width(), self.arimg[1].get_height())
        self.map = []
        for i in range(1, 6, 1):
            self.map.append(Pyimg.load("choosemap\\" + str(i) + ".png"))
        """self.avaimg = []
        self.avapos = []
        for i in range(1, 7, 1):
            self.avaimg.append([Pyimg.load("choosep\\" + str(i) + ".png"),
                                Pyimg.load("choosep\\" + str(i) + ".1.png")])
            self.avapos.append([-83 + 143 * i, 130])
        self.avasize = (self.avaimg[0][0].get_width(), self.avaimg[0][0].get_width())"""
        self.nextimg = [Pyimg.load("next.png"), Pyimg.load("next.png")]
        self.nszie = (Pyimg.load("next.png").get_width(), Pyimg.load("next.png").get_height())
        self.chosizeimg = []

        for i in range(1,6,2):
            self.chosizeimg.append((Pyimg.load("store\\c"+str(i)+".png"),
                Pyimg.load("store\\c"+str(i+1)+".png")))

        self.pos = [(430,190),(558,190),(710,190)]
        self.mchoice = 0
        self.quit = False
        self.condition = False
        self.sz = 0
        self.x = 0
    def front(self):
        self.mchoice = self.mchoice + 1
        if self.mchoice == 5:
            self.mchoice = 0
    def behind(self):
        self.mchoice = self.mchoice - 1
        if self.mchoice == -1:
            self.mchoice = 4
    def Undo(self):
        self.quit = True

    def chooseava(self):
        self.save = self.j
        print(self.save)
        self.condition = True
    def start(self):



        #truyền self.mchoice với money.cost vào
        #trả ra số tiền thắng thua





        self.temp = RacingBoy.test2(self.mchoice,self.sz,money.cost, player.amulet,sound.status)


        createhistory(self.temp)
        money.cost = money.cost + self.temp
    def savesize(self):
        self.condition = True
        self.sz = self.x
        print(self.sz)

    def play(self):

        while not self.quit:
            Event()
            self.bgimg = self.bglist[(pygame.time.get_ticks() // 5000) % 5]
            Screen.blit(self.bgimg, (0, 0))
            money.place()
            Button(quitpos, quitimg, quitsize, self.Undo)
            Button(sound.pos, sound.statusimg, sound.size, sound.place)
            Button(self.armpos[0], (self.arimg[0], self.arimg[0]), self.armsize, self.behind)
            Button(self.armpos[1], (self.arimg[1], self.arimg[1]), self.armsize, self.front)
            Screen.blit(self.map[self.mchoice], self.mapos)
            if self.condition:
                Button((770, 420), self.nextimg, self.nszie, self.start)
            for self.x in range(3):
                Button(self.pos[self.x],self.chosizeimg[self.x],(110,60),self.savesize)
            store.place()

            pygame.display.update()
        self.quit = False
        self.mchoice = 0

player = Player()
undobutton = Undobutton()
sound = Sound()
money = money()
background = Background()
startgame = Startgame()
store = Store()
def Minigame():
    t = minigame.minigame(sound.status)
    money.cost = money.cost + t*10
    player.coin = money.cost

def Event():
    for event in pygame.event.get():
        if event.type == QUIT:
            player.uppdate()
            save(player.account)
            exit()
def Exit():
    save(player.account)
    exit()
def Menuplay():
    while not player.logout:
        Event()
        background.place()
        Button(Choosepos[0], Chooseimg[0], Choosesz, startgame.play)
        Button(Choosepos[1], Chooseimg[1], Choosesz, help)
        Button(Choosepos[2], Chooseimg[2], Choosesz, about)
        Button(Choosepos[3], Chooseimg[3], Choosesz, Exit)
        Button(sound.pos, sound.statusimg, sound.size, sound.place)
        player.place()
        money.place()
        pygame.display.update()

def gameplay():
    while not player.logout:
        Event()
        Signin()
        Menuplay()
        player.logout = False

gameplay()
