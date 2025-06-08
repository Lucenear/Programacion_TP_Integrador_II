import time

# Marcamos el segundo argumento como opcional para ordenamiento pero en alg_busqueda lo completamos
def medir_tiempo(funcion, argumento1, argumento2=None):
    inicio = time.time()
    if argumento2 is None:
        resultado = funcion(argumento1)  # Para funciones con 1 argumento (ordenamiento)
    else:
        resultado = funcion(argumento1, argumento2)  # Para funciones de 2 argumentos (busqueda)
    fin = time.time() # guardamos el tiempo final
    tiempo_ejecucion = fin - inicio # hacemos calculo de tiempo de ejecucion
    return resultado, tiempo_ejecucion