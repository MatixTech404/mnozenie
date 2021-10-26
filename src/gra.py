import sys
import pygame as pg
import pygame.constants as c
import silnik as si

# czcionka
normal = pg.font.SysFont('', 120)

# kolory
CZARNY    = (15, 15, 15)
K404      = (44, 207, 1)
BIALY     = (200, 200, 200)
KPYT      = (70, 220, 30)
KODP      = (40, 40, 40)
KPRZYCISK = (127, 127, 0)


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

    def utworz_obiekty(self):
        global pole_pytania, pytanie, pytanie_rect, \
               przycisk_a, przycisk_b, przycisk_c, \
               tekst_a, tekst_b, tekst_c, \
               rect_tekst_a, rect_tekst_b, rect_tekst_c, \
               a, b

        a, b = si.losuj()

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

    def narysuj_obiekty(self, EKRAN):
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
