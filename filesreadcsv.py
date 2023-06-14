lista = []
datos=open('datos.csv','r')
_=datos.readline()
for linea in datos.readlines():
    datos_separados = linea.split(";")
    print(datos_separados)
datos.close()