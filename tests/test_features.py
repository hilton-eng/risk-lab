import pytest

from risk_lab.features import debt_to_income


def test_basic_ratio():
    assert debt_to_income(500, 2000) == 0.25


def test_zero_income_raises():
    with pytest.raises(ValueError):
        debt_to_income(500, 0)


@pytest.mark.parametrize(
    "debt, income, expected",
    [(0, 1000, 0.0), (1000, 1000, 1.0), (250, 1000, 0.25)],
)
def test_ratios(debt, income, expected):
    assert debt_to_income(debt, income) == expected
