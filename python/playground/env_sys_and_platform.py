import os, platform



def os_name():
    res = os.name
    print(res)
    return res

def platform_sys():
    res = platform.system()
    print(res)
    return res

def platform_release():
    res = platform.release()
    print(res)
    return res


def is_win():
    win = 'win'
    return win in os_name()


os_name()
platform_release()
platform_sys()

print(is_win())