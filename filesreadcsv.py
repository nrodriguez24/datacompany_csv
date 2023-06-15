import os
datos=open('datos.csv','r')
_=datos.readline()
lista= datos.readlines()

while True:
    suma=0
    contador=0
    encon= False

    print("1--> PROMEDIO DE VENTAS POR AÑO \n2--> VENTAS DE UN TRIMESTRE EN UN AÑO \n3--> SUMA TOTAL HISTORICA DE LAS VENTAS \n4--> SALIR")
    val=int(input("OPCION --> "))

    if val==1:
        a=input("\nColoque el año: ")
        for linea in lista: 
            datos_separados = linea.split(";")

            if a == datos_separados[0]:
                encon= True

                for i in range(5):
                    suma+=int(datos_separados[i])
                    contador+=1

                promedio=(suma-int(datos_separados[0]))/(contador-1)
                print(f"+++ El promedio de ventas del año {a} es: {promedio}\n")
                break

        if not encon:
            print("+++ El año ingresado no se encuentra en los datos de la empresa. Comuniquese con el desarrollador, o sea, yo. Rápido. Por favor. Sino, me echan\n")
    
    elif val==2:
        a=input("\nColoque el año: ")

        for linea in lista:
            datos_separados = linea.split(";")

            if a == datos_separados[0]:
                encon=True
                trimestre=int(input("Coloque el trimestre: "))

                if trimestre>0 and trimestre<5:
                    print(f"+++ En el {trimestre} trimestre el valor de las ventas fueron: {datos_separados[trimestre]}\n")
                    break
                else: 
                    print("ERROR los trimestres se representan del 1 al 4\n")

        if not encon:
            print("+++ El año ingresado no se encuentra en los datos de la empresa. Comuniquese con el desarrollador, o sea, yo. Rápido. Por favor. Sino, me echan\n")
    
    elif val==3:
        for linea in lista:
            datos_separados=linea.split(";")

            for i in range(4):
                suma+=int(datos_separados[i+1])

        print(f"\nLa suma total de todas las ventas en todos los años es: {suma}\n")

    elif val==4:
        break

    else:
        print("--> POR FAVOR ELIGA UNA OPCION QUE SE ENCUENTRE EN EL MENÚ")
    
    c = input("Presione Enter para continuar...")
    c = os.system('cls' if os.name == 'nt' else 'clear')
    
datos.close()