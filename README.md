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

    FIND_PACKAGE(PythonLibs 3 REQUIRED)

or

    FIND_PACKAGE(PythonLibs REQUIRED)


(the first one is probably the right one)

and re-run cmake.

on Debian(-like systems) you will have to install the `libpython3.5-dev`,`python3-pyqt5`, and `python3-pyqt5.qtquick`  packages

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

## Links

- https://doc.qt.io/archives/qq/qq10-scripting-qt.html
- https://forum.qt.io/topic/5731/fastest-way-to-execute-a-python-script-within-a-c-qt-app-on-win32-pythonqt-or-pythonize
- search for "Simon Edwards"?
- http://www.linuxjournal.com/article/8497
- http://www.codeproject.com/Articles/11805/Embedding-Python-in-C-C-Part-I
- http://www.riverbankcomputing.co.uk/software/sip/intro
- http://sourceforge.net/projects/pythonqt/files/pythonqt/
- https://docs.python.org/2/extending/embedding.html
- https://wiki.python.org/moin/EmbedingPyQtTutorial
- http://pyqt.sourceforge.net/Docs/PyQt5/signals_slots.html
- http://pyqt.sourceforge.net/Docs/PyQt5/signals_slots.html#connecting-slots-by-name
- http://stackoverflow.com/questions/17578428/pyqt5-signals-and-slots-qobject-has-no-attribute-error
- http://stackoverflow.com/questions/19427963/python-pyqt5-signals-slots
- http://stackoverflow.com/questions/19966056/pyqt5-how-can-i-connect-a-qpushbutton-to-a-slot
- http://stackoverflow.com/questions/25329091/pyqt-how-to-access-mainwindow-widgets-from-an-external-function
- http://blog.abstractfactory.io/dynamic-signals-in-pyqt/
- https://wiki.python.org/moin/PyQt/simple2
- http://stackoverflow.com/questions/17772143/the-difference-between-pyqt-and-qt-when-handling-user-defined-signal-slot
- http://pyqt.sourceforge.net/Docs/PyQt4/new_style_signals_slots.html
- https://www.commandprompt.com/community/pyqt/x1408.htm
- http://enki-editor.org/2014/08/23/Pyqt_mem_mgmt.html
