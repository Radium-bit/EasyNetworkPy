"""
Copyright(C)Radium-bit
but not include other's code
"""
import sys
from choice import *
from func import welcome, guide
from check import request_UAC, ctypes

if request_UAC() == 0:
    welcome()
    guide()
    choice()
else:
    # Re-run the program with admin rights
    print("\nNot Enough UAC Permisssion")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    input()