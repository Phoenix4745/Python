from time import sleep, time
from subprocess import call
from webbrowser import get
from pyautogui import *
from datetime import datetime, date
from discord_webhook import DiscordWebhook, DiscordEmbed
'''
curr = datetime.datetime.strptime('09:50:00', '%H:%M:%S').time()
print(curr)
print(type(curr))
sleep(3)
curr1 = datetime.datetime.now().time()
print(curr1)
a = (curr1 - curr)
print(type(a))
print(a)


date_time_str = '09:50:00'

date_time_obj = datetime.strptime('09:50:00', '%H:%M:%S')


print ("The type of the date is now",  type(date_time_obj))
print ("The date is", date_time_obj)



from datetime import datetime, date

start_time = datetime.strptime('09:50:00', '%H:%M:%S').time()
stop_time = datetime.now().time().replace(microsecond=0)
print(stop_time)
d = date(2022, 1, 1)
print(d)
datetime1 = datetime.combine(d, start_time)
print(type(datetime1))
datetime2 = datetime.combine(d, stop_time)
print(datetime2)
time_elapsed = (datetime2 - datetime1).total_seconds()

print(time_elapsed)

currentTime = datetime.now().time().replace(microsecond=0)
nextClassTime = datetime.strptime(period_time[nth_period+1], '%H:%M:%S').time()
d = date(2022, 1, 1)
time_elapsed = (datetime.combine(d, nextClassTime) - datetime.combine(d, currentTime)).total_seconds()
sleep(time_elapsed)'''

meet_code='phy'
def meet():
    bravePath = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe --profile-directory='Default' %s"
    get(bravePath).open_new_tab('https://meet.google.com/oqm-bstk-hzk')
    sleep(1.5)
    pgloaded()
    
    global k
    k = 0
    while k < 56:
        if locateOnScreen('meetError1.png', region=(375, 237, 617, 118), grayscale = True):
            print(f'Meeting Status : Not Started Yet, Retrying in {15+k} secs')
            sleep(15 + k)
            hotkey('ctrl', 'l')
            sleep(0.01)
            write('g.co/meet/10c' + meet_code)
            press('enter')
            sleep(0.1)
            k = k+5
            pgloaded()
        else:
            break
    else:
        print('Class not there')
    
    while k < 56:
        ready = locateOnScreen('getready1.png', region = (979, 367, 164, 25), grayscale = True, confidence = 0.7)
        print(ready)
        if ready == None:
            print('wait Over')
            sleep(0.8)
            joinNow = locateCenterOnScreen('joinNow1.png', region= (935, 382, 116, 80), grayscale = True)
            if joinNow:
                print('Meeting Status : Started, Joining...')
                x,y = joinNow
                print(x,y)
                click(x, y)#993, 410; 993, 399
                sleep(0.01)
                hotkey('ctrl', 'e')
                sleep(0.01)
                hotkey('ctrl', 'd')
                break
            
            elif locateOnScreen('meetError2.png', region=(434, 173, 497, 38), grayscale = True) or locateOnScreen('meetError31.png', region=(359, 173, 648, 82), grayscale = True):
                print('meetError2 or meetError3')
                sleep(0.5)
                hotkey('ctrl', 'l')
                sleep(0.01)
                write('g.co/meet/10c' + meet_code)
                press('enter')
                sleep(0.1)
                pgloaded()                
            
def pgloaded():
    while True:
        if locateOnScreen('loaded.png', region = (79, 41, 14, 14), grayscale = True):
            print(f'pgLoaded')
            sleep(0.1)
            break

meet()