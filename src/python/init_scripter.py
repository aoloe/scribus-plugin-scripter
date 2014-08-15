# Add path of init_scripter to Python module search path
from __future__ import print_function

import sys, os
scripter_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, scripter_path)
print("%s added to PYTHONPATH" % scripter_path, file=sys.stderr)

# Look for PyQt
try:
    from PyQt4.QtCore import PYQT_VERSION_STR,  QObject,  QCoreApplication
    from PyQt4.QtGui import qApp,  QMenu
except ImportError:
    print("Python cannot find the Qt4 bindings.", file=sys.stderr)
    print("Please make sure, that the needed packages are installed.", file=sys.stderr)
    print("On Ubuntu and Debian(-like) distributions you have to install python-qt4", file=sys.stderr)
    raise
try:
    from PyQt4 import QtScript
except ImportError as e:
    print("You seem to have Qt4 bindings without QtScript support.", file=sys.stderr)
    print("This is currently a requirement.", file=sys.stderr)
    print("Please make sure you have also libqt4-script installed.", file=sys.stderr)
    raise

# Shows nice looking error dialog if an unhandled exception occures.
import excepthook
excepthook.install()


# Make sure PyQt is new enough
if float(PYQT_VERSION_STR[:3]) < 4.4:
    print("Your installed PyQt4 is older than version 4.4", file=sys.stderr)
    print("A newer version is needed. Please upgrade your packages.", file=sys.stderr)
    raise ImportError("PyQt4 not new enough")

# Import helper modules
from scripter_hooks import MenuHooks
from mikro import create_pyqt_object, Error as MiKroError


# Scripter and i18n should be available everywhere globally
import __builtin__
__builtin__.Scripter = create_pyqt_object(qApp).Scripter
Scripter.qt.setParent(None)

__builtin__.app = Scripter # shorter name for lazy people
__builtin__.i18n = lambda s: unicode(QCoreApplication.translate("Scripter", s))
Scripter.Error = MiKroError
Scripter.path = scripter_path



class ScripterMenu(QObject):
    """
    Scripter menu item in mainWindow menubar
    """

    def __init__(self, parent):
        QObject.__init__(self, parent)
        self.setObjectName("Menu")
        self.popup = QMenu(i18n("Scripter"))
        MenuHooks().insertMenuAfter("E&xtras", self.popup)
        self.scriptsMenu = QMenu(i18n("Scripts"))
        MenuHooks().appendItem(self.popup, self.scriptsMenu)
        self._load_entries()


    def _load_entries(self):
        for path in [scripter_path, os.path.expanduser("~/.scribus/scripter/")]:
            autoload_path = os.path.join(path, "autoload")
            if not os.path.exists(autoload_path):
                continue
            sys.path.insert(0, autoload_path)
            from scribusscript import load_scripts
            self.autoload_scripts = scripts = load_scripts(autoload_path)
            for sd in scripts:
                try:
                    sd.install()
                except:
                    excepthook.show_current_error(i18n("Error installing %r") % sd.name)


    def addAction(self, title, callback, *args):
        self.popup.addAction(title, callback, *args)


    def addSeparator(self):
        self.popup.addSeparator()
        

def createMenu(mainWindow):
    Scripter.menu = ScripterMenu(mainWindow)

Scripter.connect("createMenu(QMainWindow*)", createMenu)
    
