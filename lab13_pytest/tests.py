import pytest
from main import bubblesort


def test_bubblesort_1():

    list1 = [12, 4, 6, 3, 8, 23, 67, 98]
    list1_sorted = [3, 4, 6, 8, 12, 23, 67, 98]

    result1 = bubblesort(list1)

    assert result1 == list1_sorted


def test_bubblesort_2():
    list2 = [1, 0, 21, 54, 67, 73, 956, 111]
    list2_sorted = [0, 1, 21, 54, 67, 73, 111, 956]

    result2 = bubblesort(list2)

    assert result2 == list2_sorted


testdata = [[12, 4, 6, 3, 8, 23, 67, 98], [1, 0, 21, 54, 67, 73, 956, 111]]

@pytest.mark.parametrize('sample', testdata)
def test_bubblesort_sample(sample):

    list_sorted = sorted(sample)
    result = bubblesort(sample)

    assert result == list_sorted