# burbuja
def burbuja(lista):
    # numero total de elementos
    n = len(lista)
    
    # Recorre la lista n veces
    for pasada in range(n):
        # comparar pares de elementos adyacentes
        for indice in range(0, n - pasada - 1):
            # Si el actual es mayor que el siguiente se intercambian
            if lista[indice] > lista[indice + 1]:
                # variable temporal para intercambiar y no perder el valor
                temp = lista[indice]
                lista[indice] = lista[indice + 1]
                lista[indice + 1] = temp
    return lista

# Merge Sort
def ordenamiento_por_combinacion(lista):
    # caso base: listas vacias o con 1 elemento ya estan ordenadas
    if len(lista) <= 1:
        return lista
    
    # dividimos la lista en dos mitades
    mitad = len(lista) // 2
    mitad_izquierda = ordenamiento_por_combinacion(lista[:mitad])  # se ordena la mitad izquierda
    mitad_derecha = ordenamiento_por_combinacion(lista[mitad:])    # se ordena la mitad derecha
    
    # combinamos las mitades ordenadas
    return combinar_listas_ordenadas(mitad_izquierda, mitad_derecha)

# funcion para combinar las dos listas ordenadas
def combinar_listas_ordenadas(lista_izquierda, lista_derecha):
    resultado = []  # lista para almacenar el resultado final
    indice_izquierda = indice_derecha = 0  # contadores en 0 para recorrer las listas
    
    # recorrer ambas listas hasta que una se agote
    while indice_izquierda < len(lista_izquierda) and indice_derecha < len(lista_derecha):
        if lista_izquierda[indice_izquierda] < lista_derecha[indice_derecha]:
            resultado.append(lista_izquierda[indice_izquierda])
            indice_izquierda += 1
        else:
            resultado.append(lista_derecha[indice_derecha])
            indice_derecha += 1
    
    # Agregamos los elementos restantes de la lista izquierda (si hay)
    while indice_izquierda < len(lista_izquierda):
        resultado.append(lista_izquierda[indice_izquierda])
        indice_izquierda += 1
    
    # agregamos los elementos restantes de la lista derecha (si hay)
    while indice_derecha < len(lista_derecha):
        resultado.append(lista_derecha[indice_derecha])
        indice_derecha += 1
    
    return resultado

# Quicksort
def quick_sort(lista):
    # caso base: listas vacias o con 1 elemento ya estan ordenadas
    if len(lista) <= 1:
        return lista
    
    # elige el primer elemento como pivote
    pivote = lista[0]
    
    # separamos elementos en menores y mayores que el pivote
    menores = []
    mayores = []
    
    # recorremos los elementos restantes (desde el indice 1) y vamos agregando a la sublista correspondiente
    for x in lista[1:]:
        if x <= pivote:
            menores.append(x)  # Agrega a menores
        else:
            mayores.append(x)  # Agrega a mayores
    
    # llamada recursiva para ordenar las sublistas
    return quick_sort(menores) + [pivote] + quick_sort(mayores)

