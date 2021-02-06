import time
import json

global prt_flag
prt_flag = False

def get_ticks():
    # 打印时间戳
    ticks = time.time()
    if prt_flag:
        print('current time ticks:', ticks)

def get_time():
    # 打印当地时间
    localtime = time.localtime(time.time())
    if prt_flag:
        print('current local time:', localtime)

    # 格式化当地时间
    formattedtime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    if prt_flag:
        print('current formatted local time:', formattedtime)

    return formattedtime
