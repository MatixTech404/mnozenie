import random
import sys
from gra import *

import pygame as pg
from pygame.constants import *

pg.init()

SZEROKOSC, WYSOKOSC = 800, 600
EKRAN = pg.display.set_mode((SZEROKOSC, WYSOKOSC), 0, 32)

gra = Gra()

# czcionki
normal = pg.font.SysFont('', 120)


a = random.randint(1, 10)
b = random.randint(1, 10)

gra.utworz_obiekty()

while True:
    for e in pg.event.get():  # obsługa zdarzeń
        if e.type == QUIT:
            pg.quit()
            sys.exit()
    
    EKRAN.fill(KODP)

    gra.narysuj_obiekty(EKRAN)
