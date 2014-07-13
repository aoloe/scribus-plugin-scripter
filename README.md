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

## TODO

- have a look at the patch for porting the older scripter to python 3: http://bugs.scribus.net/view.php?id=11207
- port the scripter to python 3 and pyqt5
