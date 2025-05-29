from tkinter import *
import time
import pyautogui
import os, sys
from PIL import Image, ImageTk
import winsound


def resource_path(relative_path):
    try:
        base_path=sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

time.sleep(3)

dir =  os.path.dirname(os.path.abspath(sys.argv[0]))

print(dir)

pyautogui.hotkey('winleft', 'd')
screensh = pyautogui.screenshot('desktop.png')

alert = dir + "/Images/sound1.png"
scream = dir + "/Images/sound2.png"

def begin(*args):
    time.sleep(2)
    updateimg(1,3)
    winsound.PlaySound(alert, winsound.SND_FILENAME)
    time.sleep(2)
    updateimg(2,3)
    time.sleep(3)
    updateimg(2,3)
    time.sleep(1)
    updateimg(3,1)
    time.sleep(1)
    updateimg(4,1)
    time.sleep(1)
    updateimg(5,0.1)
    time.sleep(3)
    updateimg(6,0.1)
    winsound.PlaySound(scream, winsound.SND_FILENAME)
    time.sleep(3)
    updateimg(7,1)
    time.sleep(3)
    screen.destroy()


#E:\Programming\NICK LAZAR\projects\Images
def updateimg(num, second):
    imgname = dir + "/Images/bsod" + str(num) + ".png"
    img = Image.open(resource_path(imgname)).resize((screen.winfo_screenwidth(), screen.winfo_screenheight()),Image.LANCZOS)

    bg1 = ImageTk.PhotoImage(img)
    checklbl.configure(image=bg1, cursor="none")
    checklbl.image = bg1
    screen.update()
    time.sleep(second)


screen = Tk() #creates window
screen.title("Title Temp") # Title
screen.attributes('-fullscreen',True)


screenwidth = screen.winfo_screenwidth()
screenheight = screen.winfo_screenheight()

screen.geometry("{}x{}+0+0".format(screen.winfo_screenwidth(),screen.winfo_screenheight()))
deskscrn = PhotoImage(file="desktop.png")
checklbl = Label(screen, image=deskscrn,bd=0)
checklbl.place(x=0,y=0)

checklbl.bind('<Button-1>', begin)

def useless():
    pass





screen.bind('<Escape>', useless)

screen.mainloop() #teleftaia entolh klenei programma