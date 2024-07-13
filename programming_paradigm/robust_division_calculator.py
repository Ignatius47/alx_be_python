def safe_divide(numerator, denominator):
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            return "Error: Cannot divide by zero."
        return numerator / denominator
    except ValueError:
        return "Error: Invalid input. Please enter numeric values."
