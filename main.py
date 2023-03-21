import pygame as pg
from funciones import *
pygame.init()
pantalla = pygame.display.set_mode((800,650))
fondo = pygame.image.load("Recursos/Fondo.jpg")
logo = pygame.image.load("Recursos/WordleLogo.png")
pantalla.blit((pygame.transform.scale(fondo, (800,650))), (0,0))
pygame.display.set_icon(logo)
pygame.display.set_caption("Wordle")
musicawin= pygame.mixer.Sound('Recursos/tomp3.cc - HD  100000 Social Credit Sound Effect.mp3')
musicaloss= pygame.mixer.Sound('Recursos/tomp3.cc - Grito meme.mp3')
retry = pygame.image.load('Recursos/retry.png')
nuevojuego = juego(pantalla)
win = pygame.image.load('Recursos/win win (1).jpg')
loss = pygame.image.load('Recursos/loss loss (1).jpg')


def PantallaVictoria():
    pantalla.blit((pygame.transform.scale(win, (800, 650))), (0, 0))
    pygame.mixer.Sound.play(musicawin)
    pygame.display.flip()
    time.sleep(2)
    Retry()
    time.sleep(2)

def PantallaDerrota():
    pantalla.blit((pygame.transform.scale(loss, (800, 650))), (0, 0))
    pygame.mixer.Sound.play(musicaloss)
    pygame.display.flip()
    time.sleep(2)
    Retry()
    time.sleep(2)

def Retry():
    pantalla.blit((pygame.transform.scale(retry, (800, 650))), (0, 0))
    pygame.display.flip()

def Jugar(nuevojuego):
    while nuevojuego.jugando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pg.quit()

            if event.type == pygame.KEYDOWN:
                nuevojuego.teclapulsada(event)
        pg.display.flip()

    if nuevojuego.winloss():
        PantallaVictoria()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    nuevojuego = juego(pantalla)
                    pantalla.blit((pygame.transform.scale(fondo, (800, 650))), (0, 0))
                    nuevojuego.colocarteclado()
                    pygame.mixer.stop()
                elif event.key == pygame.K_n:
                    pg.quit()
    else:
        PantallaDerrota()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    nuevojuego = juego(pantalla)
                    pantalla.blit((pygame.transform.scale(fondo, (800, 650))), (0, 0))
                    nuevojuego.colocarteclado()
                    pygame.mixer.stop()
                elif event.key == pygame.K_n:
                    pg.quit()



Jugar(nuevojuego)

            










# randompalabra(palabra(5))




