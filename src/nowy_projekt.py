import sys

import pygame as pg
from pygame.constants import *


# kolory
KPYT = (70, 220, 30)
KODP = (40, 40, 40)


pg.init()

SZEROKOSC, WYSOKOSC = 800, 600
EKRAN = pg.display.set_mode((SZEROKOSC, WYSOKOSC), 0, 32)


while True:
    for e in pg.event.get():  # obsługa zdarzeń
        if e.type == QUIT:
            pg.quit()
            sys.exit()
    
    EKRAN.fill(KODP)
    PYTANIE = pg.Rect(0, 0, 800, 300)

    pg.draw.rect(EKRAN, KPYT, PYTANIE)

    pg.display.update()
