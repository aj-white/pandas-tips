# String mainipulation in Pandas

### Chaining Split Expand

Unpack a dataframe into current dataframe that contains result of spliting column

```python
(
    df.assign(**pd.DataFrame(lambda df_: df_.column.split(",", n=1, expand=True), columns=[expected, column, names]))
)
```
