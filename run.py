import os
import sys
import tkinter
from tkinter import Tk
from pathlib import Path, PureWindowsPath
from tkinter import filedialog


class win:
    def __init__(self,w, winGeo, winTitle, winIcon) :
        self.winGeo = w.geometry(winGeo)
        self.winTitle = w.title(winTitle)
        self.winIcon =  winIcon
        w.iconphoto(w, tkinter.PhotoImage(file=winIcon))
        e = tkinter.Entry(w)
        f = tkinter.Entry(w)
        e.grid(row=0, column=1)
        f.grid(row=1, column=1)

        def runCommand():
            inName = e.get()
            outName = f.get()
            c = "ffmpeg -i " + inName + " -vcodec libx264 -preset veryslow -b:v 400k -maxrate 500k -profile:v high -level 4.1 -x264-params crf=23:bframes=0 -c:a aac -b:a 96k " + outName + ".flv"
            os.system ('cmd /c' + c)

        def addButton():
            quitButton = tkinter.Button(w, text="Exit", width=12, command=tkinter._exit).grid(row=4,column=0)
            button = tkinter.Button(w,text="Convert Video", command=runCommand).grid(row=4,column=1)
           

        def addLabel():
            tkinter.Label(w,text="VideoName.mp4").grid(row=0)
            tkinter.Label(w,text="New Video Name").grid(row=1)
            tkinter.Label(w,text="").grid(row=2)
        
    


        addButton()
        addLabel()