#这个是用来刷角色剧情石头的脚本
#因为操作之间的间隔只是单纯的暂停，所以显然会受到网络状况影响
#如要使用请灵性调参
#模拟器分辨率设置1440×810

import os
import time

total_times = 50  #需要挂机的剧情个数

print('start')

os.chdir('C:/Program Files (x86)/MuMu/emulator/nemu/vmonitor/bin')

num = 0
os.system('adb_server.exe kill-server')

os.system('adb_server.exe connect 127.0.0.1:7555')

os.system('adb_server.exe -s 127.0.0.1:7555 shell input tap 510 770')
time.sleep(1)
os.system('adb_server.exe -s 127.0.0.1:7555 shell input tap 830 550')

while num < total_times:      
    time.sleep(1)
    os.system('adb_server.exe -s 127.0.0.1:7555 shell input tap 900 190')
    time.sleep(1)
    os.system('adb_server.exe -s 127.0.0.1:7555 shell input tap 950 300')
    time.sleep(1)
    os.system('adb_server.exe -s 127.0.0.1:7555 shell input tap 720 560')
    time.sleep(2)
    os.system('adb_server.exe -s 127.0.0.1:7555 shell input tap 1380 60')
    time.sleep(1)
    os.system('adb_server.exe -s 127.0.0.1:7555 shell input tap 1210 70')
    time.sleep(1)
    os.system('adb_server.exe -s 127.0.0.1:7555 shell input tap 880 560')
    time.sleep(3)
    os.system('adb_server.exe -s 127.0.0.1:7555 shell input tap 720 720')
    time.sleep(1)
    os.system('adb_server.exe -s 127.0.0.1:7555 shell input tap 55 50')
    num += 1
    
print('end')
