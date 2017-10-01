"""
Outlier detection of scalar values

Any value that is more than N standard deviations away from the median is
considered an outlier. Both the standard deviation and media are tracked over
a sliding window of observations.
"""

import std
import median


class Outlier(object):
    """
    Outlier detection of scalar value based on standard deviation
    """
    def __init__(self, wsize, std_max, drift=0.1):
        self.wsize = wsize
        self.std_max = std_max
        self.running_std = std.RunningStd(wsize, drift)
        self.running_med = median.RunningMedian(wsize)

    @property
    def std(self):
        return self.running_std.std

    @property
    def median(self):
        return self.running_med.median()

    @property
    def mean(self):
        return self.running_std.last_mean

    @property
    def observations(self):
        return self.running_med.window_obs

    def add(self, obs):
        """
        Add observation to dataset
        """
        self.running_std.add(obs)
        self.running_med.add(obs)

    def add_and_chekc(self, obs):
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
        if not self.running_med.ready:
            return None
        med_ = self.running_med.median()
        return abs(obs - med_) > (self.std_max * self.running_std.std)

