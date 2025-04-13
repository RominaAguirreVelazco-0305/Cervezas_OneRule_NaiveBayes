#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Implementación simplificada de algoritmos Zero-R y One-R
"""
#Usamos la biblioteca de pandas porque esta nos permite hacer un mejor manejo de los datos 
import pandas as pd
from collections import Counter

def cargar_datos(ruta_archivo):
    """Carga datos desde un archivo de texto en formato tabla markdown"""
    # Abrimos el archivo y leemos su contenido
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Dividimos el contenido en líneas
    lineas = contenido.strip().split('\n')
    # Extraemos las cabeceras de la primera línea
    cabeceras = [h.strip() for h in lineas[0].split('|') if h.strip()]
    # Ignoramos la línea de separación (segunda línea) y tomamos las líneas de datos
    lineas_datos = lineas[2:]  
    
    # Procesamos cada línea de datos
    datos = []
    for linea in lineas_datos:
        # Dividimos la línea por el separador '|' y limpiamos los valores
        valores = [val.strip() for val in linea.split('|') if val.strip()]
        if valores:  # Si hay valores, los añadimos a nuestra lista
            datos.append(valores)
    
    # Creamos un DataFrame con los datos extraídos
    df = pd.DataFrame(datos, columns=cabeceras)
    
    # Convertimos las columnas numéricas a tipo int
    for col in df.columns:
        # Verificamos si todos los valores de la columna son números enteros
        if df[col].str.match(r'^\d+$').all():
            df[col] = df[col].astype(int)
    
    return df

def zero_r(X, y):
    """
    Implementa el algoritmo Zero-R (clase mayoritaria)
    
    Este es el clasificador más simple posible, que siempre predice
    la clase más frecuente en los datos de entrenamiento.
    """
    # Contamos la frecuencia de cada clase en los datos
    contador = Counter(y)
    # Obtenemos la clase que aparece con mayor frecuencia
    clase_mayoritaria = contador.most_common(1)[0][0]
    
    # Calculamos la precisión en los datos de entrenamiento
    correctos = sum(1 for etiqueta in y if etiqueta == clase_mayoritaria)
    precision = correctos / len(y) if len(y) > 0 else 0
    
    return clase_mayoritaria, precision

def one_r(X, y):
    """
    Implementa el algoritmo One-R (mejor atributo simple)
    
    Este algoritmo selecciona el atributo que proporciona la mayor precisión
    de clasificación utilizando reglas simples (un nivel de decisión).
    """
    mejor_atributo = None
    mejor_precision = 0
    mejores_reglas = {}
    
    # Evaluamos cada atributo en el conjunto de datos
    for atributo in X.columns:
        reglas = {}
        errores = 0
        
        # Para cada valor único del atributo actual
        for valor in X[atributo].unique():
            # Identificamos las filas donde el atributo tiene este valor
            indices = X[atributo] == valor
            # Extraemos las clases correspondientes a estas filas
            clases_valor = y[indices]
            
            if len(clases_valor) > 0:
                # Encontramos la clase mayoritaria para este valor del atributo
                contador = Counter(clases_valor)
                clase_mayoritaria = contador.most_common(1)[0][0]
                # Creamos una regla: si atributo = valor entonces clase = clase_mayoritaria
                reglas[valor] = clase_mayoritaria
                
                # Contamos los errores que comete esta regla
                # (casos donde la clase real no coincide con la clase predicha)
                errores += sum(1 for i, etiqueta in enumerate(y) 
                              if indices.iloc[i] and etiqueta != clase_mayoritaria)
        
        # Calculamos la precisión para este atributo
        precision = 1 - (errores / len(y)) if len(y) > 0 else 0
        
        # Actualizamos el mejor atributo si encontramos uno mejor
        if precision > mejor_precision:
            mejor_atributo = atributo
            mejor_precision = precision
            mejores_reglas = reglas
    
    return mejor_atributo, mejores_reglas, mejor_precision

def predecir_one_r(X, atributo, reglas, clase_por_defecto):
    """
    Realiza predicciones usando las reglas generadas por One-R
    
    Parámetros:
    - X: DataFrame con las características
    - atributo: El atributo seleccionado por One-R
    - reglas: Diccionario que mapea valores del atributo a clases
    - clase_por_defecto: Clase a usar cuando un valor no está en las reglas
    """
    predicciones = []
    
    # Para cada fila en el conjunto de datos
    for _, fila in X.iterrows():
        # Obtenemos el valor del atributo seleccionado
        valor = fila[atributo]
        # Si existe una regla para este valor, usamos la clase correspondiente
        if valor in reglas:
            predicciones.append(reglas[valor])
        else:
            # Si no hay regla, usamos la clase por defecto (generalmente la mayoritaria)
            predicciones.append(clase_por_defecto)
    
    return predicciones

def main():
    # Definimos la ruta al archivo de datos
    archivo = r'C:\Users\x\OneDrive\Escritorio\Nueva carpeta\cervezas.txt'
    # Cargamos los datos
    datos = cargar_datos(archivo)
    print(f"Datos cargados desde {archivo}: {datos.shape[0]} filas, {datos.shape[1]} columnas")
    
    # Separamos características (X) y variable objetivo (y)
    X = datos.drop('Prefiere', axis=1)
    y = datos['Prefiere']
    
    # Aplicamos el algoritmo Zero-R
    clase_zero_r, precision_zero_r = zero_r(X, y)
    print(f"\nZero-R: Clase mayoritaria = '{clase_zero_r}', Precisión = {precision_zero_r:.4f}")
    
    # Aplicamos el algoritmo One-R
    atributo_one_r, reglas_one_r, precision_one_r = one_r(X, y)
    print(f"\nOne-R: Mejor atributo = '{atributo_one_r}', Precisión = {precision_one_r:.4f}")
    print(f"Reglas One-R: {reglas_one_r}")
    
    # Comparamos los modelos
    print("\nComparación:")
    if precision_one_r > precision_zero_r:
        print(f"One-R supera a Zero-R por {precision_one_r - precision_zero_r:.4f}")
    elif precision_zero_r > precision_one_r:
        print(f"Zero-R supera a One-R por {precision_zero_r - precision_one_r:.4f}")
    else:
        print("Ambos modelos tienen el mismo rendimiento")
    
    # Hacemos una prueba de predicción con One-R
    predicciones = predecir_one_r(X, atributo_one_r, reglas_one_r, clase_zero_r)
    correctos = sum(1 for pred, real in zip(predicciones, y) if pred == real)
    print(f"\nPrueba de predicción: {correctos} correctos de {len(y)} ({correctos/len(y):.4f})")

# Punto de entrada del programa
if __name__ == "__main__":
    main()