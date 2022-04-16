from pygame import *
import sys
import random


#PANTALLA#
init()
screen = display.set_mode((800,600))
vel= 2

#PERSONAJE#
yoshi = image.load("yoshi.png")
yoshi = transform.scale(yoshi,(100,100))
yoshi = transform.flip(yoshi,True,False)
xYoshi , yYoshi = 350,400

coin = image.load("coin.png")
coin = transform.scale(coin,(100,100))
xCoin, yCoin = 500,100


mush = image.load("mushu.png")
mush = transform.scale(mush,(100,100))
xMush, yMush = -500,100


come = image.load("yoshicome.png")
come = transform.scale(come,(200,100))
come = transform.flip(come,True,False)
auxyoshi = yoshi


#FUNTE#
calibriFont = font.SysFont("Calibri", 40)
calibriFont2 = font.SysFont("Calibri", 120)
calibriFont3 = font.SysFont("Calibri", 60)
cont = 0

#SONIDO#
mixer.init()
sound = mixer.Sound ("yoshi.wav")
mixer.music.load("backmusic.wav")
mixer.music.play(-1)
mixer.music.set_volume(0.1)

#RELOJ#
clock = time.Clock()
contmush = 0

    
def pantalla3():
    while True:
        screen.fill((40,140,240))
        for e in event.get():
            if e.type == QUIT: sys.exit()
        
        
        hello = calibriFont.render("Yoshi´s GAME", True, (4,4,4))
        contador = calibriFont3.render("Monedas recolectadas: " + str(cont) ,True,(4,4,4))
        despedida = calibriFont3.render("GRACIAS POR JUGAR",True,(4,4,4))
        screen.blit(hello, (300, 0))
        screen.blit(despedida, (150, 100))
        screen.blit(contador, (100, 300))
        
        
        
        clock.tick(60) 
        display.flip()
        
        
        
def pantalla2():
    while True:
        screen.fill((40,140,240))
        for e in event.get():
            if e.type == QUIT: sys.exit()
            
        global cont, xCoin, yCoin, xYoshi, yYoshi, xMush, yMush, contmush, vel, xBala, yBala, disparo, yoshi
        hello = calibriFont.render("Yoshi´s GAME", True, (4,4,4))
        contador = calibriFont.render("Monedas recolectadas: " + str(cont) ,True,(4,4,4))
        timer = calibriFont.render("Tiempo: " + str(time.get_ticks()/1000) ,True,(4,4,4))
        game = calibriFont2.render("FIN DEL TIEMPO" ,True,(4,4,4))
        screen.blit(hello, (300, 0))
        screen.blit(contador, (0, 550))
        screen.blit(timer, (0, 0))
        screen.blit(coin, (xCoin, yCoin))
        
        yoshi = auxyoshi
        contmush= contmush + 1
        
        coinRect = Rect(xCoin, yCoin, coin.get_width(), coin.get_height())
        yoshiRect = Rect(xYoshi, yYoshi, yoshi.get_width(), yoshi.get_height())
        mushRect = Rect(xMush, yMush, mush.get_width(), mush.get_height())
        if coinRect.colliderect(yoshiRect):
            xCoin, yCoin = (random.randint(100,700),random.randint(100,500))
            cont = cont + 1
            sound.play()
            
        screen.blit(mush,(xMush, yMush))
        
        if key.get_pressed()[K_SPACE]:
            yoshiRect = Rect(xYoshi, yYoshi, come.get_width(), come.get_height())
            yoshi = come
            
            
        if contmush == 500:
            vel = 2
        
        if contmush == 600:
            xMush, yMush = random.randint(100,700),random.randint(100,500)
        
        if xYoshi <= -20:
            xYoshi = 600
        if yYoshi <= 0:
            yYoshi = 600
        if xYoshi >= 700:
            xYoshi = 0
        if yYoshi >= 600:
            yYoshi = 0
        if mushRect.colliderect(yoshiRect):
            xMush, yMush = -500, 100
            vel = 5
            contmush = 0
            
            
        if key.get_pressed()[K_d]:
            xYoshi= xYoshi + vel
        if key.get_pressed()[K_a]:
            xYoshi= xYoshi - vel
        if key.get_pressed()[K_s]:
            yYoshi= yYoshi + vel
        if key.get_pressed()[K_w]:
            yYoshi= yYoshi - vel
        
            
        screen.blit(yoshi, (xYoshi, yYoshi))
        clock.tick(60)        
        if time.get_ticks()/1000 > 40:
            screen.blit(game, (0,200))
            if time.get_ticks()/1000 > 42:
                pantalla3()
        
        display.flip()



while True:
    screen.fill((40,140,240))
    for e in event.get():
        if e.type == QUIT: sys.exit()
        
    if xYoshi <= -20:
        xYoshi = 600
    if yYoshi <= 0:
        yYoshi = 600
    if xYoshi >= 700:
        xYoshi = 0
    if yYoshi >= 600:
        yYoshi = 0
        
    if key.get_pressed()[K_d]:
        xYoshi= xYoshi + vel
    if key.get_pressed()[K_a]:
        xYoshi= xYoshi - vel
    if key.get_pressed()[K_s]:
        yYoshi= yYoshi + vel
    if key.get_pressed()[K_w]:
        yYoshi= yYoshi - vel
    
    hello = calibriFont.render("Yoshi´s GAME", True, (4,4,4))
    niv1 = calibriFont.render("INCIAR JUEGO", True, (4,4,4))
    screen.blit(niv1,(300,100))
    niv1Rect = Rect(300, 100, niv1.get_width(), niv1.get_height())
    yoshiRect = Rect(xYoshi, yYoshi, yoshi.get_width(), yoshi.get_height())
    screen.blit(yoshi,(xYoshi, yYoshi))
    screen.blit(hello, (300, 0))
    
    if niv1Rect.colliderect(yoshiRect):
        xYoshi, yYoshi = 100,100
        pantalla2()
        
    clock.tick(60) 
    display.flip()

