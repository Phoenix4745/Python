from time import sleep, time
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
    meetCheck()
    print(k)
    if k < 56:
        hotkey('ctrl', 'd')
        sleep(0.02)
        hotkey('ctrl', 'e')
        x,y = joinNow
        print(x,y)
        click(x, y)
    
def meetCheck():
    global k
    k = 0
    while k < 56:
        if locateOnScreen('meetError1.png', region=(375, 237, 617, 118), grayscale = True):
            print(f'Meeting Status : Not Started Yet, Retrying in {10+k} secs')
            sleep(10 + k)
            hotkey('ctrl', 'l')
            sleep(0.05)
            write('g.co/meet/10c' + meet_code)
            press('enter')
            sleep(0.05)
            k = k+5
            pgloaded()
        else:
            sleep(3)
            global joinNow
            for i in range(2):
                print(i)
                joinNow = locateOnScreen('joinNow.png', region= (935, 382, 116, 80), grayscale = True)
                if joinNow:
                    print(joinNow)
                    print('Meeting Status : Started, Joining...')
                    break
                else:
                    sleep(1)
            else:
                if locateOnScreen('meetError2.png', region=(434, 173, 497, 38), grayscale = True):
                    hotkey('ctrl', 'l')
                    sleep(0.05)
                    write('g.co/meet/10c' + meet_code)
                    press('enter')
                    sleep(0.05)
                    pgloaded()
                    sleep(3)
                    break
            
    else:
        print('Class not there')

def connection():
    while response := not 0:
        response = call('ping meet.google.com -n 1')
        if response == 0:
            print("Connected to internet")
            break
        else:
            print('Tying to connect')

def pgloaded():
    while True:
        pgLoad = locateOnScreen('loaded.png', region = (79, 41, 14, 14), grayscale = True)
        if pgLoad:
            print('pgLoaded')
            sleep(0.8)
            break

def sendMsg():
    webhook = DiscordWebhook(url = discordUrl)
    embed = DiscordEmbed(title='Class Joined Succesfully', description="Here are your class details with :heart:", color='03b2f8')
    embed.set_footer(text = '--Phoenix4745')
    embed.set_timestamp()
    embed.add_embed_field(name='Day', value= day, inline = False)
    embed.add_embed_field(name='Class Start Time', value= period_time[nth_period] , inline = False)
    embed.add_embed_field(name='Class', value= meet_code.title(), inline = False)
    if nth_period != totalPeriod:
        embed.add_embed_field(name='Next Class At', value= period_time[nth_period+1], inline = False)
    else:
        embed.add_embed_field(name='This is the last class !!!', value= 'Enjoy :grinning:', inline = False)

    webhook.add_embed(embed)
    webhook.execute()

#Real code Starts here

timeTable = {'Monday':{2:'english', 3:'sst', 4:'punjabi', 5:'math', 6:'bio'}, 'Tuesday':{1:'phy', 2:'bio', 3:'punjabi', 4:'chem', 5:'sst', 6:'math'}, 'Wednesday':{1:'phy', 2:'math', 3:'bio', 4:'sst', 5:'punjabi', 6:'english'}, 'Thursday':{1:'chem', 2:'phy', 3:'sst', 4:'english', 5:'punjabi', 6:'math'}, 'Friday':{2:'chem', 3:'sst', 4:'english', 5:'math'}}

period_time = {1:'09:00:00', 2:'09:50:00', 3:'10:40:00', 4:'11:45:00', 5:'12:35:00', 6:'13:25:00'}

discordUrl = 'https://discord.com/api/webhooks/933664631971516416/L6nZiojGhp2paYunm7pNstO1YoPkMtXnV01VJvzIyFAxbLP5_PUV-La9Iqd-5uiw7CrG'

day = datetime.now().strftime("%A")

if day == 'Monday' or day == 'Friday':
    nth_period = 2
else:
    nth_period = 1

totalPeriod = len(timeTable[day])

timeNow = datetime.now().time().replace(microsecond=0)
firstClassTime = datetime.strptime(period_time[nth_period], '%H:%M:%S').time()
d = date(2022, 1, 1)
time_left = (datetime.combine(d, firstClassTime) - datetime.combine(d, timeNow)).total_seconds()
if time_left < 0:
    DiscordWebhook(url= discordUrl, content=f'Good Morning Sir \nCurrent time is {timeNow} \nJoining {timeTable[day][nth_period]} Class').execute()
else:    
    DiscordWebhook(url= discordUrl, content=f'Good Morning Sir \nCurrent time is {timeNow} \nWill join {timeTable[day][nth_period].title()} class at {firstClassTime} \nSleeping for {time_left} secs').execute()
    sleep(time_left)

while nth_period <= totalPeriod:
    curr = datetime.now().strftime("%H:%M:00")
    print(curr)
    if curr == period_time[nth_period]:
        connection()
        meet_code = timeTable[day][nth_period]
        meet()
        sendMsg()
        nth_period = nth_period + 1
        if nth_period <= totalPeriod:
            currentTime = datetime.now().time().replace(microsecond=0)
            nextClassTime = datetime.strptime(period_time[nth_period], '%H:%M:%S').time()
            d = date(2022, 1, 1)
            time_left = (datetime.combine(d, nextClassTime) - datetime.combine(d, currentTime)).total_seconds()
            sleep(time_left)
    else:
        sleep(10)
else:
    print("Your Classes have finished !!  :)")
    input()