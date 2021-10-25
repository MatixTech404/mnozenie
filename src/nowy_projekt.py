import sys

import pygame as pg
from pygame.constants import *


# kolory
BIALY   = (200, 200, 200)
KPYT    = (70, 220, 30)
KODP    = (40, 40, 40)


pg.init()

SZEROKOSC, WYSOKOSC = 800, 600
EKRAN = pg.display.set_mode((SZEROKOSC, WYSOKOSC), 0, 32)


# czcionki
normal = pg.font.SysFont('', 150)


a = 5
b = 3

while True:
    for e in pg.event.get():  # obsługa zdarzeń
        if e.type == QUIT:
            pg.quit()
            sys.exit()
    
    EKRAN.fill(KODP)
    pole_pytania = pg.Rect(0, 0, 800, 300)

    pytanie = normal.render(f'Ile to {a} razy {b}?', True, BIALY)
    pytanie_rect = pytanie.get_rect(center=(400, 150))

    pg.draw.rect(EKRAN, KPYT, pole_pytania)

    EKRAN.blit(pytanie, pytanie_rect)

    pg.display.update()
