while True:


    cadena = input("introduce numeros")

    lista = list(cadena)
    
    
    N = len(lista)
    total = 0
    lista.reverse()

    des = True

    for i in range(N):
        if ":" > lista[i] > "/" or "," < lista[i] < ".":
            ""
        else:  
            des = False

    if des != False:


        for i in range(N):
                    if lista[i] == "1":
                        total = total + 1*pow(10, i)
                    elif lista[i] == "2":
                        total = total + 2*pow(10, i)
                    elif lista[i] == "3":
                        total = total + 3*pow(10, i)
                    elif lista[i] == "4":
                        total = total + 4*pow(10, i)
                    elif lista[i] == "5":
                        total = total + 5*pow(10, i)
                    elif lista[i] == "6":
                        total = total + 6*pow(10, i)
                    elif lista[i] == "7":
                        total = total + 7*pow(10, i)
                    elif lista[i] == "8":
                        total = total + 8*pow(10, i)
                    elif lista[i] == "9":
                        total = total + 9*pow(10, i)
                    elif lista[i] == "-":
                        total= total*-1
        print(total)
    else: print("malplan")