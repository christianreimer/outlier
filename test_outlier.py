import random
import outlier


def test_no_outlier():
    out = outlier.Outlier(11, 3)
    for _ in range(100):
        assert not out.add_and_check(1)


def test_outlier():
    out = outlier.Outlier(11, 3)
    for _ in range(100):
        out.add_and_check(random.random())
    assert out.add_and_check(3)

