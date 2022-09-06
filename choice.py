"""
Copyright(C)Radium-bit
but not include other's code
"""
import func
import check
"""1. 清除DNS缓存\t\t2. 重置网络设定\n\n3. 防火墙设定\t\t4. 打开安全策略\n\n5. 打开网卡适配器面板\t6. 打开证书面板\n\n7. Hosts文件相关\t\t8. 关于本项目\n\n"""
def FWC():
    func.clear()
    print("请输入要执行的操作数字代号...\n")
    print("1. 启动防火墙\n\n2. 关闭防火墙\n\n3. 启动防火墙设定面板")
    ch = int(input())
    if ch == 1:
        func.OnFirewall()
    elif ch == 2:
        func.OffFirewall()
    elif ch == 3:
        func.AdvancedFW()

def AboutHosts():
    func.clear()
    print("请输入要执行的操作数字代号...\n")
    print("1. 打开Hosts文件\n\n2. 重置Hosts文件\n\n3. 备份Hosts文件")
    ch = int(input())
    if ch == 1:
        func.OpenHFile()
    elif ch == 2:
        check.not_support()
    elif ch == 3:
        func.backupHosts()

def choice():
    ch = int(input())
    if ch == 1:
        func.clearDNS()
    elif ch == 2:
        func.resetNetwork()
    elif ch == 3:
        FWC()
    elif ch == 4:
        func.SecurityControl()
    elif ch == 5:
        func.NetworkManager()
    elif ch == 6:
        func.Crtmgr()
    elif ch == 7:
        AboutHosts()
    elif ch == 8:
        func.AboutProject()
    else:
        check.input_err()
