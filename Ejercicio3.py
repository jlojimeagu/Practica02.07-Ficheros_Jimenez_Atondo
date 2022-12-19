def tabla_multiplicar(n,m):
    nombre_fichero = 'tabla-' + str(n) + '.txt'
    try:
        with open(nombre_fichero, 'r') as file:
            lineas = file.readlines()
            print(lineas[m - 1])
    except FileNotFoundError:
        print('No existe el fichero con la tabla del ', n)
    return


n = int(input('Introduce un número entero entre 1 y 10: '))
m = int(input('Introduce otro número entero entre 1 y 10: '))

print(tabla_multiplicar(n,m))