import numpy as np
import outlier


def test_no_outlier():
    data = np.random.random(100)

    out = outlier.Outlier(100, 5)
    for d in data:
        assert not out.add_and_check(d)


def test_outlier():
    data = np.random.random(100)
    std = np.std(data)

    out = outlier.Outlier(100, 3, drift=0.001)
    for d in data:
        out.add(d)
    should_be_outlier = np.mean(data) + 3.1 * std
    assert out.check(should_be_outlier)
