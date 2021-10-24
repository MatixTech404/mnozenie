import sys

import pygame as pg
from pygame.constants import *


# kolory
KTLO = (50, 50, 50)
KPYT = (200, 200, 200)


pg.init()

SZEROKOSC, WYSOKOSC = 800, 600
EKRAN = pg.display.set_mode((SZEROKOSC, WYSOKOSC), 0, 32)


while True:
    for e in pg.event.get():  # obsługa zdarzeń
        if e.type == QUIT:
            pg.quit()
            sys.exit()
    
    EKRAN.fill(KTLO)
    PYTANIE = pg.Rect(0, 0, 800, 300)

    pg.draw.rect(EKRAN, KPYT, PYTANIE)

    pg.display.update()
