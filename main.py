import prtsc
import pic_comp
import time
import json
import _thread
import os_file_search

f = open('setting.json', encoding='utf-8')
setting_data = json.loads(f.read())

def rt_check():

    # 截屏
    prtsc.prtsc(setting_data['dir_window'])

    count = 5
    delay = 5 # 延迟5秒
    while count > 0:
        time.sleep(delay)

        # 截屏
        prtsc.prtsc(setting_data['dir_window'])

        picpath = setting_data['pic_path']+'\\'
        [pic1, pic2] = os_file_search.obj_locate()
        # print([pic1, pic2])
        if pic1 != "":
            pic1 = picpath+pic1
            pic2 = picpath+pic2
            print(pic_comp.image_contrast(pic1, pic2))

        # count -= 1

if __name__ == '__main__':
    try:
        _thread.start_new_thread( rt_check, () )
    except:
        print ('Error: 无法启动线程')

    while 1:
        pass
