"""A module for demonstrating exceptions"""

def convert(s):
    """Convert to an integer"""
    x = -1
    try:
        x = int(s)
        print("Conversion Succeeded! x =", x)
    except (ValueError, TypeError):
        print("Conversion Failed!")
    return x