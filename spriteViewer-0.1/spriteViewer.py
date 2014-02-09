#!/usr/bin/env python
#coding=utf-8
"""
Author:         Pourquier Pierre-Emmanuel <pepourquier@medianetroom.com>
Filename:       spriteViewer.py
Date created:   2014-01-21 09:02
Last modified:  2014-01-21 19:05

Description:
This script is usefull to open quickly a website sprite image and show the soordinates.
"""

import Tkinter as tk
from Tkinter import *
from sys import argv
from PIL import Image, ImageTk


class SpriteViewer(tk.Frame):
    """
    This class help users to open an image and show sprite coords for css development
    """

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.image = Image.open(argv[1] if len(argv) >=2 else "test.png")
        self.canvas = tk.Canvas(self, width=self.image.size[0], height=self.image.size[1], cursor="cross")
        self.canvasResult = tk.Canvas(self, width=self.image.size[0], height=30.0)
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(self.image.size[0]//2, self.image.size[1]//2, image=self.image_tk)
        self.bg = self.canvasResult.create_rectangle(0, 0, self.image.size[0], 30.0, fill="#e7e7e7")
        self.txt = self.canvasResult.create_text(10, 10, anchor="nw")

        self.canvasResult.itemconfig(self.txt, text="Coordinates : ")
        self.canvasResult.pack(side="top", anchor="w")

        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.bind("<Button-1>", self.callback)

    def copyToClipboard(self, coordsX, coordsY):
        """
        Copy coords to the clipboard
        """
        #TODO Use xclip instead of clipboard_clear
        self.r = Tk()
        self.r.withdraw()
        self.r.clipboard_clear()
        cX = '-%spx' % coordsX
        cY = '-%spx' % coordsY
        txt = "background:url('') no-repeat %s %s" % (cX, cY)
        txt = raw_input(txt)
        self.r.clipboard_append(txt)
        self.r.destroy()

    def callback(self, event):
        """
        Print the coords when someone click on the image
        """
        self.canvasResult.itemconfig(self.txt, text="Coordinates : " +str(event.x)+'px ,'+str(event.y)+'px')
        #TODO: copy to clipboard
        #self.copyToClipboard(str(event.x), str(event.y))


if __name__ == "__main__":
    root = tk.Tk(className="Coordinates sprite viewer")
    view = SpriteViewer(root)
    view.pack(side="top", fill="both", expand=True)
    root.mainloop()
