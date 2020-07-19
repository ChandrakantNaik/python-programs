"""
    Demonstrating EAFP (It's Easier to Ask Forgiveness than Permission)
     Here we simply attempt the operation without checks in advance, but we have an exception handler in place to deal with any 
     problems. We don't even need to know in a lot of detail exactly what might go wrong. Here we catch OSError, which covers all 
     manner of conditions such as file not found and using directories where files are expected. 
     
     EAFP is standard in Python, and that philosophy is enabled by exceptions. 
"""

import os

p = r'C:\Users\cnaik1\resume.docx'

try:
    process_file(p)
except OSError as e:
    print("Could not process file because{}", format(str(e)))