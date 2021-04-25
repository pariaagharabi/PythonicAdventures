import pytest
from basic_algorithms.factorial_recursive import fact


def test_when_number_is_negative_should_raise_error():

    with pytest.raises(ValueError, match=r"Number should be greater or equel zero!"):
        fact(-1)
