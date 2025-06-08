# importacion de archivos y libreria
import Funciones.datos as data
import Funciones.alg_ordenamiento as alg_ordenamiento
import Funciones.alg_busqueda as alg_busqueda
import Funciones.med_tiempo as med_tiempo
import random

# menu principal
print("=== Comparacion de Algoritmos ===")
print("1. Comparar algoritmos de busqueda")
print("2. Comparar algoritmos de ordenamiento")
opcion = input("Elegi opcion 1 o 2: ")

### BUESQUEDA ###
if opcion == "1":
    # Probamos busqueda
    print("\nGenerando 20.000 valores enteros... Esto puede tardar un rato, o no!")
    datos = data.generar_datos()
    
    # Calculamos y mostramos minimo y maximo
    min_valor = min(datos)
    max_valor = max(datos)
    pos_min = datos.index(min_valor)
    pos_max = datos.index(max_valor)
    print(f"\nValor minimo generado: {min_valor} | Indice: {pos_min}")
    print(f"Valor maximo generado: {max_valor} | Indice: {pos_max}")
    
    # Selecciona objetivo aleatorio de la lista
    objetivo = random.choice(datos)
    print(f"\nNumero aleatorio de la lista generada: {objetivo}\n")
    
    # Medimos busqueda lineal
    resultado_lineal, tiempo_lineal = med_tiempo.medir_tiempo(alg_busqueda.busqueda_lineal, datos, objetivo)
    posicion_lineal, pasos_lineal = resultado_lineal
    print(f"Busqueda Lineal --> Indice: {posicion_lineal} | Pasos: {pasos_lineal} | Tiempo: {tiempo_lineal:.7f} segundos")
    
    # Ordenamos datos antes de la busqueda binaria. Partimos de un ideal para comparar
    datos_ordenados = sorted(datos)
    
    # Medimos busqueda binaria
    resultado_binaria, tiempo_binaria = med_tiempo.medir_tiempo(alg_busqueda.busqueda_binaria, datos_ordenados, objetivo)
    posicion_binaria, pasos_binaria = resultado_binaria
    print(f"Busqueda Binaria --> Indice: {posicion_binaria} | Pasos: {pasos_binaria} | Tiempo: {tiempo_binaria:.7f} segundos\n")

### ORDENAMIENTO ###
elif opcion == "2":
    # Probamos ordenamiento
    print("\nGenerando 20.000 valores enteros... Esto puede tardar un rato, o no!\n")
    datos = data.generar_datos()
    
    # Copiamos los datos para evitar reusar la misma lista
    datos_burbuja = datos[:]
    datos_merge = datos[:]
    datos_quicksort = datos[:]
 
# Prestar atencion al guion bajo...omite el primer argumento que no se necesita. Habria que revisar una lambda 
    # Medimos tiempo de burbuja
    _ , tiempo_burbuja = med_tiempo.medir_tiempo(alg_ordenamiento.burbuja, datos_burbuja)
    print(f"Burbuja --> Tiempo de ejecucion: {tiempo_burbuja:.7f} segundos")
    
    # Medimos tiempo de merge sort
    _ , tiempo_merge = med_tiempo.medir_tiempo(alg_ordenamiento.ordenamiento_por_combinacion, datos_merge)
    print(f"Merge Sort --> Tiempo de ejecucion: {tiempo_merge:.7f} segundos")

    # Medimos tiempo de quicksort
    _ , tiempo_quicksort = med_tiempo.medir_tiempo(alg_ordenamiento.quick_sort, datos_quicksort)
    print(f"Quicksort --> Tiempo de ejecucion: {tiempo_quicksort:.7f} segundos")
    
# excepcion en caso de ingresar opcion incorrecta
else:
    print("Revisa las opciones...era 1 o 2")