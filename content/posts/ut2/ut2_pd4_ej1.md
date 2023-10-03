Title: Intro a Sklearn II: Guía de Kaggle. Modelado y Evaluación
Date: 2023-08-30
Category: 1. Introducciones

## Agregamos los imports necesarios  
Numpy y Pandas los usaremos para las operaciones y manipulación de datos.  
Seaborn y Matplotlib es para graficado.  
Warnings y os lo usaremos para ver el directorio de inputs.


```python
import numpy as np 
import pandas as pd 

import seaborn as sns
from matplotlib import pyplot as plt
sns.set_style("whitegrid")
%matplotlib inline

import warnings
warnings.filterwarnings("ignore")

import os 
print(os.listdir("./input"))
```

    ['gender_submission.csv', 'test.csv', 'train.csv']
    

Vamos a estar utilizando los dataset de Titanic, que ya hemos visto previamente. Tenemos el set ya particionado para test y entrenamiento de modelos, aparte de uno donde se presume que todas y solamente las mujeres sobreviven.  

## Cargamos y evaluamos nuestros datos  
Con pandas podemos importar los datos, ver algunos valores y estadísticas generales muy fácilmente.


```python
trainingData = pd.read_csv("./input/train.csv")
testData = pd.read_csv("./input/test.csv")

trainingData.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
trainingData.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Fare</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>891.000000</td>
      <td>891.000000</td>
      <td>891.000000</td>
      <td>714.000000</td>
      <td>891.000000</td>
      <td>891.000000</td>
      <td>891.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>446.000000</td>
      <td>0.383838</td>
      <td>2.308642</td>
      <td>29.699118</td>
      <td>0.523008</td>
      <td>0.381594</td>
      <td>32.204208</td>
    </tr>
    <tr>
      <th>std</th>
      <td>257.353842</td>
      <td>0.486592</td>
      <td>0.836071</td>
      <td>14.526497</td>
      <td>1.102743</td>
      <td>0.806057</td>
      <td>49.693429</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.420000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>223.500000</td>
      <td>0.000000</td>
      <td>2.000000</td>
      <td>20.125000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>7.910400</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>446.000000</td>
      <td>0.000000</td>
      <td>3.000000</td>
      <td>28.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>14.454200</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>668.500000</td>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>38.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>31.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>891.000000</td>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>80.000000</td>
      <td>8.000000</td>
      <td>6.000000</td>
      <td>512.329200</td>
    </tr>
  </tbody>
</table>
</div>



Podemos ver ya que hay datos incorrectos, por ejemplo la cabina. Deberemos procesarlos luego. Veamos que otros datos están mal y que tantos.  
Pandas nos permite contar cuantos datos son nulos:


```python
pd.isnull(trainingData).sum()
```




    PassengerId      0
    Survived         0
    Pclass           0
    Name             0
    Sex              0
    Age            177
    SibSp            0
    Parch            0
    Ticket           0
    Fare             0
    Cabin          687
    Embarked         2
    dtype: int64




```python
pd.isnull(testData).sum()
```




    PassengerId      0
    Pclass           0
    Name             0
    Sex              0
    Age             86
    SibSp            0
    Parch            0
    Ticket           0
    Fare             1
    Cabin          327
    Embarked         0
    dtype: int64



Cabin tiene muchos nulos, pero podríamos considerarlo un atributo no muy influyente para lo que queremos predecir (los supervivientes), por lo que puede ser util eliminarlo completamente. Ticket también entra en este caso, por lo que lo dropeamos. 


```python
trainingData.drop(labels=["Cabin", "Ticket"], axis=1, inplace=True)
testData.drop(labels=["Cabin", "Ticket"], axis=1, inplace=True)

```


```python
pd.isnull(trainingData).sum()
```




    PassengerId      0
    Survived         0
    Pclass           0
    Name             0
    Sex              0
    Age            177
    SibSp            0
    Parch            0
    Fare             0
    Embarked         2
    dtype: int64



Podemos ver que el campo edad también tiene muchos nulos, pero es un dato importante por lo que eliminarlo como atributo es mala idea. Veremos su distribución general para decidir como proseguir con este campo.  


```python
copy = trainingData.copy()
copy.dropna(inplace = True)
sns.distplot(copy["Age"])
```




    <Axes: xlabel='Age', ylabel='Density'>




    
![png](ut2_pd4_ej1_files/ut2_pd4_ej1_14_1.png)
    


Se denota que las edades son en general un poco mayores, tirando a la derecha en el gráfico. Para los datos faltantes podemos utilizar la media o la mediana. Debido a que los datos favorecen levemente un lado, la mediana es más objetiva.


```python
trainingData["Age"].fillna(trainingData["Age"].median(), inplace = True)
testData["Age"].fillna(testData["Age"].median(), inplace = True) 
trainingData["Embarked"].fillna("S", inplace = True)
testData["Fare"].fillna(testData["Fare"].median(), inplace = True)

copy = trainingData.copy()
copy.dropna(inplace = True)
sns.distplot(copy["Age"])
```




    <Axes: xlabel='Age', ylabel='Density'>




    
![png](ut2_pd4_ej1_files/ut2_pd4_ej1_16_1.png)
    


Puede verse intrusivo, pero permite mantener los datos lo más constantes con los originales posible.

# Graficando los datos  
Graficando y comparando las relaciones de los datos con lo que buscamos predecir nos dará mejor idea de las estructuras subyacentes y facilitará construir el mejor modelo posible para el problema, descartando variables que no inciden en el resultado o que son demasiado correlacionadas.
Por ejemplo veamos género y si la persona sobrevivió.


```python
sns.barplot(x="Sex", y="Survived", data=trainingData)
plt.title("Distribution of Survival based on Gender")
plt.show()

total_survived_females = trainingData[trainingData.Sex == "female"]["Survived"].sum()
total_survived_males = trainingData[trainingData.Sex == "male"]["Survived"].sum()

print("Total people survived is: " + str((total_survived_females + total_survived_males)))
print("Proportion of Females who survived:") 
print(total_survived_females/(total_survived_females + total_survived_males))
print("Proportion of Males who survived:")
print(total_survived_males/(total_survived_females + total_survived_males))
```


    
![png](ut2_pd4_ej1_files/ut2_pd4_ej1_19_0.png)
    


    Total people survived is: 342
    Proportion of Females who survived:
    0.6812865497076024
    Proportion of Males who survived:
    0.31871345029239767
    

Al ver la fuerte diferencia entre las proporciones de supervivencia entre los géneros.  
Veamos para otros atributos


```python
sns.barplot(x="Pclass", y="Survived", data=trainingData)
plt.ylabel("Survival Rate")
plt.title("Distribution of Survival Based on Class")
plt.show()

total_survived_one = trainingData[trainingData.Pclass == 1]["Survived"].sum()
total_survived_two = trainingData[trainingData.Pclass == 2]["Survived"].sum()
total_survived_three = trainingData[trainingData.Pclass == 3]["Survived"].sum()
total_survived_class = total_survived_one + total_survived_two + total_survived_three

print("Total people survived is: " + str(total_survived_class))
print("Proportion of Class 1 Passengers who survived:") 
print(total_survived_one/total_survived_class)
print("Proportion of Class 2 Passengers who survived:")
print(total_survived_two/total_survived_class)
print("Proportion of Class 3 Passengers who survived:")
print(total_survived_three/total_survived_class)
```


    
![png](ut2_pd4_ej1_files/ut2_pd4_ej1_21_0.png)
    


    Total people survived is: 342
    Proportion of Class 1 Passengers who survived:
    0.39766081871345027
    Proportion of Class 2 Passengers who survived:
    0.2543859649122807
    Proportion of Class 3 Passengers who survived:
    0.347953216374269
    


```python
sns.barplot(x="Pclass", y="Survived", hue="Sex", data=trainingData)
plt.ylabel("Survival Rate")
plt.title("Survival Rates Based on Gender and Class")
```




    Text(0.5, 1.0, 'Survival Rates Based on Gender and Class')




    
![png](ut2_pd4_ej1_files/ut2_pd4_ej1_22_1.png)
    



```python
sns.barplot(x="Sex", y="Survived", hue="Pclass", data=trainingData)
plt.ylabel("Survival Rate")
plt.title("Survival Rates Based on Gender and Class")
```




    Text(0.5, 1.0, 'Survival Rates Based on Gender and Class')




    
![png](ut2_pd4_ej1_files/ut2_pd4_ej1_23_1.png)
    


Las diferencias de supervivencia entre las primera y las otras clases es significativa también.


```python
survived_ages = trainingData[trainingData.Survived == 1]["Age"]
not_survived_ages = trainingData[trainingData.Survived == 0]["Age"]
plt.subplot(1, 2, 1)
sns.distplot(survived_ages, kde=False)
plt.axis([0, 100, 0, 100])
plt.title("Survived")
plt.ylabel("Proportion")
plt.subplot(1, 2, 2)
sns.distplot(not_survived_ages, kde=False)
plt.axis([0, 100, 0, 100])
plt.title("Didn't Survive")
plt.subplots_adjust(right=1.7)
plt.show()
```


    
![png](ut2_pd4_ej1_files/ut2_pd4_ej1_25_0.png)
    



```python
sns.stripplot(x="Survived", y="Age", data=trainingData, jitter=True)
```




    <Axes: xlabel='Survived', ylabel='Age'>




    
![png](ut2_pd4_ej1_files/ut2_pd4_ej1_26_1.png)
    


Podemos ver concentraciones excepcionales de supervivientes en los menores de edad respecto a los que perecieron.

> *si queremos ver todos los datos y como se relacionan, se puede crear con el siguiente comando:*


```python
sns.pairplot(trainingData)
```




    <seaborn.axisgrid.PairGrid at 0x2278ce93970>




    
![png](ut2_pd4_ej1_files/ut2_pd4_ej1_29_1.png)
    


# Feature Engineering  
Pasaremos a procesar y adaptar nuestros atributos a formas más manejables. Para nuestro caso debemos convertir todos los datos a numéricos, ya que solo estos puede tomar el modelo.  
Por ejemplo datos categóricos como género o embarcó.
Usaremos One-Hot-Encoding por sklearn


```python
set(trainingData["Sex"])
```




    {'female', 'male'}




```python
set(trainingData["Embarked"])
```




    {'C', 'Q', 'S'}




```python
from sklearn.preprocessing import LabelEncoder

le_sex = LabelEncoder()
le_sex.fit(trainingData["Sex"])

encoded_sex_training = le_sex.transform(trainingData["Sex"])
trainingData["Sex"] = encoded_sex_training
encoded_sex_testing = le_sex.transform(testData["Sex"])
testData["Sex"] = encoded_sex_testing

le_embarked = LabelEncoder()
le_embarked.fit(trainingData["Embarked"])

encoded_embarked_training = le_embarked.transform(trainingData["Embarked"])
trainingData["Embarked"] = encoded_embarked_training
encoded_embarked_testing = le_embarked.transform(testData["Embarked"])
testData["Embarked"] = encoded_embarked_testing

#vemos el resultado
trainingData.sample(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Fare</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>764</th>
      <td>765</td>
      <td>0</td>
      <td>3</td>
      <td>Eklund, Mr. Hans Linus</td>
      <td>1</td>
      <td>16.0</td>
      <td>0</td>
      <td>0</td>
      <td>7.775</td>
      <td>2</td>
    </tr>
    <tr>
      <th>425</th>
      <td>426</td>
      <td>0</td>
      <td>3</td>
      <td>Wiseman, Mr. Phillippe</td>
      <td>1</td>
      <td>28.0</td>
      <td>0</td>
      <td>0</td>
      <td>7.250</td>
      <td>2</td>
    </tr>
    <tr>
      <th>187</th>
      <td>188</td>
      <td>1</td>
      <td>1</td>
      <td>Romaine, Mr. Charles Hallace ("Mr C Rolmane")</td>
      <td>1</td>
      <td>45.0</td>
      <td>0</td>
      <td>0</td>
      <td>26.550</td>
      <td>2</td>
    </tr>
    <tr>
      <th>723</th>
      <td>724</td>
      <td>0</td>
      <td>2</td>
      <td>Hodges, Mr. Henry Price</td>
      <td>1</td>
      <td>50.0</td>
      <td>0</td>
      <td>0</td>
      <td>13.000</td>
      <td>2</td>
    </tr>
    <tr>
      <th>56</th>
      <td>57</td>
      <td>1</td>
      <td>2</td>
      <td>Rugg, Miss. Emily</td>
      <td>0</td>
      <td>21.0</td>
      <td>0</td>
      <td>0</td>
      <td>10.500</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



Podemos también combinar y crear columnas nuevas, por ejemplo unir "número de hermanos y pareja" y "número de padres e hijos" en un solo atributo "familia a bordo", y de este también podemos crear una para saber si alguien viaja solo.  


```python
trainingData["FamSize"] = trainingData["SibSp"] + trainingData["Parch"] + 1
testData["FamSize"] = testData["SibSp"] + testData["Parch"] + 1

trainingData["IsAlone"] = trainingData.FamSize.apply(lambda x: 1 if x == 1 else 0)
testData["IsAlone"] = testData.FamSize.apply(lambda x: 1 if x == 1 else 0)

trainingData.sample(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Fare</th>
      <th>Embarked</th>
      <th>FamSize</th>
      <th>IsAlone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>601</th>
      <td>602</td>
      <td>0</td>
      <td>3</td>
      <td>Slabenoff, Mr. Petco</td>
      <td>1</td>
      <td>28.0</td>
      <td>0</td>
      <td>0</td>
      <td>7.8958</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>481</th>
      <td>482</td>
      <td>0</td>
      <td>2</td>
      <td>Frost, Mr. Anthony Wood "Archie"</td>
      <td>1</td>
      <td>28.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0000</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>110</th>
      <td>111</td>
      <td>0</td>
      <td>1</td>
      <td>Porter, Mr. Walter Chamberlain</td>
      <td>1</td>
      <td>47.0</td>
      <td>0</td>
      <td>0</td>
      <td>52.0000</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>319</th>
      <td>320</td>
      <td>1</td>
      <td>1</td>
      <td>Spedden, Mrs. Frederic Oakley (Margaretta Corn...</td>
      <td>0</td>
      <td>40.0</td>
      <td>1</td>
      <td>1</td>
      <td>134.5000</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>369</th>
      <td>370</td>
      <td>1</td>
      <td>1</td>
      <td>Aubart, Mme. Leontine Pauline</td>
      <td>0</td>
      <td>24.0</td>
      <td>0</td>
      <td>0</td>
      <td>69.3000</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



Otro atributo que podemos calcular es utilizando el nombre. Sin saber el género de la persona, pero si su nombre esta precedido por Mr. o Mrs. entre otros, podemos inferir su género, lo cual es influyente en el resultado. Usaremos encoding similar a como hicimos con embarked y sex. 


```python
for name in trainingData["Name"]:
    trainingData["Title"] = trainingData["Name"].str.extract("([A-Za-z]+)\.",expand=True)
    
for name in testData["Name"]:
    testData["Title"] = testData["Name"].str.extract("([A-Za-z]+)\.",expand=True)
    
trainingData.sample(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Fare</th>
      <th>Embarked</th>
      <th>FamSize</th>
      <th>IsAlone</th>
      <th>Title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>815</th>
      <td>816</td>
      <td>0</td>
      <td>1</td>
      <td>Fry, Mr. Richard</td>
      <td>1</td>
      <td>28.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0000</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Mr</td>
    </tr>
    <tr>
      <th>154</th>
      <td>155</td>
      <td>0</td>
      <td>3</td>
      <td>Olsen, Mr. Ole Martin</td>
      <td>1</td>
      <td>28.0</td>
      <td>0</td>
      <td>0</td>
      <td>7.3125</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Mr</td>
    </tr>
    <tr>
      <th>593</th>
      <td>594</td>
      <td>0</td>
      <td>3</td>
      <td>Bourke, Miss. Mary</td>
      <td>0</td>
      <td>28.0</td>
      <td>0</td>
      <td>2</td>
      <td>7.7500</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>Miss</td>
    </tr>
    <tr>
      <th>684</th>
      <td>685</td>
      <td>0</td>
      <td>2</td>
      <td>Brown, Mr. Thomas William Solomon</td>
      <td>1</td>
      <td>60.0</td>
      <td>1</td>
      <td>1</td>
      <td>39.0000</td>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>Mr</td>
    </tr>
    <tr>
      <th>602</th>
      <td>603</td>
      <td>0</td>
      <td>1</td>
      <td>Harrington, Mr. Charles H</td>
      <td>1</td>
      <td>28.0</td>
      <td>0</td>
      <td>0</td>
      <td>42.4000</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Mr</td>
    </tr>
  </tbody>
</table>
</div>



También los codificaremos, ya que estos títulos son categóricos y deben ser consistentes.


```python
titles = set(trainingData["Title"])
print(titles)
```

    {'Mlle', 'Master', 'Mr', 'Rev', 'Lady', 'Sir', 'Mrs', 'Dr', 'Miss', 'Jonkheer', 'Major', 'Col', 'Ms', 'Don', 'Capt', 'Countess', 'Mme'}
    


```python
title_list = list(trainingData["Title"])
frequency_titles = []

for i in titles:
    frequency_titles.append(title_list.count(i))
    
titles = list(titles)

title_dataframe = pd.DataFrame({
    "Titles" : titles,
    "Frequency" : frequency_titles
})

print(title_dataframe)
```

          Titles  Frequency
    0       Mlle          2
    1     Master         40
    2         Mr        517
    3        Rev          6
    4       Lady          1
    5        Sir          1
    6        Mrs        125
    7         Dr          7
    8       Miss        182
    9   Jonkheer          1
    10     Major          2
    11       Col          2
    12        Ms          1
    13       Don          1
    14      Capt          1
    15  Countess          1
    16       Mme          1
    


```python
title_replacements = {"Mlle": "Other", "Major": "Other", "Col": "Other", "Sir": "Other", "Don": "Other", "Mme": "Other",
          "Jonkheer": "Other", "Lady": "Other", "Capt": "Other", "Countess": "Other", "Ms": "Other", "Dona": "Other"}

trainingData.replace({"Title": title_replacements}, inplace=True)
testData.replace({"Title": title_replacements}, inplace=True)

le_title = LabelEncoder()
le_title.fit(trainingData["Title"])

encoded_title_training = le_title.transform(trainingData["Title"])
trainingData["Title"] = encoded_title_training
encoded_title_testing = le_title.transform(testData["Title"])
testData["Title"] = encoded_title_testing
```

Con esto ya digerimos el valor del campo name, por lo que podemos removerlo.


```python
trainingData.drop("Name", axis = 1, inplace = True)
testData.drop("Name", axis = 1, inplace = True)

trainingData.sample(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Fare</th>
      <th>Embarked</th>
      <th>FamSize</th>
      <th>IsAlone</th>
      <th>Title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>46</th>
      <td>47</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>28.00</td>
      <td>1</td>
      <td>0</td>
      <td>15.5000</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>78</th>
      <td>79</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>0.83</td>
      <td>0</td>
      <td>2</td>
      <td>29.0000</td>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>94</th>
      <td>95</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>59.00</td>
      <td>0</td>
      <td>0</td>
      <td>7.2500</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>786</th>
      <td>787</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>18.00</td>
      <td>0</td>
      <td>0</td>
      <td>7.4958</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>569</th>
      <td>570</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>32.00</td>
      <td>0</td>
      <td>0</td>
      <td>7.8542</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



## Reescalado de Atributos  
Debido que tenemos rangos muy variados entre los campos (por ejemplo edad y fare) conviene normalizarlos para que el modelo pueda manejarlos mejor y asignarles las importancias correctas (debido a la normalización del peso de sus magnitudes).  
Usaremos el Standard Scales de sklearn.


```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

#COnvertimos nuestros datos a array ya que esto es lo que acepta el scaler
ages_train = np.array(trainingData["Age"]).reshape(-1, 1)
fares_train = np.array(trainingData["Fare"]).reshape(-1, 1)
ages_test = np.array(testData["Age"]).reshape(-1, 1)
fares_test = np.array(testData["Fare"]).reshape(-1, 1)

trainingData["Age"] = scaler.fit_transform(ages_train)
trainingData["Fare"] = scaler.fit_transform(fares_train)
testData["Age"] = scaler.fit_transform(ages_test)
testData["Fare"] = scaler.fit_transform(fares_test)

# Se puede sustituir por el minmaxscaler si se desea
trainingData.sample(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Fare</th>
      <th>Embarked</th>
      <th>FamSize</th>
      <th>IsAlone</th>
      <th>Title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>24</th>
      <td>25</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>-1.641634</td>
      <td>3</td>
      <td>1</td>
      <td>-0.224083</td>
      <td>2</td>
      <td>5</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>695</th>
      <td>696</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>1.739759</td>
      <td>0</td>
      <td>0</td>
      <td>-0.376603</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>639</th>
      <td>640</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>-0.104637</td>
      <td>1</td>
      <td>0</td>
      <td>-0.324253</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>808</th>
      <td>809</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>0.740711</td>
      <td>0</td>
      <td>0</td>
      <td>-0.386671</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>788</th>
      <td>789</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>-2.179583</td>
      <td>1</td>
      <td>2</td>
      <td>-0.234150</td>
      <td>2</td>
      <td>4</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



## Modelado, optimización y predicción  
Ahora ya que los datos están procesados podemos pasar a probar diferentes modelos y evaluarlos en su performance.  
Sklearn nos da varios algoritmos de clasificación.  


```python
# Modelos a utilizarse:
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

# Para medir desempeño:
from sklearn.metrics import make_scorer, accuracy_score 
# Validación cruzada:
from sklearn.model_selection import GridSearchCV
```


```python
X_train = trainingData.drop(labels=["PassengerId", "Survived"], axis=1) #limpiamos las variables independientes
y_train = trainingData["Survived"] #definimos la variable dependiente u objetivo
X_test = testData.drop("PassengerId", axis=1) #definimos el set de test
#No definimos en el set de test el atributo Survived como objetivo ya que es lo que queremos que prediga

X_train.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Pclass</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Fare</th>
      <th>Embarked</th>
      <th>FamSize</th>
      <th>IsAlone</th>
      <th>Title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>1</td>
      <td>-0.565736</td>
      <td>1</td>
      <td>0</td>
      <td>-0.502445</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0</td>
      <td>0.663861</td>
      <td>1</td>
      <td>0</td>
      <td>0.786845</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>0</td>
      <td>-0.258337</td>
      <td>0</td>
      <td>0</td>
      <td>-0.488854</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>0</td>
      <td>0.433312</td>
      <td>1</td>
      <td>0</td>
      <td>0.420730</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>1</td>
      <td>0.433312</td>
      <td>0</td>
      <td>0</td>
      <td>-0.486337</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



Para evitar overfitting es conveniente separar un tercer grupo de datos como validación, sklearn tiene un método que lo permite hacer.


```python
from sklearn.model_selection import train_test_split

X_training, X_valid, y_training, y_valid = train_test_split(X_train, y_train, test_size=0.2, random_state=0) 
#X_valid e y_valid son los sets de validacion
```

### SVC


```python
svc_clf = SVC() 

parameters_svc = {"kernel": ["rbf", "linear"], "probability": [True, False], "verbose": [False, False]}

grid_svc = GridSearchCV(svc_clf, parameters_svc, scoring=make_scorer(accuracy_score))
grid_svc.fit(X_training, y_training)

svc_clf = grid_svc.best_estimator_

svc_clf.fit(X_training, y_training)
pred_svc = svc_clf.predict(X_valid)
acc_svc = accuracy_score(y_valid, pred_svc)

print("El puntaje de precisión de SVC es: " + str(acc_svc))

```

    El puntaje de precisión de SVC es: 0.8212290502793296
    

### SVC Linear


```python
linsvc_clf = LinearSVC()

parameters_linsvc = {"multi_class": ["ovr", "crammer_singer"], "fit_intercept": [True, False], "max_iter": [100, 500, 1000, 1500]}

grid_linsvc = GridSearchCV(linsvc_clf, parameters_linsvc, scoring=make_scorer(accuracy_score))
grid_linsvc.fit(X_training, y_training)

linsvc_clf = grid_linsvc.best_estimator_

linsvc_clf.fit(X_training, y_training)
pred_linsvc = linsvc_clf.predict(X_valid)
acc_linsvc = accuracy_score(y_valid, pred_linsvc)

print("El puntaje de precisión de SVC Linear es: " + str(acc_linsvc))
```

    El puntaje de precisión de SVC Linear es: 0.7932960893854749
    

### Random Forest


```python
rf_clf = RandomForestClassifier()

parameters_rf = {"n_estimators": [4, 5, 6, 7, 8, 9, 10, 15], "criterion": ["gini", "entropy"], "max_features": ["auto", "sqrt", "log2"], 
                 "max_depth": [2, 3, 5, 10], "min_samples_split": [2, 3, 5, 10]}

grid_rf = GridSearchCV(rf_clf, parameters_rf, scoring=make_scorer(accuracy_score))
grid_rf.fit(X_training, y_training)

rf_clf = grid_rf.best_estimator_

rf_clf.fit(X_training, y_training)
pred_rf = rf_clf.predict(X_valid)
acc_rf = accuracy_score(y_valid, pred_rf)

print("El puntaje de precisión de Random Forest es: " + str(acc_rf))
```

    El puntaje de precisión de Random Forest es: 0.8044692737430168
    

### Regresión Logística


```python
logreg_clf = LogisticRegression()

parameters_logreg = {"penalty": ["l2"], "fit_intercept": [True, False], "solver": ["newton-cg", "lbfgs", "liblinear", "sag", "saga"],
                     "max_iter": [50, 100, 200], "warm_start": [True, False]}

grid_logreg = GridSearchCV(logreg_clf, parameters_logreg, scoring=make_scorer(accuracy_score))
grid_logreg.fit(X_training, y_training)

logreg_clf = grid_logreg.best_estimator_

logreg_clf.fit(X_training, y_training)
pred_logreg = logreg_clf.predict(X_valid)
acc_logreg = accuracy_score(y_valid, pred_logreg)

print("El puntaje de precisión de la Regresión es: " + str(acc_logreg))
```

    El puntaje de precisión de la Regresión es: 0.7988826815642458
    

### K-Neighbors


```python
knn_clf = KNeighborsClassifier()

parameters_knn = {"n_neighbors": [3, 5, 10, 15], "weights": ["uniform", "distance"], "algorithm": ["auto", "ball_tree", "kd_tree"],
                  "leaf_size": [20, 30, 50]}

grid_knn = GridSearchCV(knn_clf, parameters_knn, scoring=make_scorer(accuracy_score))
grid_knn.fit(X_training, y_training)

knn_clf = grid_knn.best_estimator_

knn_clf.fit(X_training, y_training)
pred_knn = knn_clf.predict(X_valid)
acc_knn = accuracy_score(y_valid, pred_knn)

print("El puntaje de precisión de K-Vecinos es: " + str(acc_knn))
```

    El puntaje de precisión de K-Vecinos es: 0.7653631284916201
    

### Gaussian NB


```python
gnb_clf = GaussianNB()

parameters_gnb = {}

grid_gnb = GridSearchCV(gnb_clf, parameters_gnb, scoring=make_scorer(accuracy_score))
grid_gnb.fit(X_training, y_training)

gnb_clf = grid_gnb.best_estimator_

gnb_clf.fit(X_training, y_training)
pred_gnb = gnb_clf.predict(X_valid)
acc_gnb = accuracy_score(y_valid, pred_gnb)

print("El puntaje de precisión de Gaussian NB es: " + str(acc_gnb))
```

    El puntaje de precisión de Gaussian NB es: 0.776536312849162
    

### Árbol de Decisión


```python
dt_clf = DecisionTreeClassifier()

parameters_dt = {"criterion": ["gini", "entropy"], "splitter": ["best", "random"], "max_features": ["auto", "sqrt", "log2"]}

grid_dt = GridSearchCV(dt_clf, parameters_dt, scoring=make_scorer(accuracy_score))
grid_dt.fit(X_training, y_training)

dt_clf = grid_dt.best_estimator_

dt_clf.fit(X_training, y_training)
pred_dt = dt_clf.predict(X_valid)
acc_dt = accuracy_score(y_valid, pred_dt)

print("El puntaje de precisión del Árbol de Decisión es: " + str(acc_dt))
```

    El puntaje de precisión del Árbol de Decisión es: 0.7877094972067039
    

### XGBoost


```python
from xgboost import XGBClassifier

xg_clf = XGBClassifier()

parameters_xg = {"objective" : ["reg:linear"], "n_estimators" : [5, 10, 15, 20]}

grid_xg = GridSearchCV(xg_clf, parameters_xg, scoring=make_scorer(accuracy_score))
grid_xg.fit(X_training, y_training)

xg_clf = grid_xg.best_estimator_

xg_clf.fit(X_training, y_training)
pred_xg = xg_clf.predict(X_valid)
acc_xg = accuracy_score(y_valid, pred_xg)

print("El puntaje de precisión de XGBoost es: " + str(acc_xg))
```

    [20:09:17] WARNING: C:\buildkite-agent\builds\buildkite-windows-cpu-autoscaling-group-i-0fdc6d574b9c0d168-1\xgboost\xgboost-ci-windows\src\objective\regression_obj.cu:213: reg:linear is now deprecated in favor of reg:squarederror.
    [20:09:17] WARNING: C:\buildkite-agent\builds\buildkite-windows-cpu-autoscaling-group-i-0fdc6d574b9c0d168-1\xgboost\xgboost-ci-windows\src\objective\regression_obj.cu:213: reg:linear is now deprecated in favor of reg:squarederror.
    [20:09:17] WARNING: C:\buildkite-agent\builds\buildkite-windows-cpu-autoscaling-group-i-0fdc6d574b9c0d168-1\xgboost\xgboost-ci-windows\src\objective\regression_obj.cu:213: reg:linear is now deprecated in favor of reg:squarederror.
    [20:09:17] WARNING: C:\buildkite-agent\builds\buildkite-windows-cpu-autoscaling-group-i-0fdc6d574b9c0d168-1\xgboost\xgboost-ci-windows\src\objective\regression_obj.cu:213: reg:linear is now deprecated in favor of reg:squarederror.
    [20:09:17] WARNING: C:\buildkite-agent\builds\buildkite-windows-cpu-autoscaling-group-i-0fdc6d574b9c0d168-1\xgboost\xgboost-ci-windows\src\objective\regression_obj.cu:213: reg:linear is now deprecated in favor of reg:squarederror.
    [20:09:17] WARNING: C:\buildkite-agent\builds\buildkite-windows-cpu-autoscaling-group-i-0fdc6d574b9c0d168-1\xgboost\xgboost-ci-windows\src\objective\regression_obj.cu:213: reg:linear is now deprecated in favor of reg:squarederror.
    [20:09:18] WARNING: C:\buildkite-agent\builds\buildkite-windows-cpu-autoscaling-group-i-0fdc6d574b9c0d168-1\xgboost\xgboost-ci-windows\src\objective\regression_obj.cu:213: reg:linear is now deprecated in favor of reg:squarederror.
    [20:09:18] WARNING: C:\buildkite-agent\builds\buildkite-windows-cpu-autoscaling-group-i-0fdc6d574b9c0d168-1\xgboost\xgboost-ci-windows\src\objective\regression_obj.cu:213: reg:linear is now deprecated in favor of reg:squarederror.
    [20:09:18] WARNING: C:\buildkite-agent\builds\buildkite-windows-cpu-autoscaling-group-i-0fdc6d574b9c0d168-1\xgboost\xgboost-ci-windows\src\objective\regression_obj.cu:213: reg:linear is now deprecated in favor of reg:squarederror.
    [20:09:18] WARNING: C:\buildkite-agent\builds\buildkite-windows-cpu-autoscaling-group-i-0fdc6d574b9c0d168-1\xgboost\xgboost-ci-windows\src\objective\regression_obj.cu:213: reg:linear is now deprecated in favor of reg:squarederror.
    [20:09:18] WARNING: C:\buildkite-agent\builds\buildkite-windows-cpu-autoscaling-group-i-0fdc6d574b9c0d168-1\xgboost\xgboost-ci-windows\src\objective\regression_obj.cu:213: reg:linear is now deprecated in favor of reg:squarederror.
    [20:09:18] WARNING: C:\buildkite-agent\builds\buildkite-windows-cpu-autoscaling-group-i-0fdc6d574b9c0d168-1\xgboost\xgboost-ci-windows\src\objective\regression_obj.cu:213: reg:linear is now deprecated in favor of reg:squarederror.
    [20:09:18] WARNING: C:\buildkite-agent\builds\buildkite-windows-cpu-autoscaling-group-i-0fdc6d574b9c0d168-1\xgboost\xgboost-ci-windows\src\objective\regression_obj.cu:213: reg:linear is now deprecated in favor of reg:squarederror.
    [20:09:18] WARNING: C:\buildkite-agent\builds\buildkite-windows-cpu-autoscaling-group-i-0fdc6d574b9c0d168-1\xgboost\xgboost-ci-windows\src\objective\regression_obj.cu:213: reg:linear is now deprecated in favor of reg:squarederror.
    [20:09:18] WARNING: C:\buildkite-agent\builds\buildkite-windows-cpu-autoscaling-group-i-0fdc6d574b9c0d168-1\xgboost\xgboost-ci-windows\src\objective\regression_obj.cu:213: reg:linear is now deprecated in favor of reg:squarederror.
    [20:09:18] WARNING: C:\buildkite-agent\builds\buildkite-windows-cpu-autoscaling-group-i-0fdc6d574b9c0d168-1\xgboost\xgboost-ci-windows\src\objective\regression_obj.cu:213: reg:linear is now deprecated in favor of reg:squarederror.
    [20:09:18] WARNING: C:\buildkite-agent\builds\buildkite-windows-cpu-autoscaling-group-i-0fdc6d574b9c0d168-1\xgboost\xgboost-ci-windows\src\objective\regression_obj.cu:213: reg:linear is now deprecated in favor of reg:squarederror.
    [20:09:18] WARNING: C:\buildkite-agent\builds\buildkite-windows-cpu-autoscaling-group-i-0fdc6d574b9c0d168-1\xgboost\xgboost-ci-windows\src\objective\regression_obj.cu:213: reg:linear is now deprecated in favor of reg:squarederror.
    [20:09:18] WARNING: C:\buildkite-agent\builds\buildkite-windows-cpu-autoscaling-group-i-0fdc6d574b9c0d168-1\xgboost\xgboost-ci-windows\src\objective\regression_obj.cu:213: reg:linear is now deprecated in favor of reg:squarederror.
    [20:09:18] WARNING: C:\buildkite-agent\builds\buildkite-windows-cpu-autoscaling-group-i-0fdc6d574b9c0d168-1\xgboost\xgboost-ci-windows\src\objective\regression_obj.cu:213: reg:linear is now deprecated in favor of reg:squarederror.
    [20:09:18] WARNING: C:\buildkite-agent\builds\buildkite-windows-cpu-autoscaling-group-i-0fdc6d574b9c0d168-1\xgboost\xgboost-ci-windows\src\objective\regression_obj.cu:213: reg:linear is now deprecated in favor of reg:squarederror.
    [20:09:18] WARNING: C:\buildkite-agent\builds\buildkite-windows-cpu-autoscaling-group-i-0fdc6d574b9c0d168-1\xgboost\xgboost-ci-windows\src\objective\regression_obj.cu:213: reg:linear is now deprecated in favor of reg:squarederror.
    El puntaje de precisión de XGBoost es: 0.8435754189944135
    

## Evaluando los modelos  
Una vez ejecutamos los modelos, podemos recopilar nuestros resultados:


```python
model_performance = pd.DataFrame({
    "Model": ["SVC", "Linear SVC", "Random Forest", 
              "Logistic Regression", "K Nearest Neighbors", "Gaussian Naive Bayes",  
              "Decision Tree", "XGBClassifier"],
    "Accuracy": [acc_svc, acc_linsvc, acc_rf, 
              acc_logreg, acc_knn, acc_gnb, acc_dt, acc_xg]
})

model_performance.sort_values(by="Accuracy", ascending=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Model</th>
      <th>Accuracy</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>XGBClassifier</td>
      <td>0.843575</td>
    </tr>
    <tr>
      <th>0</th>
      <td>SVC</td>
      <td>0.821229</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Random Forest</td>
      <td>0.804469</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Logistic Regression</td>
      <td>0.798883</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Linear SVC</td>
      <td>0.793296</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Decision Tree</td>
      <td>0.787709</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Gaussian Naive Bayes</td>
      <td>0.776536</td>
    </tr>
    <tr>
      <th>4</th>
      <td>K Nearest Neighbors</td>
      <td>0.765363</td>
    </tr>
  </tbody>
</table>
</div>



De aquí concluimos el presento trabajo, habiendo probado amplias herramientas como pandas, sklearn.  
La manipulación de datos, transformación de atributos y la ingeniería de atributos son esenciales en el ML, ya que a pesar de parecer cambios ínfimos, estos pueden hacer nuestros modelos un poco más performantes, un poco más precisos, que en escalas mayores puede ser toda la diferencia.
