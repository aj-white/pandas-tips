# Methods to visualise more data easily
Taken from Matt Harrisons LinkedIn Learning Course [Python Statistics Essential Training](https://github.com/LinkedInLearning/python-statistics-essential-training-4433355).

### Option Context Manager
I knew about `pandas.set_option()` but did not know about the context manager

```python
with pd.option_context('display.min_rows', 20, 'display.max_columns', 50):
    display(df
      .query('`column A`.isna()')
    )
```

### Jupyter help
adding a `?` after a method will show the docs
```python
df.style.set_sticky?
```
