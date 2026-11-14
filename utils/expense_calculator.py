import re


class Calculator:

    @staticmethod
    def _to_float(value) -> float:
        """Clean strings like '$80', '1,200.50', or '7 days' and convert to float."""
        if isinstance(value, (int, float)):
            return float(value)
        cleaned = re.sub(r"[^\d.-]", "", str(value))
        return float(cleaned) if cleaned else 0.0

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers (integers or floats).

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The product of a and b.
        """
        return Calculator._to_float(a) * Calculator._to_float(b)

    @staticmethod
    def calculate_total(*x: float) -> float:
        """Calculate sum of the given list of numbers.

        Args:
            x (list): List of numbers.

        Returns:
            float: The sum of numbers in the list x.
        """
        return sum(Calculator._to_float(val) for val in x)

    @staticmethod
    def calculate_daily_budget(total: float, days: int) -> float:
        """Calculate daily budget.

        Args:
            total (float): Total cost.
            days (int): Total number of days.

        Returns:
            float: Expense for a single day.
        """
        total_val = Calculator._to_float(total)
        days_val = int(Calculator._to_float(days))
        return total_val / days_val if days_val > 0 else 0.0
