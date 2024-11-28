import math
import pytest
from pymatcher_utils import All, Eq, IsInstance, check_value


def sum_value(a: int | float, b: int | float) -> int:
    return int(math.floor(a + b))


@pytest.mark.parametrize(
    "a_value, b_value, expect",
    [
        # normal without lib
        (1, 5, 6),
        # check value is equal
        # check returned instance is int
        (5, 7, All(Eq(12), IsInstance(int))),
        # check result that is < <n>.5 to make sure it is floored
        # check result is int
        (5.1, 7.1, All(Eq(12), IsInstance(int))),
        # check result that is > <n>.5 to make sure it is floored
        # check result is int
        (5.5, 7.1, All(Eq(12), IsInstance(int))),
        # check float and int input
        #   check output result is 12
        #   make sure we got back int
        (5.1, 7, All(Eq(12), IsInstance(int))),
    ],
)
def test_something(a_value, b_value, expect):
    result = sum_value(a_value, b_value)
    check_value(result, expect)
