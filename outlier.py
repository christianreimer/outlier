"""
Outlier detection of scalar values

Any value that is more than N standard deviations away from the median is
considered an outlier. Both the standard deviation and median are tracked over
a sliding window of observations.
"""

import runstat


class Outlier(object):
    """
    Outlier detection of scalar value based on standard deviation
    """
    def __init__(self, wsize, std_max, max_drift=0.1):
        self.wsize = wsize
        self.std_max = std_max
        self.rs = runstat.RunStat(wsize, max_drift)

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

    def add(self, obs):
        """
        Add observation to dataset
        """
        self.rs.add(obs)

    def add_and_check(self, obs):
        """
        Add observation and check if it is an outlier
        """
        self.add(obs)
        return self.check(obs)

    def check(self, obs):
        """
        Check if observation is an outlier wiouth using obs to update the
        dataset
        """
        if not self.rs.ready:
            return None
        med = self.rs.median
        return abs(obs - med) > (self.std_max * self.rs.std)
