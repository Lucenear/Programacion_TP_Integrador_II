# Busqueda Lineal
def busqueda_lineal(lista, objetivo):
    pasos = 0
    for i in range(len(lista)):
        pasos += 1  # Incrementamos por cada comparacion
        if lista[i] == objetivo:
            return i, pasos  # Devuelve indice y pasos
    return -1, pasos  # Si no se encuentra

# Busqueda Binaria
def busqueda_binaria(lista_ordenada, objetivo):
    izquierda = 0
    derecha = len(lista_ordenada) - 1
    pasos = 0
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        pasos += 1  # Incrementamos por cada iteracion
        if lista_ordenada[medio] == objetivo:
            return medio, pasos  # Devuelve indice y pasos
        elif lista_ordenada[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1, pasos  # Si no se encuentra