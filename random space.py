from tkinter import *
import pyautogui as pag
import random
from time import sleep


root = Tk()
root.title("random space presser")
root.geometry("400x240")

def space():
    pag.press('space')
    timer()

def timer():
    sleep(random.randint(0, slide1.get()))
    space()

slide1 = Scale(root, from_=0.5, to=3, resolution=0.5, orient=HORIZONTAL)
submit1 = Button(root, text="submit", command=timer)


slide1.pack()
submit1.pack()

root.mainloop()

if submit1 is True:
    root.destroy()
    timer()
