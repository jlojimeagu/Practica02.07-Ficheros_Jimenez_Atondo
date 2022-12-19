import urllib.request


def conteo(url):
    """
    :param url: ingresar la url a contar.
    :return: retorna el conteo de palabras del url.
    """
    file = urllib.request.urlopen(url)
    leer = file.read()
    return len(leer.split())

urr = input('escribe la url que quieras\n')
print(conteo(urr))
