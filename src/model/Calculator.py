import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.controller import Database
from src.model.InputOutputFunctions import tax_rate
from src.model.CalculationFunctions import calculate_non_taxable_income
from src.model.Exceptions import (
    NonNumericDeductionError, ZeroIncomeError, InvalidDeductionError,
    InvalidPercentageError, NonNumericIncomeError, UserDontExist
)

def calculate_taxes(income, deduction, tax_percentage):
    try:
        if not isinstance(income, (int, float)):
            raise NonNumericIncomeError()
        if not isinstance(deduction, (int, float)):
            raise NonNumericDeductionError()
        if income == 0:
            raise ZeroIncomeError()
        if deduction < 0 or deduction > income:
            raise InvalidDeductionError()
        if tax_percentage < 0 or tax_percentage > 100:
            raise InvalidPercentageError()

        # Tax calculation
        tax = (income - deduction) * (tax_percentage / 100)
        return tax

    except (NonNumericIncomeError, NonNumericDeductionError, ZeroIncomeError, InvalidDeductionError, InvalidPercentageError) as e:
        print(f"Error: {e}")

def search_user(user_id):
    """Search user by ID."""
    user = Database.get_user_by_id(user_id)
    if user is None:
        raise UserDontExist
    return user
