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

## Python 3

To compile against Python 3, you will need to edit the `CMakeLists.txt` in the top-level scribus directory. Change the following line

    FIND_PACKAGE(PythonLibs 2 REQUIRED)

to

    FIND_PACKAGE(PythonLibs REQUIRED)

or 

    FIND_PACKAGE(PythonLibs 3 REQUIRED)

(not sure yet, which one is the right one)

and re-run cmake.

on Debian(-like systems) you will have to install the `libpython3.5-dev` package

## Roadmap

- [ ] check if we want to stay with pythonize
- [ ] get the signals and slots to be connected accross the c++ / python boundary (or avoid using signals and slots for the communication between scribus and the scripter: is it possible?)
- [ ] specify the API structure
  - check http://wiki.scribus.net/canvas/Scripter2_API, somehow describing the new API
- [ ] create a concept for the documentation
  - https://scribus-scripter.readthedocs.org already exists
- [ ] create a platform for the documentation
- [ ] define the full API
- [ ] implement the missing commands
- [ ] remove or fix the scripter console
- [ ] port the scripts included in Scribus
  - make a list of classes and function and list their matching old scripter commands
- [ ] finish the scripts downloader
- [ ] create a test suite?

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

## Scribus Bug Tracker

- [0011207: Scripter Python 3 compatibility](http://bugs.scribus.net/view.php?id=11207)

## TODO

- have a look at the patch for porting the older scripter to python 3: http://bugs.scribus.net/view.php?id=11207
- port the scripter to python 3 and pyqt5
