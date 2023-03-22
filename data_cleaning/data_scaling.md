# Data Scaling

## Scaling vs Normalisation

- **Scaling** - Changes the *range* of the data
- **Normalisation** - Changes the shape of the distribution of your data


## Maximum absolute scaling

Scales the data to the maximum value, essentially it divdes every data point by the maximum value, resulting in a range [-1, 1]

```python
(
    df.assign(
        Max_abs_scale = lambda df_: df_.column / df_.column.abs().max()
    )
)
```

## Min-Max Scaling

Rescales the data to a range [0, 1] by subracting the minimum value and dividing by the range of values

```python
(
    df.assign(
        Min_max_scaling = lambda df_ : (df_.column - df_.column.min()) / (df_.column.max() - df_.column.min())
    )
)
```

## Z-Score scaling

Standardises the data by measureing how many standard deviations a data point is from the mean.

```python
(
    df.assign(
        Z_score = lambda df_: (df_.column - df_.column.mean()) / df_.column.std()
    )
)
```


