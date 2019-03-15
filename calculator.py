def main():
    koniec = False
    while not koniec:
        print("Podaj w oddzielnych wierszach liczbę,operację matematyczną: +, -, *, /, %,a następnie kolejną liczbę:")
        liczba1 = float(input())
        operacja = input()
        liczba2 = float(input())
        if operacja == "+":
            wynik = liczba1 + liczba2
        elif operacja == "-":
            wynik = liczba1 - liczba2
        else:
            print("Niepoprawna operacja")
            break
        print("Twój wynik to: " + str(wynik))
        print("Chcesz wykonać kolejne działanie? Wpisz tak lub nie")
        kolejne = input()
        if kolejne == "nie":
            koniec = True
        elif kolejne != "tak":
            print("Niepoprawny wybór")
            break


if __name__ == "__main__":
    main()