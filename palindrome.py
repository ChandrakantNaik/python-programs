import unittest

# import pdb; pdb.set_trace()

def digits(x):
    """ Convert an Integer into list of digits .
        Args : x - the number of digits we want.
        Returns : A list of digits, in order, of ''x''.
        >>> digits(4586378)
        [4,58,6,3,7,8]
    """
    digs = []
    while x!= 0:
        div, mod = divmod(x,10)
        digs.append(mod)
        x = div
    return digs


def is_palindrome(x):
    """ Determine if an digit is palindrome.
        Args : x - The number to check for palindromity
        Returns : True if the digits of ''x'' are a palindrome, False otherwise

        >>> is_palindrome(1234)
        False
        >>> is_palindrome(2468642)
        True    
    """
    digs = digits(x)
    for f, r in zip(digs, reversed(digs)):
        if f != r:
            return False
        return True

class Tests(unittest.TestCase):
    """ Tests for the is_palindrom function."""
    def test_negative(self):
        "Check that it returns False correctly."
        self.assertFalse(is_palindrome(1234))
    
    def test_positive(self):
        "Check that it returns True correctly."
        self.assertTrue(is_palindrome(1234321))
    
    def test_single_digit(self):
        "Check that it works for a single digit numbers."
        for i in range(10):
            self.assertTrue(is_palindrome(i))

if __name__ == '__main__':
    unittest.main()
    
