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
Here is an example using the penguin dataset
```python
sns.pairplot(penguin_df)
```
![image](https://github.com/aj-white/pandas-tips/assets/72359843/6c122a70-161e-4de9-8aad-f0ad91f953a4)

It's not that useful , you can use the hue parameter to categorise the data based on a column
```python
sns.pairplot(penguin_df, hue='Species')
```
![image](https://github.com/aj-white/pandas-tips/assets/72359843/9241ef34-3f63-4ce6-a5be-a84ca2a95bb5)

