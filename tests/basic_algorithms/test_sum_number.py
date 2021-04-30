import pytest
from basic_algorithms.sum_number import sum_number


@pytest.mark.parametrize("number", [-1, -10, -1000])
def test_when_number_is_negative_should_raise_error(number):
    with pytest.raises(ValueError, match=r"Invalid number, the number should be a positive number!"):
        sum_number(number)


@pytest.mark.parametrize("number_expected_result", [(0, 0), (1, 1), (7, 28), (15, 120)])
def test_when_number_is_greate_than_zero(number_expected_result):
    result = sum_number(number_expected_result[0])

    assert result == number_expected_result[1]
