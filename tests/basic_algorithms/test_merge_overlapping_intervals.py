import pytest
from basic_algorithms.merge_overlapping_intervals import merge_overlapping_intervals


# @pytest.fixture
# def sample_list():
#     return [1, 3, 5, 56, 78, 90, 123, 220, 300]


# @pytest.mark.parametrize("lst",  [(1, 0), (300, 8), (5, 2)])
def test_when_there_is_overlap_it_should_merge():
    inervals = [(10, 15), (20, 25), (1, 5), (-1, 2), (4, 6), (2, 4),
                (-3, 8), (-2, 1), (5, 7), (-10, -5), (-13, -8), (9, 13)]
    expected = [(-3, 8), (20, 25), (9, 15), (-13, -5)]

    actual = merge_overlapping_intervals(inervals)

    assert sorted(actual) == sorted(expected)
