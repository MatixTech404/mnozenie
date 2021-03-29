import sys
import pygame as pg
import pygame.constants as c
import silnik as si

CZARNY = (15, 15, 15)
BIALY = (240, 240, 240)
K404 = (44, 207, 1)


class Gra:
    def __init__(self):
        self.font = pg.font.SysFont('', 100)
        self.gracz = pg.Rect(1, 1, 1, 1)
        pg.init()

        # zmienne i stałe
        self.PREDKOSC = 10
        self.SZEROKOSC, self.WYSOKOSC = 700, 600
        self.zegar = pg.time.Clock()

    def __del__(self):
        pg.quit()
        sys.exit()

    def sprawdz_eventy(self):
        for e in pg.event.get():
            if e.type == c.QUIT:
                return True

            if e.type == c.MOUSEMOTION:
                self.gracz.centerx = e.pos[0]
                self.gracz.centery = e.pos[1]
        return False

    def narysuj_obiekty(self, EKRAN):
        a, b = si.losuj()

        opcja1 = self.font.render(f'{a * a * b}', True, CZARNY, BIALY)
        opcja2 = self.font.render(f'{a * b}', True, CZARNY, BIALY)
        opcja3 = self.font.render(f'{a * b * b}', True, CZARNY, BIALY)

        rect1 = opcja1.get_rect(bottomleft=EKRAN.get_rect().bottomleft)
        rect2 = opcja2.get_rect(midbottom=EKRAN.get_rect().midbottom)
        rect3 = opcja3.get_rect(bottomright=EKRAN.get_rect().bottomright)

        opcje = [rect1, rect2, rect3]
        
        napis = self.font.render(f'{a} X {b} =', True, BIALY, CZARNY)
        rnapis = napis.get_rect(centerx=EKRAN.get_rect().centerx,
                                y=0)
        
        EKRAN.fill(CZARNY)
        EKRAN.blit(napis, rnapis)

        # narysuj gracza
        pg.draw.rect(EKRAN, K404, self.gracz)

        # sprawdź, czy nie zaszła kolizja
        for r in opcje:
            if self.gracz.colliderect(r):
                if r is rect1:
                    opcja = 0
                elif r is rect2:
                    opcja = 1
                else:
                    opcja = 2

        EKRAN.blit(opcja1, rect1)
        EKRAN.blit(opcja2, rect2)
        EKRAN.blit(opcja3, rect3)
        pygame.display.update()
