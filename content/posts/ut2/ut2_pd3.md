Title: Intro a Scikit
Date: 2023-08-30
Category: Intro

## En este ejercicio se practicará pre procesamiento de datos y recuperado por python
1. Descargar el dataset “wine” del repositorio UCI y cargar el dataset en formato CSV.
2. Imprimir todas las columnas de las primeras 10 filas.
3. Convertir los valores numéricos en string a float, en caso de ser necesario
4. Obtener los valores mínimos y máximos correspondientes a cada columna.
5. Obtener la media de los valores de cada columna.
6. Obtener la desviación estándar de los valores de cada columna.
7. Normalizar los valores el dataset original.
8. Estandarizar los valores del dataset original.
9. Dividir el dataset en conjuntos de entrenamiento y testing.

---

*Importamos el csv de la página de UCI:*


```python
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine"

column_names = ["Class", "Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium", "Total phenols",
                "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins", "Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline" ]

wine = pd.read_csv(url+".data", names=column_names)
wine.describe()
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
      <th>Class</th>
      <th>Alcohol</th>
      <th>Malic acid</th>
      <th>Ash</th>
      <th>Alcalinity of ash</th>
      <th>Magnesium</th>
      <th>Total phenols</th>
      <th>Flavanoids</th>
      <th>Nonflavanoid phenols</th>
      <th>Proanthocyanins</th>
      <th>Color intensity</th>
      <th>Hue</th>
      <th>OD280/OD315 of diluted wines</th>
      <th>Proline</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>178.000000</td>
      <td>178.000000</td>
      <td>178.000000</td>
      <td>178.000000</td>
      <td>178.000000</td>
      <td>178.000000</td>
      <td>178.000000</td>
      <td>178.000000</td>
      <td>178.000000</td>
      <td>178.000000</td>
      <td>178.000000</td>
      <td>178.000000</td>
      <td>178.000000</td>
      <td>178.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1.938202</td>
      <td>13.000618</td>
      <td>2.336348</td>
      <td>2.366517</td>
      <td>19.494944</td>
      <td>99.741573</td>
      <td>2.295112</td>
      <td>2.029270</td>
      <td>0.361854</td>
      <td>1.590899</td>
      <td>5.058090</td>
      <td>0.957449</td>
      <td>2.611685</td>
      <td>746.893258</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.775035</td>
      <td>0.811827</td>
      <td>1.117146</td>
      <td>0.274344</td>
      <td>3.339564</td>
      <td>14.282484</td>
      <td>0.625851</td>
      <td>0.998859</td>
      <td>0.124453</td>
      <td>0.572359</td>
      <td>2.318286</td>
      <td>0.228572</td>
      <td>0.709990</td>
      <td>314.907474</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>11.030000</td>
      <td>0.740000</td>
      <td>1.360000</td>
      <td>10.600000</td>
      <td>70.000000</td>
      <td>0.980000</td>
      <td>0.340000</td>
      <td>0.130000</td>
      <td>0.410000</td>
      <td>1.280000</td>
      <td>0.480000</td>
      <td>1.270000</td>
      <td>278.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1.000000</td>
      <td>12.362500</td>
      <td>1.602500</td>
      <td>2.210000</td>
      <td>17.200000</td>
      <td>88.000000</td>
      <td>1.742500</td>
      <td>1.205000</td>
      <td>0.270000</td>
      <td>1.250000</td>
      <td>3.220000</td>
      <td>0.782500</td>
      <td>1.937500</td>
      <td>500.500000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2.000000</td>
      <td>13.050000</td>
      <td>1.865000</td>
      <td>2.360000</td>
      <td>19.500000</td>
      <td>98.000000</td>
      <td>2.355000</td>
      <td>2.135000</td>
      <td>0.340000</td>
      <td>1.555000</td>
      <td>4.690000</td>
      <td>0.965000</td>
      <td>2.780000</td>
      <td>673.500000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>3.000000</td>
      <td>13.677500</td>
      <td>3.082500</td>
      <td>2.557500</td>
      <td>21.500000</td>
      <td>107.000000</td>
      <td>2.800000</td>
      <td>2.875000</td>
      <td>0.437500</td>
      <td>1.950000</td>
      <td>6.200000</td>
      <td>1.120000</td>
      <td>3.170000</td>
      <td>985.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>3.000000</td>
      <td>14.830000</td>
      <td>5.800000</td>
      <td>3.230000</td>
      <td>30.000000</td>
      <td>162.000000</td>
      <td>3.880000</td>
      <td>5.080000</td>
      <td>0.660000</td>
      <td>3.580000</td>
      <td>13.000000</td>
      <td>1.710000</td>
      <td>4.000000</td>
      <td>1680.000000</td>
    </tr>
  </tbody>
</table>
</div>



*Podemos corroborar que se cargo correctamente inspeccionando las primeras 10 filas:*


```python
print(wine.head(10))
```

       Class  Alcohol  Malic acid   Ash  Alcalinity of ash  Magnesium  \
    0      1    14.23        1.71  2.43               15.6        127   
    1      1    13.20        1.78  2.14               11.2        100   
    2      1    13.16        2.36  2.67               18.6        101   
    3      1    14.37        1.95  2.50               16.8        113   
    4      1    13.24        2.59  2.87               21.0        118   
    5      1    14.20        1.76  2.45               15.2        112   
    6      1    14.39        1.87  2.45               14.6         96   
    7      1    14.06        2.15  2.61               17.6        121   
    8      1    14.83        1.64  2.17               14.0         97   
    9      1    13.86        1.35  2.27               16.0         98   
    
       Total phenols  Flavanoids  Nonflavanoid phenols  Proanthocyanins  \
    0           2.80        3.06                  0.28             2.29   
    1           2.65        2.76                  0.26             1.28   
    2           2.80        3.24                  0.30             2.81   
    3           3.85        3.49                  0.24             2.18   
    4           2.80        2.69                  0.39             1.82   
    5           3.27        3.39                  0.34             1.97   
    6           2.50        2.52                  0.30             1.98   
    7           2.60        2.51                  0.31             1.25   
    8           2.80        2.98                  0.29             1.98   
    9           2.98        3.15                  0.22             1.85   
    
       Color intensity   Hue  OD280/OD315 of diluted wines  Proline  
    0             5.64  1.04                          3.92     1065  
    1             4.38  1.05                          3.40     1050  
    2             5.68  1.03                          3.17     1185  
    3             7.80  0.86                          3.45     1480  
    4             4.32  1.04                          2.93      735  
    5             6.75  1.05                          2.85     1450  
    6             5.25  1.02                          3.58     1290  
    7             5.05  1.06                          3.58     1295  
    8             5.20  1.08                          2.85     1045  
    9             7.22  1.01                          3.55     1045  
    

*Verificamos que todos los tipos son los correctos:*


```python
print(wine.dtypes)
```

    Class                             int64
    Alcohol                         float64
    Malic acid                      float64
    Ash                             float64
    Alcalinity of ash               float64
    Magnesium                         int64
    Total phenols                   float64
    Flavanoids                      float64
    Nonflavanoid phenols            float64
    Proanthocyanins                 float64
    Color intensity                 float64
    Hue                             float64
    OD280/OD315 of diluted wines    float64
    Proline                           int64
    dtype: object
    

*Obtenemos los minimos y máximos de los datos:*


```python
print("Mínimos:")
print(wine.min())
print("--------------------")
print("Máximos:")
print(wine.max())
```

    Mínimos:
    Class                             1.00
    Alcohol                          11.03
    Malic acid                        0.74
    Ash                               1.36
    Alcalinity of ash                10.60
    Magnesium                        70.00
    Total phenols                     0.98
    Flavanoids                        0.34
    Nonflavanoid phenols              0.13
    Proanthocyanins                   0.41
    Color intensity                   1.28
    Hue                               0.48
    OD280/OD315 of diluted wines      1.27
    Proline                         278.00
    dtype: float64
    --------------------
    Máximos:
    Class                              3.00
    Alcohol                           14.83
    Malic acid                         5.80
    Ash                                3.23
    Alcalinity of ash                 30.00
    Magnesium                        162.00
    Total phenols                      3.88
    Flavanoids                         5.08
    Nonflavanoid phenols               0.66
    Proanthocyanins                    3.58
    Color intensity                   13.00
    Hue                                1.71
    OD280/OD315 of diluted wines       4.00
    Proline                         1680.00
    dtype: float64
    

*Vemos las medias:*


```python
print(wine.mean())
```

    Class                             1.938202
    Alcohol                          13.000618
    Malic acid                        2.336348
    Ash                               2.366517
    Alcalinity of ash                19.494944
    Magnesium                        99.741573
    Total phenols                     2.295112
    Flavanoids                        2.029270
    Nonflavanoid phenols              0.361854
    Proanthocyanins                   1.590899
    Color intensity                   5.058090
    Hue                               0.957449
    OD280/OD315 of diluted wines      2.611685
    Proline                         746.893258
    dtype: float64
    

*Vemos las desviaciones:*


```python
print(wine.std())
```

    Class                             0.775035
    Alcohol                           0.811827
    Malic acid                        1.117146
    Ash                               0.274344
    Alcalinity of ash                 3.339564
    Magnesium                        14.282484
    Total phenols                     0.625851
    Flavanoids                        0.998859
    Nonflavanoid phenols              0.124453
    Proanthocyanins                   0.572359
    Color intensity                   2.318286
    Hue                               0.228572
    OD280/OD315 of diluted wines      0.709990
    Proline                         314.907474
    dtype: float64
    

*Para Normalizaciones y estandarizaciones usaremos librerias de scikit learn, en conjunto a pandas:*


```python
normal = StandardScaler()
estandar = MinMaxScaler()

wineNormal = pd.DataFrame(normal.fit_transform(wine), columns=wine.columns)
wineEstandar = pd.DataFrame(estandar.fit_transform(wine), columns=wine.columns)

# Debemos sobrescribir la columna Class ya que no se deben normalizar sus valores

wineNormal["Class"] = wine["Class"]
wineEstandar["Class"] = wine["Class"]

print("Normalizado:")
print(wineNormal.head(10))
print("----------------------------")
print("Estándar:")
print(wineEstandar.head(10))
```

    Normalizado:
       Class   Alcohol  Malic acid       Ash  Alcalinity of ash  Magnesium  \
    0      1  1.518613   -0.562250  0.232053          -1.169593   1.913905   
    1      1  0.246290   -0.499413 -0.827996          -2.490847   0.018145   
    2      1  0.196879    0.021231  1.109334          -0.268738   0.088358   
    3      1  1.691550   -0.346811  0.487926          -0.809251   0.930918   
    4      1  0.295700    0.227694  1.840403           0.451946   1.281985   
    5      1  1.481555   -0.517367  0.305159          -1.289707   0.860705   
    6      1  1.716255   -0.418624  0.305159          -1.469878  -0.262708   
    7      1  1.308617   -0.167278  0.890014          -0.569023   1.492625   
    8      1  2.259772   -0.625086 -0.718336          -1.650049  -0.192495   
    9      1  1.061565   -0.885409 -0.352802          -1.049479  -0.122282   
    
       Total phenols  Flavanoids  Nonflavanoid phenols  Proanthocyanins  \
    0       0.808997    1.034819             -0.659563         1.224884   
    1       0.568648    0.733629             -0.820719        -0.544721   
    2       0.808997    1.215533             -0.498407         2.135968   
    3       2.491446    1.466525             -0.981875         1.032155   
    4       0.808997    0.663351              0.226796         0.401404   
    5       1.562093    1.366128             -0.176095         0.664217   
    6       0.328298    0.492677             -0.498407         0.681738   
    7       0.488531    0.482637             -0.417829        -0.597284   
    8       0.808997    0.954502             -0.578985         0.681738   
    9       1.097417    1.125176             -1.143031         0.453967   
    
       Color intensity       Hue  OD280/OD315 of diluted wines   Proline  
    0         0.251717  0.362177                      1.847920  1.013009  
    1        -0.293321  0.406051                      1.113449  0.965242  
    2         0.269020  0.318304                      0.788587  1.395148  
    3         1.186068 -0.427544                      1.184071  2.334574  
    4        -0.319276  0.362177                      0.449601 -0.037874  
    5         0.731870  0.406051                      0.336606  2.239039  
    6         0.083015  0.274431                      1.367689  1.729520  
    7        -0.003499  0.449924                      1.367689  1.745442  
    8         0.061386  0.537671                      0.336606  0.949319  
    9         0.935177  0.230557                      1.325316  0.949319  
    ----------------------------
    Estándar:
       Class   Alcohol  Malic acid       Ash  Alcalinity of ash  Magnesium  \
    0      1  0.842105    0.191700  0.572193           0.257732   0.619565   
    1      1  0.571053    0.205534  0.417112           0.030928   0.326087   
    2      1  0.560526    0.320158  0.700535           0.412371   0.336957   
    3      1  0.878947    0.239130  0.609626           0.319588   0.467391   
    4      1  0.581579    0.365613  0.807487           0.536082   0.521739   
    5      1  0.834211    0.201581  0.582888           0.237113   0.456522   
    6      1  0.884211    0.223320  0.582888           0.206186   0.282609   
    7      1  0.797368    0.278656  0.668449           0.360825   0.554348   
    8      1  1.000000    0.177866  0.433155           0.175258   0.293478   
    9      1  0.744737    0.120553  0.486631           0.278351   0.304348   
    
       Total phenols  Flavanoids  Nonflavanoid phenols  Proanthocyanins  \
    0       0.627586    0.573840              0.283019         0.593060   
    1       0.575862    0.510549              0.245283         0.274448   
    2       0.627586    0.611814              0.320755         0.757098   
    3       0.989655    0.664557              0.207547         0.558360   
    4       0.627586    0.495781              0.490566         0.444795   
    5       0.789655    0.643460              0.396226         0.492114   
    6       0.524138    0.459916              0.320755         0.495268   
    7       0.558621    0.457806              0.339623         0.264984   
    8       0.627586    0.556962              0.301887         0.495268   
    9       0.689655    0.592827              0.169811         0.454259   
    
       Color intensity       Hue  OD280/OD315 of diluted wines   Proline  
    0         0.372014  0.455285                      0.970696  0.561341  
    1         0.264505  0.463415                      0.780220  0.550642  
    2         0.375427  0.447154                      0.695971  0.646933  
    3         0.556314  0.308943                      0.798535  0.857347  
    4         0.259386  0.455285                      0.608059  0.325963  
    5         0.466724  0.463415                      0.578755  0.835949  
    6         0.338737  0.439024                      0.846154  0.721826  
    7         0.321672  0.471545                      0.846154  0.725392  
    8         0.334471  0.487805                      0.578755  0.547076  
    9         0.506826  0.430894                      0.835165  0.547076  
    

*Para separar los datos en grupos de datos para entrenar o testear de manera estratificada según la Class, podemos usar scikit:*


```python
wineTrain, wineTest = train_test_split(wine,stratify=wine["Class"], test_size=0.3)
print(wineTest.describe())
```

               Class    Alcohol  Malic acid        Ash  Alcalinity of ash  \
    count  54.000000  54.000000   54.000000  54.000000          54.000000   
    mean    1.944444  12.927222    2.286481   2.328148          19.253704   
    std     0.787081   0.820617    1.009282   0.253504           3.003439   
    min     1.000000  11.030000    0.980000   1.750000          11.400000   
    25%     1.000000  12.337500    1.635000   2.200000          17.425000   
    50%     2.000000  12.945000    1.865000   2.310000          19.500000   
    75%     3.000000  13.505000    2.975000   2.457500          21.000000   
    max     3.000000  14.750000    4.950000   2.870000          26.500000   
    
            Magnesium  Total phenols  Flavanoids  Nonflavanoid phenols  \
    count   54.000000      54.000000   54.000000             54.000000   
    mean    99.185185       2.250370    1.952778              0.377222   
    std     14.849019       0.582765    0.967762              0.130245   
    min     78.000000       1.100000    0.480000              0.130000   
    25%     88.000000       1.812500    0.975000              0.282500   
    50%     95.000000       2.210000    2.020000              0.370000   
    75%    108.000000       2.675000    2.742500              0.477500   
    max    151.000000       3.850000    3.690000              0.660000   
    
           Proanthocyanins  Color intensity        Hue  \
    count        54.000000        54.000000  54.000000   
    mean          1.641481         5.009259   0.937519   
    std           0.582802         2.394423   0.229923   
    min           0.640000         1.280000   0.560000   
    25%           1.350000         2.862500   0.755000   
    50%           1.585000         4.800000   0.925000   
    75%           1.892500         6.200000   1.070000   
    max           3.580000        10.520000   1.710000   
    
           OD280/OD315 of diluted wines      Proline  
    count                     54.000000    54.000000  
    mean                       2.589259   753.629630  
    std                        0.647724   335.677816  
    min                        1.330000   312.000000  
    25%                        1.942500   487.500000  
    50%                        2.775000   675.000000  
    75%                        3.092500  1050.000000  
    max                        3.580000  1480.000000  
    
