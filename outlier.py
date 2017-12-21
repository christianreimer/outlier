"""
Outlier detection of scalar values

Any value that is more than N standard deviations away from the median is
considered an outlier. Both the standard deviation and median are tracked over
a sliding window of observations.

Example:
>>>
>>> import random
>>> import outlier
>>>
>>> # Detect outliers over a sliding window of 100 observations
>>> # Any number that is 3 (or more) stddev away from median is an outlier
>>> out = outlier.Outlier(window_size=100, max_standard_dev=3)
>>> for _ in range(100):
>>>     out.add(random.randint(0, 10))
>>>
>>> outliers = []
>>> normal = []
>>> for _ in range(20):
>>>     observation = random.randint(5, 25)
>>>     if out.check(observation):
>>>         outliers.append(observation)
>>>     else:
>>>         normal.append(observation)
>>>
>>> print('Abnormal observations: {}'.format(sorted(outliers)))
Abnormal observations: [14, 14, 17, 17, 18, 19, 23, 24, 24, 25]
>>>
>>> print('Normal observations: {}'.format(sorted(normal)))
Normal observations: [6, 6, 7, 7, 9, 10, 11, 11, 12, 13]
>>>
"""

import runstat


class Outlier(object):
    """
    Outlier detection of scalar value based on standard deviation
    """

    def __init__(self, window_size, max_standard_dev, max_drift=0.1):
        self.window_size = window_size
        self.max_standard_dev = max_standard_dev
        self.rs = runstat.RunStat(window_size, max_drift)

    @property
    def std(self):
        return self.rs.std  # pragma: no cover

    @property
    def median(self):
        return self.rs.median  # pragma: no cover

    @property
    def mean(self):
        return self.rs.mean  # pragma: no cover

    @property
    def observations(self):
        return iter(self.rs)  # pragma: no cover

    def add(self, observation):
        """
        Add observation to dataset
        """
        self.rs.add(observation)

    def add_and_check(self, observation):
        """
        Add observation and check if it is an outlier
        """
        self.add(observation)
        return self.check(observation)

    def check(self, observation):
        """
        Check if observation is an outlier wiouth using observation to update
        the dataset
        """
        if not self.rs.ready:
            return None
        med = self.rs.median
        return abs(observation - med) > (self.max_standard_dev * self.rs.std)
