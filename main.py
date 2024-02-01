import books
import funkcje


while True:
    print("="*20)
    print(" i - informacja o bibliotece")
    print(" edy - edycja ksiozki")
    print(" f - znalezienie ksiazki")
    print(" e - exit i koniec")

    inp = input("Wybierz obcje: ")

    if inp == "i":
        funkcje.inf_biblioteka(books.biblioteka)
    elif inp == "edy":
        funkcje.edycja_ksiozek(books.biblioteka)
    elif inp == "f":
        funkcje.szukam(books.biblioteka)
        print(f"Twoja ksiozka to najlepsza o tytule: ")
        funkcje.inf_ksiozka(funkcje.i)
    elif inp == "e":
        break
    else:
        print(" Nie nie nie nie nie nie nie nie nie nie nie nie nie nie nie nie nie ma takiej komendy :( ")