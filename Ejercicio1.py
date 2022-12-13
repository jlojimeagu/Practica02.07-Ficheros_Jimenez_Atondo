def tabla_multiplicar(num):
    nombre_fichero = 'tabla-' + str(num) + '.txt'
    file = open(nombre_fichero, 'w')
    for numero in range(1, 11):
        file.write(str(num) + ' x ' + str(numero) + ' = ' + str(num * numero) + '\n')
    file.close()
    
num = int(input("Introduce un numero del 1 a 10\n"))
tabla_multiplicar(num)