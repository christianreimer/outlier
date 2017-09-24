"""
Running mean over N observations
"""


class RunningMean(object):
    """
    Running mean over N observations
    """
    def __init__(self, wsize):
        self.wsize = wsize
        self.sum = 0
        self.observations = []
        self.ready = False

    def __len__(self):
        return len(self.observations)

    def __str__(self):
        return 'RunningMean[{}] {}'.format(self.wsize, self.mean())

    def __iter__(self):
        return iter(self.observations)

    def add(self, obs):
        self.observations.append(obs)
        self.sum += obs

        if self.ready:
            discard = self.observations.pop(0)
            self.sum -= discard
        elif len(self.observations) == self.wsize:
            self.ready = True

    def mean(self):
        return self.ready and self.sum / self.wsize or None
