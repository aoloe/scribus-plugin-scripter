# scribus-plugin-scripter

Development version of the new Scribus scripter 

## Install

Clone the `scribus-plugin-scripter` repository and put – or symlink – its `src` directory into `scribus/plugins//` as `scripter-dev`. Then `scribus/plugins/CMakeList.txt` file and replace the following line

    ADD_SUBDIRECTORY(scripter)

with

    ADD_SUBDIRECTORY(scripter-dev)

and, then, rerun cmake with the 

    -DWANT_SCRIPTER2=1 

option.

## Notes

The error happens in:

    #23 0x00007fffcb7aadf8 in Pythonize::runScript (this=0x19bae00, 
        scriptPath=0x1a9a158 "/home/ale/docs/bin/scribus/lib/scribus/plugins/scripter/init_scripter.py")

If i reduce the `init_scripter.py` file to its first lines

    # Add path of init_scripter to Python module search path
    import sys, os
    scripter_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, scripter_path)
    print >> sys.stderr, "%s added to PYTHONPATH" % scripter_path

scribus runs correctly.

The next step will to find out which is the offending line.

## TODO

- have a look at the patch for porting the older scripter to python 3: http://bugs.scribus.net/view.php?id=11207
- port the scripter to python 3 and pyqt5
