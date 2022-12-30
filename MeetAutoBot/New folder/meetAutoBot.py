from time import sleep
from subprocess import call
from webbrowser import get
from pyautogui import locateOnScreen, hotkey, press, write, click
from datetime import datetime, date
from discord_webhook import DiscordWebhook, DiscordEmbed

def meet():
    
    bravePath = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe --profile-directory='Profile 1' %s"
    get(bravePath).open_new_tab('https://g.co/meet/10c' + meet_code)
    sleep(3)
    pgloaded()
    meetCheck()
    hotkey('ctrl', 'd')
    sleep(0.1)
    hotkey('ctrl', 'e')
    sleep(1)
    click(993, 411)
    
def meetCheck():
    while True:
        if locateOnScreen('meetError1.png', region=(375, 237, 617, 118), grayscale = True) or locateOnScreen('meetError2.png', region=(434, 173, 497, 38), grayscale = True):
            print('Meeting Status : Not Started Yet, Retrying in 15secs')
            sleep(15)
            hotkey('ctrl', 'l')
            sleep(0.1)
            write('g.co/meet/10c' + meet_code)
            press('enter')
            sleep(1)
            pgloaded()
        else:
            print('Meeting Status : Started, Joining...')
            sleep(3)
            break

def connection():
    while response := not 0:
        response = call('ping www.google.com -n 1')
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
            sleep(1)
            break

def dayToday():
    now =  datetime.now().strftime("%A")
    return now

def sendMsg():
    webhook = DiscordWebhook(url = discordUrl)
    embed = DiscordEmbed(title='Class Joined Succesfully', description="Here are your class details with :heart:", color='03b2f8')
    embed.set_footer(text = '--Phoenix4745')
    embed.set_timestamp()
    embed.add_embed_field(name='Day', value= day, inline = False)
    embed.add_embed_field(name='Time', value= period_time[nth_period] , inline = False)
    embed.add_embed_field(name='Class', value= meet_code, inline = False)
    if nth_period + 1 != total_period:
        embed.add_embed_field(name='Next Class At', value= period_time[nth_period+1], inline = False)
    else:
        embed.add_embed_field(name='This is the last class !!!', value= 'Enjoy :grinning:', inline = False)

    webhook.add_embed(embed)
    webhook.execute()

#Real code Starts here

days_of_week = {'Monday' : '0', 'Tuesday': '1', 'Wednesday' : '2', 'Thursday' : '3', 'Friday' : '4'}        

timeTable = [['Mon',['','english', 'sst', 'punjabi', 'math', 'bio']], ['Tue',['phy', 'bio', 'punjabi', 'chem', 'sst', 'math']], ['Wed',['phy', 'math', 'bio', 'sst', 'punjabi', 'english']], ['Thu',['chem', 'phy', 'sst', 'english', 'punjabi', 'math']], ['Fri',['', 'chem', 'sst', 'english', 'math']]]

period_time = ['08:58:00', '09:48:00', '10:38:00', '11:43:00', '12:33:00', '13:23:00']

discordUrl = 'https://discord.com/api/webhooks/933664631971516416/L6nZiojGhp2paYunm7pNstO1YoPkMtXnV01VJvzIyFAxbLP5_PUV-La9Iqd-5uiw7CrG'

day = dayToday()

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

DiscordWebhook(url= discordUrl, content='Good Morning Sir \nCurrent time is '+ str(timeNow) +'\nWill join class at ' + str(firstClassTime) + '\nSleeping for ' + str(time_left) + ' secs').execute()

sleep(time_left)

while nth_period < total_period:
        curr = datetime.now().strftime("%H:%M:00")
        print(curr)
        if curr == period_time[nth_period]:
            connection()
            meet_code = timeTable[int(day_code)][1][nth_period]
            meet()
            sendMsg()
            nth_period = nth_period + 1
            currentTime = datetime.now().time().replace(microsecond=0)
            nextClassTime = datetime.strptime(period_time[nth_period], '%H:%M:%S').time()
            d = date(2022, 1, 1)
            time_left = (datetime.combine(d, nextClassTime) - datetime.combine(d, currentTime)).total_seconds()
            sleep(time_left)
        else:
            sleep(10)

print("Your Classes have finished !!")
input()
