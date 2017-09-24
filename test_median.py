import median


def test_empty():
    m = median.RunningMedian()
    assert not m.median()


def test_not_full():
    lng = 5
    m = median.RunningMedian(lng)
    for _ in range(lng - 1):
        m.add(1)
    assert not m.median()


def test_all_same_number_odd():
    m = median.RunningMedian(3)
    for _ in range(3):
        m.add(314159)
    assert m.median() == 314159


def test_all_same_number_even():
    m = median.RunningMedian(4)
    for _ in range(4):
        m.add(314159)
    assert m.median() == 314159


def test_cutover_odd():
    m = median.RunningMedian(3)
    m.add(1)
    m.add(1)
    m.add(2)  # 1 1 2
    assert m.median() == 1
    m.add(3)  # 1 2 3
    assert m.median() == 2
    m.add(2)  # 2 2 3
    assert m.median() == 2


def test_cutover_even():
    m = median.RunningMedian(4)
    m.add(1)
    m.add(1)
    m.add(1)
    m.add(2)  # 1 1 1 2
    assert m.median() == 1
    m.add(3)  # 1 1 2 3
    assert m.median() == 1.5
    m.add(2)  # 1 2 2 3
    assert m.median() == 2


def test_length():
    m = median.RunningMedian(3)
    assert not len(m)
    m.add(1)
    assert len(m) == 1
    m.add(1)
    m.add(1)
    m.add(1)
    m.add(1)
    assert len(m) == 3
