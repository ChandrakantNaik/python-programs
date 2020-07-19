"""Demonstrating LBYL (Look Before Your Leap)

There are several problems with this approach, some obvious and some insidious. One obvious problem is that we only perform 
an existence check. What if the file exists, but contains garbage? What if the path refers to a directory instead of a file? 
According to LBYL, we should add preemptive tests for these too. A more subtle problem is that there is a race condition here. 
It's possible for the file to be deleted, for example by another process, between the existence check and the process_file call, 
a classic atomicity issue. There's really no good way to deal with this. Handling of errors from process_file will be needed in 
any case.
"""

import os

p = r'C:\Users\cnaik1\resume.docx'

if os.path.exists(p):
    process_file(p)
else:
    print("No such file as {}", format(p))