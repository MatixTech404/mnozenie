import random
import sys

import pygame as pg
from pygame.constants import *


# kolory
BIALY     = (200, 200, 200)
KPYT      = (70, 220, 30)
KODP      = (40, 40, 40)
KPRZYCISK = (127, 127, 0)


pg.init()

SZEROKOSC, WYSOKOSC = 800, 600
EKRAN = pg.display.set_mode((SZEROKOSC, WYSOKOSC), 0, 32)


# czcionki
normal = pg.font.SysFont('', 120)


a = random.randint(1, 10)
b = random.randint(1, 10)

while True:
    for e in pg.event.get():  # obsługa zdarzeń
        if e.type == QUIT:
            pg.quit()
            sys.exit()
    
    EKRAN.fill(KODP)
    pole_pytania = pg.Rect(0, 0, 800, 300)

    pytanie = normal.render(f'Ile to {a} razy {b}?', True, BIALY)
    pytanie_rect = pytanie.get_rect(center=(400, 150))

    przycisk_a = pg.Rect(50, 350, 167, 200)
    przycisk_b = pg.Rect(317, 350, 167, 200)
    przycisk_c = pg.Rect(583, 350, 167, 200)

    tekst_a = normal.render(f'{a * a * b}', True, BIALY)
    tekst_b = normal.render(f'{a * b}', True, BIALY)
    tekst_c = normal.render(f'{a * b * b}', True, BIALY)

    rect_tekst_a = tekst_a.get_rect(center=(133, 450))
    rect_tekst_b = tekst_b.get_rect(center=(400, 450))
    rect_tekst_c = tekst_c.get_rect(center=(666, 450))

    pg.draw.rect(EKRAN, KPYT, pole_pytania)

    pg.draw.rect(EKRAN, KPRZYCISK, przycisk_a)
    pg.draw.rect(EKRAN, KPRZYCISK, przycisk_b)
    pg.draw.rect(EKRAN, KPRZYCISK, przycisk_c)

    EKRAN.blit(tekst_a, rect_tekst_a)
    EKRAN.blit(tekst_b, rect_tekst_b)
    EKRAN.blit(tekst_c, rect_tekst_c)

    EKRAN.blit(pytanie, pytanie_rect)

    pg.draw.line(EKRAN, (255, 255, 255), (267, 0), (267, 600))
    pg.draw.line(EKRAN, (255, 255, 255), (533, 0), (533, 600))

    pg.display.update()
