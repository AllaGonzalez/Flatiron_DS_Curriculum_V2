
# Introduction - Pandas ETL

## Introduction

In this section, you will learn invaluable skills that will form the foundation of your data processing work. Before you can apply machine learning algorithms or do interesting analysis, you often must clean and transform your data into a suitable format. Such initial data wrangling processes are often refered to as Extract Transform Load (ETL). Our primary tool of choice for performing ETL and basic analyses will be the Pandas package.

## Objectives

You will be able to:

* Apply functions to columns to extract pertinent information
* Group datasets by categories or features
* Find duplicate data
* Remove duplicate data
* Create pivot tables


## Why ETL?

ETL is an essential first step to data analysis and data science. It also will form the foundation for exploratory data analysis. Often, you will be thrown a dataset that you have little to no information about. In these cases, your first step is to explore the data and get familiar with it. What are the columns? How many observations do you have? Are there missing values? If we have user level data, how can we explore aggregate trends along features like gender, race, or geography? All of these can be answered by applying ETL to transform raw datasets into alternative useful views.

## Quick ETL Examples

While you'll see complete examples and explanations for all of these techniques (and more), here's a quick preview of some ETL techniques covered in this section! For more details, continue on to future lessons!

### Reading in Data


```python
import pandas as pd
df = pd.read_csv('Yelp_Reviews.csv')
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
      <th>Unnamed: 0</th>
      <th>business_id</th>
      <th>cool</th>
      <th>date</th>
      <th>funny</th>
      <th>review_id</th>
      <th>stars</th>
      <th>text</th>
      <th>useful</th>
      <th>user_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>pomGBqfbxcqPv14c3XH-ZQ</td>
      <td>0</td>
      <td>2012-11-13</td>
      <td>0</td>
      <td>dDl8zu1vWPdKGihJrwQbpw</td>
      <td>5</td>
      <td>I love this place! My fiance And I go here atl...</td>
      <td>0</td>
      <td>msQe1u7Z_XuqjGoqhB0J5g</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>jtQARsP6P-LbkyjbO1qNGg</td>
      <td>1</td>
      <td>2014-10-23</td>
      <td>1</td>
      <td>LZp4UX5zK3e-c5ZGSeo3kA</td>
      <td>1</td>
      <td>Terrible. Dry corn bread. Rib tips were all fa...</td>
      <td>3</td>
      <td>msQe1u7Z_XuqjGoqhB0J5g</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>Ums3gaP2qM3W1XcA5r6SsQ</td>
      <td>0</td>
      <td>2014-09-05</td>
      <td>0</td>
      <td>jsDu6QEJHbwP2Blom1PLCA</td>
      <td>5</td>
      <td>Delicious healthy food. The steak is amazing. ...</td>
      <td>0</td>
      <td>msQe1u7Z_XuqjGoqhB0J5g</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>vgfcTvK81oD4r50NMjU2Ag</td>
      <td>0</td>
      <td>2011-02-25</td>
      <td>0</td>
      <td>pfavA0hr3nyqO61oupj-lA</td>
      <td>1</td>
      <td>This place sucks. The customer service is horr...</td>
      <td>2</td>
      <td>msQe1u7Z_XuqjGoqhB0J5g</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10</td>
      <td>yFumR3CWzpfvTH2FCthvVw</td>
      <td>0</td>
      <td>2016-06-15</td>
      <td>0</td>
      <td>STiFMww2z31siPY7BWNC2g</td>
      <td>5</td>
      <td>I have been an Emerald Club member for a numbe...</td>
      <td>0</td>
      <td>TlvV-xJhmh7LCwJYXkV-cg</td>
    </tr>
  </tbody>
</table>
</div>



### Appling Functions


```python
df['Review_Word_Length'] = df.text.map(lambda x: len(x.split()))
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
      <th>Unnamed: 0</th>
      <th>business_id</th>
      <th>cool</th>
      <th>date</th>
      <th>funny</th>
      <th>review_id</th>
      <th>stars</th>
      <th>text</th>
      <th>useful</th>
      <th>user_id</th>
      <th>Review_Word_Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>pomGBqfbxcqPv14c3XH-ZQ</td>
      <td>0</td>
      <td>2012-11-13</td>
      <td>0</td>
      <td>dDl8zu1vWPdKGihJrwQbpw</td>
      <td>5</td>
      <td>I love this place! My fiance And I go here atl...</td>
      <td>0</td>
      <td>msQe1u7Z_XuqjGoqhB0J5g</td>
      <td>58</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>jtQARsP6P-LbkyjbO1qNGg</td>
      <td>1</td>
      <td>2014-10-23</td>
      <td>1</td>
      <td>LZp4UX5zK3e-c5ZGSeo3kA</td>
      <td>1</td>
      <td>Terrible. Dry corn bread. Rib tips were all fa...</td>
      <td>3</td>
      <td>msQe1u7Z_XuqjGoqhB0J5g</td>
      <td>30</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>Ums3gaP2qM3W1XcA5r6SsQ</td>
      <td>0</td>
      <td>2014-09-05</td>
      <td>0</td>
      <td>jsDu6QEJHbwP2Blom1PLCA</td>
      <td>5</td>
      <td>Delicious healthy food. The steak is amazing. ...</td>
      <td>0</td>
      <td>msQe1u7Z_XuqjGoqhB0J5g</td>
      <td>30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>vgfcTvK81oD4r50NMjU2Ag</td>
      <td>0</td>
      <td>2011-02-25</td>
      <td>0</td>
      <td>pfavA0hr3nyqO61oupj-lA</td>
      <td>1</td>
      <td>This place sucks. The customer service is horr...</td>
      <td>2</td>
      <td>msQe1u7Z_XuqjGoqhB0J5g</td>
      <td>82</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10</td>
      <td>yFumR3CWzpfvTH2FCthvVw</td>
      <td>0</td>
      <td>2016-06-15</td>
      <td>0</td>
      <td>STiFMww2z31siPY7BWNC2g</td>
      <td>5</td>
      <td>I have been an Emerald Club member for a numbe...</td>
      <td>0</td>
      <td>TlvV-xJhmh7LCwJYXkV-cg</td>
      <td>32</td>
    </tr>
  </tbody>
</table>
</div>



### Grouping Data


```python
df.groupby('business_id')['stars'].mean().head()
```




    business_id
    -050d_XIor1NpCuWkbIVaQ    5.0
    -0qht1roIqleKiQkBLDkbw    1.0
    -3zffZUHoY8bQjGfPSoBKQ    5.0
    -6tvduBzjLI1ISfs3F_qTg    5.0
    -9nai28tnoylwViuJVrYEQ    5.0
    Name: stars, dtype: float64



### Checking for Duplicates


```python
#Use the keep=False to keep the duplicates and sort values to put duplicates next to each other
df[df.duplicated(keep=False)].sort_values(by='business_id')
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
      <th>Unnamed: 0</th>
      <th>business_id</th>
      <th>cool</th>
      <th>date</th>
      <th>funny</th>
      <th>review_id</th>
      <th>stars</th>
      <th>text</th>
      <th>useful</th>
      <th>user_id</th>
      <th>Review_Word_Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2232</th>
      <td>1729</td>
      <td>-GY2fx-8udXPY8qn2HVBCg</td>
      <td>0</td>
      <td>2016-08-30</td>
      <td>0</td>
      <td>yQ6P1_CvM94wMLYw1T0UWA</td>
      <td>5</td>
      <td>Just opened a new account today.  So far I am ...</td>
      <td>1</td>
      <td>sZfZGrI592euyacKUcwQYg</td>
      <td>55</td>
    </tr>
    <tr>
      <th>473</th>
      <td>1729</td>
      <td>-GY2fx-8udXPY8qn2HVBCg</td>
      <td>0</td>
      <td>2016-08-30</td>
      <td>0</td>
      <td>yQ6P1_CvM94wMLYw1T0UWA</td>
      <td>5</td>
      <td>Just opened a new account today.  So far I am ...</td>
      <td>1</td>
      <td>sZfZGrI592euyacKUcwQYg</td>
      <td>55</td>
    </tr>
    <tr>
      <th>1690</th>
      <td>754</td>
      <td>-LRlx2j9_LB3evsRRcC9MA</td>
      <td>0</td>
      <td>2017-10-07</td>
      <td>0</td>
      <td>kUqPsZmWwLIMSstGHhWssA</td>
      <td>5</td>
      <td>The vet took the time to explain what was poss...</td>
      <td>0</td>
      <td>VgaYZ7004pTwEDSDWR6u4Q</td>
      <td>33</td>
    </tr>
    <tr>
      <th>222</th>
      <td>754</td>
      <td>-LRlx2j9_LB3evsRRcC9MA</td>
      <td>0</td>
      <td>2017-10-07</td>
      <td>0</td>
      <td>kUqPsZmWwLIMSstGHhWssA</td>
      <td>5</td>
      <td>The vet took the time to explain what was poss...</td>
      <td>0</td>
      <td>VgaYZ7004pTwEDSDWR6u4Q</td>
      <td>33</td>
    </tr>
    <tr>
      <th>811</th>
      <td>2767</td>
      <td>-MKWJZnMjSit406AUKf7Pg</td>
      <td>0</td>
      <td>2015-01-03</td>
      <td>2</td>
      <td>rJhrQD3-b9GjTso0dxIkwg</td>
      <td>1</td>
      <td>Drove 37 miles on a Saturday at 12:30pm for lu...</td>
      <td>0</td>
      <td>kzP96uX8TUMmmvLtd-I3RQ</td>
      <td>18</td>
    </tr>
    <tr>
      <th>2358</th>
      <td>2767</td>
      <td>-MKWJZnMjSit406AUKf7Pg</td>
      <td>0</td>
      <td>2015-01-03</td>
      <td>2</td>
      <td>rJhrQD3-b9GjTso0dxIkwg</td>
      <td>1</td>
      <td>Drove 37 miles on a Saturday at 12:30pm for lu...</td>
      <td>0</td>
      <td>kzP96uX8TUMmmvLtd-I3RQ</td>
      <td>18</td>
    </tr>
    <tr>
      <th>898</th>
      <td>3126</td>
      <td>-eIvRc3aEvufstBumpBTPQ</td>
      <td>0</td>
      <td>2015-07-02</td>
      <td>0</td>
      <td>rn49y5dm_3sRZ5_LrODFLA</td>
      <td>5</td>
      <td>After going to several physio clinics over the...</td>
      <td>0</td>
      <td>uK0LdXjF93PuPzVgo-Jsgg</td>
      <td>95</td>
    </tr>
    <tr>
      <th>2588</th>
      <td>3126</td>
      <td>-eIvRc3aEvufstBumpBTPQ</td>
      <td>0</td>
      <td>2015-07-02</td>
      <td>0</td>
      <td>rn49y5dm_3sRZ5_LrODFLA</td>
      <td>5</td>
      <td>After going to several physio clinics over the...</td>
      <td>0</td>
      <td>uK0LdXjF93PuPzVgo-Jsgg</td>
      <td>95</td>
    </tr>
    <tr>
      <th>2074</th>
      <td>2092</td>
      <td>-lJtyCOTVInWusU9YF120A</td>
      <td>0</td>
      <td>2015-11-08</td>
      <td>0</td>
      <td>qFNtxmCldq0bUoRF1OdpQA</td>
      <td>5</td>
      <td>One of our favorite Italian restaurants. Fabul...</td>
      <td>0</td>
      <td>Ac3vNCPDwirpxSkIwtcvVA</td>
      <td>27</td>
    </tr>
    <tr>
      <th>594</th>
      <td>2092</td>
      <td>-lJtyCOTVInWusU9YF120A</td>
      <td>0</td>
      <td>2015-11-08</td>
      <td>0</td>
      <td>qFNtxmCldq0bUoRF1OdpQA</td>
      <td>5</td>
      <td>One of our favorite Italian restaurants. Fabul...</td>
      <td>0</td>
      <td>Ac3vNCPDwirpxSkIwtcvVA</td>
      <td>27</td>
    </tr>
    <tr>
      <th>467</th>
      <td>1707</td>
      <td>01fuY2NNscttoTxOYbuZXw</td>
      <td>0</td>
      <td>2016-07-08</td>
      <td>0</td>
      <td>TUFmvhAynUbjSbOJa79sRw</td>
      <td>5</td>
      <td>Loved the food! Atmosphere funky and artsy. St...</td>
      <td>0</td>
      <td>MejkKZgdUNfekUoNO1QJOA</td>
      <td>45</td>
    </tr>
    <tr>
      <th>1489</th>
      <td>1707</td>
      <td>01fuY2NNscttoTxOYbuZXw</td>
      <td>0</td>
      <td>2016-07-08</td>
      <td>0</td>
      <td>TUFmvhAynUbjSbOJa79sRw</td>
      <td>5</td>
      <td>Loved the food! Atmosphere funky and artsy. St...</td>
      <td>0</td>
      <td>MejkKZgdUNfekUoNO1QJOA</td>
      <td>45</td>
    </tr>
    <tr>
      <th>1473</th>
      <td>1527</td>
      <td>04u-szAykldu-caSDHQaKA</td>
      <td>0</td>
      <td>2012-02-09</td>
      <td>0</td>
      <td>VkEeSwaqHgp6VFeANMoFow</td>
      <td>4</td>
      <td>I have been looking for a good Chinese restrai...</td>
      <td>0</td>
      <td>iNSL4q8MUvZ1ItVGboPpbQ</td>
      <td>19</td>
    </tr>
    <tr>
      <th>398</th>
      <td>1527</td>
      <td>04u-szAykldu-caSDHQaKA</td>
      <td>0</td>
      <td>2012-02-09</td>
      <td>0</td>
      <td>VkEeSwaqHgp6VFeANMoFow</td>
      <td>4</td>
      <td>I have been looking for a good Chinese restrai...</td>
      <td>0</td>
      <td>iNSL4q8MUvZ1ItVGboPpbQ</td>
      <td>19</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>744</td>
      <td>07F9bkUm3cs83CzGvTi0TA</td>
      <td>1</td>
      <td>2015-03-15</td>
      <td>0</td>
      <td>wgr_hOfIWlXR-glOC-qKYQ</td>
      <td>5</td>
      <td>Kudos to Charlotte Motor Speedway!! They took ...</td>
      <td>1</td>
      <td>Cxv3SNudPrCavvHJfIbwhQ</td>
      <td>384</td>
    </tr>
    <tr>
      <th>215</th>
      <td>744</td>
      <td>07F9bkUm3cs83CzGvTi0TA</td>
      <td>1</td>
      <td>2015-03-15</td>
      <td>0</td>
      <td>wgr_hOfIWlXR-glOC-qKYQ</td>
      <td>5</td>
      <td>Kudos to Charlotte Motor Speedway!! They took ...</td>
      <td>1</td>
      <td>Cxv3SNudPrCavvHJfIbwhQ</td>
      <td>384</td>
    </tr>
    <tr>
      <th>2520</th>
      <td>2202</td>
      <td>0QBFtNNj9RIggZGeivcbEg</td>
      <td>0</td>
      <td>2013-07-23</td>
      <td>0</td>
      <td>6bzlzJj3jrbWSnXtv80D_A</td>
      <td>5</td>
      <td>Great food and service. Spinach enchiladas are...</td>
      <td>0</td>
      <td>VTjCebjbadCMAGRoXvs7Zw</td>
      <td>13</td>
    </tr>
    <tr>
      <th>629</th>
      <td>2202</td>
      <td>0QBFtNNj9RIggZGeivcbEg</td>
      <td>0</td>
      <td>2013-07-23</td>
      <td>0</td>
      <td>6bzlzJj3jrbWSnXtv80D_A</td>
      <td>5</td>
      <td>Great food and service. Spinach enchiladas are...</td>
      <td>0</td>
      <td>VTjCebjbadCMAGRoXvs7Zw</td>
      <td>13</td>
    </tr>
    <tr>
      <th>871</th>
      <td>3004</td>
      <td>0bbWKI1lA-bmEeeWOrDmSA</td>
      <td>0</td>
      <td>2015-11-12</td>
      <td>0</td>
      <td>71xNE0qpjhgEz44PgbfIDA</td>
      <td>3</td>
      <td>It's an ok place. Quantities are greater than ...</td>
      <td>0</td>
      <td>hjHrV1WzO8RDRYJ-ep2OZA</td>
      <td>64</td>
    </tr>
    <tr>
      <th>2192</th>
      <td>3004</td>
      <td>0bbWKI1lA-bmEeeWOrDmSA</td>
      <td>0</td>
      <td>2015-11-12</td>
      <td>0</td>
      <td>71xNE0qpjhgEz44PgbfIDA</td>
      <td>3</td>
      <td>It's an ok place. Quantities are greater than ...</td>
      <td>0</td>
      <td>hjHrV1WzO8RDRYJ-ep2OZA</td>
      <td>64</td>
    </tr>
    <tr>
      <th>1992</th>
      <td>3243</td>
      <td>0dFOy1BeJWuYTyIsi-gAqw</td>
      <td>0</td>
      <td>2015-05-10</td>
      <td>1</td>
      <td>ed8to80UuSExhgfJOyWphQ</td>
      <td>1</td>
      <td>Well I had to give a star because required. Th...</td>
      <td>1</td>
      <td>dOsSS5r_YXViQznl6EvXlg</td>
      <td>42</td>
    </tr>
    <tr>
      <th>940</th>
      <td>3243</td>
      <td>0dFOy1BeJWuYTyIsi-gAqw</td>
      <td>0</td>
      <td>2015-05-10</td>
      <td>1</td>
      <td>ed8to80UuSExhgfJOyWphQ</td>
      <td>1</td>
      <td>Well I had to give a star because required. Th...</td>
      <td>1</td>
      <td>dOsSS5r_YXViQznl6EvXlg</td>
      <td>42</td>
    </tr>
    <tr>
      <th>859</th>
      <td>2953</td>
      <td>0yAJCh0TBZcnZkdZWZ6bVQ</td>
      <td>0</td>
      <td>2016-01-18</td>
      <td>0</td>
      <td>qrzJrDPyfqP7djhb6sxb3A</td>
      <td>4</td>
      <td>i've been going for over a year. great service...</td>
      <td>0</td>
      <td>Y5DIwt-653VndVu53ATpLQ</td>
      <td>37</td>
    </tr>
    <tr>
      <th>1435</th>
      <td>2953</td>
      <td>0yAJCh0TBZcnZkdZWZ6bVQ</td>
      <td>0</td>
      <td>2016-01-18</td>
      <td>0</td>
      <td>qrzJrDPyfqP7djhb6sxb3A</td>
      <td>4</td>
      <td>i've been going for over a year. great service...</td>
      <td>0</td>
      <td>Y5DIwt-653VndVu53ATpLQ</td>
      <td>37</td>
    </tr>
    <tr>
      <th>1538</th>
      <td>4134</td>
      <td>19VNsxhnPZ11zc0KBauonQ</td>
      <td>0</td>
      <td>2015-02-03</td>
      <td>0</td>
      <td>iXEO9493AVcDZmOkGJpIgw</td>
      <td>1</td>
      <td>worst customer service.Mainly the manager Matt...</td>
      <td>1</td>
      <td>z7dWikbkqL7NelG4JeSt4g</td>
      <td>20</td>
    </tr>
    <tr>
      <th>1169</th>
      <td>4134</td>
      <td>19VNsxhnPZ11zc0KBauonQ</td>
      <td>0</td>
      <td>2015-02-03</td>
      <td>0</td>
      <td>iXEO9493AVcDZmOkGJpIgw</td>
      <td>1</td>
      <td>worst customer service.Mainly the manager Matt...</td>
      <td>1</td>
      <td>z7dWikbkqL7NelG4JeSt4g</td>
      <td>20</td>
    </tr>
    <tr>
      <th>1678</th>
      <td>3132</td>
      <td>1ForN8iXqYZ_dZZcOkvVeA</td>
      <td>0</td>
      <td>2014-03-29</td>
      <td>0</td>
      <td>9vEk6nrlA8fcej0SsbD3gA</td>
      <td>5</td>
      <td>This was the cutest little diner I have ever b...</td>
      <td>1</td>
      <td>ZcgHNMGUKp-J9hRqgoDx6A</td>
      <td>34</td>
    </tr>
    <tr>
      <th>903</th>
      <td>3132</td>
      <td>1ForN8iXqYZ_dZZcOkvVeA</td>
      <td>0</td>
      <td>2014-03-29</td>
      <td>0</td>
      <td>9vEk6nrlA8fcej0SsbD3gA</td>
      <td>5</td>
      <td>This was the cutest little diner I have ever b...</td>
      <td>1</td>
      <td>ZcgHNMGUKp-J9hRqgoDx6A</td>
      <td>34</td>
    </tr>
    <tr>
      <th>1316</th>
      <td>4652</td>
      <td>1HnYxHZw2icWQ7-T4AmQ0Q</td>
      <td>0</td>
      <td>2017-06-18</td>
      <td>0</td>
      <td>fekMspN8qzJtai03tCUUvQ</td>
      <td>5</td>
      <td>Awesome place!!! Love that they have old style...</td>
      <td>0</td>
      <td>vuJ39vRaVZTgkT6I4L1jjA</td>
      <td>24</td>
    </tr>
    <tr>
      <th>1536</th>
      <td>4652</td>
      <td>1HnYxHZw2icWQ7-T4AmQ0Q</td>
      <td>0</td>
      <td>2017-06-18</td>
      <td>0</td>
      <td>fekMspN8qzJtai03tCUUvQ</td>
      <td>5</td>
      <td>Awesome place!!! Love that they have old style...</td>
      <td>0</td>
      <td>vuJ39vRaVZTgkT6I4L1jjA</td>
      <td>24</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1077</th>
      <td>3776</td>
      <td>wkChwNgC7YSc8KZgXiGT0Q</td>
      <td>1</td>
      <td>2016-09-12</td>
      <td>0</td>
      <td>9n1T-wVxsfQZbQ3cdRf46A</td>
      <td>5</td>
      <td>Magnificent views at sunset. Excellent appetiz...</td>
      <td>1</td>
      <td>ceIxPqfjhZbMdht4tGk7TQ</td>
      <td>22</td>
    </tr>
    <tr>
      <th>2452</th>
      <td>3776</td>
      <td>wkChwNgC7YSc8KZgXiGT0Q</td>
      <td>1</td>
      <td>2016-09-12</td>
      <td>0</td>
      <td>9n1T-wVxsfQZbQ3cdRf46A</td>
      <td>5</td>
      <td>Magnificent views at sunset. Excellent appetiz...</td>
      <td>1</td>
      <td>ceIxPqfjhZbMdht4tGk7TQ</td>
      <td>22</td>
    </tr>
    <tr>
      <th>2311</th>
      <td>1777</td>
      <td>wke61EJKd1Yw6q1BR1npZw</td>
      <td>0</td>
      <td>2014-07-23</td>
      <td>0</td>
      <td>B03DD42snaOU-mbDtntohw</td>
      <td>5</td>
      <td>Now this is a great bar! Bartenders were perso...</td>
      <td>0</td>
      <td>9zVMFFM_J51ZaS2wMzPziA</td>
      <td>49</td>
    </tr>
    <tr>
      <th>482</th>
      <td>1777</td>
      <td>wke61EJKd1Yw6q1BR1npZw</td>
      <td>0</td>
      <td>2014-07-23</td>
      <td>0</td>
      <td>B03DD42snaOU-mbDtntohw</td>
      <td>5</td>
      <td>Now this is a great bar! Bartenders were perso...</td>
      <td>0</td>
      <td>9zVMFFM_J51ZaS2wMzPziA</td>
      <td>49</td>
    </tr>
    <tr>
      <th>2330</th>
      <td>3749</td>
      <td>x5iQFVJkFl7fSXC6uVjwPw</td>
      <td>0</td>
      <td>2012-06-18</td>
      <td>1</td>
      <td>6qTtineIwJXZHVDmHtKDZg</td>
      <td>1</td>
      <td>We just moved to Mesa and were happy to hear a...</td>
      <td>3</td>
      <td>fOCV2evqdjDpfI-6ULvr5Q</td>
      <td>97</td>
    </tr>
    <tr>
      <th>1064</th>
      <td>3749</td>
      <td>x5iQFVJkFl7fSXC6uVjwPw</td>
      <td>0</td>
      <td>2012-06-18</td>
      <td>1</td>
      <td>6qTtineIwJXZHVDmHtKDZg</td>
      <td>1</td>
      <td>We just moved to Mesa and were happy to hear a...</td>
      <td>3</td>
      <td>fOCV2evqdjDpfI-6ULvr5Q</td>
      <td>97</td>
    </tr>
    <tr>
      <th>1430</th>
      <td>2894</td>
      <td>xVEtGucSRLk5pxxN0t4i6g</td>
      <td>1</td>
      <td>2009-06-09</td>
      <td>0</td>
      <td>9bfnqemozlvKzbmc8gbItw</td>
      <td>5</td>
      <td>The best piece of meat I have ever had!!! This...</td>
      <td>1</td>
      <td>r2hoX58seF3kwP-U2W__QA</td>
      <td>59</td>
    </tr>
    <tr>
      <th>845</th>
      <td>2894</td>
      <td>xVEtGucSRLk5pxxN0t4i6g</td>
      <td>1</td>
      <td>2009-06-09</td>
      <td>0</td>
      <td>9bfnqemozlvKzbmc8gbItw</td>
      <td>5</td>
      <td>The best piece of meat I have ever had!!! This...</td>
      <td>1</td>
      <td>r2hoX58seF3kwP-U2W__QA</td>
      <td>59</td>
    </tr>
    <tr>
      <th>556</th>
      <td>1985</td>
      <td>xkiYAerQQXL25legNhVsSw</td>
      <td>0</td>
      <td>2015-04-26</td>
      <td>0</td>
      <td>cIyDRhWeHtZ_pDQBe4sG8Q</td>
      <td>4</td>
      <td>The pizza was ok and the chips as an appetizer...</td>
      <td>0</td>
      <td>zdG-3ABz7-mv1P3cs2_Rfg</td>
      <td>23</td>
    </tr>
    <tr>
      <th>1943</th>
      <td>1985</td>
      <td>xkiYAerQQXL25legNhVsSw</td>
      <td>0</td>
      <td>2015-04-26</td>
      <td>0</td>
      <td>cIyDRhWeHtZ_pDQBe4sG8Q</td>
      <td>4</td>
      <td>The pizza was ok and the chips as an appetizer...</td>
      <td>0</td>
      <td>zdG-3ABz7-mv1P3cs2_Rfg</td>
      <td>23</td>
    </tr>
    <tr>
      <th>1789</th>
      <td>1984</td>
      <td>xmgLfJ5Jo6hHjY61hzO_EQ</td>
      <td>0</td>
      <td>2014-03-13</td>
      <td>0</td>
      <td>1dartEoF9n7-Fcgx7DWilA</td>
      <td>1</td>
      <td>Went on a Sunday and the gal did not use sanit...</td>
      <td>0</td>
      <td>Xu6kxX18Uv14MSZTY7PSgw</td>
      <td>57</td>
    </tr>
    <tr>
      <th>555</th>
      <td>1984</td>
      <td>xmgLfJ5Jo6hHjY61hzO_EQ</td>
      <td>0</td>
      <td>2014-03-13</td>
      <td>0</td>
      <td>1dartEoF9n7-Fcgx7DWilA</td>
      <td>1</td>
      <td>Went on a Sunday and the gal did not use sanit...</td>
      <td>0</td>
      <td>Xu6kxX18Uv14MSZTY7PSgw</td>
      <td>57</td>
    </tr>
    <tr>
      <th>788</th>
      <td>2669</td>
      <td>y9hgPwF68tpWEp6onX-3TQ</td>
      <td>0</td>
      <td>2017-10-26</td>
      <td>0</td>
      <td>aNIPAlsp_cO1VhyP8ReJ7g</td>
      <td>3</td>
      <td>I wanted to give this place 5 stars the beer i...</td>
      <td>0</td>
      <td>U_SbWcSZRLfkvZt3jshKJA</td>
      <td>52</td>
    </tr>
    <tr>
      <th>2499</th>
      <td>2669</td>
      <td>y9hgPwF68tpWEp6onX-3TQ</td>
      <td>0</td>
      <td>2017-10-26</td>
      <td>0</td>
      <td>aNIPAlsp_cO1VhyP8ReJ7g</td>
      <td>3</td>
      <td>I wanted to give this place 5 stars the beer i...</td>
      <td>0</td>
      <td>U_SbWcSZRLfkvZt3jshKJA</td>
      <td>52</td>
    </tr>
    <tr>
      <th>1359</th>
      <td>4846</td>
      <td>yADOyFmSlHuixlQ4MtHhcQ</td>
      <td>0</td>
      <td>2017-10-05</td>
      <td>0</td>
      <td>pE6BNYU3mEi9y1pS5fnPpQ</td>
      <td>5</td>
      <td>The servers in this place are great they all k...</td>
      <td>0</td>
      <td>06LACu59TbIHOXYn14CkPA</td>
      <td>39</td>
    </tr>
    <tr>
      <th>1655</th>
      <td>4846</td>
      <td>yADOyFmSlHuixlQ4MtHhcQ</td>
      <td>0</td>
      <td>2017-10-05</td>
      <td>0</td>
      <td>pE6BNYU3mEi9y1pS5fnPpQ</td>
      <td>5</td>
      <td>The servers in this place are great they all k...</td>
      <td>0</td>
      <td>06LACu59TbIHOXYn14CkPA</td>
      <td>39</td>
    </tr>
    <tr>
      <th>1414</th>
      <td>3046</td>
      <td>yQUXMWSA8H7wvkLa4iCD8g</td>
      <td>0</td>
      <td>2014-08-28</td>
      <td>0</td>
      <td>KmKCR_cHmAYA12Uy3XPHCA</td>
      <td>2</td>
      <td>Rude waitress and slow service. No offers for ...</td>
      <td>1</td>
      <td>KeYB7tU5F5PFb7X1QoWJ6Q</td>
      <td>78</td>
    </tr>
    <tr>
      <th>883</th>
      <td>3046</td>
      <td>yQUXMWSA8H7wvkLa4iCD8g</td>
      <td>0</td>
      <td>2014-08-28</td>
      <td>0</td>
      <td>KmKCR_cHmAYA12Uy3XPHCA</td>
      <td>2</td>
      <td>Rude waitress and slow service. No offers for ...</td>
      <td>1</td>
      <td>KeYB7tU5F5PFb7X1QoWJ6Q</td>
      <td>78</td>
    </tr>
    <tr>
      <th>2373</th>
      <td>3509</td>
      <td>yY3jNsrpCyKTqQuRuLV8gw</td>
      <td>0</td>
      <td>2017-07-16</td>
      <td>0</td>
      <td>rWc72Fx8ZKuat39dI-JLyw</td>
      <td>5</td>
      <td>Amazing food and drinks. I've tried multiple m...</td>
      <td>0</td>
      <td>SGc1Qk_LR8G8WEEA5QafEw</td>
      <td>26</td>
    </tr>
    <tr>
      <th>989</th>
      <td>3509</td>
      <td>yY3jNsrpCyKTqQuRuLV8gw</td>
      <td>0</td>
      <td>2017-07-16</td>
      <td>0</td>
      <td>rWc72Fx8ZKuat39dI-JLyw</td>
      <td>5</td>
      <td>Amazing food and drinks. I've tried multiple m...</td>
      <td>0</td>
      <td>SGc1Qk_LR8G8WEEA5QafEw</td>
      <td>26</td>
    </tr>
    <tr>
      <th>2129</th>
      <td>3041</td>
      <td>ynyDiLHzTdf4du9xMhscxg</td>
      <td>0</td>
      <td>2015-10-30</td>
      <td>0</td>
      <td>M-0AaEDTwBSIv_HJu4-pjw</td>
      <td>5</td>
      <td>Rachael is an artist! I've been going to her f...</td>
      <td>0</td>
      <td>lYXRVN2TJDEVB39G3HzplA</td>
      <td>31</td>
    </tr>
    <tr>
      <th>882</th>
      <td>3041</td>
      <td>ynyDiLHzTdf4du9xMhscxg</td>
      <td>0</td>
      <td>2015-10-30</td>
      <td>0</td>
      <td>M-0AaEDTwBSIv_HJu4-pjw</td>
      <td>5</td>
      <td>Rachael is an artist! I've been going to her f...</td>
      <td>0</td>
      <td>lYXRVN2TJDEVB39G3HzplA</td>
      <td>31</td>
    </tr>
    <tr>
      <th>1515</th>
      <td>2659</td>
      <td>zJGtD3y-pAIGNId4codEEg</td>
      <td>1</td>
      <td>2013-08-11</td>
      <td>1</td>
      <td>lwInYPtM4M2jfAftXk-xlA</td>
      <td>4</td>
      <td>We've been to Otro many times. Stick with the ...</td>
      <td>1</td>
      <td>BjmYO90f7e7oiwyoffC82w</td>
      <td>150</td>
    </tr>
    <tr>
      <th>785</th>
      <td>2659</td>
      <td>zJGtD3y-pAIGNId4codEEg</td>
      <td>1</td>
      <td>2013-08-11</td>
      <td>1</td>
      <td>lwInYPtM4M2jfAftXk-xlA</td>
      <td>4</td>
      <td>We've been to Otro many times. Stick with the ...</td>
      <td>1</td>
      <td>BjmYO90f7e7oiwyoffC82w</td>
      <td>150</td>
    </tr>
    <tr>
      <th>1521</th>
      <td>2193</td>
      <td>zKw09ftu1730wEIZBZPoFg</td>
      <td>3</td>
      <td>2015-01-04</td>
      <td>0</td>
      <td>JV-yxKxMFp-d0rLDc_2_6w</td>
      <td>5</td>
      <td>So relaxing combined with the meditation  and ...</td>
      <td>5</td>
      <td>3mZFkwfa6XV0BBazRTva9w</td>
      <td>31</td>
    </tr>
    <tr>
      <th>623</th>
      <td>2193</td>
      <td>zKw09ftu1730wEIZBZPoFg</td>
      <td>3</td>
      <td>2015-01-04</td>
      <td>0</td>
      <td>JV-yxKxMFp-d0rLDc_2_6w</td>
      <td>5</td>
      <td>So relaxing combined with the meditation  and ...</td>
      <td>5</td>
      <td>3mZFkwfa6XV0BBazRTva9w</td>
      <td>31</td>
    </tr>
    <tr>
      <th>1483</th>
      <td>496</td>
      <td>zg5rJfgT4jhzg1d6r2twnA</td>
      <td>0</td>
      <td>2014-06-21</td>
      <td>0</td>
      <td>Zbj0HgdN3AT4l-mbH-EfjA</td>
      <td>3</td>
      <td>Burger week\r\n\r\n1. Blazing Pineapple Burger...</td>
      <td>0</td>
      <td>UGW-9bbBEB3eP1o6mWD_WA</td>
      <td>62</td>
    </tr>
    <tr>
      <th>118</th>
      <td>496</td>
      <td>zg5rJfgT4jhzg1d6r2twnA</td>
      <td>0</td>
      <td>2014-06-21</td>
      <td>0</td>
      <td>Zbj0HgdN3AT4l-mbH-EfjA</td>
      <td>3</td>
      <td>Burger week\r\n\r\n1. Blazing Pineapple Burger...</td>
      <td>0</td>
      <td>UGW-9bbBEB3eP1o6mWD_WA</td>
      <td>62</td>
    </tr>
    <tr>
      <th>274</th>
      <td>988</td>
      <td>ziv21pDfyrgdhlrlNIgDfg</td>
      <td>0</td>
      <td>2016-08-11</td>
      <td>0</td>
      <td>fus9odxu9bjE2lSxfwNfdw</td>
      <td>5</td>
      <td>Get this!!!  Wow Karlo is amazing and best cus...</td>
      <td>2</td>
      <td>ywjqPgnMrDZKOhA33v92Cw</td>
      <td>62</td>
    </tr>
    <tr>
      <th>1833</th>
      <td>988</td>
      <td>ziv21pDfyrgdhlrlNIgDfg</td>
      <td>0</td>
      <td>2016-08-11</td>
      <td>0</td>
      <td>fus9odxu9bjE2lSxfwNfdw</td>
      <td>5</td>
      <td>Get this!!!  Wow Karlo is amazing and best cus...</td>
      <td>2</td>
      <td>ywjqPgnMrDZKOhA33v92Cw</td>
      <td>62</td>
    </tr>
  </tbody>
</table>
<p>666 rows × 11 columns</p>
</div>



### Removing Duplicates


```python
df = df[df.duplicated()]
```

### Rechecking for Duplicates


```python
#Duplicates should no longer exist
df[df.duplicated(keep=False)].sort_values(by='business_id')
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
      <th>Unnamed: 0</th>
      <th>business_id</th>
      <th>cool</th>
      <th>date</th>
      <th>funny</th>
      <th>review_id</th>
      <th>stars</th>
      <th>text</th>
      <th>useful</th>
      <th>user_id</th>
      <th>Review_Word_Length</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>



### Creating Pivot Tables


```python
#This transforms the data into a person by person spreadsheet and what stars they gave various restaurants
#Most values are NaN (null or missing) because people only review a few restaurants of those that exist
usr_reviews = df.pivot(index='user_id', columns='business_id', values='stars')
usr_reviews.head()
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
      <th>business_id</th>
      <th>-GY2fx-8udXPY8qn2HVBCg</th>
      <th>-LRlx2j9_LB3evsRRcC9MA</th>
      <th>-MKWJZnMjSit406AUKf7Pg</th>
      <th>-eIvRc3aEvufstBumpBTPQ</th>
      <th>-lJtyCOTVInWusU9YF120A</th>
      <th>01fuY2NNscttoTxOYbuZXw</th>
      <th>04u-szAykldu-caSDHQaKA</th>
      <th>07F9bkUm3cs83CzGvTi0TA</th>
      <th>0QBFtNNj9RIggZGeivcbEg</th>
      <th>0bbWKI1lA-bmEeeWOrDmSA</th>
      <th>...</th>
      <th>xmgLfJ5Jo6hHjY61hzO_EQ</th>
      <th>y9hgPwF68tpWEp6onX-3TQ</th>
      <th>yADOyFmSlHuixlQ4MtHhcQ</th>
      <th>yQUXMWSA8H7wvkLa4iCD8g</th>
      <th>yY3jNsrpCyKTqQuRuLV8gw</th>
      <th>ynyDiLHzTdf4du9xMhscxg</th>
      <th>zJGtD3y-pAIGNId4codEEg</th>
      <th>zKw09ftu1730wEIZBZPoFg</th>
      <th>zg5rJfgT4jhzg1d6r2twnA</th>
      <th>ziv21pDfyrgdhlrlNIgDfg</th>
    </tr>
    <tr>
      <th>user_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>-Zdxj4wuj4D_899B7tPE3g</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>-ciBvC2RcMtt3JeRW0NDvg</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>06LACu59TbIHOXYn14CkPA</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>0XKTRsa8Y1A3RHJB5LhuUg</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17YRCR1n1FcLAerv2qtmkw</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 331 columns</p>
</div>



## Summary

In this brief introduction, you learned the acronym ETL and got to preview a few examples of ETL processes using pandas. In the upcoming lessons you'll get a much richer understanding of these and other techniques for wrangling your data!
