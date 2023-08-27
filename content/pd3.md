Title: My First Project
Date: 2016-02-03 10:20
Category: Regression


Importamos librerias y datos de UCI


```python
import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]

iris = pd.read_csv(url, names=column_names)
```

"pandas" nos retorna un DataFrame, un tipo de dato nuevo con amplias funcionalidades y métodos que nos facilita la manipulación de los datos.


```python
#Medias
print("Medias: ")
print(iris.mean(numeric_only=True))
```

*Numeric Only nos permite calcular las medias solo de las columnas numericas, para evitar errores.*


```python
#Desviación Estandar
print("Desviación Estandar: ")
print(iris.std(numeric_only=True))
```


```python
#Varianzas
print("Varianzas: ")
print(iris.var(numeric_only=True))
```


```python
#Conteos de clases
print("Cant. Setosa:")
print((iris["class"] == "Iris-setosa").sum())
print("Cant. Versicolor:")
print((iris["class"] == "Iris-versicolor").sum())
print("Cant. Virginica:")
print((iris["class"] == "Iris-virginica").sum())

```
