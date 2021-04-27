import pytest
from basic_algorithms.binary_search import binary_search


@pytest.fixture
def sample_list():
    return [1, 3, 5, 56, 78, 90, 123, 220, 300]


@pytest.mark.parametrize("key_expected_result",  [(1, 0), (300, 8), (5, 2)])
def test_when_element_exists_should_return_index(sample_list, key_expected_result):
    result = binary_search(sample_list, key_expected_result[0])

    assert result == key_expected_result[1]


@pytest.mark.parametrize("key", [-100, 1000, None, 0])
def test_when_element_not_exists_should_return_negative_number(sample_list, key):
    result = binary_search(sample_list, key)

    assert result < 0


@pytest.mark.parametrize("lst", [None, []])
def test_when_list_is_blank_should_return_negative_number(lst):
    result = binary_search(lst, 1)

    assert result < 0
