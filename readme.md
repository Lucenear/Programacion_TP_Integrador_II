# 🧩 Trabajo Práctico Integrador - Programación I

Trabajo práctico integrador de Programación I, correspondiente a la **Tecnicatura Universitaria en Programación a Distancia**, dictada por la **UTN**.

---

## 👥 Alumnos

- **Farias, Gustavo**  
  📧 fariasg1988@gmail.com  
- **Frias, Walter**  
  📧 agustin.front242@gmail.com  

## 👨‍🏫 Profesor
- **Enferrel, Ariel**

## 🧑‍🏫 Tutor
- **Gonzalez, Franco**

## 🎥 Enlace al video explicativo
https://drive.google.com/drive/folders/10BBdYFF5BF6XfWMis4ssfav6oG2bZYUa?usp=sharing

---

## 💡 Descripción del programa

Este trabajo se enfoca en el **análisis comparativo de algoritmos de búsqueda y ordenamiento en Python**. Hemos implementado un programa de consola que compara:

1. **Búsqueda Lineal** vs **Búsqueda Binaria**  
2. **Ordenamiento Burbuja** vs **Quicksort** vs **Merge Sort**

El objetivo principal es demostrar cómo la elección del algoritmo afecta el rendimiento en listas de 20.000 números enteros, midiendo tiempo, pasos realizados y posiciones encontradas.  
El programa incluye un **menú interactivo** para elegir entre pruebas de búsqueda o de ordenamiento.

---

## 🔍 Características principales

### 🔎 Comparación de algoritmos

- **Búsqueda Lineal**: Ideal para listas no ordenadas.  
- **Búsqueda Binaria**: Más eficiente, requiere que la lista esté ordenada.  
- **Ordenamiento Burbuja**: Simple pero lento.  
- **Quicksort y Merge Sort**: Algoritmos recursivos, eficientes para grandes volúmenes.

### ⏱️ Medición de rendimiento

- Tiempo de ejecución (en segundos).  
- Número de pasos realizados por cada algoritmo.

### 🔢 Generación de datos aleatorios

- Listas de 20.000 enteros entre 1 y 200.000.

### 🧭 Menú interactivo

- Permite elegir entre pruebas de búsqueda u ordenamiento.  
- Muestra valores mínimo y máximo generados.  
- Indica la posición del objetivo encontrado.

---

## 🧠 Reflexión del equipo

### ✅ La importancia de elegir buenos algoritmos

- **Búsqueda binaria** fue hasta **30x más rápida** que la lineal, siempre que los datos estén ordenados.  
- **Burbuja** es ineficiente (O(n²)), mientras que **Merge Sort** y **Quicksort** (O(n log n)) demostraron gran eficiencia.

### ✅ Medición de tiempo

- Usamos `time.time()` para capturar tiempos sin necesidad de decoradores.  
- Aprendimos a manejar resultados recursivos (como en Merge Sort).

### ✅ Validación y prueba

- Aseguramos que el número objetivo esté en la lista (`random.choice(datos)`).  
- Implementamos contadores de pasos para evaluar eficiencia.  
- Validamos la necesidad de ordenar datos antes de usar búsqueda binaria.

### ✅ Organización del código

- Separación de responsabilidades en archivos independientes.  
- Evitamos imprimir en módulos auxiliares; toda la salida va por `main.py`.

### ✅ Recursividad

- Quicksort y Merge Sort nos enseñaron cómo dividir problemas y fusionar soluciones.  
- Aprendimos a implementar estrategias como el uso de pivotes y combinación de sublistas.

---

## 📊 Resultados destacados

### 🔍 Búsqueda Binaria

- **Tiempo promedio**: `0.000004 s`  
- **Pasos**: ~17 iteraciones (logarítmico)

### 🔍 Búsqueda Lineal

- **Tiempo promedio**: `0.000123 s`  
- **Pasos**: ~50,000 iteraciones (lineales)

### 📈 Ordenamiento

- **Burbuja**: `0.876543 s` (ineficiente)  
- **Quicksort/Merge Sort**: `0.009876 s` (óptimos para grandes volúmenes)

---

## 📁 Estructura del Proyecto
```
TP_INTEGRADOR_II
├── Funciones/
│ ├── alg_busqueda.py # Implementación de búsqueda lineal y binaria
│ ├── alg_ordenamiento.py # Algoritmos de ordenamiento (burbuja, quicksort, merge sort)
│ ├── datos.py # Generación de datos aleatorios (20.000 enteros)
│ ├── med_tiempo.py # Medición de rendimiento
├── main.py # Menú, impresión de resultados y lógica principal
├── readme.md # Documento explicativo del proyecto
```

---

## 📚 Recursos utilizados

- 📘 [Libro: Introducción a la Programación (UV)](https://www.uv.mx/personal/pmartinez/files/2021/03/Libro-completo-Introduccion-a-la-programacion.pdf)  
- 🎓 [Khan Academy: Algoritmos](https://es.khanacademy.org/computing/computer-science/algorithms)

---

## 🧪 ¿Cómo ejecutar el proyecto?
1) Clonar el repositorio:
```
git clone https://github.com/Lucenear/Programacion_TP_Integrador_II.git
```
2) Ejecutar el programa:
```
python main.py  
```

---