Trabajo Práctico Integrador - Programación I
Trabajo práctico integrador de Programación I , correspondiente a la Tecnicatura Universitaria en Programación a distancia dictada por la UTN.

👥 Alumnos
Farias, Gustavo
📧 fariasg1988@gmail.com
Frias, Walter
📧 agustin.front242@gmail.com
👨‍🏫 Profesor
Ariel Enferrel

🧑‍🏫 Tutor
Franco Gonzalez

🎥 Enlace al video explicativo
Ver video del proyecto

💡 Descripción del programa
Este trabajo se enfoca en el análisis comparativo de algoritmos de búsqueda y ordenamiento en Python.

Hemos implementado un programa de consola que compara:
Búsqueda Lineal vs Búsqueda Binaria
Ordenamiento Burbuja vs Quicksort vs Merge Sort
Objetivo principal:
Validar cómo la elección de un algoritmo afecta el rendimiento en listas de 20.000 números enteros , con medición de tiempo, pasos realizados y posiciones encontradas.

Características principales:
Comparación de algoritmos:
Búsqueda Lineal: Ideal para listas no ordenadas.
Búsqueda Binaria: Requiere lista ordenada, pero es más eficiente en grandes datasets.
Ordenamiento Burbuja: Lento pero simple de entender.
Quicksort y Merge Sort: Algoritmos recursivos con alta escalabilidad.
Medición de rendimiento:
Tiempo de ejecución (en segundos).
Número de pasos realizados por cada algoritmo.
Generación de datos aleatorios:
Listas de 20.000 enteros entre 1 y 200.000.
Menú interactivo:
Permite elegir entre pruebas de búsqueda o ordenamiento.
Muestra valores mínimo/máximo generados y posición del objetivo.
🧠 Reflexión del equipo
Este trabajo nos permitió aprender varias lecciones clave:

✅ La importancia de elegir buenos algoritmos:

La búsqueda binaria fue hasta 30x más rápida que la lineal en listas grandes, siempre que los datos estén ordenados.
Burbuja es ineficiente para listas extensas (O(n²) ), mientras que Merge Sort y Quicksort (O(n log n) ) destacaron en su eficiencia.
✅ Cómo medir el tiempo de ejecución de funciones:

Usamos time.time() para capturar tiempos de ejecución sin depender de decoradores complejos.
Aprendimos a manejar resultados de funciones recursivas (como Merge Sort) para extraer tiempo y posición del objetivo.
✅ Validación y prueba de código:

Garantizamos que el objetivo siempre esté en la lista con random.choice(datos).
Validamos la necesidad de ordenar datos previo a la búsqueda binaria.
Implementamos contadores de pasos para entender cómo cada algoritmo llega al resultado.
✅ División de responsabilidades en el código:

Separamos funcionalidades en archivos independientes (datos.py, alg_busqueda.py, alg_ordenamiento.py, med_tiempo.py, main.py) para mejorar mantenibilidad.
Evitamos imprimir resultados en módulos auxiliares, centralizando toda la salida en main.py.
✅ Entendiendo la recursividad:

Merge Sort y Quicksort nos ayudaron a comprender cómo dividir problemas complejos en subproblemas manejables.
Aprendimos a fusionar sublistas ordenadas y particionar datos con pivotes.
📊 Resultados destacados
Búsqueda:
Búsqueda Binaria:
Tiempo promedio: 0.000004 segundos (vs. 0.000123 segundos de la lineal).
Pasos: ~17 iteraciones (logarítmicos) vs. ~50,000 pasos (lineales).
Ordenamiento:
ALGORITMO
TIEMPO DE EJECUCIÓN (20,000 ELEMENTOS)
Burbuja
0.876543 segundos
Quicksort
0.009876 segundos
Merge Sort
0.008765 segundos

📁 Estructura del Proyecto


1
2
3
4
5
6
7
TP_INTEGRADOR_II/
├── datos.py                 # Generación de datos aleatorios (20,000 enteros)
├── alg_busqueda.py          # Implementación de búsqueda lineal y binaria
├── alg_ordenamiento.py      # Algoritmos de ordenamiento (burbuja, quicksort, merge sort)
├── med_tiempo.py            # Medición de rendimiento sin impresiones internas
├── main.py                  # Menú, impresión de resultados y lógica de interacción
├── readme.md                # Documento explicativo del proyecto
📚 Recursos utilizados
Libro: Introducción a la programación
Khan Academy: Algoritmos de búsqueda y ordenamiento
📝 Notas adicionales
Simplificación para estudiantes:
Variables descriptivas y comentarios paso a paso para facilitar la comprensión.
Evitamos decoradores complejos y usamos lambda solo cuando fue necesario.
Escalabilidad:
Aunque este trabajo se enfoca en búsqueda y ordenamiento básico, la estructura modular permite agregar nuevos algoritmos fácilmente.
Optimización futura:
Podríamos integrar gráficos con matplotlib o medición de uso de memoria con sys.getsizeof().