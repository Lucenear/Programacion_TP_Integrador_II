import random

def generar_datos():
# Generamos lista de 20.000 numeros enteros entre 1 y 200.000
    return [random.randint(1, 200000) for n in range(20000)]