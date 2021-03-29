# Copyright (c)
import pygame
import sys

from pygame.constants import *

import silnik as si
from gra import Gra


def zakoncz():
    pygame.quit()
    sys.exit()


def koniec(wybor: int) -> None:
    global EKRAN, CZARNY, BIALY, font
    EKRAN.fill(CZARNY)
    ntekst = font.render('Dobrze' if wybor == 1 else 'Źle', True, BIALY, CZARNY)
    EKRAN.blit(ntekst, ntekst.get_rect(centerx=EKRAN.get_rect().centerx,
                                       centery=EKRAN.get_rect().centery))
    pygame.display.update()

    # nowa pętla zdarzen
    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                zakoncz()

            if e.type == KEYDOWN:
                if e.key == K_ESCAPE or e.key == K_q:
                    zakoncz()
                if e.key == K_r:
                    pygame.quit()


gracz = pygame.Rect(1, 1, 1, 1)

pygame.init()
CZARNY = (10, 10, 10)
BIALY = (240, 240, 240)
K404 = (44, 207, 1)

# zmienne i stałe
PREDKOSC = 10
SZEROKOSC, WYSOKOSC = 700, 600
EKRAN = pygame.display.set_mode((SZEROKOSC, WYSOKOSC), 0, 32)
zegar = pygame.time.Clock()

a, b = si.losuj()

# ruch
gora = False
lewo = False
dol = False
prawo = False

# teksty i czcionki
font = pygame.font.SysFont('', 100)
napis = font.render(f'{a} X {b} =', True, BIALY, CZARNY)
rnapis = napis.get_rect(centerx=EKRAN.get_rect().centerx,
                        y=0)

opcja1 = font.render(f'{a*a*b}', True, CZARNY, BIALY)
opcja2 = font.render(f'{a * b}', True, CZARNY, BIALY)
opcja3 = font.render(f'{a*b*b}', True, CZARNY, BIALY)

rect1 = opcja1.get_rect(bottomleft=EKRAN.get_rect().bottomleft)
rect2 = opcja2.get_rect(midbottom=EKRAN.get_rect().midbottom)
rect3 = opcja3.get_rect(bottomright=EKRAN.get_rect().bottomright)

opcje = [rect1, rect2, rect3]
opcja = int()

# pierwsze rysowanie elementów
EKRAN.fill(CZARNY)
EKRAN.blit(napis, rnapis)
EKRAN.blit(opcja1, rect1)
EKRAN.blit(opcja2, rect2)
EKRAN.blit(opcja3, rect3)
pygame.display.update()

while True:
    # sprawdzanie eventów
    for e in pygame.event.get():
        if e.type == QUIT:
            zakoncz()

        if e.type == MOUSEMOTION:
            gracz.centerx = e.pos[0]
            gracz.centery = e.pos[1]

    # narysuj tło i tekst
    EKRAN.fill(CZARNY)
    EKRAN.blit(napis, rnapis)

    # narysuj gracza
    pygame.draw.rect(EKRAN, K404, gracz)

    # sprawdź, czy nie zaszła kolizja
    for r in opcje:
        if gracz.colliderect(r):
            if r is rect1:
                opcja = 0
            elif r is rect2:
                opcja = 1
            else:
                opcja = 2
            koniec(opcja)

    EKRAN.blit(opcja1, rect1)
    EKRAN.blit(opcja2, rect2)
    EKRAN.blit(opcja3, rect3)
    pygame.display.update()
    zegar.tick(60)
