import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]

iris = pd.read_csv(url, names=column_names)

#print(iris.prod)

#Medias
print("Medias: ")
print(iris.mean(numeric_only=True))

#Desviación Estandar
print("Desviación Estandar: ")
print(iris.std(numeric_only=True))

#Varianzas
print("Varianzas: ")
print(iris.var(numeric_only=True))

#Conteos de clases
print("Cant. Setosa:")
print((iris["class"] == "Iris-setosa").sum())
print("Cant. Versicolor:")
print((iris["class"] == "Iris-versicolor").sum())
print("Cant. Virginica:")
print((iris["class"] == "Iris-virginica").sum())

#Se puede acceder al collab en
# https://colab.research.google.com/drive/1iUUoSrKjRWDrPuNMptsYeDOykzwXV4Gh?usp=sharing