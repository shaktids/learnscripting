---
title: "Panda Series"
description: "class pandas. Series ( data=None , index=None , dtype=None , name=None , copy=False , fastpath=False )[[source]](https://github.com/pandas…"
lang: other
categories: ["Machine Learning"]
author: "Shakti Das"
pubDate: 2022-09-08T16:38:19Z
legacy: true
wpId: 2248
---

*class*`pandas.``Series`(*data=None*, *index=None*, *dtype=None*, *name=None*, *copy=False*, *fastpath=False*)[[source]](https://github.com/pandas-dev/pandas/blob/v1.2.1/pandas/core/series.py#L149-L4970)

One-dimensional ndarray with axis labels (including time series).

Labels need not be unique but must be a hashable type. The object supports both integer- and label-based indexing and provides a host of methods for performing operations involving the index. Statistical methods from ndarray have been overridden to automatically exclude missing data (currently represented as NaN).

Operations between Series (+, -, /, *, \**) align values based on their associated index values– they need not be the same length. The resulting index will be the sorted union of the two indexes. Parameters**data**array-like, Iterable, dict, or scalar value

Contains data stored in Series. If data is a dict, argument order is maintained.**index**array-like or Index (1d)

Values must be hashable and have the same length as data. Non-unique index values are allowed. Will default to RangeIndex (0, 1, 2, …, n) if not provided. If data is dict-like and index is None, then the values in the index are used to reindex the Series after it is created using the keys in the data.**dtype**str, numpy.dtype, or ExtensionDtype, optional

Data type for the output Series. If not specified, this will be inferred from data. See the [user guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#basics-dtypes) for more usages.**name**str, optional

The name to give to the Series.**copy**bool, default False

Copy input data.

Attributes

|  |  |  |
| --- | --- | --- |
| S.N | Function | Meaning |
| 1 | [`T`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.T.html#pandas.Series.T) | Return the transpose, which is by definition self. |
| 2 | [`array`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.array.html#pandas.Series.array) | The ExtensionArray of the data backing this Series or Index. |
| 3 | [`at`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.at.html#pandas.Series.at) | Access a single value for a row/column label pair. |
| 4 | [`attrs`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.attrs.html#pandas.Series.attrs) | Dictionary of global attributes of this dataset. |
| 5 | [`axes`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.axes.html#pandas.Series.axes) | Return a list of the row axis labels. |
| 6 | [`dtype`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dtype.html#pandas.Series.dtype) | Return the dtype object of the underlying data. |
| 7 | [`dtypes`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dtypes.html#pandas.Series.dtypes) | Return the dtype object of the underlying data. |
| 8 | [`flags`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.flags.html#pandas.Series.flags) | Get the properties associated with this pandas object. |
| 9 | [`hasnans`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.hasnans.html#pandas.Series.hasnans) | Return if I have any nans; enables various perf speedups. |
| 10 | [`iat`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.iat.html#pandas.Series.iat) | Access a single value for a row/column pair by integer position. |
| 11 | [`iloc`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.iloc.html#pandas.Series.iloc) | Purely integer-location based indexing for selection by position. |
| 12 | [`index`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.index.html#pandas.Series.index) | The index (axis labels) of the Series. |
| 13 | [`is_monotonic`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.is_monotonic.html#pandas.Series.is_monotonic) | Return boolean if values in the object are monotonic\_increasing. |
| 14 | [`is_monotonic_decreasing`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.is_monotonic_decreasing.html#pandas.Series.is_monotonic_decreasing) | Return boolean if values in the object are monotonic\_decreasing. |
| 15 | [`is_monotonic_increasing`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.is_monotonic_increasing.html#pandas.Series.is_monotonic_increasing) | Alias for is\_monotonic. |
| 16 | [`is_unique`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.is_unique.html#pandas.Series.is_unique) | Return boolean if values in the object are unique. |
| 17 | [`loc`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.loc.html#pandas.Series.loc) | Access a group of rows and columns by label(s) or a boolean array. |
| 18 | [`name`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.name.html#pandas.Series.name) | Return the name of the Series. |
| 19 | [`nbytes`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.nbytes.html#pandas.Series.nbytes) | Return the number of bytes in the underlying data. |
| 20 | [`ndim`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.ndim.html#pandas.Series.ndim) | Number of dimensions of the underlying data, by definition 1. |
| 21 | [`shape`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.shape.html#pandas.Series.shape) | Return a tuple of the shape of the underlying data. |
| 22 | [`size`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.size.html#pandas.Series.size) | Return the number of elements in the underlying data. |
| 23 | [`values`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.values.html#pandas.Series.values) | Return Series as ndarray or ndarray-like depending on the type. |

#### 1. pandas.Series.T

*property*Series.**T**

Return the transpose, which is by definition self.

#### 2. pandas.Series.array

*property*Series.**array**

The ExtensionArray of the data backing this Series or Index.ReturnsExtensionArray

An ExtensionArray of the values stored within. For extension types, this is the actual array. For NumPy native types, this is a thin (no copy) wrapper around [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray).

`.array` differs `.values` which may require converting the data to a different form.

#### 3. pandas.Series.at

*property*Series.**at**

Access a single value for a row/column label pair.

Similar to `loc`, in that both provide label-based lookups. Use `at` if you only need to get or set a single value in a DataFrame or Series.RaisesKeyError

If ‘label’ does not exist in DataFrame.

#### 4. pandas.Series.attrs

*property*Series.**attrs**

Dictionary of global attributes of this dataset.

#### 5. pandas.Series.axes

*property*Series.**axes**

Return a list of the row axis labels.

#### 6.pandas.Series.dtype

*property*Series.**dtype**

Return the dtype object of the underlying data.

#### 7.pandas.Series.dtypes

*property*Series.**dtypes**

Return the dtype object of the underlying data.

#### 8. pandas.Series.flags

*property*Series.**flags**

Get the properties associated with this pandas object.

The available flags are

- [`Flags.allows_duplicate_labels`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Flags.allows_duplicate_labels.html#pandas.Flags.allows_duplicate_labels)

#### 9. pandas.Series.hasnans

*property*Series.**hasnans**

Return True if there are any NaNs.

Enables various performance speedups.

#### 10. pandas.Series.iat

*property*Series.**iat**

Access a single value for a row/column pair by integer position.

Similar to `iloc`, in that both provide integer-based lookups. Use `iat` if you only need to get or set a single value in a DataFrame or Series.RaisesIndexError

When integer position is out of bounds.

#### 11. pandas.Series.iloc

*property*Series.**iloc**

Purely integer-location based indexing for selection by position.

`.iloc[]` is primarily integer position based (from `0` to `length-1` of the axis), but may also be used with a boolean array.

Allowed inputs are:

- An integer, e.g. `5`.
- A list or array of integers, e.g. `[4, 3, 0]`.
- A slice object with ints, e.g. `1:7`.
- A boolean array.
- A `callable` function with one argument (the calling Series or DataFrame) and that returns valid output for indexing (one of the above). This is useful in method chains, when you don’t have a reference to the calling object, but would like to base your selection on some value.

`.iloc` will raise `IndexError` if a requested indexer is out-of-bounds, except *slice* indexers which allow out-of-bounds indexing (this conforms with python/numpy *slice* semantics).

#### 12. pandas.Series.index

Series.**index**

The index (axis labels) of the Series.

#### 13. pandas.Series.is\_monotonic

*property*Series.**is\_monotonic**

Return boolean if values in the object are monotonic\_increasing.Returns bool

#### 14. pandas.Series.is\_monotonic\_decreasing

*property*Series.**is\_monotonic\_decreasing**

Return boolean if values in the object are monotonic\_decreasing.Returns bool

#### 15. pandas.Series.is\_monotonic\_increasing

*property*Series.**is\_monotonic\_increasing**

Alias for is\_monotonic.

#### 16. pandas.Series.is\_unique

*property*Series.**is\_unique**

Return boolean if values in the object are unique.
Returns bool

#### 17. pandas.Series.loc

*property*Series.**loc**

Access a group of rows and columns by label(s) or a boolean array.

`.loc[]` is primarily label based, but may also be used with a boolean array.

Allowed inputs are:

- A single label, e.g. `5` or `'a'`, (note that `5` is interpreted as a *label* of the index, and **never** as an integer position along the index).
- A list or array of labels, e.g. `['a', 'b', 'c']`.
- A slice object with labels, e.g. `'a':'f'`.WarningNote that contrary to usual python slices, **both** the start and the stop are included
- A boolean array of the same length as the axis being sliced, e.g. `[True, False, True]`.
- An alignable boolean Series. The index of the key will be aligned before masking.
- An alignable Index. The Index of the returned selection will be the input.
- A `callable` function with one argument (the calling Series or DataFrame) and that returns valid output for indexing (one of the above)

See more at [Selection by Label](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-label).RaisesKeyError

If any items are not found.IndexingError

If an indexed key is passed and its index is unalignable to the frame index.

#### 18. pandas.Series.name

*property*Series.**name**

Return the name of the Series.

The name of a Series becomes its index or column name if it is used to form a DataFrame. It is also used whenever displaying the Series using the interpreter.Returnslabel (hashable object)

The name of the Series, also the column name if part of a DataFrame.

See also[`Series.rename`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.rename.html#pandas.Series.rename)

Sets the Series name when given a scalar input.[`Index.name`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Index.name.html#pandas.Index.name)

Corresponding Index property.

Examples

The Series name can be set initially when calling the constructor.

```
>>> s = pd.Series([1, 2, 3], dtype=np.int64, name='Numbers')
>>> s
0    1
1    2
2    3
Name: Numbers, dtype: int64
>>> s.name = "Integers"
>>> s
0    1
1    2
2    3
Name: Integers, dtype: int64
```

The name of a Series within a DataFrame is its column name.

```
>>> df = pd.DataFrame([[1, 2], [3, 4], [5, 6]],
...                   columns=["Odd Numbers", "Even Numbers"])
>>> df
   Odd Numbers  Even Numbers
0            1             2
1            3             4
2            5             6
>>> df["Even Numbers"].name
'Even Numbers'
```

#### 19. pandas.Series.nbytes

*property*Series.**nbytes**

Return the number of bytes in the underlying data.

#### 20. pandas.Series.ndim

*property*Series.**ndim**

Number of dimensions of the underlying data, by definition 1.

#### 21. pandas.Series.shape

*property*Series.**shape**

Return a tuple of the shape of the underlying data.

#### 22. pandas.Series.size

*property*Series.**size**

Return the number of elements in the underlying data.

#### 23. pandas.Series.values

*property*Series.**values**

Return Series as ndarray or ndarray-like depending on the dtype.

Warning

We recommend using [`Series.array`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.array.html#pandas.Series.array) or [`Series.to_numpy()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy), depending on whether you need a reference to the underlying data or a NumPy array.Returnsnumpy.ndarray or ndarray-like

See also[`Series.array`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.array.html#pandas.Series.array)

Reference to the underlying data.[`Series.to_numpy`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy)

A NumPy array representing the underlying data.

Examples

```
>>> pd.Series([1, 2, 3]).values
array([1, 2, 3])
```

```
>>> pd.Series(list('aabc')).values
array(['a', 'a', 'b', 'c'], dtype=object)
```

```
>>> pd.Series(list('aabc')).astype('category').values
['a', 'a', 'b', 'c']
Categories (3, object): ['a', 'b', 'c']
```

Timezone aware datetime data is converted to UTC:

```
>>> pd.Series(pd.date_range('20130101', periods=3,
...                         tz='US/Eastern')).values
array(['2013-01-01T05:00:00.000000000',
       '2013-01-02T05:00:00.000000000',
       '2013-01-03T05:00:00.000000000'], dtype='datetime64[ns]')
```

## Methods

|  |  |  |
| --- | --- | --- |
| S.N | Method | Meaning |
| 1 | [`abs`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.abs.html#pandas.Series.abs)() | Return a Series/DataFrame with absolute numeric value of each element. |
| 2 | [`add`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.add.html#pandas.Series.add)(other[, level, fill\_value, axis]) | Return Addition of series and other, element-wise (binary operator add). |
| 3 | [`add_prefix`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.add_prefix.html#pandas.Series.add_prefix)(prefix) | Prefix labels with string prefix. |
| 4 | [`add_suffix`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.add_suffix.html#pandas.Series.add_suffix)(suffix) | Suffix labels with string suffix. |
| 5 | [`agg`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.agg.html#pandas.Series.agg)([func, axis]) | Aggregate using one or more operations over the specified axis. |
| 6 | [`aggregate`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.aggregate.html#pandas.Series.aggregate)([func, axis]) | Aggregate using one or more operations over the specified axis. |
| 7 | [`align`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.align.html#pandas.Series.align)(other[, join, axis, level, copy, …]) | Align two objects on their axes with the specified join method. |
| 8 | [`all`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.all.html#pandas.Series.all)([axis, bool\_only, skipna, level]) | Return whether all elements are True, potentially over an axis. |
| 9 | [`any`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.any.html#pandas.Series.any)([axis, bool\_only, skipna, level]) | Return whether any element is True, potentially over an axis. |
| 10 | [`append`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.append.html#pandas.Series.append)(to\_append[, ignore\_index, …]) | Concatenate two or more Series. |
| 11 | [`apply`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.apply.html#pandas.Series.apply)(func[, convert\_dtype, args]) | Invoke function on values of Series. |
| 12 | [`argmax`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.argmax.html#pandas.Series.argmax)([axis, skipna]) | Return int position of the largest value in the Series. |
| 13 | [`argmin`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.argmin.html#pandas.Series.argmin)([axis, skipna]) | Return int position of the smallest value in the Series. |
| 14 | [`argsort`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.argsort.html#pandas.Series.argsort)([axis, kind, order]) | Return the integer indices that would sort the Series values. |
| 15 | [`asfreq`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.asfreq.html#pandas.Series.asfreq)(freq[, method, how, normalize, …]) | Convert TimeSeries to specified frequency. |
| 16 | [`asof`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.asof.html#pandas.Series.asof)(where[, subset]) | Return the last row(s) without any NaNs before where. |
| 17 | [`astype`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.astype.html#pandas.Series.astype)(dtype[, copy, errors]) | Cast a pandas object to a specified dtype `dtype`. |
| 18 | [`at_time`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.at_time.html#pandas.Series.at_time)(time[, asof, axis]) | Select values at particular time of day (e.g., 9:30AM). |
| 19 | [`autocorr`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.autocorr.html#pandas.Series.autocorr)([lag]) | Compute the lag-N autocorrelation. |
| 20 | [`backfill`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.backfill.html#pandas.Series.backfill)([axis, inplace, limit, downcast]) | Synonym for [`DataFrame.fillna()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html#pandas.DataFrame.fillna) with `method='bfill'`. |
| 21 | [`between`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.between.html#pandas.Series.between)(left, right[, inclusive]) | Return boolean Series equivalent to left &lt;= series &lt;= right. |
| 22 | [`between_time`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.between_time.html#pandas.Series.between_time)(start\_time, end\_time[, …]) | Select values between particular times of the day (e.g., 9:00-9:30 AM). |
| 23 | [`bfill`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.bfill.html#pandas.Series.bfill)([axis, inplace, limit, downcast]) | Synonym for [`DataFrame.fillna()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html#pandas.DataFrame.fillna) with `method='bfill'`. |
| 24 | [`bool`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.bool.html#pandas.Series.bool)() | Return the bool of a single element Series or DataFrame. |
| 25 | [`cat`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.cat.html#pandas.Series.cat) | alias of `pandas.core.arrays.categorical.CategoricalAccessor` |
| 26 | [`clip`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.clip.html#pandas.Series.clip)([lower, upper, axis, inplace]) | Trim values at input threshold(s). |
| 27 | [`combine`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.combine.html#pandas.Series.combine)(other, func[, fill\_value]) | Combine the Series with a Series or scalar according to func. |
| 28 | [`combine_first`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.combine_first.html#pandas.Series.combine_first)(other) | Combine Series values, choosing the calling Series’s values first. |
| 29 | [`compare`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.compare.html#pandas.Series.compare)(other[, align\_axis, keep\_shape, …]) | Compare to another Series and show the differences. |
| 30 | [`convert_dtypes`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.convert_dtypes.html#pandas.Series.convert_dtypes)([infer\_objects, …]) | Convert columns to best possible dtypes using dtypes supporting `pd.NA`. |
| 31 | [`copy`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.copy.html#pandas.Series.copy)([deep]) | Make a copy of this object’s indices and data. |
| 32 | [`corr`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.corr.html#pandas.Series.corr)(other[, method, min\_periods]) | Compute correlation with other Series, excluding missing values. |
| 33 | [`count`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.count.html#pandas.Series.count)([level]) | Return number of non-NA/null observations in the Series. |
| 34 | [`cov`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.cov.html#pandas.Series.cov)(other[, min\_periods, ddof]) | Compute covariance with Series, excluding missing values. |
| 35 | [`cummax`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.cummax.html#pandas.Series.cummax)([axis, skipna]) | Return cumulative maximum over a DataFrame or Series axis. |
| 36 | [`cummin`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.cummin.html#pandas.Series.cummin)([axis, skipna]) | Return cumulative minimum over a DataFrame or Series axis. |
| 37 | [`cumprod`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.cumprod.html#pandas.Series.cumprod)([axis, skipna]) | Return cumulative product over a DataFrame or Series axis. |
| 38 | [`cumsum`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.cumsum.html#pandas.Series.cumsum)([axis, skipna]) | Return cumulative sum over a DataFrame or Series axis. |
| 39 | [`describe`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.describe.html#pandas.Series.describe)([percentiles, include, exclude, …]) | Generate descriptive statistics. |
| 40 | [`diff`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.diff.html#pandas.Series.diff)([periods]) | First discrete difference of element. |
| 41 | [`div`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.div.html#pandas.Series.div)(other[, level, fill\_value, axis]) | Return Floating division of series and other, element-wise (binary operator truediv). |
| 42 | [`divide`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.divide.html#pandas.Series.divide)(other[, level, fill\_value, axis]) | Return Floating division of series and other, element-wise (binary operator truediv). |
| 43 | [`divmod`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.divmod.html#pandas.Series.divmod)(other[, level, fill\_value, axis]) | Return Integer division and modulo of series and other, element-wise (binary operator divmod). |
| 44 | [`dot`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dot.html#pandas.Series.dot)(other) | Compute the dot product between the Series and the columns of other. |
| 45 | [`drop`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.drop.html#pandas.Series.drop)([labels, axis, index, columns, level, …]) | Return Series with specified index labels removed. |
| 46 | [`drop_duplicates`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.drop_duplicates.html#pandas.Series.drop_duplicates)([keep, inplace]) | Return Series with duplicate values removed. |
| 47 | [`droplevel`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.droplevel.html#pandas.Series.droplevel)(level[, axis]) | Return DataFrame with requested index / column level(s) removed. |
| 48 | [`dropna`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dropna.html#pandas.Series.dropna)([axis, inplace, how]) | Return a new Series with missing values removed. |
| 49 | [`dt`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.html#pandas.Series.dt) | alias of `pandas.core.indexes.accessors.CombinedDatetimelikeProperties` |
| 50 | [`duplicated`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.duplicated.html#pandas.Series.duplicated)([keep]) | Indicate duplicate Series values. |
| 51 | [`eq`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.eq.html#pandas.Series.eq)(other[, level, fill\_value, axis]) | Return Equal to of series and other, element-wise (binary operator eq). |
| 52 | [`equals`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.equals.html#pandas.Series.equals)(other) | Test whether two objects contain the same elements. |
| 53 | [`ewm`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.ewm.html#pandas.Series.ewm)([com, span, halflife, alpha, …]) | Provide exponential weighted (EW) functions. |
| 54 | [`expanding`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.expanding.html#pandas.Series.expanding)([min\_periods, center, axis]) | Provide expanding transformations. |
| 55 | [`explode`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.explode.html#pandas.Series.explode)([ignore\_index]) | Transform each element of a list-like to a row. |
| 56 | [`factorize`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.factorize.html#pandas.Series.factorize)([sort, na\_sentinel]) | Encode the object as an enumerated type or categorical variable. |
| 57 | [`ffill`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.ffill.html#pandas.Series.ffill)([axis, inplace, limit, downcast]) | Synonym for [`DataFrame.fillna()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html#pandas.DataFrame.fillna) with `method='ffill'`. |
| 58 | [`fillna`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.fillna.html#pandas.Series.fillna)([value, method, axis, inplace, …]) | Fill NA/NaN values using the specified method. |
| 59 | [`filter`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.filter.html#pandas.Series.filter)([items, like, regex, axis]) | Subset the dataframe rows or columns according to the specified index labels. |
| 60 | [`first`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.first.html#pandas.Series.first)(offset) | Select initial periods of time series data based on a date offset. |
| 61 | [`first_valid_index`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.first_valid_index.html#pandas.Series.first_valid_index)() | Return index for first non-NA/null value. |
| 62 | [`floordiv`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.floordiv.html#pandas.Series.floordiv)(other[, level, fill\_value, axis]) | Return Integer division of series and other, element-wise (binary operator floordiv). |
| 63 | [`ge`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.ge.html#pandas.Series.ge)(other[, level, fill\_value, axis]) | Return Greater than or equal to of series and other, element-wise (binary operator ge). |
| 64 | [`get`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.get.html#pandas.Series.get)(key[, default]) | Get item from object for given key (ex: DataFrame column). |
| 65 | [`groupby`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.groupby.html#pandas.Series.groupby)([by, axis, level, as\_index, sort, …]) | Group Series using a mapper or by a Series of columns. |
| 66 | [`gt`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.gt.html#pandas.Series.gt)(other[, level, fill\_value, axis]) | Return Greater than of series and other, element-wise (binary operator gt). |
| 67 | [`head`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.head.html#pandas.Series.head)([n]) | Return the first n rows. |
| 68 | [`hist`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.hist.html#pandas.Series.hist)([by, ax, grid, xlabelsize, xrot, …]) | Draw histogram of the input series using matplotlib. |
| 69 | [`idxmax`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.idxmax.html#pandas.Series.idxmax)([axis, skipna]) | Return the row label of the maximum value. |
| 70 | [`idxmin`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.idxmin.html#pandas.Series.idxmin)([axis, skipna]) | Return the row label of the minimum value. |
| 71 | [`infer_objects`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.infer_objects.html#pandas.Series.infer_objects)() | Attempt to infer better dtypes for object columns. |
| 72 | [`interpolate`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.interpolate.html#pandas.Series.interpolate)([method, axis, limit, inplace, …]) | Fill NaN values using an interpolation method. |
| 73 | [`isin`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.isin.html#pandas.Series.isin)(values) | Whether elements in Series are contained in values. |
| 74 | [`isna`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.isna.html#pandas.Series.isna)() | Detect missing values. |
| 75 | [`isnull`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.isnull.html#pandas.Series.isnull)() | Detect missing values. |
| 76 | [`item`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.item.html#pandas.Series.item)() | Return the first element of the underlying data as a Python scalar. |
| 77 | [`items`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.items.html#pandas.Series.items)() | Lazily iterate over (index, value) tuples. |
| 78 | [`iteritems`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.iteritems.html#pandas.Series.iteritems)() | Lazily iterate over (index, value) tuples. |
| 79 | [`keys`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.keys.html#pandas.Series.keys)() | Return alias for index. |
| 80 | [`kurt`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.kurt.html#pandas.Series.kurt)([axis, skipna, level, numeric\_only]) | Return unbiased kurtosis over requested axis. |
| 81 | [`kurtosis`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.kurtosis.html#pandas.Series.kurtosis)([axis, skipna, level, numeric\_only]) | Return unbiased kurtosis over requested axis. |
| 82 | [`last`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.last.html#pandas.Series.last)(offset) | Select final periods of time series data based on a date offset. |
| 83 | [`last_valid_index`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.last_valid_index.html#pandas.Series.last_valid_index)() | Return index for last non-NA/null value. |
| 84 | [`le`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.le.html#pandas.Series.le)(other[, level, fill\_value, axis]) | Return Less than or equal to of series and other, element-wise (binary operator le). |
| 85 | [`lt`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.lt.html#pandas.Series.lt)(other[, level, fill\_value, axis]) | Return Less than of series and other, element-wise (binary operator lt). |
| 86 | [`mad`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.mad.html#pandas.Series.mad)([axis, skipna, level]) | Return the mean absolute deviation of the values over the requested axis. |
| 87 | [`map`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html#pandas.Series.map)(arg[, na\_action]) | Map values of Series according to input correspondence. |
| 88 | [`mask`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.mask.html#pandas.Series.mask)(cond[, other, inplace, axis, level, …]) | Replace values where the condition is True. |
| 89 | [`max`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.max.html#pandas.Series.max)([axis, skipna, level, numeric\_only]) | Return the maximum of the values over the requested axis. |
| 90 | [`mean`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.mean.html#pandas.Series.mean)([axis, skipna, level, numeric\_only]) | Return the mean of the values over the requested axis. |
| 91 | [`median`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.median.html#pandas.Series.median)([axis, skipna, level, numeric\_only]) | Return the median of the values over the requested axis. |
| 92 | [`memory_usage`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.memory_usage.html#pandas.Series.memory_usage)([index, deep]) | Return the memory usage of the Series. |
| 93 | [`min`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.min.html#pandas.Series.min)([axis, skipna, level, numeric\_only]) | Return the minimum of the values over the requested axis. |
| 94 | [`mod`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.mod.html#pandas.Series.mod)(other[, level, fill\_value, axis]) | Return Modulo of series and other, element-wise (binary operator mod). |
| 95 | [`mode`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.mode.html#pandas.Series.mode)([dropna]) | Return the mode(s) of the Series. |
| 96 | [`mul`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.mul.html#pandas.Series.mul)(other[, level, fill\_value, axis]) | Return Multiplication of series and other, element-wise (binary operator mul). |
| 97 | [`multiply`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.multiply.html#pandas.Series.multiply)(other[, level, fill\_value, axis]) | Return Multiplication of series and other, element-wise (binary operator mul). |
| 98 | [`ne`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.ne.html#pandas.Series.ne)(other[, level, fill\_value, axis]) | Return Not equal to of series and other, element-wise (binary operator ne). |
| 99 | [`nlargest`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.nlargest.html#pandas.Series.nlargest)([n, keep]) | Return the largest n elements. |
| 100 | [`notna`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.notna.html#pandas.Series.notna)() | Detect existing (non-missing) values. |
| 101 | [`notnull`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.notnull.html#pandas.Series.notnull)() | Detect existing (non-missing) values. |
| 102 | [`nsmallest`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.nsmallest.html#pandas.Series.nsmallest)([n, keep]) | Return the smallest n elements. |
| 103 | [`nunique`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.nunique.html#pandas.Series.nunique)([dropna]) | Return number of unique elements in the object. |
| 104 | [`pad`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.pad.html#pandas.Series.pad)([axis, inplace, limit, downcast]) | Synonym for [`DataFrame.fillna()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html#pandas.DataFrame.fillna) with `method='ffill'`. |
| 105 | [`pct_change`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.pct_change.html#pandas.Series.pct_change)([periods, fill\_method, limit, freq]) | Percentage change between the current and a prior element. |
| 106 | [`pipe`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.pipe.html#pandas.Series.pipe)(func, \*args, \*\*kwargs) | Apply func(self, \*args, \*\*kwargs). |
| 107 | [`plot`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.plot.html#pandas.Series.plot) | alias of `pandas.plotting._core.PlotAccessor` |
| 108 | [`pop`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.pop.html#pandas.Series.pop)(item) | Return item and drops from series. |
| 109 | [`pow`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.pow.html#pandas.Series.pow)(other[, level, fill\_value, axis]) | Return Exponential power of series and other, element-wise (binary operator pow). |
| 110 | [`prod`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.prod.html#pandas.Series.prod)([axis, skipna, level, numeric\_only, …]) | Return the product of the values over the requested axis. |
| 111 | [`product`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.product.html#pandas.Series.product)([axis, skipna, level, numeric\_only, …]) | Return the product of the values over the requested axis. |
| 112 | [`quantile`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.quantile.html#pandas.Series.quantile)([q, interpolation]) | Return value at the given quantile. |
| 113 | [`radd`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.radd.html#pandas.Series.radd)(other[, level, fill\_value, axis]) | Return Addition of series and other, element-wise (binary operator radd). |
| 114 | [`rank`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.rank.html#pandas.Series.rank)([axis, method, numeric\_only, …]) | Compute numerical data ranks (1 through n) along axis. |
| 115 | [`ravel`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.ravel.html#pandas.Series.ravel)([order]) | Return the flattened underlying data as an ndarray. |
| 116 | [`rdiv`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.rdiv.html#pandas.Series.rdiv)(other[, level, fill\_value, axis]) | Return Floating division of series and other, element-wise (binary operator rtruediv). |
| 117 | [`rdivmod`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.rdivmod.html#pandas.Series.rdivmod)(other[, level, fill\_value, axis]) | Return Integer division and modulo of series and other, element-wise (binary operator rdivmod). |
| 118 | [`reindex`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.reindex.html#pandas.Series.reindex)([index]) | Conform Series to new index with optional filling logic. |
| 119 | [`reindex_like`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.reindex_like.html#pandas.Series.reindex_like)(other[, method, copy, limit, …]) | Return an object with matching indices as other object. |
| 120 | [`rename`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.rename.html#pandas.Series.rename)([index, axis, copy, inplace, level, …]) | Alter Series index labels or name. |
| 121 | [`rename_axis`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.rename_axis.html#pandas.Series.rename_axis)([mapper, index, columns, axis, …]) | Set the name of the axis for the index or columns. |
| 122 | [`reorder_levels`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.reorder_levels.html#pandas.Series.reorder_levels)(order) | Rearrange index levels using input order. |
| 123 | [`repeat`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.repeat.html#pandas.Series.repeat)(repeats[, axis]) | Repeat elements of a Series. |
| 124 | [`replace`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.replace.html#pandas.Series.replace)([to\_replace, value, inplace, limit, …]) | Replace values given in to\_replace with value. |
| 125 | [`resample`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.resample.html#pandas.Series.resample)(rule[, axis, closed, label, …]) | Resample time-series data. |
| 126 | [`reset_index`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.reset_index.html#pandas.Series.reset_index)([level, drop, name, inplace]) | Generate a new DataFrame or Series with the index reset. |
| 127 | [`rfloordiv`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.rfloordiv.html#pandas.Series.rfloordiv)(other[, level, fill\_value, axis]) | Return Integer division of series and other, element-wise (binary operator rfloordiv). |
| 128 | [`rmod`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.rmod.html#pandas.Series.rmod)(other[, level, fill\_value, axis]) | Return Modulo of series and other, element-wise (binary operator rmod). |
| 129 | [`rmul`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.rmul.html#pandas.Series.rmul)(other[, level, fill\_value, axis]) | Return Multiplication of series and other, element-wise (binary operator rmul). |
| 130 | [`rolling`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.rolling.html#pandas.Series.rolling)(window[, min\_periods, center, …]) | Provide rolling window calculations. |
| 131 | [`round`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.round.html#pandas.Series.round)([decimals]) | Round each value in a Series to the given number of decimals. |
| 132 | [`rpow`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.rpow.html#pandas.Series.rpow)(other[, level, fill\_value, axis]) | Return Exponential power of series and other, element-wise (binary operator rpow). |
| 133 | [`rsub`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.rsub.html#pandas.Series.rsub)(other[, level, fill\_value, axis]) | Return Subtraction of series and other, element-wise (binary operator rsub). |
| 134 | [`rtruediv`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.rtruediv.html#pandas.Series.rtruediv)(other[, level, fill\_value, axis]) | Return Floating division of series and other, element-wise (binary operator rtruediv). |
| 135 | [`sample`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.sample.html#pandas.Series.sample)([n, frac, replace, weights, …]) | Return a random sample of items from an axis of object. |
| 136 | [`searchsorted`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.searchsorted.html#pandas.Series.searchsorted)(value[, side, sorter]) | Find indices where elements should be inserted to maintain order. |
| 137 | [`sem`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.sem.html#pandas.Series.sem)([axis, skipna, level, ddof, numeric\_only]) | Return unbiased standard error of the mean over requested axis. |
| 138 | [`set_axis`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.set_axis.html#pandas.Series.set_axis)(labels[, axis, inplace]) | Assign desired index to given axis. |
| 139 | [`set_flags`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.set_flags.html#pandas.Series.set_flags)(\*[, copy, allows\_duplicate\_labels]) | Return a new object with updated flags. |
| 140 | [`shift`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.shift.html#pandas.Series.shift)([periods, freq, axis, fill\_value]) | Shift index by desired number of periods with an optional time freq. |
| 141 | [`skew`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.skew.html#pandas.Series.skew)([axis, skipna, level, numeric\_only]) | Return unbiased skew over requested axis. |
| 142 | [`slice_shift`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.slice_shift.html#pandas.Series.slice_shift)([periods, axis]) | (DEPRECATED) Equivalent to shift without copying data. |
| 143 | [`sort_index`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.sort_index.html#pandas.Series.sort_index)([axis, level, ascending, …]) | Sort Series by index labels. |
| 144 | [`sort_values`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.sort_values.html#pandas.Series.sort_values)([axis, ascending, inplace, …]) | Sort by the values. |
| 145 | [`sparse`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.sparse.html#pandas.Series.sparse) | alias of `pandas.core.arrays.sparse.accessor.SparseAccessor` |
| 146 | [`squeeze`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.squeeze.html#pandas.Series.squeeze)([axis]) | Squeeze 1 dimensional axis objects into scalars. |
| 147 | [`std`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.std.html#pandas.Series.std)([axis, skipna, level, ddof, numeric\_only]) | Return sample standard deviation over requested axis. |
| 148 | [`str`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.html#pandas.Series.str) | alias of `pandas.core.strings.accessor.StringMethods` |
| 149 | [`sub`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.sub.html#pandas.Series.sub)(other[, level, fill\_value, axis]) | Return Subtraction of series and other, element-wise (binary operator sub). |
| 150 | [`subtract`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.subtract.html#pandas.Series.subtract)(other[, level, fill\_value, axis]) | Return Subtraction of series and other, element-wise (binary operator sub). |
| 151 | [`sum`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.sum.html#pandas.Series.sum)([axis, skipna, level, numeric\_only, …]) | Return the sum of the values over the requested axis. |
| 152 | [`swapaxes`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.swapaxes.html#pandas.Series.swapaxes)(axis1, axis2[, copy]) | Interchange axes and swap values axes appropriately. |
| 153 | [`swaplevel`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.swaplevel.html#pandas.Series.swaplevel)([i, j, copy]) | Swap levels i and j in a [`MultiIndex`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.MultiIndex.html#pandas.MultiIndex). |
| 154 | [`tail`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.tail.html#pandas.Series.tail)([n]) | Return the last n rows. |
| 155 | [`take`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.take.html#pandas.Series.take)(indices[, axis, is\_copy]) | Return the elements in the given *positional* indices along an axis. |
| 156 | [`to_clipboard`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.to_clipboard.html#pandas.Series.to_clipboard)([excel, sep]) | Copy object to the system clipboard. |
| 157 | [`to_csv`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.to_csv.html#pandas.Series.to_csv)([path\_or\_buf, sep, na\_rep, …]) | Write object to a comma-separated values (csv) file. |
| 158 | [`to_dict`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.to_dict.html#pandas.Series.to_dict)([into]) | Convert Series to {label -> value} dict or dict-like object. |
| 159 | [`to_excel`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.to_excel.html#pandas.Series.to_excel)(excel\_writer[, sheet\_name, na\_rep, …]) | Write object to an Excel sheet. |
| 160 | [`to_frame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.to_frame.html#pandas.Series.to_frame)([name]) | Convert Series to DataFrame. |
| 161 | [`to_hdf`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.to_hdf.html#pandas.Series.to_hdf)(path\_or\_buf, key[, mode, complevel, …]) | Write the contained data to an HDF5 file using HDFStore. |
| 162 | [`to_json`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.to_json.html#pandas.Series.to_json)([path\_or\_buf, orient, date\_format, …]) | Convert the object to a JSON string. |
| 163 | [`to_latex`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.to_latex.html#pandas.Series.to_latex)([buf, columns, col\_space, header, …]) | Render object to a LaTeX tabular, longtable, or nested table/tabular. |
| 164 | [`to_list`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.to_list.html#pandas.Series.to_list)() | Return a list of the values. |
| 165 | [`to_markdown`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.to_markdown.html#pandas.Series.to_markdown)([buf, mode, index, storage\_options]) | Print Series in Markdown-friendly format. |
| 166 | [`to_numpy`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy)([dtype, copy, na\_value]) | A NumPy ndarray representing the values in this Series or Index. |
| 167 | [`to_period`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.to_period.html#pandas.Series.to_period)([freq, copy]) | Convert Series from DatetimeIndex to PeriodIndex. |
| 168 | [`to_pickle`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.to_pickle.html#pandas.Series.to_pickle)(path[, compression, protocol, …]) | Pickle (serialize) object to file. |
| 169 | [`to_sql`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.to_sql.html#pandas.Series.to_sql)(name, con[, schema, if\_exists, …]) | Write records stored in a DataFrame to a SQL database. |
| 170 | [`to_string`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.to_string.html#pandas.Series.to_string)([buf, na\_rep, float\_format, …]) | Render a string representation of the Series. |
| 171 | [`to_timestamp`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.to_timestamp.html#pandas.Series.to_timestamp)([freq, how, copy]) | Cast to DatetimeIndex of Timestamps, at *beginning* of period. |
| 172 | [`to_xarray`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.to_xarray.html#pandas.Series.to_xarray)() | Return an xarray object from the pandas object. |
| 173 | [`tolist`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.tolist.html#pandas.Series.tolist)() | Return a list of the values. |
| 174 | [`transform`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.transform.html#pandas.Series.transform)(func[, axis]) | Call `func` on self producing a Series with transformed values. |
| 175 | [`transpose`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.transpose.html#pandas.Series.transpose)(\*args, \*\*kwargs) | Return the transpose, which is by definition self. |
| 176 | [`truediv`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.truediv.html#pandas.Series.truediv)(other[, level, fill\_value, axis]) | Return Floating division of series and other, element-wise (binary operator truediv). |
| 177 | [`truncate`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.truncate.html#pandas.Series.truncate)([before, after, axis, copy]) | Truncate a Series or DataFrame before and after some index value. |
| 178 | [`tshift`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.tshift.html#pandas.Series.tshift)([periods, freq, axis]) | (DEPRECATED) Shift the time index, using the index’s frequency if available. |
| 179 | [`tz_convert`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.tz_convert.html#pandas.Series.tz_convert)(tz[, axis, level, copy]) | Convert tz-aware axis to target time zone. |
| 180 | [`tz_localize`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.tz_localize.html#pandas.Series.tz_localize)(tz[, axis, level, copy, …]) | Localize tz-naive index of a Series or DataFrame to target time zone. |
| 181 | [`unique`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.unique.html#pandas.Series.unique)() | Return unique values of Series object. |
| 182 | [`unstack`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.unstack.html#pandas.Series.unstack)([level, fill\_value]) | Unstack, also known as pivot, Series with MultiIndex to produce DataFrame. |
| 183 | [`update`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.update.html#pandas.Series.update)(other) | Modify Series in place using values from passed Series. |
| 184 | [`value_counts`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html#pandas.Series.value_counts)([normalize, sort, ascending, …]) | Return a Series containing counts of unique values. |
| 185 | [`var`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.var.html#pandas.Series.var)([axis, skipna, level, ddof, numeric\_only]) | Return unbiased variance over requested axis. |
| 186 | [`view`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.view.html#pandas.Series.view)([dtype]) | Create a new view of the Series. |
| 187 | [`where`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.where.html#pandas.Series.where)(cond[, other, inplace, axis, level, …]) | Replace values where the condition is False. |
| 188 | [`xs`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.xs.html#pandas.Series.xs)(key[, axis, level, drop\_level]) | Return cross-section from the Series/DataFrame. |

#### 1.pandas.Series.add

Series.**add**(*other*, *level=None*, *fill\_value=None*, *axis=0*)[[source]](https://github.com/pandas-dev/pandas/blob/v1.4.4/pandas/core/ops/__init__.py#L176-L197)

Return Addition of series and other, element-wise (binary operator add).

Equivalent to `series + other`, but with support to substitute a fill\_value for missing data in either one of the inputs.Parameters**other**Series or scalar value**fill\_value**None or float value, default None (NaN)

Fill existing missing (NaN) values, and any new element needed for successful Series alignment, with this value before computation. If data in both corresponding Series locations is missing the result of filling (at that location) will be missing.**level**int or name

Broadcast across a level, matching Index values on the passed MultiIndex level.ReturnsSeries

The result of the operation.

See also[`Series.radd`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.radd.html#pandas.Series.radd)

Reverse of the Addition operator, see [Python documentation](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types) for more details.

Examples

```
>>> a = pd.Series([1, 1, 1, np.nan], index=['a', 'b', 'c', 'd'])
>>> a
a    1.0
b    1.0
c    1.0
d    NaN
dtype: float64
>>> b = pd.Series([1, np.nan, 1, np.nan], index=['a', 'b', 'd', 'e'])
>>> b
a    1.0
b    NaN
d    1.0
e    NaN
dtype: float64
>>> a.add(b, fill_value=0)
a    2.0
b    1.0
c    1.0
d    1.0
e    NaN
dtype: float64
```

#### 2.pandas.Series.add

Series.**add**(*other*, *level=None*, *fill\_value=None*, *axis=0*)[[source]](https://github.com/pandas-dev/pandas/blob/v1.4.4/pandas/core/ops/__init__.py#L176-L197)

Return Addition of series and other, element-wise (binary operator add).

Equivalent to `series + other`, but with support to substitute a fill\_value for missing data in either one of the inputs.Parameters**other**Series or scalar value**fill\_value**None or float value, default None (NaN)

Fill existing missing (NaN) values, and any new element needed for successful Series alignment, with this value before computation. If data in both corresponding Series locations is missing the result of filling (at that location) will be missing.**level**int or name

Broadcast across a level, matching Index values on the passed MultiIndex level.ReturnsSeries

The result of the operation.

See also[`Series.radd`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.radd.html#pandas.Series.radd)

Reverse of the Addition operator, see [Python documentation](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types) for more details.

Examples

```
>>> a = pd.Series([1, 1, 1, np.nan], index=['a', 'b', 'c', 'd'])
>>> a
a    1.0
b    1.0
c    1.0
d    NaN
dtype: float64
>>> b = pd.Series([1, np.nan, 1, np.nan], index=['a', 'b', 'd', 'e'])
>>> b
a    1.0
b    NaN
d    1.0
e    NaN
dtype: float64
>>> a.add(b, fill_value=0)
a    2.0
b    1.0
c    1.0
d    1.0
e    NaN
dtype: float64
```

#### 3.pandas.Series.add\_prefix

Series.**add\_prefix**(*prefix*)[[source]](https://github.com/pandas-dev/pandas/blob/v1.4.4/pandas/core/generic.py#L4382-L4444)

Prefix labels with string prefix.

For Series, the row labels are prefixed. For DataFrame, the column labels are prefixed.Parameters**prefix**str

The string to add before each label.ReturnsSeries or DataFrame

New Series or DataFrame with updated labels.

See also[`Series.add_suffix`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.add_suffix.html#pandas.Series.add_suffix)

Suffix row labels with string suffix.[`DataFrame.add_suffix`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.add_suffix.html#pandas.DataFrame.add_suffix)

Suffix column labels with string suffix.

Examples

```
>>> s = pd.Series([1, 2, 3, 4])
>>> s
0    1
1    2
2    3
3    4
dtype: int64
```

```
>>> s.add_prefix('item_')
item_0    1
item_1    2
item_2    3
item_3    4
dtype: int64
```

```
>>> df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [3, 4, 5, 6]})
>>> df
   A  B
0  1  3
1  2  4
2  3  5
3  4  6
```

```
>>> df.add_prefix('col_')
     col_A  col_B
0       1       3
1       2       4
2       3       5
3       4       6
```

#### 4.pandas.Series.add\_suffix

Series.**add\_suffix**(*suffix*)[[source]](https://github.com/pandas-dev/pandas/blob/v1.4.4/pandas/core/generic.py#L4446-L4508)

Suffix labels with string suffix.

For Series, the row labels are suffixed. For DataFrame, the column labels are suffixed.Parameters**suffix**str

The string to add after each label.ReturnsSeries or DataFrame

New Series or DataFrame with updated labels.

See also[`Series.add_prefix`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.add_prefix.html#pandas.Series.add_prefix)

Prefix row labels with string prefix.[`DataFrame.add_prefix`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.add_prefix.html#pandas.DataFrame.add_prefix)

Prefix column labels with string prefix.

Examples

```
>>> s = pd.Series([1, 2, 3, 4])
>>> s
0    1
1    2
2    3
3    4
dtype: int64
```

```
>>> s.add_suffix('_item')
0_item    1
1_item    2
2_item    3
3_item    4
dtype: int64
```

```
>>> df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [3, 4, 5, 6]})
>>> df
   A  B
0  1  3
1  2  4
2  3  5
3  4  6
```

```
>>> df.add_suffix('_col')
     A_col  B_col
0       1       3
1       2       4
2       3       5
3       4       6
```
