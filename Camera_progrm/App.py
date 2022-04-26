from picamera import PiCamera
from time import sleep

camera = PiCamera()
import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
var = 0

def Camera():
    camera.start_preview(fullscreen=False, window=(100,20,640,480) )
    

def CameraDes():
    camera.stop_preview()
    

def Picture(): 
   global var
   var = var + 1
   camera.capture('/home/pi/Pictures/image%s.jpg' % var)
    
    
def TL():
    for filename in camera.capture_continuous('/home/pi/Pictures/img{counter:03d}.jpg'):
        sleep(10)


canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")

canvas.pack()


frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1)

cameraActivate = tk.Button(root, text="Activer la caméra", padx=10,
                           pady=5, fg="white", bg="#263D42", command=Camera)

cameraActivate.pack()

cameraDesActivate = tk.Button(root, text="Désactiver la caméra", padx=10,
                           pady=5, fg="white", bg="#263D42", command=CameraDes)

cameraDesActivate.pack()

cameraPicture = tk.Button(root, text="Prendre une photo", padx=10,
                           pady=5, fg="white", bg="#263D42", command=Picture)

cameraPicture.pack()


TimeLapse = tk.Button(root, text="Time lapse", padx=10,
                           pady=5, fg="white", bg="#263D42", command=TL)

TimeLapse.pack()

root.mainloop()

