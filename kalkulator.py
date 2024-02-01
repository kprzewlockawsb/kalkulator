print('------KALKULATOR---------')
while True:
    print('Wybierz operacje')
    print('1.Dodawanie')
    print('2.Odejmowanie')
    print('3.Mnozenie')
    print('4.Dzielenie')
    print('5.Wyjscie')
    
    wybor = input('Wybierz operacje: (1/2/3/4/5): ')
    if wybor =='5':
        print('Wychodze z kalkulatora...')
        break
    num1=float(input('Podaj pierwsza liczbe: '))
    num2=float(input('Podaj druga liczbe: '))
    if wybor=='1':
        print('Wynik: ',num1+num2)
    elif wybor=='2':
        print('Wynik: ',num1-num2)
    elif wybor=='3':
        print('Wynik: ',num1*num2)
    elif wybor=='4':
        if num2 !=0:
            print('Wynik: ',num1/num2)
        else:
            print('Pamietaj cholero nie dziel przez 0')
    else:
        print('Nieprawidlowy wybor. Sprobuj ponownie')
