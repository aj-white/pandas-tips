# Validate data

## Check for consistent mapping of two columns
Where two columns have a consistent mapping

Consider this df:

| Index | Col1 | Col2 |
| ------|------|------|
|0|train|red|
|1|train|red|
|2|car|blue|
|3|van|green|
|4|train|green|
|5|car|blue|

In Col2 train should be green.
The following snippet

```python
df.loc[~df.sort_values(["Col1", "Col2"]).duplicated(keep=False)]
```
This will return:
| Index | Col1 | Col2 |
| ------|------|------|
|3|van|green|
|4|train|green|
