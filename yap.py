
from Tkinter import *
from picamera import PiCamera

redAWB = 0.29
blueAWB = 4.43
AWBsliderRes = 0.01
brightnessSliderRes = 1
gains = (redAWB,blueAWB)
camera = PiCamera() 
#camera.exposure_mode = 'off'
camera.vflip = True
camera.hflip = True
camera.resolution = (800, 600)
camera.framerate = 15
#camera.shutter_speed = camera.exposure_speed
#camera.drc_strength = "high"
camera.start_preview(fullscreen=False,resolution=(640,480),window=(0,0,640,480))    

def takePicture():
    camera.capture("testAWB.png", )
    camera.stop_preview()
    imgg = PhotoImage(file='testAWB.png')
    logoo.configure(image=imgg)
    logoo.image = imgg
    master.update_idletasks()

   

 

def cikis():
   exit()
  
def takeYuvPicture():
    camera.capture("testAWB.data", "yuv")


def repos(val):
    previewX = master.winfo_x()
    previewY = master.winfo_y()    

def exposure():
        camera.exposure_mode=exposureMode.get().lower()

def drc():
        camera.drc_strength=drcMode.get().lower()

def mode(val):
        #flicker()
        exposure()
        drc()

master = Tk()
master.attributes("-fullscreen", True)
master.configure(background='black')
previewX = master.winfo_x()
previewY = master.winfo_y()


logoo = Label(
      master
    
    )
logoo.place(x=0, y=0)
img = PhotoImage(file='logo.png')

logo = Label(
    master,
    image=img
)

logo.place(x=640, y=50)

btn = Button(master, text="Kaydet", command = takePicture ,height =5, 
          width = 17)
btn.place(x=640, y=150)


master.bind("<Return>", takePicture)
master.bind("<Configure>", repos)
master.bind("<Return>", mode)
btnn = Button(master, text="Cikis", command = cikis,height =5, 
          width = 17)
btnn.place(x=640, y=350)



mainloop()
