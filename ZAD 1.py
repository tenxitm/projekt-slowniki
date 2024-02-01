k = {
    "tytul": "Jak pokochać informatykę ;)",
    "liczba_stron": 1000,
    "Autor": "Patryk"
}

def wyswietlenie_danych():          
    for p, w in k.items():
        print(f'{p} : {w}')
        print("=" * 20)

def edycja():
    while True:
        print("EDYCJA, co chcesz edytować:")
        print(" t - tytuł")
        print(" l - liczba stron")
        print(" a - autor")
        print(" e - exit")
        inp = input("Wybierz opcję: ")

        if inp == "t":
            nowy_tytul = input("Nowy tytuł: ")
            k["tytul"] = nowy_tytul
        elif inp == "l":
            nowa_liczba_stron = input("Nowa liczba stron: ")
            k["liczba_stron"] = int(nowa_liczba_stron)
        elif inp == "a":
            nowy_autor = input("Nowy autor: ")
            k["Autor"] = nowy_autor
        elif inp == "e":
            break
        else:
            print("Nie ma takiej komendy!")


wyswietlenie_danych()

edycja()

wyswietlenie_danych()
