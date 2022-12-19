import os
def excistencia(num):
    """

    :param num: el numero de la tabla del .txt
    :return: retorna 2 opciones si existe lo lee y si no existe indica que no existe.
    """
    manueh = "tabla-"+str(num)+'.txt'
    if os.path.isfile(manueh):
        file = open(manueh, 'r')
        print(file.read())
    else:
        print('este archivo no existe')
    return

nume = (input('escribe\n'))

print(excistencia(nume))
