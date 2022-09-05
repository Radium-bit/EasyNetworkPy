"""
Copyright(C)Radium-bit
but not include other's code
"""

import ctypes

def request_UAC():    ## Check Permission from UAC, the way from
    try:              ## https://stackoverflow.com/questions/130763/request-uac-elevation-from-within-a-python-script
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def input_err():
    print("输入错误或已退出！,Debug-code 0x0001")


def not_support():
    print("Error! 功能尚未支持，Debug code 0x0002")
