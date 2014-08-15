#!/usr/bin/env python
"""
This script creates hash codes for scripts in the autload folder.
Normally permitdlg warns about imports and private attribute access.
The idea is to ship Scribus with "signed" scripts which can be safely
used although they might use unsafe statements. 
"""

from __future__ import print_function

import sys
import os
import pprint
from scripter_runtime import hash_source


def main(files):
    # XXX add to build process somehow?
    allowed = []
    for name in files:
        if not name.endswith(("~", "#", ".pyc", ".pyo")):
            fn = os.path.join("autoload", name)
            if not os.path.isdir(fn):
                allowed.append(hash_source(fn))
    print("allowed_scripts = ", end='')
    pprint.pprint(allowed)
    
    
if __name__ == "__main__":
    main(sys.argv[1:])
