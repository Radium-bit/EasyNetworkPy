"""
Copyright(C)Radium-bit
but not include other's code
"""
import sys
from choice import *
from check import request_UAC, ctypes

if request_UAC() == 0:
    func.welcome()
    func.guide()
    choice()
else:
    # Re-run the program with admin rights
    print("\nNot Enough UAC Permisssion, your Group is ")
    func.system("whoami")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    input()
