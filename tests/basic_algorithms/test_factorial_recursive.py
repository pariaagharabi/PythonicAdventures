import pytest
from basic_algorithms.factorial_recursive import fact


@pytest.mark.parametrize("number", [-1, -10, -1000])
def test_when_number_is_negative_should_raise_error(number):
    with pytest.raises(ValueError, match=r"Number should be greater or equel zero!"):
        fact(number)


@pytest.mark.parametrize("number_expected_result", [(0, 1), (1, 1), (2, 2), (3, 6), (5, 120), (7, 5040)])
def test_when_number_is_zero_should_return_one(number_expected_result):
    result = fact(number_expected_result[0])

    assert result == number_expected_result[1]
