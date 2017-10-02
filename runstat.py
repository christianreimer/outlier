"""
Basic statictic measures over a running window of N observations.

Onc the observation window is filled, the values for Median, Mean, StdDev will
be continually calculated. To prevent excessive cpomputations, the variances
for StdDev will only be recalculated when the mean has drifted by a
configurable amount.
"""

import sortedcontainers
import math


class RunStat(object):
    """
    Statistic measures over a running window of N observations
    """

    def __init__(self, wsize, max_drift=0.05):
        self._wsize = wsize
        self._max_drift = max_drift
        self._pivot = wsize // 2
        self._observations = []
        self._sorted_observations = sortedcontainers.SortedList()
        self._variances = []
        self._var_sum = 0
        self._sum = 0
        self._mean = None

        self.mean = None
        self.median = None
        self.std = None
        self.ready = False

        if wsize % 2:
            self._pivot_f = self._pivot_odd
        else:
            self._pivot -= 1
            self._pivot_f = self._pivot_even

    def __len__(self):
        return len(self._observations)

    def __iter__(self):
        return iter(self._observations)

    def __str__(self):
        return "<RunStat[{}] mean:{} median:{} std:{}>".format(  # pragma: no cover
            self._wsize, self.mean, self.median, self.std)

    def add(self, obs):
        """
        Add obs to window
        """
        self._observations.append(obs)
        self._sorted_observations.add(obs)
        self._sum += obs

        if self.ready:
            # The window was already full, so we need to discard the oldest
            # observation
            discard = self._observations.pop(0)
            self._sorted_observations.remove(discard)
            self._sum -= discard
        elif len(self._observations) == self._wsize:
            # This observation caused the window to be full, so we are now
            # ready
            self.ready = True

        self._update_median()
        self._update_mean()
        self._update_std(obs)

    def _update_median(self):
        if self.ready:
            self.median = self._pivot_f()

    def _update_mean(self):
        if self.ready:
            self.mean = self._sum / self._wsize

    def _update_std(self, obs):
        if self._check_drift():
            self._variances = [math.pow(x - self.mean, 2) for x in
                               self._observations]
            self._var_sum = sum(self._variances)
            self._mean = self.mean
        elif self.ready:
            self._var_sum -= self._variances[0]
            self._variances.append(math.pow(obs - self.mean, 2))
            self._var_sum += self._variances[-1]

        try:
            self.std = math.sqrt(self._var_sum / self._wsize)
        except ValueError:
            self.std = 0

    def _pivot_odd(self):
        """
        Return the central element for a window with odd length.
        """
        return self._sorted_observations[self._pivot]

    def _pivot_even(self):
        """
        Return tohe central element for a window with even length.
        """
        return sum(self._sorted_observations[self._pivot:self._pivot + 2]) / 2

    def _check_drift(self):
        """"
        Return True if we have drifted from the mean and need to recalcualte
        the standard deviation
        """
        if self.ready and self._mean is not None:
            # Ready and we have an existing mean, so check if we drifted too
            # far and need to recompute
            try:
                drift = abs(self._mean - self.mean) / self._mean
            except ZeroDivisionError:
                # The current mean is 0
                drift = abs(self._mean - self.mean)
            return drift >= self._max_drift
        elif self.ready:
            # Just became ready, no existing mean, so computation is neeed
            return True
        else:
            # Not ready yet
            return False

