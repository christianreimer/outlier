"""
Running standard deviation calculation over the last N observations.

To avoid having to recalculate the std on each observation, it will donly be
done when the mean of the observations has drifted more then max_drift.
"""

import mean
import math


class RunningStd(object):
    """
    Running Standard Deviation
    """
    def __init__(self, wsize, drift):
        self.wsize = wsize
        self.max_drift = drift
        self.running_mean = mean.RunningMean(wsize)
        self.last_mean = None
        self.std = None

    def add(self, obs):
        self.running_mean.add(obs)
        mean_new = self.running_mean.mean()
        if self._check_drift(mean_new):
            self._recompute()

    def _check_drift(self, mean_new):
        if self.running_mean.ready and self.last_mean:
            drift = abs(self.last_mean - mean_new) / self.last_mean
            return drift >= self.max_drift
        elif self.running_mean.ready:
            return True
        else:
            return False

    def _recompute(self):
        mean = self.running_mean.mean()
        variance_lst = [math.pow(x - mean, 2) for x in self.running_mean]
        self.std = math.sqrt(sum(variance_lst) / self.wsize)
        self.last_mean = mean

    def std(self):
        return self.std
