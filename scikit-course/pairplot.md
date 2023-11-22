# Seaborn Pairplot

## What is it  ?

From the docs
> Plot pairwise relationships in a dataset.
> By default, this function will create a grid of Axes such that each numeric variable in data will by shared across the y-axes across a single row and the x-axes across a single column. The diagonal plots are treated differently: a univariate distribution plot is drawn to show the marginal distribution of the data in each column.
>

Shows relationships between *numerical* data.
Creates a grid of plots, on the diagonal is the data distribution for each numerical column.
The rest of the plots shows the relationship of the data.

### Example
Here is an example using the penguin dataset (plot has been truncated due to size)
```python
sns.pairplot(penguin_df)
```
![image](https://github.com/aj-white/pandas-tips/assets/72359843/6c122a70-161e-4de9-8aad-f0ad91f953a4)

It's not that useful , you can use the hue parameter to categorise the data based on a column
```python
sns.pairplot(penguin_df, hue='Species')
```
![image](https://github.com/aj-white/pandas-tips/assets/72359843/9241ef34-3f63-4ce6-a5be-a84ca2a95bb5)

You will notice that the plot has been truncated due to its size, you can provide a list of columns to filter the output (**NB** remember columns must be numeric)
```python
cols = ["Culmen Length (mm)", "Culmen Depth (mm)", "Flipper Length (mm)", "Body Mass (g)"]
sns.pairplot(df, hue='Species', vars=cols)
```
![image](https://github.com/aj-white/pandas-tips/assets/72359843/302539dd-8ba5-4fed-9dd5-7da286248fcb)

You can also change the type of plot
```python
sns.pairplot(df, hue='Species', vars=cols, kind='kde')
```
#### KDE - Kernel Density Estimates
![image](https://github.com/aj-white/pandas-tips/assets/72359843/9be1e23f-049d-45ec-af04-8e946f3c61d1)

#### hist - Histograms (2D)
```python
sns.pairplot(df, hue='Species', vars=cols, kind='hist')
```
![image](https://github.com/aj-white/pandas-tips/assets/72359843/7293d9d7-d04b-4178-95b8-f90e8d91ac72)

#### reg - Regression Lines over Scatter Plot
```python
sns.pairplot(df, hue='Species', vars=cols, kind='reg')
```
![image](https://github.com/aj-white/pandas-tips/assets/72359843/0a054b3a-afec-480a-b277-48b664d7c774)

You can also change the diagonal plots, in this case we've got scatter and histograms
```python
sns.pairplot(df, hue='Species', vars=cols, kind='scatter', diag_kind='hist')
```
![image](https://github.com/aj-white/pandas-tips/assets/72359843/31a70e58-9837-475c-91be-fa72a28e2bea)

If the scatter plots overlap you can increase the height of each subplot
```pyton
sns.pairplot(df, hue='Species', vars=cols, kind='scatter', diag_kind='hist', height=4)
```

It's also possible to change the markers for each group using [matplotlib marker codes](https://matplotlib.org/stable/api/markers_api.html)
```python
sns.pairplot(df, hue='Species', vars=cols, kind="scatter", diag_kind='hist', markers=['o', 'p', '*'])
```
![image](https://github.com/aj-white/pandas-tips/assets/72359843/4a831ca1-ada2-4b62-b556-bac78bf8b27a)

You can also use the pallete option to choose a seaborn colour palette.

### Further Info

[Seaborn pairplot docs](https://seaborn.pydata.org/generated/seaborn.pairplot.html)

Method signature
```python
seaborn.pairplot(
  data, *, hue=None, hue_order=None, palette=None, vars=None, x_vars=None, y_vars=None,
  kind='scatter', diag_kind='auto', markers=None, height=2.5, aspect=1,
  corner=False, dropna=False, plot_kws=None, diag_kws=None, grid_kws=None, size=None
)
```
