def safe_divide(numerator, denominator):
        try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            return "Error: Cannot divide by zero."
        return numerator / denominator
    except ValueError:
        return "Error: Please enter numeric values only."
