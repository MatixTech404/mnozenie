import random
import sys

import pygame as pg
from pygame.constants import *


def czy_btn_wcisniety(le, lbtns):
    x = le.pos[0]
    y = le.pos[1]

    indeks = 0
    for i in lbtns:
        if i.top <= y <= i.bottom:
            if i.left <= x <= i.right:
                break
        indeks += 1

    if indeks == len(btns):
        return -1
    return indeks


def losuj_odp(pop_odp):
    r = random.randint(0, 2)
    if r == 0:
        lt_a = f'{pop_odp}'
        lt_b = f'{random.randint(1, 100)}'
        lt_c = f'{random.randint(1, 100)}'
        li_c = 0
    elif r == 1:
        lt_a = f'{random.randint(1, 100)}'
        lt_b = f'{pop_odp}'
        lt_c = f'{random.randint(1, 100)}'
        li_c = 1
    else:
        lt_a = f'{random.randint(1, 100)}'
        lt_b = f'{random.randint(1, 100)}'
        lt_c = f'{pop_odp}'
        li_c = 2

    if lt_a == lt_b or lt_a == lt_c or lt_b == lt_c:
        lt_a, lt_b, lt_c, _ = losuj_odp(pop_odp)
    return lt_a, lt_b, lt_c, li_c


pg.init()

SZEROKOSC, WYSOKOSC = 800, 600
EKRAN = pg.display.set_mode((SZEROKOSC, WYSOKOSC), 0, 32)

btns = []

# czcionki
normal = pg.font.SysFont('', 120)

# kolory
CZARNY    = (15, 15, 15)
K404      = (44, 207, 1)
BIALY     = (200, 200, 200)
KPYT      = (70, 220, 30)
KODP      = (40, 40, 40)
Kbtn = (127, 127, 0)


a = random.randint(1, 10)
b = random.randint(1, 10)


pole_pytania = pg.Rect(0, 0, 800, 300)

pytanie = normal.render(f'Ile to {a} razy {b}?', True, BIALY)
pytanie_rect = pytanie.get_rect(center=(400, WYSOKOSC / 3))


btn_a = pg.Rect(50, 350, 167, 200)
btn_b = pg.Rect(317, 350, 167, 200)
btn_c = pg.Rect(583, 350, 167, 200)
btns_odp = [btn_a, btn_b, btn_c]

btns[len(btns):(len(btns)+2)] = btns_odp


t_a, t_b, t_c, i_c = losuj_odp(a * b)


tekst_a = normal.render(t_a, True, BIALY)
tekst_b = normal.render(t_b, True, BIALY)
tekst_c = normal.render(t_c, True, BIALY)

rect_tekst_a = tekst_a.get_rect(center=(133, 450))
rect_tekst_b = tekst_b.get_rect(center=(400, 450))
rect_tekst_c = tekst_c.get_rect(center=(666, 450))

while True:
    for e in pg.event.get():  # obsługa zdarzeń
        if e.type == QUIT:
            pg.quit()
            sys.exit()

        if e.type == MOUSEBUTTONDOWN and e.button == BUTTON_LEFT:
            btn = czy_btn_wcisniety(e, btns)
            if btn != -1:
                btn_odp = czy_btn_wcisniety(e, btns_odp)
                if i_c == btn_odp:
                    print("dobrze")
                else:
                    print("źle")

    EKRAN.fill(KODP)

    pg.draw.rect(EKRAN, KPYT, pole_pytania)

    pg.draw.rect(EKRAN, Kbtn, btn_a)
    pg.draw.rect(EKRAN, Kbtn, btn_b)
    pg.draw.rect(EKRAN, Kbtn, btn_c)

    EKRAN.blit(tekst_a, rect_tekst_a)
    EKRAN.blit(tekst_b, rect_tekst_b)
    EKRAN.blit(tekst_c, rect_tekst_c)

    EKRAN.blit(pytanie, pytanie_rect)

    pg.draw.line(EKRAN, (255, 255, 255), (267, 0), (267, 600))
    pg.draw.line(EKRAN, (255, 255, 255), (533, 0), (533, 600))

    pg.display.update()
