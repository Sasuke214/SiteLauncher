from distutils.core import setup
import py2exe
import sys
if len(sys.argv) == 1:
    sys.argv.append("py2exe")
setup( options = {"py2exe": {"includes": ["tkinter","webbrowser"]}},
       console=["websitelauncher.py"])

