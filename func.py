"""
Copyright(C)Radium-bit
"""
from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def welcome():
    print("\n欢迎使用EasyNetwork网络快捷管理程序")
    input("\n")
    clear()
    print("\033[1;33;0mWARNING\n你需要管理员权限来执行此程序！\n现在检查权限，并确认进行下一步\n\033[0m")
    print("当前用户组为：\n")
    system("whoami")
    input("")


def guide():
    print("请输入要执行的操作数字代号...\n\n")
    print("1. 清除DNS缓存\t\t2. 重置网络设定\n\n3. 防火墙设定\t\t4. 打开安全策略\n\n5. 打开网卡适配器面板\t6. 打开证书面板\n\n7. Hosts文件相关\t\t8. 关于本项目\n\n")
    print("不输入按空格或任意键退出，输入后请回车确认\n")

def clearDNS():
    system("ipconfig /flushdns")


def resetNetwork():
    system("netsh winsock reset")


def SecurityControl():
    system("secpol.msc")
    return 0


def NetworkManager():
    system("ncpa.cpl")
    return 0


def Crtmgr():
    system("certmgr.msc")
    return 0


## Firewall Control Part
def OnFirewall():
    system("netsh advfirewall set allprofiles state on")
    print("Windows防火墙已开启")
    system("pause")
    return 0


def OffFirewall():
    system("netsh advfirewall set allprofiles state off")
    system("Windows防火墙已关闭")
    system("pause")
    return 0


def AdvancedFW():
    system("control.exe /name Microsoft.WindowsFirewall")
    return 0


## Hosts Modify part
def OpenHFile():
    system("notepad %systemroot%/system32/drivers/etc/hosts")
    return 0


def resetHosts():
    return 2


def backupHosts():
    """
	char* path, str[50], command[100];
	path = str;
	printf("请输入想要备份Hosts文件到的路径。");
	printf("例如：C:\\Users\\Public\n");
	scanf("%s", path);
	sprintf(command, "copy C:\\Windows\\System32\\drivers\\etc\\hosts %s", str);
	system(command);
	"""
    return 2


def trying() -> object:
    print("Test is OK!")

def AboutProject():
    system("start https://github.com/Radium-bit/EasyNetwork")
