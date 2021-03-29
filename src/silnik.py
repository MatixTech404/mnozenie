import random


def losuj():
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    return a, b


def sprodp(a: int, b: int, c: int) -> bool:
    return a * b == c


def main():
    a, b = losuj()
    p, n = 0, 0
    i = 0

    while i < 10:
        try:
            c = int(input(f'Ile to {a} * {b}? >>> '))
        except ValueError:
            print('Wyjątek ValueError obsłużony pomyślnie :-)')
            continue

        if c > 100:
            print('Wskazówka: można podać max. liczbę 100')
        elif sprodp(a, b, c) and i != 9:
            print('Dobrze! Spróbuj teraz z innymi liczbami')
            a, b = losuj()
            p += 1
            i += 1
        elif sprodp(a, b, c):
            print('Dobrze! To już koniec testu')
            p += 1
            i += 1
        elif i == 9:
            print(f'Prawie. Nistety nie masz więcej prób. Poprawna odpowiedź to {a * b}')
            n += 1
            i += 1
        else:
            print(f'Prawie. Spróbuj jeszcze raz')
            n += 1
            i += 1
        print(f'Popranych odpowiedzi: {p}, niepoprawnych: {n}')


if __name__ == '__main__':
    main()
