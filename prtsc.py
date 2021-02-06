from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import win32gui
import sys
import json

import get_hwnd
import get_time

f = open('setting.json', encoding='utf-8')
setting_data = json.loads(f.read())

# 根据title截图
def prtsc(title):
    hwnd = win32gui.FindWindow(None, title)
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(hwnd).toImage()

    ctime = get_time.get_time()
    img.save(f"{setting_data['pic_path']}{setting_data['pic_prefix']}{ctime}.jpg")

# 打印当前运行程序的hwnd和title
def prt_hwnd():
    get_hwnd.prt_hwnd_title()
