import books

def inf_ksiozka(dc: dict) -> None:
    for k, v in dc.items():
        print(f"{k}:  {v}")


def inf_biblioteka(lst: list) -> None:
    for dic in lst:
        inf_ksiozka(dic)
        print("="*20)


def szukam(lis: list) -> dict:
    inf_biblioteka(lis)
    while True:
        pozdrawiam = []
        inp = input("e - exit | Wprowadz tytol, lub rodzaj")

        if inp == "e":
            break
        else:
            for el in lis:
                for k, v  in el.items():
                    if v.lower() == inp.lowwer():
                        pozdrawiam.append(el)
            if len(pozdrawiam) == 1:
                return pozdrawiam[0]
            elif len(pozdrawiam) > 1:
                inf_biblioteka(pozdrawiam)
                print("Nope")
            else:
                print("Brak takiej komendy")


# --------------------------------------------------


def edycja_ksiozek(lis: list) -> None:
    while True:
        print("Jaką książke chcesz zedytowac:   ")
        ksiazka = szukam(lis)
        if ksiazka is None:
            break
        else:
            for x in range(len(lis)):
                if ksiazka == lis[x]:
                    break
            inf_ksiozka(ksiazka)
            i = "id"
            while i == "id":
                i = input("Co edytujesz:  ").lower()
                if i == "id":
                    print('Id nie do edycji npc')
            
            for k, v in ksiazka.items():
                if k.lower() == i:
                    y = input("Nowe dane: ")
                    ksiazka[k] = y
                    break
            lis[x] = ksiazka


# ----------------------------------------------




                
