
# Obtaining Your Data

## Introduction
In this lesson, you'll synthesize many of your data loading skills to date in order to merge multiple datasets from various sources.

## Objectives
You will be able to:
* Understand the ETL process and the steps it consists of
* Understand the challenges of working with data from multiple sources 

## Loading SQL DB to DataFrames
<img src="Database-Schema.png">


```python
import sqlite3
import pandas as pd

#Create a connection
con = sqlite3.connect('data.sqlite')
#Create a cursor
cur = con.cursor()
#Select some data
cur.execute("""select * from orders join orderdetails using(orderNumber);""")
df = pd.DataFrame(cur.fetchall())
df.columns = [i[0] for i in cur.description]
print(df.shape)
df.head()
```

    (2996, 11)





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
      <th>orderNumber</th>
      <th>orderDate</th>
      <th>requiredDate</th>
      <th>shippedDate</th>
      <th>status</th>
      <th>comments</th>
      <th>customerNumber</th>
      <th>productCode</th>
      <th>quantityOrdered</th>
      <th>priceEach</th>
      <th>orderLineNumber</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10100</td>
      <td>2003-01-06</td>
      <td>2003-01-13</td>
      <td>2003-01-10</td>
      <td>Shipped</td>
      <td></td>
      <td>363</td>
      <td>S18_1749</td>
      <td>30</td>
      <td>136.00</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10100</td>
      <td>2003-01-06</td>
      <td>2003-01-13</td>
      <td>2003-01-10</td>
      <td>Shipped</td>
      <td></td>
      <td>363</td>
      <td>S18_2248</td>
      <td>50</td>
      <td>55.09</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10100</td>
      <td>2003-01-06</td>
      <td>2003-01-13</td>
      <td>2003-01-10</td>
      <td>Shipped</td>
      <td></td>
      <td>363</td>
      <td>S18_4409</td>
      <td>22</td>
      <td>75.46</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>10100</td>
      <td>2003-01-06</td>
      <td>2003-01-13</td>
      <td>2003-01-10</td>
      <td>Shipped</td>
      <td></td>
      <td>363</td>
      <td>S24_3969</td>
      <td>49</td>
      <td>35.29</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10101</td>
      <td>2003-01-09</td>
      <td>2003-01-18</td>
      <td>2003-01-11</td>
      <td>Shipped</td>
      <td>Check on availability.</td>
      <td>128</td>
      <td>S18_2325</td>
      <td>25</td>
      <td>108.06</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
import sqlite3
import pandas as pd
```


```python
#Create a connection
con = sqlite3.connect('data.sqlite')
#Create a cursor
cur = con.cursor()
#Select some data
cur.execute("""select * from products;""")
df = pd.DataFrame(cur.fetchall())
df.columns = [i[0] for i in cur.description]
print(df.shape)
df.head()
```

    (110, 9)





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
      <th>productCode</th>
      <th>productName</th>
      <th>productLine</th>
      <th>productScale</th>
      <th>productVendor</th>
      <th>productDescription</th>
      <th>quantityInStock</th>
      <th>buyPrice</th>
      <th>MSRP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>S10_1678</td>
      <td>1969 Harley Davidson Ultimate Chopper</td>
      <td>Motorcycles</td>
      <td>1:10</td>
      <td>Min Lin Diecast</td>
      <td>This replica features working kickstand, front...</td>
      <td>7933</td>
      <td>48.81</td>
      <td>95.70</td>
    </tr>
    <tr>
      <th>1</th>
      <td>S10_1949</td>
      <td>1952 Alpine Renault 1300</td>
      <td>Classic Cars</td>
      <td>1:10</td>
      <td>Classic Metal Creations</td>
      <td>Turnable front wheels; steering function; deta...</td>
      <td>7305</td>
      <td>98.58</td>
      <td>214.30</td>
    </tr>
    <tr>
      <th>2</th>
      <td>S10_2016</td>
      <td>1996 Moto Guzzi 1100i</td>
      <td>Motorcycles</td>
      <td>1:10</td>
      <td>Highway 66 Mini Classics</td>
      <td>Official Moto Guzzi logos and insignias, saddl...</td>
      <td>6625</td>
      <td>68.99</td>
      <td>118.94</td>
    </tr>
    <tr>
      <th>3</th>
      <td>S10_4698</td>
      <td>2003 Harley-Davidson Eagle Drag Bike</td>
      <td>Motorcycles</td>
      <td>1:10</td>
      <td>Red Start Diecast</td>
      <td>Model features, official Harley Davidson logos...</td>
      <td>5582</td>
      <td>91.02</td>
      <td>193.66</td>
    </tr>
    <tr>
      <th>4</th>
      <td>S10_4757</td>
      <td>1972 Alfa Romeo GTA</td>
      <td>Classic Cars</td>
      <td>1:10</td>
      <td>Motor City Art Classics</td>
      <td>Features include: Turnable front wheels; steer...</td>
      <td>3252</td>
      <td>85.68</td>
      <td>136.00</td>
    </tr>
  </tbody>
</table>
</div>



## Merging Data

Recall that you can also join data from multiple tables in sql.


```python
#Create a connection
con = sqlite3.connect('data.sqlite')
#Create a cursor
cur = con.cursor()
#Select some data
cur.execute("""select * from products
                        join orderdetails
                        using (productCode);""")
df = pd.DataFrame(cur.fetchall())
df.columns = [i[0] for i in cur.description]
print(df.shape)
df.head()
```

    (2996, 13)





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
      <th>productCode</th>
      <th>productName</th>
      <th>productLine</th>
      <th>productScale</th>
      <th>productVendor</th>
      <th>productDescription</th>
      <th>quantityInStock</th>
      <th>buyPrice</th>
      <th>MSRP</th>
      <th>orderNumber</th>
      <th>quantityOrdered</th>
      <th>priceEach</th>
      <th>orderLineNumber</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>S10_1678</td>
      <td>1969 Harley Davidson Ultimate Chopper</td>
      <td>Motorcycles</td>
      <td>1:10</td>
      <td>Min Lin Diecast</td>
      <td>This replica features working kickstand, front...</td>
      <td>7933</td>
      <td>48.81</td>
      <td>95.70</td>
      <td>10107</td>
      <td>30</td>
      <td>81.35</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>S10_1678</td>
      <td>1969 Harley Davidson Ultimate Chopper</td>
      <td>Motorcycles</td>
      <td>1:10</td>
      <td>Min Lin Diecast</td>
      <td>This replica features working kickstand, front...</td>
      <td>7933</td>
      <td>48.81</td>
      <td>95.70</td>
      <td>10121</td>
      <td>34</td>
      <td>86.13</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>S10_1678</td>
      <td>1969 Harley Davidson Ultimate Chopper</td>
      <td>Motorcycles</td>
      <td>1:10</td>
      <td>Min Lin Diecast</td>
      <td>This replica features working kickstand, front...</td>
      <td>7933</td>
      <td>48.81</td>
      <td>95.70</td>
      <td>10134</td>
      <td>41</td>
      <td>90.92</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>S10_1678</td>
      <td>1969 Harley Davidson Ultimate Chopper</td>
      <td>Motorcycles</td>
      <td>1:10</td>
      <td>Min Lin Diecast</td>
      <td>This replica features working kickstand, front...</td>
      <td>7933</td>
      <td>48.81</td>
      <td>95.70</td>
      <td>10145</td>
      <td>45</td>
      <td>76.56</td>
      <td>6</td>
    </tr>
    <tr>
      <th>4</th>
      <td>S10_1678</td>
      <td>1969 Harley Davidson Ultimate Chopper</td>
      <td>Motorcycles</td>
      <td>1:10</td>
      <td>Min Lin Diecast</td>
      <td>This replica features working kickstand, front...</td>
      <td>7933</td>
      <td>48.81</td>
      <td>95.70</td>
      <td>10159</td>
      <td>49</td>
      <td>81.35</td>
      <td>14</td>
    </tr>
  </tbody>
</table>
</div>



You can also merge data from a separate csv file. For example, say you take a separate data source regarding daily sales data for the various branches. You might first generate a view from our database:


```python
#Create a connection
con = sqlite3.connect('data.sqlite')
#Create a cursor
cur = con.cursor()
#Select some data
cur.execute("""select * from customers
                        join orders
                        using(customerNumber);""")
df = pd.DataFrame(cur.fetchall())
df.columns = [i[0] for i in cur.description]
print(df.shape)
df.head()
```

    (326, 19)





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
      <th>customerNumber</th>
      <th>customerName</th>
      <th>contactLastName</th>
      <th>contactFirstName</th>
      <th>phone</th>
      <th>addressLine1</th>
      <th>addressLine2</th>
      <th>city</th>
      <th>state</th>
      <th>postalCode</th>
      <th>country</th>
      <th>salesRepEmployeeNumber</th>
      <th>creditLimit</th>
      <th>orderNumber</th>
      <th>orderDate</th>
      <th>requiredDate</th>
      <th>shippedDate</th>
      <th>status</th>
      <th>comments</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>103</td>
      <td>Atelier graphique</td>
      <td>Schmitt</td>
      <td>Carine</td>
      <td>40.32.2555</td>
      <td>54, rue Royale</td>
      <td></td>
      <td>Nantes</td>
      <td></td>
      <td>44000</td>
      <td>France</td>
      <td>1370</td>
      <td>21000.00</td>
      <td>10123</td>
      <td>2003-05-20</td>
      <td>2003-05-29</td>
      <td>2003-05-22</td>
      <td>Shipped</td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>103</td>
      <td>Atelier graphique</td>
      <td>Schmitt</td>
      <td>Carine</td>
      <td>40.32.2555</td>
      <td>54, rue Royale</td>
      <td></td>
      <td>Nantes</td>
      <td></td>
      <td>44000</td>
      <td>France</td>
      <td>1370</td>
      <td>21000.00</td>
      <td>10298</td>
      <td>2004-09-27</td>
      <td>2004-10-05</td>
      <td>2004-10-01</td>
      <td>Shipped</td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td>103</td>
      <td>Atelier graphique</td>
      <td>Schmitt</td>
      <td>Carine</td>
      <td>40.32.2555</td>
      <td>54, rue Royale</td>
      <td></td>
      <td>Nantes</td>
      <td></td>
      <td>44000</td>
      <td>France</td>
      <td>1370</td>
      <td>21000.00</td>
      <td>10345</td>
      <td>2004-11-25</td>
      <td>2004-12-01</td>
      <td>2004-11-26</td>
      <td>Shipped</td>
      <td></td>
    </tr>
    <tr>
      <th>3</th>
      <td>112</td>
      <td>Signal Gift Stores</td>
      <td>King</td>
      <td>Jean</td>
      <td>7025551838</td>
      <td>8489 Strong St.</td>
      <td></td>
      <td>Las Vegas</td>
      <td>NV</td>
      <td>83030</td>
      <td>USA</td>
      <td>1166</td>
      <td>71800.00</td>
      <td>10124</td>
      <td>2003-05-21</td>
      <td>2003-05-29</td>
      <td>2003-05-25</td>
      <td>Shipped</td>
      <td>Customer very concerned about the exact color ...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>112</td>
      <td>Signal Gift Stores</td>
      <td>King</td>
      <td>Jean</td>
      <td>7025551838</td>
      <td>8489 Strong St.</td>
      <td></td>
      <td>Las Vegas</td>
      <td>NV</td>
      <td>83030</td>
      <td>USA</td>
      <td>1166</td>
      <td>71800.00</td>
      <td>10278</td>
      <td>2004-08-06</td>
      <td>2004-08-16</td>
      <td>2004-08-09</td>
      <td>Shipped</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>



And then load the seperate datefile:


```python
daily_sums = pd.read_csv('Daily_Sales_Summaries.csv')
daily_sums.head()
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
      <th>orderDate</th>
      <th>min</th>
      <th>max</th>
      <th>sum</th>
      <th>mean</th>
      <th>std</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2003-01-06</td>
      <td>1660.12</td>
      <td>4080.00</td>
      <td>10223.83</td>
      <td>2555.957500</td>
      <td>1132.572429</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2003-01-09</td>
      <td>1463.85</td>
      <td>4343.56</td>
      <td>10549.01</td>
      <td>2637.252500</td>
      <td>1244.866467</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2003-01-10</td>
      <td>1768.33</td>
      <td>3726.45</td>
      <td>5494.78</td>
      <td>2747.390000</td>
      <td>1384.599930</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2003-01-29</td>
      <td>1283.48</td>
      <td>5571.80</td>
      <td>50218.95</td>
      <td>3138.684375</td>
      <td>1168.280303</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2003-01-31</td>
      <td>1338.04</td>
      <td>4566.99</td>
      <td>40206.20</td>
      <td>3092.784615</td>
      <td>1148.570425</td>
    </tr>
  </tbody>
</table>
</div>




```python
merged = pd.merge(df, daily_sums)
```

## Checking Merged Data

It's always good practice to check assumptions and preview transformed data views throughout your process. Let's take a look:


```python
merged.head()
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
      <th>customerNumber</th>
      <th>customerName</th>
      <th>contactLastName</th>
      <th>contactFirstName</th>
      <th>phone</th>
      <th>addressLine1</th>
      <th>addressLine2</th>
      <th>city</th>
      <th>state</th>
      <th>postalCode</th>
      <th>...</th>
      <th>orderDate</th>
      <th>requiredDate</th>
      <th>shippedDate</th>
      <th>status</th>
      <th>comments</th>
      <th>min</th>
      <th>max</th>
      <th>sum</th>
      <th>mean</th>
      <th>std</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>103</td>
      <td>Atelier graphique</td>
      <td>Schmitt</td>
      <td>Carine</td>
      <td>40.32.2555</td>
      <td>54, rue Royale</td>
      <td></td>
      <td>Nantes</td>
      <td></td>
      <td>44000</td>
      <td>...</td>
      <td>2003-05-20</td>
      <td>2003-05-29</td>
      <td>2003-05-22</td>
      <td>Shipped</td>
      <td></td>
      <td>2163.50</td>
      <td>5282.64</td>
      <td>14571.44</td>
      <td>3642.860000</td>
      <td>1322.891537</td>
    </tr>
    <tr>
      <th>1</th>
      <td>103</td>
      <td>Atelier graphique</td>
      <td>Schmitt</td>
      <td>Carine</td>
      <td>40.32.2555</td>
      <td>54, rue Royale</td>
      <td></td>
      <td>Nantes</td>
      <td></td>
      <td>44000</td>
      <td>...</td>
      <td>2004-09-27</td>
      <td>2004-10-05</td>
      <td>2004-10-01</td>
      <td>Shipped</td>
      <td></td>
      <td>1938.24</td>
      <td>4128.54</td>
      <td>6066.78</td>
      <td>3033.390000</td>
      <td>1548.775983</td>
    </tr>
    <tr>
      <th>2</th>
      <td>103</td>
      <td>Atelier graphique</td>
      <td>Schmitt</td>
      <td>Carine</td>
      <td>40.32.2555</td>
      <td>54, rue Royale</td>
      <td></td>
      <td>Nantes</td>
      <td></td>
      <td>44000</td>
      <td>...</td>
      <td>2004-11-25</td>
      <td>2004-12-01</td>
      <td>2004-11-26</td>
      <td>Shipped</td>
      <td></td>
      <td>557.60</td>
      <td>7573.50</td>
      <td>20564.45</td>
      <td>2570.556250</td>
      <td>2178.832190</td>
    </tr>
    <tr>
      <th>3</th>
      <td>350</td>
      <td>Marseille Mini Autos</td>
      <td>Lebihan</td>
      <td>Laurence</td>
      <td>91.24.4555</td>
      <td>12, rue des Bouchers</td>
      <td></td>
      <td>Marseille</td>
      <td></td>
      <td>13008</td>
      <td>...</td>
      <td>2004-11-25</td>
      <td>2004-12-02</td>
      <td>2004-11-29</td>
      <td>Shipped</td>
      <td></td>
      <td>557.60</td>
      <td>7573.50</td>
      <td>20564.45</td>
      <td>2570.556250</td>
      <td>2178.832190</td>
    </tr>
    <tr>
      <th>4</th>
      <td>112</td>
      <td>Signal Gift Stores</td>
      <td>King</td>
      <td>Jean</td>
      <td>7025551838</td>
      <td>8489 Strong St.</td>
      <td></td>
      <td>Las Vegas</td>
      <td>NV</td>
      <td>83030</td>
      <td>...</td>
      <td>2003-05-21</td>
      <td>2003-05-29</td>
      <td>2003-05-25</td>
      <td>Shipped</td>
      <td>Customer very concerned about the exact color ...</td>
      <td>798.38</td>
      <td>4704.92</td>
      <td>40207.06</td>
      <td>2680.470667</td>
      <td>1255.052262</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 24 columns</p>
</div>



Pandas merge method conveniently uses common column names between the dataframes. You can always specifically specify what columns to join on by using the `on` clause as in `pd.merge(df1, df2, on=[col1, col2])`. Unfortunately, columns that are not identically named beforehand will not work with this convenience method. Additionally, it is imperative to check the formatting of the join keys between the tables. A number formatted as a string can often ruin joins, and separate formatting conventions such as 'U.S.' versus 'USA' are also important preprocessing considerations before merging data files from various sources. In this case, everything worked smoothly, but it's good to keep in mind what problems may occur.

## Saving Transformed Data to File
Finally, we can save our transformed dataset.


```python
merged.to_csv('Merged_Dataset.csv', index=False)
```

## Summary
Well done! In this lesson you reviewed merges, as well as potential pitfalls in merging datasets from different sources. In the next lab, you'll get some practice doing this as an initial step to a regression task.
