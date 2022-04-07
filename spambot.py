import pyautogui
from time import sleep

sleep(0.1)
print("Program made by GP_Gamer98")
sleep(0.1)
print("You have 5 seconds to open the program to be spammed (e.g. Telegram, Roblox)")
sleep(5)
print("KABOOM!")
read=open("words.txt","r")

for word in read:
    pyautogui.typewrite(word)
