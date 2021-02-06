import os
import json

f = open('setting.json', encoding='utf-8')
setting_data = json.loads(f.read())

def obj_locate():
    res = ["", ""]

    for root, dirs, files in os.walk(".\\pic\\", topdown=False):
        for name in files:
            if -1 != name.find(f"{setting_data['pic_prefix']}") and -1 != name.find('.jpg'):
                if name >= res[0]:
                    res[1] = res[0]
                    res[0] = name
                    continue
                if name >= res[1]:
                    res[1] = name
    return res
