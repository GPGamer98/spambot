from timeit import repeat
import pyautogui
from time import sleep

sleep(0.1)
print("Program made by GP_Gamer98")
sleep(0.1)
time=input("Put here the number of seconds the spam bot must wait to execute the script:  ")
sleep(time)
print("KABOOM!")
read=open("words.txt","r")

for word in read:
    pyautogui.typewrite(word)