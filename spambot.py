import pyautogui
from time import sleep

sleep(0.1)
print("Program made by GP_Gamer98")
sleep(0.1)
timestr=input("Put here the amount of time in seconds that the script must wait to be executed: ")
timeint=int(timestr)
print("You have "+timestr+" seconds to open the program that the spambot will spam.")
sleep(timeint)
print("KABOOM!")
read=open("words.txt","r")

for word in read:
    pyautogui.typewrite(word)
