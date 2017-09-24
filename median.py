"""
Running median over the last N observations
"""

import sortedcontainers


class RunningMedian(object):
    """
    Running median over the last N observations.
    Most have seen at least N observations before a median is returned.
    """
    def __init__(self, wsize=101):
        self.wsize = wsize
        self.pivot = wsize // 2
        self.window_sorted = sortedcontainers.SortedList()
        self.window_obs = []
        self.ready = False

        if wsize % 2:
            self._pivot = self._pivot_odd
        else:
            self.pivot -= 1
            self._pivot = self._pivot_even

    def __len__(self):
        return len(self.window_obs)

    def __iter__(self):
        return iter(self.window_obs)

    def _pivot_odd(self):
        """
        Return the central element for a window with odd length.
        """
        return self.window_sorted[self.pivot]

    def _pivot_even(self):
        """
        Return the central element for a window with even length.
        """
        return sum(self.window_sorted[self.pivot:self.pivot + 2]) / 2

    def add(self, observation):
        """
        Add observation to window.
        """
        self.window_obs.append(observation)
        self.window_sorted.add(observation)

        if self.ready:
            discard = self.window_obs.pop(0)
            self.window_sorted.remove(discard)
        elif len(self.window_obs) == self.wsize:
            self.ready = True

    def median(self):
        """
        Return the median value or None if insufficient observations have been
        recorded.
        """
        return self.ready and self._pivot() or None


def main():
    import random
    m = RunningMedian(101)
    for _ in range(1_000_000):
        m.add(random.random())
        m.median()


if __name__ == '__main__':
    main()
