# RT_Check

## 介绍

RT_Check（Real-time Check）是一个根据窗口截屏来实现实时检查的py脚本。

图片的比较阈值可在setting.json中设置"diff_threshold"。（当前版本尚未使用图片阈值）

## 安装、使用

1. 安装python3；
2. 安装所需py库文件，见下表；
   | No. | Name |
   | :-: | :-: |
   |1| json|
   |2| os |
   |3| time|
   |4| _thread|
   |5| PyQt5.QtWidgets |
   |6| PyQt5.QtGui |
   |7| win32gui |
   |8| sys |
   |9| math |
   |10| operator |
   |11| functools.reduce |
   |12| pillow |
3. 打开需要实时check的窗口，然后运行first_step.py，获取该窗口的title；
4. 运行main.py。

## Licence

[MIT © DarkBlue.](./LICENSE)

