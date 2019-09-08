
# Importing Data Using Pandas

## Introduction

Pandas is a popular library for efficiently wrangling data. Pandas is particularly optimized to work with two-dimensional tabular data that is organized in rows and columns. In this lesson, you will learn how to import tabular data as a pandas DataFrame object, how to access and manipulate the data in DataFrame objects, and how to export DataFrames to some common file formats. 

For more information on pandas, refer to https://pandas.pydata.org/pandas-docs/stable/

## Objectives
You will be able to:
* Import data from csv files and Excel files
* Understand and explain key arguments for imports
* Save information to csv and Excel files
* Access data within a Pandas DataFrame (print() and .head())

## Loading Pandas

When importing pandas, it is standard to import it under the alias `pd`


```python
import pandas as pd
```

## Importing Data

There are a few main functions for importing data into a pandas DataFrame including:

* `pd.read_csv()`
* `pd.read_excel()`
* `pd.read_json()`
* `pd.DataFrame.from_dict()`

Most of these methods are fairly straightforward; you use `.read_csv()` for csv files, `.read_excel()` for excel files (both new and old .xlx and .xlsx) and `.read_json()` for json files. That said, there are a few nuances you should know about. The first is that the `.read_csv()` format can be used for any plain-text delimited file. This may include (but is not limited to) pipe (|) delimited files (.psv) and tab separated files (.tsv).

Let's look at an example by investigating a file, bp.txt, stored in the Data folder.


```python
df = pd.read_csv('Data/bp.txt', delimiter='\t')
```

We've now loaded the data from a file into a DataFrame. To investigate the DataFrame, we can use a method called `head(n)` or `tail(n)`, which will respectively return first and last __n__ items in the DataFrame.


```python
df.head(3)
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
      <th>Pt</th>
      <th>BP</th>
      <th>Age</th>
      <th>Weight</th>
      <th>BSA</th>
      <th>Dur</th>
      <th>Pulse</th>
      <th>Stress</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>105</td>
      <td>47</td>
      <td>85.4</td>
      <td>1.75</td>
      <td>5.1</td>
      <td>63</td>
      <td>33</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>115</td>
      <td>49</td>
      <td>94.2</td>
      <td>2.10</td>
      <td>3.8</td>
      <td>70</td>
      <td>14</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>116</td>
      <td>49</td>
      <td>95.3</td>
      <td>1.98</td>
      <td>8.2</td>
      <td>72</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.tail(4)
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
      <th>Pt</th>
      <th>BP</th>
      <th>Age</th>
      <th>Weight</th>
      <th>BSA</th>
      <th>Dur</th>
      <th>Pulse</th>
      <th>Stress</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>106</td>
      <td>46</td>
      <td>87.0</td>
      <td>1.87</td>
      <td>3.6</td>
      <td>62</td>
      <td>18</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>113</td>
      <td>46</td>
      <td>94.5</td>
      <td>1.90</td>
      <td>4.3</td>
      <td>70</td>
      <td>12</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>110</td>
      <td>48</td>
      <td>90.5</td>
      <td>1.88</td>
      <td>9.0</td>
      <td>71</td>
      <td>99</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>122</td>
      <td>56</td>
      <td>95.7</td>
      <td>2.09</td>
      <td>7.0</td>
      <td>75</td>
      <td>99</td>
    </tr>
  </tbody>
</table>
</div>



This example shows that the data was tab delimited (\t), so an appropriate file extension could have also been .tsv. Once we've loaded the dataset, we can export it to any format we would like with the related methods:

* `df.to_csv()`
* `df.to_excel()`
* `df.to_json()`
* `df.to_dict()`

There are also several other options available, but these are the most common.

## Skipping and Limiting Rows

Another feature that you may have to employ is skipping rows when there is metadata stored at the top of a file. You can do this using the optional parameter `skiprows`. Similarly, if you want to only load a portion of a large file as an initial preview, you can use the `nrows` parameter.


```python
df = pd.read_csv('Data/ACS_16_5YR_B24011_with_ann.csv', nrows=100)
df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>GEO.id</th>
      <th>GEO.id2</th>
      <th>GEO.display-label</th>
      <th>HD01_VD01</th>
      <th>HD02_VD01</th>
      <th>HD01_VD02</th>
      <th>HD02_VD02</th>
      <th>HD01_VD03</th>
      <th>HD02_VD03</th>
      <th>HD01_VD04</th>
      <th>...</th>
      <th>HD01_VD32</th>
      <th>HD02_VD32</th>
      <th>HD01_VD33</th>
      <th>HD02_VD33</th>
      <th>HD01_VD34</th>
      <th>HD02_VD34</th>
      <th>HD01_VD35</th>
      <th>HD02_VD35</th>
      <th>HD01_VD36</th>
      <th>HD02_VD36</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Id</td>
      <td>Id2</td>
      <td>Geography</td>
      <td>Estimate; Total:</td>
      <td>Margin of Error; Total:</td>
      <td>Estimate; Total: - Management, business, scien...</td>
      <td>Margin of Error; Total: - Management, business...</td>
      <td>Estimate; Total: - Management, business, scien...</td>
      <td>Margin of Error; Total: - Management, business...</td>
      <td>Estimate; Total: - Management, business, scien...</td>
      <td>...</td>
      <td>Estimate; Total: - Natural resources, construc...</td>
      <td>Margin of Error; Total: - Natural resources, c...</td>
      <td>Estimate; Total: - Production, transportation,...</td>
      <td>Margin of Error; Total: - Production, transpor...</td>
      <td>Estimate; Total: - Production, transportation,...</td>
      <td>Margin of Error; Total: - Production, transpor...</td>
      <td>Estimate; Total: - Production, transportation,...</td>
      <td>Margin of Error; Total: - Production, transpor...</td>
      <td>Estimate; Total: - Production, transportation,...</td>
      <td>Margin of Error; Total: - Production, transpor...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0500000US01001</td>
      <td>01001</td>
      <td>Autauga County, Alabama</td>
      <td>33267</td>
      <td>2306</td>
      <td>48819</td>
      <td>1806</td>
      <td>55557</td>
      <td>4972</td>
      <td>63333</td>
      <td>...</td>
      <td>31402</td>
      <td>5135</td>
      <td>35594</td>
      <td>3034</td>
      <td>36059</td>
      <td>3893</td>
      <td>47266</td>
      <td>13608</td>
      <td>19076</td>
      <td>4808</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0500000US01003</td>
      <td>01003</td>
      <td>Baldwin County, Alabama</td>
      <td>31540</td>
      <td>683</td>
      <td>49524</td>
      <td>1811</td>
      <td>57150</td>
      <td>6980</td>
      <td>63422</td>
      <td>...</td>
      <td>35603</td>
      <td>3882</td>
      <td>30549</td>
      <td>1606</td>
      <td>29604</td>
      <td>4554</td>
      <td>35504</td>
      <td>6260</td>
      <td>24182</td>
      <td>3580</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0500000US01005</td>
      <td>01005</td>
      <td>Barbour County, Alabama</td>
      <td>26575</td>
      <td>1653</td>
      <td>41652</td>
      <td>2638</td>
      <td>51797</td>
      <td>5980</td>
      <td>52775</td>
      <td>...</td>
      <td>37847</td>
      <td>11189</td>
      <td>26094</td>
      <td>4884</td>
      <td>25339</td>
      <td>4900</td>
      <td>37282</td>
      <td>6017</td>
      <td>16607</td>
      <td>3497</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0500000US01007</td>
      <td>01007</td>
      <td>Bibb County, Alabama</td>
      <td>30088</td>
      <td>2224</td>
      <td>40787</td>
      <td>2896</td>
      <td>50069</td>
      <td>12841</td>
      <td>67917</td>
      <td>...</td>
      <td>45952</td>
      <td>5622</td>
      <td>28983</td>
      <td>3401</td>
      <td>31881</td>
      <td>2317</td>
      <td>26580</td>
      <td>2901</td>
      <td>23479</td>
      <td>4942</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 75 columns</p>
</div>



### Notice the first row is descriptions of the variables

We could manually remove:


```python
df = df.drop(0)
df.head(2)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>GEO.id</th>
      <th>GEO.id2</th>
      <th>GEO.display-label</th>
      <th>HD01_VD01</th>
      <th>HD02_VD01</th>
      <th>HD01_VD02</th>
      <th>HD02_VD02</th>
      <th>HD01_VD03</th>
      <th>HD02_VD03</th>
      <th>HD01_VD04</th>
      <th>...</th>
      <th>HD01_VD32</th>
      <th>HD02_VD32</th>
      <th>HD01_VD33</th>
      <th>HD02_VD33</th>
      <th>HD01_VD34</th>
      <th>HD02_VD34</th>
      <th>HD01_VD35</th>
      <th>HD02_VD35</th>
      <th>HD01_VD36</th>
      <th>HD02_VD36</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0500000US01001</td>
      <td>01001</td>
      <td>Autauga County, Alabama</td>
      <td>33267</td>
      <td>2306</td>
      <td>48819</td>
      <td>1806</td>
      <td>55557</td>
      <td>4972</td>
      <td>63333</td>
      <td>...</td>
      <td>31402</td>
      <td>5135</td>
      <td>35594</td>
      <td>3034</td>
      <td>36059</td>
      <td>3893</td>
      <td>47266</td>
      <td>13608</td>
      <td>19076</td>
      <td>4808</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0500000US01003</td>
      <td>01003</td>
      <td>Baldwin County, Alabama</td>
      <td>31540</td>
      <td>683</td>
      <td>49524</td>
      <td>1811</td>
      <td>57150</td>
      <td>6980</td>
      <td>63422</td>
      <td>...</td>
      <td>35603</td>
      <td>3882</td>
      <td>30549</td>
      <td>1606</td>
      <td>29604</td>
      <td>4554</td>
      <td>35504</td>
      <td>6260</td>
      <td>24182</td>
      <td>3580</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 75 columns</p>
</div>



Or if we knew from the start, we could use the skiprows argument:


```python
df = pd.read_csv('Data/ACS_16_5YR_B24011_with_ann.csv', skiprows=1, nrows=100)
df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Id</th>
      <th>Id2</th>
      <th>Geography</th>
      <th>Estimate; Total:</th>
      <th>Margin of Error; Total:</th>
      <th>Estimate; Total: - Management, business, science, and arts occupations:</th>
      <th>Margin of Error; Total: - Management, business, science, and arts occupations:</th>
      <th>Estimate; Total: - Management, business, science, and arts occupations: - Management, business, and financial occupations:</th>
      <th>Margin of Error; Total: - Management, business, science, and arts occupations: - Management, business, and financial occupations:</th>
      <th>Estimate; Total: - Management, business, science, and arts occupations: - Management, business, and financial occupations: - Management occupations</th>
      <th>...</th>
      <th>Estimate; Total: - Natural resources, construction, and maintenance occupations: - Installation, maintenance, and repair occupations</th>
      <th>Margin of Error; Total: - Natural resources, construction, and maintenance occupations: - Installation, maintenance, and repair occupations</th>
      <th>Estimate; Total: - Production, transportation, and material moving occupations:</th>
      <th>Margin of Error; Total: - Production, transportation, and material moving occupations:</th>
      <th>Estimate; Total: - Production, transportation, and material moving occupations: - Production occupations</th>
      <th>Margin of Error; Total: - Production, transportation, and material moving occupations: - Production occupations</th>
      <th>Estimate; Total: - Production, transportation, and material moving occupations: - Transportation occupations</th>
      <th>Margin of Error; Total: - Production, transportation, and material moving occupations: - Transportation occupations</th>
      <th>Estimate; Total: - Production, transportation, and material moving occupations: - Material moving occupations</th>
      <th>Margin of Error; Total: - Production, transportation, and material moving occupations: - Material moving occupations</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0500000US01001</td>
      <td>1001</td>
      <td>Autauga County, Alabama</td>
      <td>33267</td>
      <td>2306</td>
      <td>48819</td>
      <td>1806</td>
      <td>55557</td>
      <td>4972</td>
      <td>63333</td>
      <td>...</td>
      <td>31402</td>
      <td>5135</td>
      <td>35594</td>
      <td>3034</td>
      <td>36059</td>
      <td>3893</td>
      <td>47266</td>
      <td>13608</td>
      <td>19076</td>
      <td>4808</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0500000US01003</td>
      <td>1003</td>
      <td>Baldwin County, Alabama</td>
      <td>31540</td>
      <td>683</td>
      <td>49524</td>
      <td>1811</td>
      <td>57150</td>
      <td>6980</td>
      <td>63422</td>
      <td>...</td>
      <td>35603</td>
      <td>3882</td>
      <td>30549</td>
      <td>1606</td>
      <td>29604</td>
      <td>4554</td>
      <td>35504</td>
      <td>6260</td>
      <td>24182</td>
      <td>3580</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0500000US01005</td>
      <td>1005</td>
      <td>Barbour County, Alabama</td>
      <td>26575</td>
      <td>1653</td>
      <td>41652</td>
      <td>2638</td>
      <td>51797</td>
      <td>5980</td>
      <td>52775</td>
      <td>...</td>
      <td>37847</td>
      <td>11189</td>
      <td>26094</td>
      <td>4884</td>
      <td>25339</td>
      <td>4900</td>
      <td>37282</td>
      <td>6017</td>
      <td>16607</td>
      <td>3497</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0500000US01007</td>
      <td>1007</td>
      <td>Bibb County, Alabama</td>
      <td>30088</td>
      <td>2224</td>
      <td>40787</td>
      <td>2896</td>
      <td>50069</td>
      <td>12841</td>
      <td>67917</td>
      <td>...</td>
      <td>45952</td>
      <td>5622</td>
      <td>28983</td>
      <td>3401</td>
      <td>31881</td>
      <td>2317</td>
      <td>26580</td>
      <td>2901</td>
      <td>23479</td>
      <td>4942</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0500000US01009</td>
      <td>1009</td>
      <td>Blount County, Alabama</td>
      <td>34900</td>
      <td>2063</td>
      <td>46593</td>
      <td>2963</td>
      <td>47003</td>
      <td>6189</td>
      <td>50991</td>
      <td>...</td>
      <td>42489</td>
      <td>7176</td>
      <td>32969</td>
      <td>3767</td>
      <td>31814</td>
      <td>4551</td>
      <td>41375</td>
      <td>5280</td>
      <td>26755</td>
      <td>2963</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 75 columns</p>
</div>



## Header

Relatedly to skiprows is the header option. This specifies the row where column names are and starts the load from that point:


```python
# look at the error output once you run this cell. What type of error is it?
df = pd.read_csv('Data/ACS_16_5YR_B24011_with_ann.csv', header=1)
df.head()
```


    ---------------------------------------------------------------------------

    UnicodeDecodeError                        Traceback (most recent call last)

    pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._convert_tokens (pandas\_libs\parsers.c:14858)()


    pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._convert_with_dtype (pandas\_libs\parsers.c:17119)()


    pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._string_convert (pandas\_libs\parsers.c:17347)()


    pandas/_libs/parsers.pyx in pandas._libs.parsers._string_box_utf8 (pandas\_libs\parsers.c:23041)()


    UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in position 2: invalid continuation byte

    
    During handling of the above exception, another exception occurred:


    UnicodeDecodeError                        Traceback (most recent call last)

    <ipython-input-6-a2d61668e2c4> in <module>()
    ----> 1 df = pd.read_csv('Data/ACS_16_5YR_B24011_with_ann.csv', header=1)
          2 df.head()


    ~\Anaconda3wenv\lib\site-packages\pandas\io\parsers.py in parser_f(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, escapechar, comment, encoding, dialect, tupleize_cols, error_bad_lines, warn_bad_lines, skipfooter, skip_footer, doublequote, delim_whitespace, as_recarray, compact_ints, use_unsigned, low_memory, buffer_lines, memory_map, float_precision)
        653                     skip_blank_lines=skip_blank_lines)
        654 
    --> 655         return _read(filepath_or_buffer, kwds)
        656 
        657     parser_f.__name__ = name


    ~\Anaconda3wenv\lib\site-packages\pandas\io\parsers.py in _read(filepath_or_buffer, kwds)
        409 
        410     try:
    --> 411         data = parser.read(nrows)
        412     finally:
        413         parser.close()


    ~\Anaconda3wenv\lib\site-packages\pandas\io\parsers.py in read(self, nrows)
       1003                 raise ValueError('skipfooter not supported for iteration')
       1004 
    -> 1005         ret = self._engine.read(nrows)
       1006 
       1007         if self.options.get('as_recarray'):


    ~\Anaconda3wenv\lib\site-packages\pandas\io\parsers.py in read(self, nrows)
       1746     def read(self, nrows=None):
       1747         try:
    -> 1748             data = self._reader.read(nrows)
       1749         except StopIteration:
       1750             if self._first_chunk:


    pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader.read (pandas\_libs\parsers.c:10862)()


    pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._read_low_memory (pandas\_libs\parsers.c:11138)()


    pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._read_rows (pandas\_libs\parsers.c:12175)()


    pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._convert_column_data (pandas\_libs\parsers.c:14136)()


    pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._convert_tokens (pandas\_libs\parsers.c:14972)()


    pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._convert_with_dtype (pandas\_libs\parsers.c:17119)()


    pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._string_convert (pandas\_libs\parsers.c:17347)()


    pandas/_libs/parsers.pyx in pandas._libs.parsers._string_box_utf8 (pandas\_libs\parsers.c:23041)()


    UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in position 2: invalid continuation byte


## Encoding

Encoding errors like the one above are always frustrating. This has to do with how the strings within the file itself are formatted. The most common encoding other than `utf-8` that you are likely to come across is `latin-1`.


```python
df = pd.read_csv('Data/ACS_16_5YR_B24011_with_ann.csv', header=1, encoding='latin-1')
df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Id</th>
      <th>Id2</th>
      <th>Geography</th>
      <th>Estimate; Total:</th>
      <th>Margin of Error; Total:</th>
      <th>Estimate; Total: - Management, business, science, and arts occupations:</th>
      <th>Margin of Error; Total: - Management, business, science, and arts occupations:</th>
      <th>Estimate; Total: - Management, business, science, and arts occupations: - Management, business, and financial occupations:</th>
      <th>Margin of Error; Total: - Management, business, science, and arts occupations: - Management, business, and financial occupations:</th>
      <th>Estimate; Total: - Management, business, science, and arts occupations: - Management, business, and financial occupations: - Management occupations</th>
      <th>...</th>
      <th>Estimate; Total: - Natural resources, construction, and maintenance occupations: - Installation, maintenance, and repair occupations</th>
      <th>Margin of Error; Total: - Natural resources, construction, and maintenance occupations: - Installation, maintenance, and repair occupations</th>
      <th>Estimate; Total: - Production, transportation, and material moving occupations:</th>
      <th>Margin of Error; Total: - Production, transportation, and material moving occupations:</th>
      <th>Estimate; Total: - Production, transportation, and material moving occupations: - Production occupations</th>
      <th>Margin of Error; Total: - Production, transportation, and material moving occupations: - Production occupations</th>
      <th>Estimate; Total: - Production, transportation, and material moving occupations: - Transportation occupations</th>
      <th>Margin of Error; Total: - Production, transportation, and material moving occupations: - Transportation occupations</th>
      <th>Estimate; Total: - Production, transportation, and material moving occupations: - Material moving occupations</th>
      <th>Margin of Error; Total: - Production, transportation, and material moving occupations: - Material moving occupations</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0500000US01001</td>
      <td>1001</td>
      <td>Autauga County, Alabama</td>
      <td>33267</td>
      <td>2306</td>
      <td>48819</td>
      <td>1806</td>
      <td>55557</td>
      <td>4972</td>
      <td>63333</td>
      <td>...</td>
      <td>31402</td>
      <td>5135</td>
      <td>35594</td>
      <td>3034</td>
      <td>36059</td>
      <td>3893</td>
      <td>47266</td>
      <td>13608</td>
      <td>19076</td>
      <td>4808</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0500000US01003</td>
      <td>1003</td>
      <td>Baldwin County, Alabama</td>
      <td>31540</td>
      <td>683</td>
      <td>49524</td>
      <td>1811</td>
      <td>57150</td>
      <td>6980</td>
      <td>63422</td>
      <td>...</td>
      <td>35603</td>
      <td>3882</td>
      <td>30549</td>
      <td>1606</td>
      <td>29604</td>
      <td>4554</td>
      <td>35504</td>
      <td>6260</td>
      <td>24182</td>
      <td>3580</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0500000US01005</td>
      <td>1005</td>
      <td>Barbour County, Alabama</td>
      <td>26575</td>
      <td>1653</td>
      <td>41652</td>
      <td>2638</td>
      <td>51797</td>
      <td>5980</td>
      <td>52775</td>
      <td>...</td>
      <td>37847</td>
      <td>11189</td>
      <td>26094</td>
      <td>4884</td>
      <td>25339</td>
      <td>4900</td>
      <td>37282</td>
      <td>6017</td>
      <td>16607</td>
      <td>3497</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0500000US01007</td>
      <td>1007</td>
      <td>Bibb County, Alabama</td>
      <td>30088</td>
      <td>2224</td>
      <td>40787</td>
      <td>2896</td>
      <td>50069</td>
      <td>12841</td>
      <td>67917</td>
      <td>...</td>
      <td>45952</td>
      <td>5622</td>
      <td>28983</td>
      <td>3401</td>
      <td>31881</td>
      <td>2317</td>
      <td>26580</td>
      <td>2901</td>
      <td>23479</td>
      <td>4942</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0500000US01009</td>
      <td>1009</td>
      <td>Blount County, Alabama</td>
      <td>34900</td>
      <td>2063</td>
      <td>46593</td>
      <td>2963</td>
      <td>47003</td>
      <td>6189</td>
      <td>50991</td>
      <td>...</td>
      <td>42489</td>
      <td>7176</td>
      <td>32969</td>
      <td>3767</td>
      <td>31814</td>
      <td>4551</td>
      <td>41375</td>
      <td>5280</td>
      <td>26755</td>
      <td>2963</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 75 columns</p>
</div>



## Selecting Specific Columns  

You can also specify specific columns if you only want to load specific features.


```python
df = pd.read_csv('Data/ACS_16_5YR_B24011_with_ann.csv', usecols=[0,1,2,5,6], encoding='latin-1')
df.head(2)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>GEO.id</th>
      <th>GEO.id2</th>
      <th>GEO.display-label</th>
      <th>HD01_VD02</th>
      <th>HD02_VD02</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Id</td>
      <td>Id2</td>
      <td>Geography</td>
      <td>Estimate; Total: - Management, business, scien...</td>
      <td>Margin of Error; Total: - Management, business...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0500000US01001</td>
      <td>01001</td>
      <td>Autauga County, Alabama</td>
      <td>48819</td>
      <td>1806</td>
    </tr>
  </tbody>
</table>
</div>



## Or


```python
df = pd.read_csv('Data/ACS_16_5YR_B24011_with_ann.csv', usecols=['GEO.id', 'GEO.id2'], encoding='latin-1')
df.head(2)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>GEO.id</th>
      <th>GEO.id2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Id</td>
      <td>Id2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0500000US01001</td>
      <td>01001</td>
    </tr>
  </tbody>
</table>
</div>



## Selecting Specific Sheets
You can also specify specific sheets for Excel files!


```python
import pandas as pd
```

This can be done by index number


```python
df1 = pd.read_excel('Data/Yelp_Selected_Businesses.xlsx')
df1.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
      <th>Unnamed: 8</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>business_id</td>
      <td>cool</td>
      <td>date</td>
      <td>funny</td>
      <td>review_id</td>
      <td>stars</td>
      <td>text</td>
      <td>useful</td>
      <td>user_id</td>
    </tr>
    <tr>
      <th>1</th>
      <td>RESDUcs7fIiihp38-d6_6g</td>
      <td>0</td>
      <td>2015-09-16</td>
      <td>0</td>
      <td>gkcPdbblTvZDMSwx8nVEKw</td>
      <td>5</td>
      <td>Got here early on football Sunday 7:30am as I ...</td>
      <td>0</td>
      <td>SKteB5rgDlkkUa1Zxe1N0Q</td>
    </tr>
    <tr>
      <th>2</th>
      <td>RESDUcs7fIiihp38-d6_6g</td>
      <td>0</td>
      <td>2017-09-09</td>
      <td>0</td>
      <td>mQfl6ci46mu0xaZrkRUhlA</td>
      <td>5</td>
      <td>This buffet is amazing.  Yes, it is expensive,...</td>
      <td>0</td>
      <td>f638AHA_GoHbyDB7VFMz7A</td>
    </tr>
    <tr>
      <th>3</th>
      <td>RESDUcs7fIiihp38-d6_6g</td>
      <td>0</td>
      <td>2013-01-14</td>
      <td>0</td>
      <td>EJ7DJ8bm7-2PLFB9WKx4LQ</td>
      <td>3</td>
      <td>I was really looking forward to this but it wa...</td>
      <td>0</td>
      <td>-wVPuTiIEG85LwTK46Prpw</td>
    </tr>
    <tr>
      <th>4</th>
      <td>RESDUcs7fIiihp38-d6_6g</td>
      <td>0</td>
      <td>2017-02-08</td>
      <td>0</td>
      <td>lMarDJDg4-e_0YoJOKJoWA</td>
      <td>2</td>
      <td>This place....lol our server was nice.  But fo...</td>
      <td>0</td>
      <td>A21zMqdN76ueLZFpmbue0Q</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.read_excel('Data/Yelp_Selected_Businesses.xlsx', sheet_name=2)
df2.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
      <th>Unnamed: 8</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>business_id</td>
      <td>cool</td>
      <td>date</td>
      <td>funny</td>
      <td>review_id</td>
      <td>stars</td>
      <td>text</td>
      <td>useful</td>
      <td>user_id</td>
    </tr>
    <tr>
      <th>1</th>
      <td>YJ8ljUhLsz6CtT_2ORNFmg</td>
      <td>1</td>
      <td>2013-04-25</td>
      <td>0</td>
      <td>xgUz0Ck4_ciNaeIk-H8GBQ</td>
      <td>5</td>
      <td>I loved this place. Easily the most hipsters p...</td>
      <td>1</td>
      <td>6cpo8iqgnW3jnozhmY7eAA</td>
    </tr>
    <tr>
      <th>2</th>
      <td>YJ8ljUhLsz6CtT_2ORNFmg</td>
      <td>0</td>
      <td>2014-07-07</td>
      <td>0</td>
      <td>Au7MG4QlAxqq9meyKSQmaw</td>
      <td>5</td>
      <td>So my boyfriend and I came here for my birthda...</td>
      <td>0</td>
      <td>8bFE3u1dMoYXkS7ORqlssw</td>
    </tr>
    <tr>
      <th>3</th>
      <td>YJ8ljUhLsz6CtT_2ORNFmg</td>
      <td>0</td>
      <td>2015-12-04</td>
      <td>0</td>
      <td>8IQnZ54nenXjlK-FGZ82Bg</td>
      <td>5</td>
      <td>I really enjoyed their food. Went there for th...</td>
      <td>1</td>
      <td>bJmE1ms0MyZ6KHjmfZDWGw</td>
    </tr>
    <tr>
      <th>4</th>
      <td>YJ8ljUhLsz6CtT_2ORNFmg</td>
      <td>2</td>
      <td>2016-07-06</td>
      <td>1</td>
      <td>XY42LMhKoXzwtLoku4mvLA</td>
      <td>5</td>
      <td>A complete Vegas experience. We arrived right ...</td>
      <td>3</td>
      <td>PbccpC-I-8rxzF2bCDh8YA</td>
    </tr>
  </tbody>
</table>
</div>



Or the name of the sheet itself


```python
df = pd.read_excel('Data/Yelp_Selected_Businesses.xlsx', sheet_name='Biz_id_RESDU')
df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
      <th>Unnamed: 8</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>business_id</td>
      <td>cool</td>
      <td>date</td>
      <td>funny</td>
      <td>review_id</td>
      <td>stars</td>
      <td>text</td>
      <td>useful</td>
      <td>user_id</td>
    </tr>
    <tr>
      <th>1</th>
      <td>RESDUcs7fIiihp38-d6_6g</td>
      <td>0</td>
      <td>2015-09-16</td>
      <td>0</td>
      <td>gkcPdbblTvZDMSwx8nVEKw</td>
      <td>5</td>
      <td>Got here early on football Sunday 7:30am as I ...</td>
      <td>0</td>
      <td>SKteB5rgDlkkUa1Zxe1N0Q</td>
    </tr>
    <tr>
      <th>2</th>
      <td>RESDUcs7fIiihp38-d6_6g</td>
      <td>0</td>
      <td>2017-09-09</td>
      <td>0</td>
      <td>mQfl6ci46mu0xaZrkRUhlA</td>
      <td>5</td>
      <td>This buffet is amazing.  Yes, it is expensive,...</td>
      <td>0</td>
      <td>f638AHA_GoHbyDB7VFMz7A</td>
    </tr>
    <tr>
      <th>3</th>
      <td>RESDUcs7fIiihp38-d6_6g</td>
      <td>0</td>
      <td>2013-01-14</td>
      <td>0</td>
      <td>EJ7DJ8bm7-2PLFB9WKx4LQ</td>
      <td>3</td>
      <td>I was really looking forward to this but it wa...</td>
      <td>0</td>
      <td>-wVPuTiIEG85LwTK46Prpw</td>
    </tr>
    <tr>
      <th>4</th>
      <td>RESDUcs7fIiihp38-d6_6g</td>
      <td>0</td>
      <td>2017-02-08</td>
      <td>0</td>
      <td>lMarDJDg4-e_0YoJOKJoWA</td>
      <td>2</td>
      <td>This place....lol our server was nice.  But fo...</td>
      <td>0</td>
      <td>A21zMqdN76ueLZFpmbue0Q</td>
    </tr>
  </tbody>
</table>
</div>



## Loading a Full Workbook and Previewing Sheet Names
You can also load an entire excel workbook (which is a collection of spreadsheets) with the `pd.ExcelFile()` method.


```python
workbook = pd.ExcelFile('Data/Yelp_Selected_Businesses.xlsx')
workbook.sheet_names
```




    ['Biz_id_RESDU',
     'Biz_id_4JNXU',
     'Biz_id_YJ8lj',
     'Biz_id_ujHia',
     'Biz_id_na4Th']




```python
df = workbook.parse(sheet_name=1)
df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
      <th>Unnamed: 8</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>business_id</td>
      <td>cool</td>
      <td>date</td>
      <td>funny</td>
      <td>review_id</td>
      <td>stars</td>
      <td>text</td>
      <td>useful</td>
      <td>user_id</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4JNXUYY8wbaaDmk3BPzlWw</td>
      <td>0</td>
      <td>2012-06-10</td>
      <td>0</td>
      <td>wl8BO_I-is-JaMwMW5c_gQ</td>
      <td>4</td>
      <td>I booked a table here for brunch and it did no...</td>
      <td>0</td>
      <td>fo4mpUqgXL2mJqALc9AvbA</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4JNXUYY8wbaaDmk3BPzlWw</td>
      <td>0</td>
      <td>2012-01-20</td>
      <td>0</td>
      <td>cf9RrqHY9eQ9M53OPyXLtg</td>
      <td>4</td>
      <td>Came here for lunch after a long night of part...</td>
      <td>0</td>
      <td>TVvTtXwPXsvrg2KJGoOUTg</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4JNXUYY8wbaaDmk3BPzlWw</td>
      <td>0</td>
      <td>2017-05-10</td>
      <td>0</td>
      <td>BvmhSQ6WFm2Jxu01G8OpdQ</td>
      <td>5</td>
      <td>Loved the fried goat cheese in tomato sauce al...</td>
      <td>0</td>
      <td>etbAVunw-4kwr6VTRweZpA</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4JNXUYY8wbaaDmk3BPzlWw</td>
      <td>0</td>
      <td>2014-05-03</td>
      <td>0</td>
      <td>IoKp9n1489XohTV_-EJ0IQ</td>
      <td>5</td>
      <td>Love the outdoor atmosphere. Price was right, ...</td>
      <td>0</td>
      <td>vKXux2Xx3xcicTgYZoR0pg</td>
    </tr>
  </tbody>
</table>
</div>



## Saving Data
Once we have data loaded that we may want to export back out, we use the **`.to_csv()`** or **`.to_excel()`** methods of any dataframe object.


```python
df.to_csv('NewSavedView.csv', index=False) #Notice how we have to pass index=False if we do not want it included in our output
```


```python
df.to_excel('NewSavedView.xlsx')
```

## Summary

We've spent some time looking into how data importing with Pandas works and some of the methods you can use to manage the import and access of data. In the next lesson, you'll get some hands on practice!
