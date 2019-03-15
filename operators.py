def main():
    x = 3
    y = 7

    suma = x + y
    print("Wynik dodawania: " + str(suma))

    roznica = x - y
    print("Wynik odejmowania: " + str(roznica))

    z = 5
    z = z + 5
    print(z)
    z += 5
    print(z)

    #print(str(x) + "<" + str(y) + " == " + str(x<y))
    #print(str(x) + ">" + str(y) + " == " + str(x > y))

    print(x<y)

    #age = 15
    #working_age = 18 <= age <= 65
    #print(working_age)
    print("Give me your age")
    age = int(input())
    if age >= 21:
        print("You can drink alcohol and have a gun")
    elif age >= 18:
        print("You can drink alcohol")
    else:
        print("You can\'t drink alcohol and can\'t have a gun")


if __name__ == "__main__":
    main()