# Outlier detection on a stream of scalar observations

[![Build Status](https://travis-ci.org/christianreimer/outlier.svg?branch=master)](https://travis-ci.org/christianreimer/outlier)  [![Coverage Status](https://coveralls.io/repos/github/christianreimer/outlier/badge.svg?branch=master)](https://coveralls.io/github/christianreimer/outlier?branch=master)  [![Python Version](https://img.shields.io/badge/python-3.6-blue.svg)](https://img.shields.io/badge/python-3.6-blue.svg)

This module provides the ability to easily detect outliers in streaming scalar data. For example, a stream of measurements can be checked on a running basis and the outliers will be flagged. If the nature of the data changes, the system will self correct as the values in the sliding window normalize around the new norm.

### Example

```python
>>>
>>> import outlier
>>> import random
>>>
>>> out = outlier.Outlier(window_size=100, max_standard_dev=3)
>>> for _ in range(100):
...     out.add(random.randint(20, 30))
...
>>> for i in range(100):
...     obs = random.randint(0, 50)
...     if out.add_and_check(obs):
...             print(f'Value:{obs} Sample Number:{i} is an outlier')
Value:17 Sample Number:2 is an outlier
Value:14 Sample Number:3 is an outlier
Value:45 Sample Number:5 is an outlier
Value:48 Sample Number:7 is an outlier
Value:50 Sample Number:8 is an outlier
Value:48 Sample Number:15 is an outlier
Value:48 Sample Number:17 is an outlier
>>>
```


### Intalation
```bash
$ git clone https://github.com/christianreimer/outlier.git
$ pip install -f requirements.txt
```

And optionally
```bash
$ pip install -f requirements_test.txt
$ make test
```
