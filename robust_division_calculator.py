def safe_divide(numerator, denominator):
    numerator = float(numerator)
    denominator = float(denominator)
    
    ZeroDivisionError
    if denominator == 0:
        return "Error: Dividion by zero is not allowed."
    
    ValueError
    return "Error: Invalid input. Please enter numeric values."