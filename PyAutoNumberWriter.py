ascii_art = '''
   ___       ___       __     _      __    _ __     
  / _ \__ __/ _ |__ __/ /____| | /| / /___(_) /____ 
 / ___/ // / __ / // / __/ _ \\ |/ |/ / __/ / __/ -_)
/_/   \\_, /_/ |_\\_,_/\\__/\\___/__/|__/_/ /_/\\__/\__/
     /___/                           By Lilhaerden
'''

import pyautogui
import time

_counter_ = 0
count = 0
print(ascii_art)
print("This program is completely free, if you paid you have been scammed.")
print("")
number = int(input("Please enter the number to be written: "))
repeat = int(input("Please enter how many times it will be written: "))
time.sleep(2)

def dial_phone():
    global _counter_, count
    pyautogui.write(str(number))
    pyautogui.press("tab")
    _counter_ += 1
    count += 1
    print(count)

while True:
    if _counter_ < repeat:
        dial_phone()
    elif _counter_ == repeat:
        break
