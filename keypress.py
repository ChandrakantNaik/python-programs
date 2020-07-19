"""
    keypress - A module for detecting a single keypress.
    msvcrt : Microsoft Visual C Runtime

"""

try:
    import msvcrt

    def getkey():
        """Wait for a keypress and return a single character string."""
        return msvcrt.getch()

except ImportError:

    import sys
    import tty
    import termios

    def getkey():
        """Wait for a keypress and return a single character string."""
        fd = sys.stdin.fileno()
        original_attributes = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
        return ch

    # If either of the Unix-specific tty or termios are not found,
    # we allow the ImportError to propagate from here
"""
    Within the first try block we attempt to import msvcrt, the Microsoft Visual C runtime. If this succeeds, we then proceed to 
    define a function getkey(), which delegates to the msvcrt. getch() function. Even though we are inside a try block at this point, 
    the function will be declared at the current scope, which is the module scope. If, however, the import of msvcrt fails because 
    we're not running on Windows, an ImportError will be raised, and execution will transfer to the except block. This is a case of
    an error being silenced explicitly because we're going to attempt an alternative course of action in the exception handler. 
    Within the except block we import three modules needed for a getkey() implementation on Unix-like systems, and then proceed to 
    the alternative definition of getkey(), which again binds the function implementation to a name in the module scope. This Unix
    implementation of getkey() uses a try…finally construct to restore various terminal attributes after the terminal has been put 
    into raw mode for the purposes of reading a single character. In the event that our program is running on neither Windows nor a 
    Unix-like system, the import tty statement will raise a second import error. This time we make no attempt to intercept this 
    exception. We allow it to propagate to our caller, which is whatever attempted to import this keypress module. We know how to 
    signal this error, but not how to handle it, so we defer that decision to our caller. The error will not pass silently. If the 
    caller has more knowledge or alternative tactics available, it can in turn intercept this exception and take appropriate action, 
    perhaps degrading to using Python's input built-in function and giving a different message to the user.
"""