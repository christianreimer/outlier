import numpy as np
import outlier


def test_no_outlier():
    data = np.random.random(100)

    out = outlier.Outlier(100, 5)
    for d in data:
        assert not out.add_and_check(d)


def outlier_test(wsize, factor, low, high):
    data = np.random.randint(low, high, 1000)
    out = outlier.Outlier(wsize, factor, max_drift=0.001)
    success_count = 0
    count = 0

    for d in data:
        out.add(d)
        if not out.rs.ready:
            continue

        a = np.array(list(out.rs))
        s = np.std(a)
        m = np.mean(a)

        d = np.random.randint(low + high // 2, high * factor)
        np_outlier = d >= (factor * s + m)

        if out.check(d) == np_outlier:
            success_count += 1
        count += 1

    return success_count / count


def test_odd_95pct():
    assert outlier_test(101, 3, 0, 100) >= 0.95


def test_even_95pct():
    assert outlier_test(100, 3, 0, 100) >= 0.95


def test_odd_98pct():
    assert outlier_test(101, 3, 0, 100) >= 0.98


def test_even_98pct():
    assert outlier_test(100, 3, 0, 100) >= 0.98


