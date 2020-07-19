"""A module for demonstrating exceptions"""

def convert(s):
    """Convert to an integer"""
    try:
        x = int(s)
        print("Conversion Succeeded! x =", x)
    except ValueError:
        print("Conversion Failed!")
        x = -1
    except TypeError:
        print("Conversion Failed!")
        x = -1
    return x