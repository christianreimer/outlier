# Outlier detection on a stream of scalar observations

[![Build Status](https://travis-ci.org/christianreimer/outlier.svg?branch=master)](https://travis-ci.org/christianreimer/outlier)  [![Coverage Status](https://coveralls.io/repos/github/christianreimer/outlier/badge.svg?branch=master)](https://coveralls.io/github/christianreimer/outlier?branch=master)  [![Python Version](https://img.shields.io/badge/python-3.6-blue.svg)](https://img.shields.io/badge/python-3.6-blue.svg)

This module provides the ability to easily detect outliers in streaming scalar data. For example, a stream of measurements can be checked on a running basis and the outliers will be flagged. If the nature of the data changes, the system will self correct as the values in the sliding window normalize around the new norm.

### Example

```python
>>> import random
>>> import outlier
>>>
>>> # Detect outliers over a sliding window of 100 observations
>>> # Any number that is 3 (or more) stddev away from median is an outlier
>>> out = outlier.Outlier(wsize=100, std_max=3)
>>> for _ in range(100):
>>>     out.add(random.randint(0, 10))  # Just adds the observation
>>>
>>> outliers = []
>>> normal = []
>>> for _ in range(20):
>>>     obs = random.randit(0, 20)
>>>     if out.add_and_check(obs):  # Adds the observation to the data set and
>>>         outliers.append(obs)    # checks if it is an outlier
>>>     else:
>>>         normal.append(obs)
>>>
>>> print('Abnormal observations: {}'.format(sorted(outliers)))
Abnormal observations: [17, 17, 18, 20]
>>>
>>> print('Normal observations: {}'.format(sorted(normal)))
Normal observations: [0, 2, 3, 5, 6, 7, 7, 8, 8, 9, 11, 13, 13, 13, 16, 16]
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
