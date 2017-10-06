# Outlier detection on a stream of scalar observations

[![Build Status](https://travis-ci.org/christianreimer/outlier.svg?branch=master)](https://travis-ci.org/christianreimer/outlier)  [![Coverage Status](https://coveralls.io/repos/github/christianreimer/outlier/badge.svg?branch=master)](https://coveralls.io/github/christianreimer/outlier?branch=master)  [![Python Version](https://img.shields.io/badge/python-3.6-blue.svg)](https://img.shields.io/badge/python-3.6-blue.svg)

This module provides the ability to easily detect outliers in streaming scalar data. For example, a stream of measurements can be checked on a running basis and the outliers will be flagged. If the nature of the data changes, the system will self correct as the values in the sliding window normalize around the new norm.

```python
>>> import random
>>> import outlier
>>>
>>> # Detect outliers over a sliding window of 100 observations
>>> # Any number that is 3 (or more) stddev away from median is an outlier
>>> out = outlier.Outlier(wsize=100, std_max=3)
>>> for _ in range(100):
>>>     out.add(random.randint(0, 10))
>>>
>>> outliers = []
>>> normal = []
>>> for _ in range(20):
>>>     obs = random.randint(5, 25)
>>>     if out.check(obs):
>>>         outliers.append(obs)
>>>     else:
>>>         normal.append(obs)
>>>
>>> print('Abnormal observations: {}'.format(sorted(outliers)))
Abnormal observations: [14, 14, 17, 17, 18, 19, 23, 24, 24, 25]
>>>
>>> print('Normal observations:   {}'.format(sorted(normal)))
Normal observations:   [6, 6, 7, 7, 9, 10, 11, 11, 12, 13]
>>>
>>> print(out.std)
3.278337993557102
>>> print(out.mean)
4.55
>>> print(out.median)
4.0
>>>


```


