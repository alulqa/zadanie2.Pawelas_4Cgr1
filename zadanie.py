import json

class Produkt:
    def __init__(self, nazwa, cena, kategoria, ilosc):
        self.nazwa = nazwa
        self.cena = float(cena)
        self.kategoria = kategoria
        self.ilosc = int(ilosc)

magazyn = [
    Produkt("mleko", 4.50, "spozywczy", 5),
    Produkt("sól", 2.50, "przyprawa", 0)
]

dane_do_zapisu = [{"nazwa": p.nazwa, "cena": p.cena, "kategoria": p.kategoria, "ilosc": p.ilosc} for p in magazyn]
with open("magazyn.json", "w", encoding="utf-8") as plik:
    json.dump(dane_do_zapisu, plik, ensure_ascii=False, indent=4)

print("zapisano do pliku")

while True:
    print("--- MENU ---")
    print("1 - Wszystkie produkty")
    print("2 - Dostępne produkty")
    print("3 - Wyszukaj produkt")
    print("4 - Produkty do podanej ceny")
    print("5 - Kup produkt")
    print("0 - Zakończ program")
    
    opcja = input("Wybierz opcję: ")

    if opcja == "1":
        print("--- WSZYSTKIE PRODUKTY ---")
        for p in magazyn:
            print(f"Nazwa: {p.nazwa}, Kategoria: {p.kategoria}, Cena: {p.cena} zł, Sztuk: {p.ilosc}")
        print()

    elif opcja == "2":
        print("--- DOSTĘPNE PRODUKTY ---")
        for p in magazyn:
            if p.ilosc == 0:
             continue
        print(f"Nazwa: {p.nazwa}, Kategoria: {p.kategoria}, Cena: {p.cena} zł, Sztuk: {p.ilosc}")
  

    elif opcja == "3":
        szukana = input("Podaj nazwę produktu: ").lower()
        czyznaleziono = False
        for p in magazyn:
            if p.nazwa.lower() == szukana:
                print(f"Znaleziono: {p.nazwa}, Kategoria: {p.kategoria}, cena: {p.cena} zł, Sztuk: {p.ilosc}")
                czyznaleziono = True
                break
        if not czyznaleziono:
            print("Nie znaleziono produktu.")
        print()

    elif opcja == "4":
        try:
            max_cena = float(input("Podaj maksymalną cenę: "))
            print(f"--- PRODUKTY DO {max_cena}---")
            for p in magazyn:
                if p.cena <= max_cena:
                    print(f"Nazwa: {p.nazwa}, Kategoria: {p.kategoria}, Cena: {p.cena} zł, Sztuk: {p.ilosc}")
        except ValueError:
            print("Podano nieprawidłową cenę")
        print()

    elif opcja == "5":
        podana_nazwa = input("Podaj produkt: ").lower()
        czyznaleziono = False
        for p in magazyn:
            if p.nazwa.lower() == podana_nazwa:
                czyznaleziono = True
                if p.ilosc == 0:
                    print("Produkt niedostępny")
                else:
                    p.ilosc -= 1
                    print(f"Kupiono {p.nazwa}")
                    print(f"Pozostało sztuk: {p.ilosc}")
                break
        if not czyznaleziono:
            print("Nie znaleziono produktu")
        print()

    elif opcja == "0":
        print("Zakonczono program")
        break

    else:
        print("Wybierz cyfrę od 0 do 5")