from time import sleep
from subprocess import call
from webbrowser import get
from pyautogui import locateOnScreen, hotkey, press, write, click, locateCenterOnScreen
from datetime import datetime, date
from discord_webhook import DiscordWebhook, DiscordEmbed

def meet():
    bravePath = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe --profile-directory='Profile 1' %s"
    get(bravePath).open_new_tab('https://g.co/meet/10c' + meet_code)
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
                click(x, y)#993; 410, 405, 399, 417
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

def connection():
    while response := not 0:
        response = call('ping discord.com -n 1')
        if response == 0:
            print("Connected to internet")
            break
        else:
            print('Tying to connect')
            sleep(1)

def pgloaded():
    while True:
        if locateOnScreen('loaded.png', region = (79, 41, 14, 14), grayscale = True):
            print('pgLoaded')
            sleep(0.7)
            break

def sendMsg():
    webhook = DiscordWebhook(url = discordUrl)
    if k < 56:
        embed = DiscordEmbed(title='Class Joined Succesfully', description="Here are your class details with :heart:", color='03b2f8')
    else:
        embed = DiscordEmbed(title=f'There is no {meet_code.title()} class today', description="", color='03b2f8')
    embed.set_footer(text = '--Phoenix4745')
    embed.set_timestamp()
    embed.add_embed_field(name='Day', value= day, inline = False)
    if k < 56: 
        embed.add_embed_field(name='Class Start Time', value= period_time[nth_period] , inline = False)
        embed.add_embed_field(name='Class', value= meet_code.title(), inline = False)
    if nth_period + 1 != total_period:
        embed.add_embed_field(name='Next Class At', value= period_time[nth_period+1], inline = False)
    else:
        embed.add_embed_field(name='This is the last class !!!', value= 'Enjoy :grinning:', inline = False)

    webhook.add_embed(embed)
    webhook.execute()

#Real code Starts here

days_of_week = {'Monday' : 0, 'Tuesday': 1, 'Wednesday' : 2, 'Thursday' : 3, 'Friday' : 4}

timeTable = [['Mon',['','english', 'sst', 'punjabi', 'math', 'bio']], ['Tue',['phy', 'bio', 'punjabi', 'chem', 'sst', 'math']], ['Wed',['phy', 'math', 'bio', 'sst', 'punjabi', 'english']], ['Thu',['chem', 'phy', 'sst', 'english', 'punjabi', 'math']], ['Fri',['', 'chem', 'sst', 'english', 'math']]]

period_time = ['09:00:00', '09:50:00', '10:40:00', '11:45:00', '12:35:00', '13:25:00']

discordUrl = 'https://discord.com/api/webhooks/933664631971516416/L6nZiojGhp2paYunm7pNstO1YoPkMtXnV01VJvzIyFAxbLP5_PUV-La9Iqd-5uiw7CrG'

connection()

day = datetime.now().strftime("%A")

if day == 'Monday' or day == 'Friday':
    nth_period = 1
else:
    nth_period = 0

if day != 'Friday':
    total_period = 6
else:
    total_period = 5

day_code = days_of_week[day]

timeNow = datetime.now().time().replace(microsecond=0)
firstClassTime = datetime.strptime(period_time[nth_period], '%H:%M:%S').time()
d = date(2022, 1, 1)
time_left = (datetime.combine(d, firstClassTime) - datetime.combine(d, timeNow)).total_seconds()

DiscordWebhook(url= discordUrl, content=f'Good Morning Sir \nCurrent time is {timeNow} \nWill join {timeTable[day_code][1][nth_period].title()} class at {firstClassTime} \nSleeping for {time_left} secs').execute()

sleep(time_left)

while nth_period < total_period:
    connection()
    meet_code = timeTable[day_code][1][nth_period]
    meet()
    #sendMsg()
    nth_period = nth_period + 1
    if nth_period < total_period:
        currentTime = datetime.now().time().replace(microsecond=0)
        nextClassTime = datetime.strptime(period_time[nth_period], '%H:%M:%S').time()
        d = date(2022, 1, 1)
        time_left = (datetime.combine(d, nextClassTime) - datetime.combine(d, currentTime)).total_seconds()
        sleep(time_left)
else:
    print("Your Classes have finished !!  :)")
    input()