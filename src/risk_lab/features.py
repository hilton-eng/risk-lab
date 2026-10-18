def debt_to_income(debt: float, income: float) -> float:
    """Return debt divided by income. Income must be positive."""
    if income <= 0:
        raise ValueError("income must be positive")
    return debt * income
