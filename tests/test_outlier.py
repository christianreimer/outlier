import numpy as np
import outlier


def test_no_outlier():
    data = np.random.random(100)

    out = outlier.Outlier(100, 5)
    for d in data:
        assert not out.add_and_check(d)


def test_outlier():
    data = np.random.randint(0, 100, 500)
    out = outlier.Outlier(100, 3, max_drift=0.001)
    results = []

    for d in data:
        out.add(d)
        if not out.rs.ready:
            continue

        a = np.array(list(out.rs))
        s = np.std(a)
        m = np.mean(a)

        d = np.random.randint(50, 500)

        if out.check(d):
            results.append(d >= (3 * s + m))
        else:
            results.append(d < (3 * s + m))

    correct = sum([1 for r in results if r])
    assert correct / len(results) >= 0.98
