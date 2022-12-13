def tabla_multiplicar(num):
    """ Funcion que calcula la tabla de multiplicar de un numero
               Parametros:
                   - nombre_fichero: fichero que se crea al calcular la tabla
                     del numero introducido
                   - num: numero que introduce el usuario
               Salidas:
                   - la tabla de multiplicar del numero creada por la funcion
    """
    nombre_fichero = 'tabla-' + str(num) + '.txt'
    file = open(nombre_fichero, 'w')
    for numero in range(1, 11):
        file.write(str(num) + ' x ' + str(numero) + ' = ' + str(num * numero) + '\n')
    file.close()

num = int(input("Introduce un numero del 1 a 10\n"))
tabla_multiplicar(num)
help(tabla_multiplicar(num))
