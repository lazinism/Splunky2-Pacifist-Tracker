import tkinter as Tk
from threading import Thread
import sys
import ctypes
import os
import time
import re
from playsound import playsound
from pathlib import Path

class myUI:
    def mywork(self,item, label):
        f = open(item, 'r', encoding='utf-8', errors='ignore')
        murderer = False
        path = getattr(sys, '_MEIPASS', os.getcwd())
        while True:
            for line in f:
                if line:
                    s = line.strip()
                    label.config(text=s)
                    if re.match("MURDERED \d+!", s):
                        if not murderer:
                            murderer = True
                            playsound(path+'\\pc\\beep.mp3')
                    else:
                        murderer = False
                    f.seek(0)
            time.sleep(0.001)

    def getscreensize(self):
        user32 = ctypes.windll.user32
        return "+"+"20"+"+"+str(user32.GetSystemMetrics(1)-120)

    def move(self,event,root):
        x, y = root.winfo_pointerxy()
        root.geometry(f"+{x}+{y}")

    def elem(self,event,root):
        root.withdraw()
        sys.exit(0)
        root.destroy()

    def __init__(self):
        root = Tk.Tk()
        root.title("Lazinism")
        root.resizable(False, False)
        root.overrideredirect(True)
        root.geometry(self.getscreensize())
        label = Tk.Label(root, text="Lazinism", bg='Red', fg='White', height=1, anchor=Tk.CENTER, font=("맑은고딕", 30, "bold"))
        label.grid(row=0, column=0, columnspan=5, sticky='ew')    
        label.pack()
        local = os.getenv('LocalAppData')
        taskThread = Thread(target=self.mywork, args=(local+"\\spelunky.fyi\\modlunky2\\trackers\\pacifist.txt", label), daemon=True)
        taskThread.start()
        root.wm_attributes('-topmost', True)
        #tk.wm_attributes("-transparentcolor", "white")
        root.grid_columnconfigure(0, weight=1)
        root.bind('<B1-Motion>',lambda event, r=root: self.move(event,r))
        root.bind('<Double-Button-3>',lambda event, r=root: self.elem(event,r))
        root.mainloop()
        
        
if __name__ == "__main__":
    
    ui = myUI()
