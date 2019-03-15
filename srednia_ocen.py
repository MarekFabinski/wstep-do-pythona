def main():

    print("Podaj liczbę ocen, które będą "
          "wchodzić w skład średniej")
    liczba_ocen = int(input())
    suma = 0
    for i in range(1, liczba_ocen+1):
        print("Podaj ocenę " + str(i))
        ocena = float(input())
        if ocena < 0:
            liczba_ocen = i - 1
            break
        suma += ocena
    print("Suma ocen to: " + str(suma))
    print("Średnia ocen to: " + str(suma/liczba_ocen))

    """
    print("Podaj liczbę ocen, które będą wchodzić w skład średniej")
    liczba_ocen = int(input())
    suma = 0
    i = 1
    while i <= liczba_ocen:
        print("Podaj ocenę " + str(i))
        ocena = float(input())
        if ocena < 0:
            continue
        suma += ocena
        i += 1
    print("Suma ocen to: " + str(suma))
    print("Średnia ocen to: " + str(suma / liczba_ocen))
    """

if __name__ == "__main__":
    main()