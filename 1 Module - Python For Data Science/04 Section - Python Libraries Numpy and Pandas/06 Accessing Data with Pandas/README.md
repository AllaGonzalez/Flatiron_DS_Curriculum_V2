
# Accessing Data within Pandas

## Introduction
In this lesson we're going to dig into various methods for accessing data from our Pandas Series and DataFrames.

## Objectives

You will be able to:
* Understand and explain some key Pandas methods
* Access DataFrame data by using the label
* Perform boolean indexing on both Series and DataFrames
* Use simple selectors for series
* Set new Series and DataFrame inputs

## Importing pandas and the data

First, let's make sure we import `pandas` as `pd`.


```python
import pandas as pd
```

To show how to access data with Pandas, let's use the "wine" data set in the scikit-learn library (you might have heard about this library before - you'll use it extensively when we get to machine learning!). Don't worry about the code below, we're essentially just making sure you have access to the wine data set.

The data contained in the wine data set are the results of a chemical analysis of wines grown in Italy. It contains the quantities of 13 wine constituents. 


```python
from sklearn.datasets import load_wine

data = load_wine()
df = pd.DataFrame(data.data, columns=data.feature_names)
```

Great! Our data set is now stored in the variable `df`. As you know, you can look at its elements by using `df` or `print(df)`.


```python
print(df)
```

         alcohol  malic_acid   ash  alcalinity_of_ash  magnesium  total_phenols  \
    0      14.23        1.71  2.43               15.6      127.0           2.80   
    1      13.20        1.78  2.14               11.2      100.0           2.65   
    2      13.16        2.36  2.67               18.6      101.0           2.80   
    3      14.37        1.95  2.50               16.8      113.0           3.85   
    4      13.24        2.59  2.87               21.0      118.0           2.80   
    5      14.20        1.76  2.45               15.2      112.0           3.27   
    6      14.39        1.87  2.45               14.6       96.0           2.50   
    7      14.06        2.15  2.61               17.6      121.0           2.60   
    8      14.83        1.64  2.17               14.0       97.0           2.80   
    9      13.86        1.35  2.27               16.0       98.0           2.98   
    10     14.10        2.16  2.30               18.0      105.0           2.95   
    11     14.12        1.48  2.32               16.8       95.0           2.20   
    12     13.75        1.73  2.41               16.0       89.0           2.60   
    13     14.75        1.73  2.39               11.4       91.0           3.10   
    14     14.38        1.87  2.38               12.0      102.0           3.30   
    15     13.63        1.81  2.70               17.2      112.0           2.85   
    16     14.30        1.92  2.72               20.0      120.0           2.80   
    17     13.83        1.57  2.62               20.0      115.0           2.95   
    18     14.19        1.59  2.48               16.5      108.0           3.30   
    19     13.64        3.10  2.56               15.2      116.0           2.70   
    20     14.06        1.63  2.28               16.0      126.0           3.00   
    21     12.93        3.80  2.65               18.6      102.0           2.41   
    22     13.71        1.86  2.36               16.6      101.0           2.61   
    23     12.85        1.60  2.52               17.8       95.0           2.48   
    24     13.50        1.81  2.61               20.0       96.0           2.53   
    25     13.05        2.05  3.22               25.0      124.0           2.63   
    26     13.39        1.77  2.62               16.1       93.0           2.85   
    27     13.30        1.72  2.14               17.0       94.0           2.40   
    28     13.87        1.90  2.80               19.4      107.0           2.95   
    29     14.02        1.68  2.21               16.0       96.0           2.65   
    ..       ...         ...   ...                ...        ...            ...   
    148    13.32        3.24  2.38               21.5       92.0           1.93   
    149    13.08        3.90  2.36               21.5      113.0           1.41   
    150    13.50        3.12  2.62               24.0      123.0           1.40   
    151    12.79        2.67  2.48               22.0      112.0           1.48   
    152    13.11        1.90  2.75               25.5      116.0           2.20   
    153    13.23        3.30  2.28               18.5       98.0           1.80   
    154    12.58        1.29  2.10               20.0      103.0           1.48   
    155    13.17        5.19  2.32               22.0       93.0           1.74   
    156    13.84        4.12  2.38               19.5       89.0           1.80   
    157    12.45        3.03  2.64               27.0       97.0           1.90   
    158    14.34        1.68  2.70               25.0       98.0           2.80   
    159    13.48        1.67  2.64               22.5       89.0           2.60   
    160    12.36        3.83  2.38               21.0       88.0           2.30   
    161    13.69        3.26  2.54               20.0      107.0           1.83   
    162    12.85        3.27  2.58               22.0      106.0           1.65   
    163    12.96        3.45  2.35               18.5      106.0           1.39   
    164    13.78        2.76  2.30               22.0       90.0           1.35   
    165    13.73        4.36  2.26               22.5       88.0           1.28   
    166    13.45        3.70  2.60               23.0      111.0           1.70   
    167    12.82        3.37  2.30               19.5       88.0           1.48   
    168    13.58        2.58  2.69               24.5      105.0           1.55   
    169    13.40        4.60  2.86               25.0      112.0           1.98   
    170    12.20        3.03  2.32               19.0       96.0           1.25   
    171    12.77        2.39  2.28               19.5       86.0           1.39   
    172    14.16        2.51  2.48               20.0       91.0           1.68   
    173    13.71        5.65  2.45               20.5       95.0           1.68   
    174    13.40        3.91  2.48               23.0      102.0           1.80   
    175    13.27        4.28  2.26               20.0      120.0           1.59   
    176    13.17        2.59  2.37               20.0      120.0           1.65   
    177    14.13        4.10  2.74               24.5       96.0           2.05   
    
         flavanoids  nonflavanoid_phenols  proanthocyanins  color_intensity   hue  \
    0          3.06                  0.28             2.29         5.640000  1.04   
    1          2.76                  0.26             1.28         4.380000  1.05   
    2          3.24                  0.30             2.81         5.680000  1.03   
    3          3.49                  0.24             2.18         7.800000  0.86   
    4          2.69                  0.39             1.82         4.320000  1.04   
    5          3.39                  0.34             1.97         6.750000  1.05   
    6          2.52                  0.30             1.98         5.250000  1.02   
    7          2.51                  0.31             1.25         5.050000  1.06   
    8          2.98                  0.29             1.98         5.200000  1.08   
    9          3.15                  0.22             1.85         7.220000  1.01   
    10         3.32                  0.22             2.38         5.750000  1.25   
    11         2.43                  0.26             1.57         5.000000  1.17   
    12         2.76                  0.29             1.81         5.600000  1.15   
    13         3.69                  0.43             2.81         5.400000  1.25   
    14         3.64                  0.29             2.96         7.500000  1.20   
    15         2.91                  0.30             1.46         7.300000  1.28   
    16         3.14                  0.33             1.97         6.200000  1.07   
    17         3.40                  0.40             1.72         6.600000  1.13   
    18         3.93                  0.32             1.86         8.700000  1.23   
    19         3.03                  0.17             1.66         5.100000  0.96   
    20         3.17                  0.24             2.10         5.650000  1.09   
    21         2.41                  0.25             1.98         4.500000  1.03   
    22         2.88                  0.27             1.69         3.800000  1.11   
    23         2.37                  0.26             1.46         3.930000  1.09   
    24         2.61                  0.28             1.66         3.520000  1.12   
    25         2.68                  0.47             1.92         3.580000  1.13   
    26         2.94                  0.34             1.45         4.800000  0.92   
    27         2.19                  0.27             1.35         3.950000  1.02   
    28         2.97                  0.37             1.76         4.500000  1.25   
    29         2.33                  0.26             1.98         4.700000  1.04   
    ..          ...                   ...              ...              ...   ...   
    148        0.76                  0.45             1.25         8.420000  0.55   
    149        1.39                  0.34             1.14         9.400000  0.57   
    150        1.57                  0.22             1.25         8.600000  0.59   
    151        1.36                  0.24             1.26        10.800000  0.48   
    152        1.28                  0.26             1.56         7.100000  0.61   
    153        0.83                  0.61             1.87        10.520000  0.56   
    154        0.58                  0.53             1.40         7.600000  0.58   
    155        0.63                  0.61             1.55         7.900000  0.60   
    156        0.83                  0.48             1.56         9.010000  0.57   
    157        0.58                  0.63             1.14         7.500000  0.67   
    158        1.31                  0.53             2.70        13.000000  0.57   
    159        1.10                  0.52             2.29        11.750000  0.57   
    160        0.92                  0.50             1.04         7.650000  0.56   
    161        0.56                  0.50             0.80         5.880000  0.96   
    162        0.60                  0.60             0.96         5.580000  0.87   
    163        0.70                  0.40             0.94         5.280000  0.68   
    164        0.68                  0.41             1.03         9.580000  0.70   
    165        0.47                  0.52             1.15         6.620000  0.78   
    166        0.92                  0.43             1.46        10.680000  0.85   
    167        0.66                  0.40             0.97        10.260000  0.72   
    168        0.84                  0.39             1.54         8.660000  0.74   
    169        0.96                  0.27             1.11         8.500000  0.67   
    170        0.49                  0.40             0.73         5.500000  0.66   
    171        0.51                  0.48             0.64         9.899999  0.57   
    172        0.70                  0.44             1.24         9.700000  0.62   
    173        0.61                  0.52             1.06         7.700000  0.64   
    174        0.75                  0.43             1.41         7.300000  0.70   
    175        0.69                  0.43             1.35        10.200000  0.59   
    176        0.68                  0.53             1.46         9.300000  0.60   
    177        0.76                  0.56             1.35         9.200000  0.61   
    
         od280/od315_of_diluted_wines  proline  
    0                            3.92   1065.0  
    1                            3.40   1050.0  
    2                            3.17   1185.0  
    3                            3.45   1480.0  
    4                            2.93    735.0  
    5                            2.85   1450.0  
    6                            3.58   1290.0  
    7                            3.58   1295.0  
    8                            2.85   1045.0  
    9                            3.55   1045.0  
    10                           3.17   1510.0  
    11                           2.82   1280.0  
    12                           2.90   1320.0  
    13                           2.73   1150.0  
    14                           3.00   1547.0  
    15                           2.88   1310.0  
    16                           2.65   1280.0  
    17                           2.57   1130.0  
    18                           2.82   1680.0  
    19                           3.36    845.0  
    20                           3.71    780.0  
    21                           3.52    770.0  
    22                           4.00   1035.0  
    23                           3.63   1015.0  
    24                           3.82    845.0  
    25                           3.20    830.0  
    26                           3.22   1195.0  
    27                           2.77   1285.0  
    28                           3.40    915.0  
    29                           3.59   1035.0  
    ..                            ...      ...  
    148                          1.62    650.0  
    149                          1.33    550.0  
    150                          1.30    500.0  
    151                          1.47    480.0  
    152                          1.33    425.0  
    153                          1.51    675.0  
    154                          1.55    640.0  
    155                          1.48    725.0  
    156                          1.64    480.0  
    157                          1.73    880.0  
    158                          1.96    660.0  
    159                          1.78    620.0  
    160                          1.58    520.0  
    161                          1.82    680.0  
    162                          2.11    570.0  
    163                          1.75    675.0  
    164                          1.68    615.0  
    165                          1.75    520.0  
    166                          1.56    695.0  
    167                          1.75    685.0  
    168                          1.80    750.0  
    169                          1.92    630.0  
    170                          1.83    510.0  
    171                          1.63    470.0  
    172                          1.71    660.0  
    173                          1.74    740.0  
    174                          1.56    750.0  
    175                          1.56    835.0  
    176                          1.62    840.0  
    177                          1.60    560.0  
    
    [178 rows x 13 columns]


Now what if you only want to see only a few lines of the data, based on certain constraints? You'll learn how to access data in this lesson!

## Methods and attributes to access data information

It won't be a surprise that our `df` object is a pandas DataFrame object. Let's verify this using the `type()`-function


```python
type(df)
```




    pandas.core.frame.DataFrame



There are some methods and attributes associated with pandas objects (both DataFrames *and* series!) which make retrieving information from the data particularly easy. Some commonly used methods:
- `.head()`
- `.tail()`

And attributes:
- `.index`
- `.columns`
- `.dtypes`
- `.shape`

### Some methods: `.head()`, `.tail()` and `.info()`

By using `.head()` and `.tail()`, you can select the first $n$ rows from your dataframe. The default $n$ is 5, but you can change this value inside the parentheses. For example:


```python
# First 5 rows of df
df.head()
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
      <th>alcohol</th>
      <th>malic_acid</th>
      <th>ash</th>
      <th>alcalinity_of_ash</th>
      <th>magnesium</th>
      <th>total_phenols</th>
      <th>flavanoids</th>
      <th>nonflavanoid_phenols</th>
      <th>proanthocyanins</th>
      <th>color_intensity</th>
      <th>hue</th>
      <th>od280/od315_of_diluted_wines</th>
      <th>proline</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>14.23</td>
      <td>1.71</td>
      <td>2.43</td>
      <td>15.6</td>
      <td>127.0</td>
      <td>2.80</td>
      <td>3.06</td>
      <td>0.28</td>
      <td>2.29</td>
      <td>5.64</td>
      <td>1.04</td>
      <td>3.92</td>
      <td>1065.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>13.20</td>
      <td>1.78</td>
      <td>2.14</td>
      <td>11.2</td>
      <td>100.0</td>
      <td>2.65</td>
      <td>2.76</td>
      <td>0.26</td>
      <td>1.28</td>
      <td>4.38</td>
      <td>1.05</td>
      <td>3.40</td>
      <td>1050.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13.16</td>
      <td>2.36</td>
      <td>2.67</td>
      <td>18.6</td>
      <td>101.0</td>
      <td>2.80</td>
      <td>3.24</td>
      <td>0.30</td>
      <td>2.81</td>
      <td>5.68</td>
      <td>1.03</td>
      <td>3.17</td>
      <td>1185.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>14.37</td>
      <td>1.95</td>
      <td>2.50</td>
      <td>16.8</td>
      <td>113.0</td>
      <td>3.85</td>
      <td>3.49</td>
      <td>0.24</td>
      <td>2.18</td>
      <td>7.80</td>
      <td>0.86</td>
      <td>3.45</td>
      <td>1480.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>13.24</td>
      <td>2.59</td>
      <td>2.87</td>
      <td>21.0</td>
      <td>118.0</td>
      <td>2.80</td>
      <td>2.69</td>
      <td>0.39</td>
      <td>1.82</td>
      <td>4.32</td>
      <td>1.04</td>
      <td>2.93</td>
      <td>735.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# last 3 rows of df
df.tail(3)
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
      <th>alcohol</th>
      <th>malic_acid</th>
      <th>ash</th>
      <th>alcalinity_of_ash</th>
      <th>magnesium</th>
      <th>total_phenols</th>
      <th>flavanoids</th>
      <th>nonflavanoid_phenols</th>
      <th>proanthocyanins</th>
      <th>color_intensity</th>
      <th>hue</th>
      <th>od280/od315_of_diluted_wines</th>
      <th>proline</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>175</th>
      <td>13.27</td>
      <td>4.28</td>
      <td>2.26</td>
      <td>20.0</td>
      <td>120.0</td>
      <td>1.59</td>
      <td>0.69</td>
      <td>0.43</td>
      <td>1.35</td>
      <td>10.2</td>
      <td>0.59</td>
      <td>1.56</td>
      <td>835.0</td>
    </tr>
    <tr>
      <th>176</th>
      <td>13.17</td>
      <td>2.59</td>
      <td>2.37</td>
      <td>20.0</td>
      <td>120.0</td>
      <td>1.65</td>
      <td>0.68</td>
      <td>0.53</td>
      <td>1.46</td>
      <td>9.3</td>
      <td>0.60</td>
      <td>1.62</td>
      <td>840.0</td>
    </tr>
    <tr>
      <th>177</th>
      <td>14.13</td>
      <td>4.10</td>
      <td>2.74</td>
      <td>24.5</td>
      <td>96.0</td>
      <td>2.05</td>
      <td>0.76</td>
      <td>0.56</td>
      <td>1.35</td>
      <td>9.2</td>
      <td>0.61</td>
      <td>1.60</td>
      <td>560.0</td>
    </tr>
  </tbody>
</table>
</div>



To get a concise summary of the dataframe you can use `.info()`


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 178 entries, 0 to 177
    Data columns (total 13 columns):
    alcohol                         178 non-null float64
    malic_acid                      178 non-null float64
    ash                             178 non-null float64
    alcalinity_of_ash               178 non-null float64
    magnesium                       178 non-null float64
    total_phenols                   178 non-null float64
    flavanoids                      178 non-null float64
    nonflavanoid_phenols            178 non-null float64
    proanthocyanins                 178 non-null float64
    color_intensity                 178 non-null float64
    hue                             178 non-null float64
    od280/od315_of_diluted_wines    178 non-null float64
    proline                         178 non-null float64
    dtypes: float64(13)
    memory usage: 18.2 KB


### Some attributes

Using `.index` you can access the index or row labels of the DataFrame.


```python
df.index
```




    RangeIndex(start=0, stop=178, step=1)



Using `.columns`, you can access the column labels of the DataFrame.


```python
df.columns
```




    Index(['alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium',
           'total_phenols', 'flavanoids', 'nonflavanoid_phenols',
           'proanthocyanins', 'color_intensity', 'hue',
           'od280/od315_of_diluted_wines', 'proline'],
          dtype='object')



Using `.dtypes` returns the dtypes in the DataFrame (compare with `.info()!)


```python
df.dtypes
```




    alcohol                         float64
    malic_acid                      float64
    ash                             float64
    alcalinity_of_ash               float64
    magnesium                       float64
    total_phenols                   float64
    flavanoids                      float64
    nonflavanoid_phenols            float64
    proanthocyanins                 float64
    color_intensity                 float64
    hue                             float64
    od280/od315_of_diluted_wines    float64
    proline                         float64
    dtype: object



`.shape` returns a tuple representing the dimensionality  (in `(rows,columns)` ) of the DataFrame.


```python
df.shape
```




    (178, 13)



## Selecting dataframe information

In the previous section, we deliberately omitted 2 very important attributes:
- `.iloc`, which is a pandas dataframe indexer used for integer-location based indexing / selection by position.
- `.loc`, which has 2 use cases:
       - Selecting by label / index
       - Selecting with a boolean / conditional lookup


### `.iloc`

You can use `.iloc` to select single rows. To select the 4th row, you can use `.iloc[3]` like:


```python
df.iloc[3]
```




    alcohol                           14.37
    malic_acid                         1.95
    ash                                2.50
    alcalinity_of_ash                 16.80
    magnesium                        113.00
    total_phenols                      3.85
    flavanoids                         3.49
    nonflavanoid_phenols               0.24
    proanthocyanins                    2.18
    color_intensity                    7.80
    hue                                0.86
    od280/od315_of_diluted_wines       3.45
    proline                         1480.00
    Name: 3, dtype: float64



You can use a colon to select several rows. Note that you'll use a structure `.iloc[a:b]` where the row with index `a` will be included in the selection and the row with index `b` is excluded.


```python
df.iloc[5:8]
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
      <th>alcohol</th>
      <th>malic_acid</th>
      <th>ash</th>
      <th>alcalinity_of_ash</th>
      <th>magnesium</th>
      <th>total_phenols</th>
      <th>flavanoids</th>
      <th>nonflavanoid_phenols</th>
      <th>proanthocyanins</th>
      <th>color_intensity</th>
      <th>hue</th>
      <th>od280/od315_of_diluted_wines</th>
      <th>proline</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>14.20</td>
      <td>1.76</td>
      <td>2.45</td>
      <td>15.2</td>
      <td>112.0</td>
      <td>3.27</td>
      <td>3.39</td>
      <td>0.34</td>
      <td>1.97</td>
      <td>6.75</td>
      <td>1.05</td>
      <td>2.85</td>
      <td>1450.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>14.39</td>
      <td>1.87</td>
      <td>2.45</td>
      <td>14.6</td>
      <td>96.0</td>
      <td>2.50</td>
      <td>2.52</td>
      <td>0.30</td>
      <td>1.98</td>
      <td>5.25</td>
      <td>1.02</td>
      <td>3.58</td>
      <td>1290.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>14.06</td>
      <td>2.15</td>
      <td>2.61</td>
      <td>17.6</td>
      <td>121.0</td>
      <td>2.60</td>
      <td>2.51</td>
      <td>0.31</td>
      <td>1.25</td>
      <td>5.05</td>
      <td>1.06</td>
      <td>3.58</td>
      <td>1295.0</td>
    </tr>
  </tbody>
</table>
</div>



Next, you can use `,` to perform *column* selections based on their index as well. The command below selects full columns 3-6:


```python
df.iloc[:,3:7]
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
      <th>alcalinity_of_ash</th>
      <th>magnesium</th>
      <th>total_phenols</th>
      <th>flavanoids</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15.6</td>
      <td>127.0</td>
      <td>2.80</td>
      <td>3.06</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11.2</td>
      <td>100.0</td>
      <td>2.65</td>
      <td>2.76</td>
    </tr>
    <tr>
      <th>2</th>
      <td>18.6</td>
      <td>101.0</td>
      <td>2.80</td>
      <td>3.24</td>
    </tr>
    <tr>
      <th>3</th>
      <td>16.8</td>
      <td>113.0</td>
      <td>3.85</td>
      <td>3.49</td>
    </tr>
    <tr>
      <th>4</th>
      <td>21.0</td>
      <td>118.0</td>
      <td>2.80</td>
      <td>2.69</td>
    </tr>
    <tr>
      <th>5</th>
      <td>15.2</td>
      <td>112.0</td>
      <td>3.27</td>
      <td>3.39</td>
    </tr>
    <tr>
      <th>6</th>
      <td>14.6</td>
      <td>96.0</td>
      <td>2.50</td>
      <td>2.52</td>
    </tr>
    <tr>
      <th>7</th>
      <td>17.6</td>
      <td>121.0</td>
      <td>2.60</td>
      <td>2.51</td>
    </tr>
    <tr>
      <th>8</th>
      <td>14.0</td>
      <td>97.0</td>
      <td>2.80</td>
      <td>2.98</td>
    </tr>
    <tr>
      <th>9</th>
      <td>16.0</td>
      <td>98.0</td>
      <td>2.98</td>
      <td>3.15</td>
    </tr>
    <tr>
      <th>10</th>
      <td>18.0</td>
      <td>105.0</td>
      <td>2.95</td>
      <td>3.32</td>
    </tr>
    <tr>
      <th>11</th>
      <td>16.8</td>
      <td>95.0</td>
      <td>2.20</td>
      <td>2.43</td>
    </tr>
    <tr>
      <th>12</th>
      <td>16.0</td>
      <td>89.0</td>
      <td>2.60</td>
      <td>2.76</td>
    </tr>
    <tr>
      <th>13</th>
      <td>11.4</td>
      <td>91.0</td>
      <td>3.10</td>
      <td>3.69</td>
    </tr>
    <tr>
      <th>14</th>
      <td>12.0</td>
      <td>102.0</td>
      <td>3.30</td>
      <td>3.64</td>
    </tr>
    <tr>
      <th>15</th>
      <td>17.2</td>
      <td>112.0</td>
      <td>2.85</td>
      <td>2.91</td>
    </tr>
    <tr>
      <th>16</th>
      <td>20.0</td>
      <td>120.0</td>
      <td>2.80</td>
      <td>3.14</td>
    </tr>
    <tr>
      <th>17</th>
      <td>20.0</td>
      <td>115.0</td>
      <td>2.95</td>
      <td>3.40</td>
    </tr>
    <tr>
      <th>18</th>
      <td>16.5</td>
      <td>108.0</td>
      <td>3.30</td>
      <td>3.93</td>
    </tr>
    <tr>
      <th>19</th>
      <td>15.2</td>
      <td>116.0</td>
      <td>2.70</td>
      <td>3.03</td>
    </tr>
    <tr>
      <th>20</th>
      <td>16.0</td>
      <td>126.0</td>
      <td>3.00</td>
      <td>3.17</td>
    </tr>
    <tr>
      <th>21</th>
      <td>18.6</td>
      <td>102.0</td>
      <td>2.41</td>
      <td>2.41</td>
    </tr>
    <tr>
      <th>22</th>
      <td>16.6</td>
      <td>101.0</td>
      <td>2.61</td>
      <td>2.88</td>
    </tr>
    <tr>
      <th>23</th>
      <td>17.8</td>
      <td>95.0</td>
      <td>2.48</td>
      <td>2.37</td>
    </tr>
    <tr>
      <th>24</th>
      <td>20.0</td>
      <td>96.0</td>
      <td>2.53</td>
      <td>2.61</td>
    </tr>
    <tr>
      <th>25</th>
      <td>25.0</td>
      <td>124.0</td>
      <td>2.63</td>
      <td>2.68</td>
    </tr>
    <tr>
      <th>26</th>
      <td>16.1</td>
      <td>93.0</td>
      <td>2.85</td>
      <td>2.94</td>
    </tr>
    <tr>
      <th>27</th>
      <td>17.0</td>
      <td>94.0</td>
      <td>2.40</td>
      <td>2.19</td>
    </tr>
    <tr>
      <th>28</th>
      <td>19.4</td>
      <td>107.0</td>
      <td>2.95</td>
      <td>2.97</td>
    </tr>
    <tr>
      <th>29</th>
      <td>16.0</td>
      <td>96.0</td>
      <td>2.65</td>
      <td>2.33</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>148</th>
      <td>21.5</td>
      <td>92.0</td>
      <td>1.93</td>
      <td>0.76</td>
    </tr>
    <tr>
      <th>149</th>
      <td>21.5</td>
      <td>113.0</td>
      <td>1.41</td>
      <td>1.39</td>
    </tr>
    <tr>
      <th>150</th>
      <td>24.0</td>
      <td>123.0</td>
      <td>1.40</td>
      <td>1.57</td>
    </tr>
    <tr>
      <th>151</th>
      <td>22.0</td>
      <td>112.0</td>
      <td>1.48</td>
      <td>1.36</td>
    </tr>
    <tr>
      <th>152</th>
      <td>25.5</td>
      <td>116.0</td>
      <td>2.20</td>
      <td>1.28</td>
    </tr>
    <tr>
      <th>153</th>
      <td>18.5</td>
      <td>98.0</td>
      <td>1.80</td>
      <td>0.83</td>
    </tr>
    <tr>
      <th>154</th>
      <td>20.0</td>
      <td>103.0</td>
      <td>1.48</td>
      <td>0.58</td>
    </tr>
    <tr>
      <th>155</th>
      <td>22.0</td>
      <td>93.0</td>
      <td>1.74</td>
      <td>0.63</td>
    </tr>
    <tr>
      <th>156</th>
      <td>19.5</td>
      <td>89.0</td>
      <td>1.80</td>
      <td>0.83</td>
    </tr>
    <tr>
      <th>157</th>
      <td>27.0</td>
      <td>97.0</td>
      <td>1.90</td>
      <td>0.58</td>
    </tr>
    <tr>
      <th>158</th>
      <td>25.0</td>
      <td>98.0</td>
      <td>2.80</td>
      <td>1.31</td>
    </tr>
    <tr>
      <th>159</th>
      <td>22.5</td>
      <td>89.0</td>
      <td>2.60</td>
      <td>1.10</td>
    </tr>
    <tr>
      <th>160</th>
      <td>21.0</td>
      <td>88.0</td>
      <td>2.30</td>
      <td>0.92</td>
    </tr>
    <tr>
      <th>161</th>
      <td>20.0</td>
      <td>107.0</td>
      <td>1.83</td>
      <td>0.56</td>
    </tr>
    <tr>
      <th>162</th>
      <td>22.0</td>
      <td>106.0</td>
      <td>1.65</td>
      <td>0.60</td>
    </tr>
    <tr>
      <th>163</th>
      <td>18.5</td>
      <td>106.0</td>
      <td>1.39</td>
      <td>0.70</td>
    </tr>
    <tr>
      <th>164</th>
      <td>22.0</td>
      <td>90.0</td>
      <td>1.35</td>
      <td>0.68</td>
    </tr>
    <tr>
      <th>165</th>
      <td>22.5</td>
      <td>88.0</td>
      <td>1.28</td>
      <td>0.47</td>
    </tr>
    <tr>
      <th>166</th>
      <td>23.0</td>
      <td>111.0</td>
      <td>1.70</td>
      <td>0.92</td>
    </tr>
    <tr>
      <th>167</th>
      <td>19.5</td>
      <td>88.0</td>
      <td>1.48</td>
      <td>0.66</td>
    </tr>
    <tr>
      <th>168</th>
      <td>24.5</td>
      <td>105.0</td>
      <td>1.55</td>
      <td>0.84</td>
    </tr>
    <tr>
      <th>169</th>
      <td>25.0</td>
      <td>112.0</td>
      <td>1.98</td>
      <td>0.96</td>
    </tr>
    <tr>
      <th>170</th>
      <td>19.0</td>
      <td>96.0</td>
      <td>1.25</td>
      <td>0.49</td>
    </tr>
    <tr>
      <th>171</th>
      <td>19.5</td>
      <td>86.0</td>
      <td>1.39</td>
      <td>0.51</td>
    </tr>
    <tr>
      <th>172</th>
      <td>20.0</td>
      <td>91.0</td>
      <td>1.68</td>
      <td>0.70</td>
    </tr>
    <tr>
      <th>173</th>
      <td>20.5</td>
      <td>95.0</td>
      <td>1.68</td>
      <td>0.61</td>
    </tr>
    <tr>
      <th>174</th>
      <td>23.0</td>
      <td>102.0</td>
      <td>1.80</td>
      <td>0.75</td>
    </tr>
    <tr>
      <th>175</th>
      <td>20.0</td>
      <td>120.0</td>
      <td>1.59</td>
      <td>0.69</td>
    </tr>
    <tr>
      <th>176</th>
      <td>20.0</td>
      <td>120.0</td>
      <td>1.65</td>
      <td>0.68</td>
    </tr>
    <tr>
      <th>177</th>
      <td>24.5</td>
      <td>96.0</td>
      <td>2.05</td>
      <td>0.76</td>
    </tr>
  </tbody>
</table>
<p>178 rows × 4 columns</p>
</div>



Last but not least, you can perform column and row selections at once:


```python
df.iloc[5:10,3:9]
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
      <th>alcalinity_of_ash</th>
      <th>magnesium</th>
      <th>total_phenols</th>
      <th>flavanoids</th>
      <th>nonflavanoid_phenols</th>
      <th>proanthocyanins</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>15.2</td>
      <td>112.0</td>
      <td>3.27</td>
      <td>3.39</td>
      <td>0.34</td>
      <td>1.97</td>
    </tr>
    <tr>
      <th>6</th>
      <td>14.6</td>
      <td>96.0</td>
      <td>2.50</td>
      <td>2.52</td>
      <td>0.30</td>
      <td>1.98</td>
    </tr>
    <tr>
      <th>7</th>
      <td>17.6</td>
      <td>121.0</td>
      <td>2.60</td>
      <td>2.51</td>
      <td>0.31</td>
      <td>1.25</td>
    </tr>
    <tr>
      <th>8</th>
      <td>14.0</td>
      <td>97.0</td>
      <td>2.80</td>
      <td>2.98</td>
      <td>0.29</td>
      <td>1.98</td>
    </tr>
    <tr>
      <th>9</th>
      <td>16.0</td>
      <td>98.0</td>
      <td>2.98</td>
      <td>3.15</td>
      <td>0.22</td>
      <td>1.85</td>
    </tr>
  </tbody>
</table>
</div>



### `.loc`

 #### a) `.loc` label-based indexing

You can `.loc` to select columns based on their (row index and) column name. Examples:


```python
df.loc[:,"magnesium"]
```




    0      127.0
    1      100.0
    2      101.0
    3      113.0
    4      118.0
    5      112.0
    6       96.0
    7      121.0
    8       97.0
    9       98.0
    10     105.0
    11      95.0
    12      89.0
    13      91.0
    14     102.0
    15     112.0
    16     120.0
    17     115.0
    18     108.0
    19     116.0
    20     126.0
    21     102.0
    22     101.0
    23      95.0
    24      96.0
    25     124.0
    26      93.0
    27      94.0
    28     107.0
    29      96.0
           ...  
    148     92.0
    149    113.0
    150    123.0
    151    112.0
    152    116.0
    153     98.0
    154    103.0
    155     93.0
    156     89.0
    157     97.0
    158     98.0
    159     89.0
    160     88.0
    161    107.0
    162    106.0
    163    106.0
    164     90.0
    165     88.0
    166    111.0
    167     88.0
    168    105.0
    169    112.0
    170     96.0
    171     86.0
    172     91.0
    173     95.0
    174    102.0
    175    120.0
    176    120.0
    177     96.0
    Name: magnesium, Length: 178, dtype: float64



An alternative method here is simply calling `df["magnesium"]`!


```python
df.loc[7:16,"magnesium"]
```




    7     121.0
    8      97.0
    9      98.0
    10    105.0
    11     95.0
    12     89.0
    13     91.0
    14    102.0
    15    112.0
    16    120.0
    Name: magnesium, dtype: float64



#### b) boolean indexing using `.loc`

Sometimes you'd like to select certain rows in your data set based on the value for a certain variable. Imagine you'd like to create a new dataframe that only contains the wines with an alcohol percentage below 12. This can be done as follows:


```python
df.loc[df["alcohol"]<12]
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
      <th>alcohol</th>
      <th>malic_acid</th>
      <th>ash</th>
      <th>alcalinity_of_ash</th>
      <th>magnesium</th>
      <th>total_phenols</th>
      <th>flavanoids</th>
      <th>nonflavanoid_phenols</th>
      <th>proanthocyanins</th>
      <th>color_intensity</th>
      <th>hue</th>
      <th>od280/od315_of_diluted_wines</th>
      <th>proline</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>74</th>
      <td>11.96</td>
      <td>1.09</td>
      <td>2.30</td>
      <td>21.0</td>
      <td>101.0</td>
      <td>3.38</td>
      <td>2.14</td>
      <td>0.13</td>
      <td>1.65</td>
      <td>3.21</td>
      <td>0.99</td>
      <td>3.13</td>
      <td>886.0</td>
    </tr>
    <tr>
      <th>75</th>
      <td>11.66</td>
      <td>1.88</td>
      <td>1.92</td>
      <td>16.0</td>
      <td>97.0</td>
      <td>1.61</td>
      <td>1.57</td>
      <td>0.34</td>
      <td>1.15</td>
      <td>3.80</td>
      <td>1.23</td>
      <td>2.14</td>
      <td>428.0</td>
    </tr>
    <tr>
      <th>77</th>
      <td>11.84</td>
      <td>2.89</td>
      <td>2.23</td>
      <td>18.0</td>
      <td>112.0</td>
      <td>1.72</td>
      <td>1.32</td>
      <td>0.43</td>
      <td>0.95</td>
      <td>2.65</td>
      <td>0.96</td>
      <td>2.52</td>
      <td>500.0</td>
    </tr>
    <tr>
      <th>84</th>
      <td>11.84</td>
      <td>0.89</td>
      <td>2.58</td>
      <td>18.0</td>
      <td>94.0</td>
      <td>2.20</td>
      <td>2.21</td>
      <td>0.22</td>
      <td>2.35</td>
      <td>3.05</td>
      <td>0.79</td>
      <td>3.08</td>
      <td>520.0</td>
    </tr>
    <tr>
      <th>87</th>
      <td>11.65</td>
      <td>1.67</td>
      <td>2.62</td>
      <td>26.0</td>
      <td>88.0</td>
      <td>1.92</td>
      <td>1.61</td>
      <td>0.40</td>
      <td>1.34</td>
      <td>2.60</td>
      <td>1.36</td>
      <td>3.21</td>
      <td>562.0</td>
    </tr>
    <tr>
      <th>88</th>
      <td>11.64</td>
      <td>2.06</td>
      <td>2.46</td>
      <td>21.6</td>
      <td>84.0</td>
      <td>1.95</td>
      <td>1.69</td>
      <td>0.48</td>
      <td>1.35</td>
      <td>2.80</td>
      <td>1.00</td>
      <td>2.75</td>
      <td>680.0</td>
    </tr>
    <tr>
      <th>94</th>
      <td>11.62</td>
      <td>1.99</td>
      <td>2.28</td>
      <td>18.0</td>
      <td>98.0</td>
      <td>3.02</td>
      <td>2.26</td>
      <td>0.17</td>
      <td>1.35</td>
      <td>3.25</td>
      <td>1.16</td>
      <td>2.96</td>
      <td>345.0</td>
    </tr>
    <tr>
      <th>96</th>
      <td>11.81</td>
      <td>2.12</td>
      <td>2.74</td>
      <td>21.5</td>
      <td>134.0</td>
      <td>1.60</td>
      <td>0.99</td>
      <td>0.14</td>
      <td>1.56</td>
      <td>2.50</td>
      <td>0.95</td>
      <td>2.26</td>
      <td>625.0</td>
    </tr>
    <tr>
      <th>103</th>
      <td>11.82</td>
      <td>1.72</td>
      <td>1.88</td>
      <td>19.5</td>
      <td>86.0</td>
      <td>2.50</td>
      <td>1.64</td>
      <td>0.37</td>
      <td>1.42</td>
      <td>2.06</td>
      <td>0.94</td>
      <td>2.44</td>
      <td>415.0</td>
    </tr>
    <tr>
      <th>109</th>
      <td>11.61</td>
      <td>1.35</td>
      <td>2.70</td>
      <td>20.0</td>
      <td>94.0</td>
      <td>2.74</td>
      <td>2.92</td>
      <td>0.29</td>
      <td>2.49</td>
      <td>2.65</td>
      <td>0.96</td>
      <td>3.26</td>
      <td>680.0</td>
    </tr>
    <tr>
      <th>110</th>
      <td>11.46</td>
      <td>3.74</td>
      <td>1.82</td>
      <td>19.5</td>
      <td>107.0</td>
      <td>3.18</td>
      <td>2.58</td>
      <td>0.24</td>
      <td>3.58</td>
      <td>2.90</td>
      <td>0.75</td>
      <td>2.81</td>
      <td>562.0</td>
    </tr>
    <tr>
      <th>112</th>
      <td>11.76</td>
      <td>2.68</td>
      <td>2.92</td>
      <td>20.0</td>
      <td>103.0</td>
      <td>1.75</td>
      <td>2.03</td>
      <td>0.60</td>
      <td>1.05</td>
      <td>3.80</td>
      <td>1.23</td>
      <td>2.50</td>
      <td>607.0</td>
    </tr>
    <tr>
      <th>113</th>
      <td>11.41</td>
      <td>0.74</td>
      <td>2.50</td>
      <td>21.0</td>
      <td>88.0</td>
      <td>2.48</td>
      <td>2.01</td>
      <td>0.42</td>
      <td>1.44</td>
      <td>3.08</td>
      <td>1.10</td>
      <td>2.31</td>
      <td>434.0</td>
    </tr>
    <tr>
      <th>115</th>
      <td>11.03</td>
      <td>1.51</td>
      <td>2.20</td>
      <td>21.5</td>
      <td>85.0</td>
      <td>2.46</td>
      <td>2.17</td>
      <td>0.52</td>
      <td>2.01</td>
      <td>1.90</td>
      <td>1.71</td>
      <td>2.87</td>
      <td>407.0</td>
    </tr>
    <tr>
      <th>116</th>
      <td>11.82</td>
      <td>1.47</td>
      <td>1.99</td>
      <td>20.8</td>
      <td>86.0</td>
      <td>1.98</td>
      <td>1.60</td>
      <td>0.30</td>
      <td>1.53</td>
      <td>1.95</td>
      <td>0.95</td>
      <td>3.33</td>
      <td>495.0</td>
    </tr>
    <tr>
      <th>120</th>
      <td>11.45</td>
      <td>2.40</td>
      <td>2.42</td>
      <td>20.0</td>
      <td>96.0</td>
      <td>2.90</td>
      <td>2.79</td>
      <td>0.32</td>
      <td>1.83</td>
      <td>3.25</td>
      <td>0.80</td>
      <td>3.39</td>
      <td>625.0</td>
    </tr>
    <tr>
      <th>121</th>
      <td>11.56</td>
      <td>2.05</td>
      <td>3.23</td>
      <td>28.5</td>
      <td>119.0</td>
      <td>3.18</td>
      <td>5.08</td>
      <td>0.47</td>
      <td>1.87</td>
      <td>6.00</td>
      <td>0.93</td>
      <td>3.69</td>
      <td>465.0</td>
    </tr>
    <tr>
      <th>124</th>
      <td>11.87</td>
      <td>4.31</td>
      <td>2.39</td>
      <td>21.0</td>
      <td>82.0</td>
      <td>2.86</td>
      <td>3.03</td>
      <td>0.21</td>
      <td>2.91</td>
      <td>2.80</td>
      <td>0.75</td>
      <td>3.64</td>
      <td>380.0</td>
    </tr>
    <tr>
      <th>127</th>
      <td>11.79</td>
      <td>2.13</td>
      <td>2.78</td>
      <td>28.5</td>
      <td>92.0</td>
      <td>2.13</td>
      <td>2.24</td>
      <td>0.58</td>
      <td>1.76</td>
      <td>3.00</td>
      <td>0.97</td>
      <td>2.44</td>
      <td>466.0</td>
    </tr>
  </tbody>
</table>
</div>



You can verify that simply using `df[df["alcohol"]<12]`, you can obtain the same result!

However, the .`loc` attribute is useful if you'd only want the color intensity for the wines with an alcohol percentage below 12. You can obtain the result as follows:


```python
df.loc[df["alcohol"]<12, ["color_intensity"]]
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
      <th>color_intensity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>74</th>
      <td>3.21</td>
    </tr>
    <tr>
      <th>75</th>
      <td>3.80</td>
    </tr>
    <tr>
      <th>77</th>
      <td>2.65</td>
    </tr>
    <tr>
      <th>84</th>
      <td>3.05</td>
    </tr>
    <tr>
      <th>87</th>
      <td>2.60</td>
    </tr>
    <tr>
      <th>88</th>
      <td>2.80</td>
    </tr>
    <tr>
      <th>94</th>
      <td>3.25</td>
    </tr>
    <tr>
      <th>96</th>
      <td>2.50</td>
    </tr>
    <tr>
      <th>103</th>
      <td>2.06</td>
    </tr>
    <tr>
      <th>109</th>
      <td>2.65</td>
    </tr>
    <tr>
      <th>110</th>
      <td>2.90</td>
    </tr>
    <tr>
      <th>112</th>
      <td>3.80</td>
    </tr>
    <tr>
      <th>113</th>
      <td>3.08</td>
    </tr>
    <tr>
      <th>115</th>
      <td>1.90</td>
    </tr>
    <tr>
      <th>116</th>
      <td>1.95</td>
    </tr>
    <tr>
      <th>120</th>
      <td>3.25</td>
    </tr>
    <tr>
      <th>121</th>
      <td>6.00</td>
    </tr>
    <tr>
      <th>124</th>
      <td>2.80</td>
    </tr>
    <tr>
      <th>127</th>
      <td>3.00</td>
    </tr>
  </tbody>
</table>
</div>



## Selectors for series

Until now we've only really discussed pandas DataFrames. Most of these methods and selectors are also applicable to pandas series. See how you can convert a one-column DataFrame into a Pandas Series:


```python
# Let's save our color intensity dataframe into an object `col_intensity`
col_intensity = df["color_intensity"]
```


```python
type(col_intensity)
```




    pandas.core.series.Series



Note how col_intensity is now a pandas *Series*.

Many of the commands discussed before are readily applicable to series:


```python
col_intensity[0:3]
```




    0    5.64
    1    4.38
    2    5.68
    Name: color_intensity, dtype: float64




```python
col_intensity[col_intensity > 8] # or col_intensity.loc[col_intensity>8]
```




    18      8.700000
    49      8.900000
    144     8.210000
    148     8.420000
    149     9.400000
    150     8.600000
    151    10.800000
    153    10.520000
    156     9.010000
    158    13.000000
    159    11.750000
    164     9.580000
    166    10.680000
    167    10.260000
    168     8.660000
    169     8.500000
    171     9.899999
    172     9.700000
    175    10.200000
    176     9.300000
    177     9.200000
    Name: color_intensity, dtype: float64



## Changing and setting values in DataFrames and series

### Changing values

Imagine that for some reason, you're not interested in the color intensity values for color intensities above 10, and simply want to set all color intensities to 10 when they are bigger than 10. You can use a selector method and then assign it a new value, just like this:


```python
df.loc[df["color_intensity"]>10, "color_intensity"] = 10
```

### Creating new columns

Now imagine that we want to create a new column named "shade" which has a value "light" when the color_intensity is below 7, and "dark" when the intensity is > 7. This can be done as follows:


```python
df.loc[df["color_intensity"]>7, "shade"] = "dark"
df.loc[df["color_intensity"]<=7, "shade"] = "light"
```

Have another look at `df`. `shade` is added as a 14th column! 

## Summary

We've introduced a range of techniques for accessing information in Pandas Series and DataFrames, selecting rows and columns, changing values, and creating new columns! Now, it's time for some practice! Let's start working on a lab where you will get a chance to combine some of these methods!
