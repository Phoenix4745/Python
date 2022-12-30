from pyautogui import *
from time import *

sleep(7)
#screenshot('meetError3.png')
begin = time()
a = locate('getready1.png', 'gettingReady.png' ,region = (979, 367, 164, 25), grayscale = True, confidence = 0.7)
end = time()
print(a)
print(f"Total runtime of the program is {end - begin}")