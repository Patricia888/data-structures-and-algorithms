from .towers_of_hanoi import towers_of_hanoi


def test_towers_of_hanoi_with_2_disks():
    '''test with 2 disks'''
    assert towers_of_hanoi(2) == (3, [2, 1], [], [])


def test_towers_of_hanoi_with_3_disks():
    """test with 3 disks"""
    assert towers_of_hanoi(3) == (7, [3, 2, 1], [], [])


def test_towers_of_hanoi_with_7_disks():
    """test with 7 disks"""
    assert towers_of_hanoi(7) == (127, [7, 6, 5, 4, 3, 2, 1], [], [])


def test_towers_of_hanoi_with_10_disks():
    """test with 10 disks"""
    assert towers_of_hanoi(10) == (1023, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [], [])
