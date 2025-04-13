# 🤖 Implementación de Algoritmos Zero-R y One-R

Este proyecto implementa dos algoritmos básicos de minería de datos para la clasificación: Zero-R y One-R.

## 📝 Descripción

El código proporciona una implementación simplificada de los siguientes algoritmos:

* **Zero-R**: 📊 El clasificador más simple posible, que siempre predice la clase mayoritaria en los datos de entrenamiento. Sirve como línea base para comparar con otros algoritmos.

* **One-R**: 🔍 Un algoritmo que genera reglas de clasificación basadas en un solo atributo. Evalúa cada atributo y selecciona aquel que proporciona la mayor precisión de clasificación.

## ✨ Funcionalidades

- 📂 Carga de datos desde archivos de texto en formato tabla markdown
- 📈 Implementación del algoritmo Zero-R para predecir la clase mayoritaria
- 🧩 Implementación del algoritmo One-R para crear reglas basadas en un solo atributo
- 📏 Evaluación y comparación de ambos modelos
- 🔮 Predicción de nuevas instancias usando las reglas generadas

## 🛠️ Requisitos

- 🐍 Python 3.x
- 🐼 Pandas
- 📦 Collections (incluido en Python estándar)

## 🚀 Uso

1. Asegúrese de tener el dataset en formato tabla markdown
2. Ajuste la ruta del archivo en la función main()
3. Ejecute el script:

```bash
python taquitos.py
```

## 📋 Ejemplo de salida

```
Datos cargados desde [ruta]: 20 filas, 8 columnas

Zero-R: Clase mayoritaria = 'Sí', Precisión = 0.6500

One-R: Mejor atributo = 'Estudiante', Precisión = 1.0000
Reglas One-R: {'1': 'Sí', '2': 'Sí', '3': 'No', ...}

Comparación:
One-R supera a Zero-R por 0.3500

Prueba de predicción: 20 correctos de 20 (1.0000)
```

## 🏗️ Estructura del código

- `cargar_datos()`: 📄 Carga y procesa el archivo de datos
- `zero_r()`: 📊 Implementa el algoritmo Zero-R
- `one_r()`: 🔍 Implementa el algoritmo One-R
- `predecir_one_r()`: 🔮 Realiza predicciones usando las reglas de One-R
- `main()`: ⚙️ Función principal que ejecuta todo el proceso

## 🎓 Contexto académico

Este código fue desarrollado como parte de la actividad 5.2 "Implementación de algoritmos Zero-R y One-R" para la cátedra de minería de datos en la Universidad de Guadalajara, Centro Universitario de Ciencias Exactas e Ingenierías.
