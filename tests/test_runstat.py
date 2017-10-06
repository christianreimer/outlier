import numpy as np
import pytest
import random
import math
import runstat


def max_std_err(wsize, max_drift):
    return math.sqrt(wsize * math.pow(max_drift, 2))


def median_test(wsize, dsize):
    a = np.random.rand(dsize)
    rs = runstat.RunStat(wsize)

    for i in range(wsize):
        rs.add(a[i])

    for i in range(wsize, dsize):
        assert rs.median == np.median(a[i - wsize: i])
        rs.add(a[i])


def mean_test(wsize, dsize):
    a = np.random.rand(dsize)
    rs = runstat.RunStat(wsize)

    for i in range(wsize):
        rs.add(a[i])

    for i in range(wsize, dsize):
        assert rs.mean == pytest.approx(np.mean(a[i - wsize: i]), 0.00001)
        rs.add(a[i])


def std_test(wsize, dsize):
    a = np.random.rand(dsize)
    rs = runstat.RunStat(wsize, max_drift=0.0)

    err = max_std_err(wsize, 0.001)

    for i in range(wsize):
        rs.add(a[i])

    result = []
    for i in range(wsize, dsize):
        np_std = np.std(a[i - wsize: i])
        max_err = np.mean(a[i - wsize: i]) * err + 0.00001
        result.append(rs.std == pytest.approx(np_std, 0.001))
        rs.add(a[i])
    return result


def test_median_even():
    median_test(10, 100)


def test_median_odd():
    median_test(11, 100)


def test_mean_even():
    mean_test(10, 100)


def test_mean_odd():
    mean_test(11, 100)


def test_std_even():
    assert all(std_test(100, 1000))


def test_zero_mean_std():
    rs = runstat.RunStat(5)
    rs.add(0)
    rs.add(0)
    rs.add(0)
    rs.add(0)
    rs.add(0)
    rs.add(0)
    assert rs.std == 0


def test_imginary():
    rs = runstat.RunStat(1)
    rs.add(-1)
    rs._var_sum = -1
    rs._update_std(-1)
    assert rs.std == 0


def test_dictlike_len():
    wsize = random.randint(1, 100)
    rs = runstat.RunStat(wsize)

    for i in range(0, wsize + 3):
        rs.add(i)

    assert len(rs) == wsize


def test_dictlike_iter():
    rs = runstat.RunStat(10)
    data = list(range(5))
    for d in data:
        rs.add(d)
    assert data == list(rs)

