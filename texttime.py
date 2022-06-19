import time, threading

# from win32api import GetKeyState

giay = 0
phut = 0


def demgiay():
    global giay, phut
    while (1):
        time.sleep(1)
        giay += 1
        if (giay == 60):
            giay = 0
            phut += 1
            if (phut == 60): phut = 0

def init():
    t = threading.Thread(target=demgiay)
    t.start()


'''
def key_down(key):
    state = GetKeyState(ord(key))
    if (state != 0) and (state != 1):
        return True
    else:
        return False
'''
