import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
from playsound import playsound
from tkinter import *
import tkinter
import keyboard
from PIL import Image,ImageTk
from pydub import AudioSegment
from pydub.playback import play




def recordandplay():
    try:

        recording = sd.rec(int(5 * 44100),
                        samplerate=44100, channels=2)

        sd.wait()


        write("recording0.wav", 44100, recording)

        wv.write("recording1.wav", recording, 44100, sampwidth=2)

        
        sound = AudioSegment.from_file('recording1.wav', format="wav")

        
        octaves = 0.5

        new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))


        hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
        
        hipitch_sound = hipitch_sound.set_frame_rate(44100)


        
        img2=ImageTk.PhotoImage(Image.open("bl.png"))
        l.configure(image=img2)
        l.image=img2
        hipitch_sound.export("out.wav", format="wav")
        playsound("out.wav")

        # play(hipitch_sound)
        # win.bind("<Return>", change_img)
    except:
        pass





class gorbe:

    def __init__(self, name):
        self.name = name


    def talk(self,text):
        engine.say(text)
        engine.runAndWait()


tom = gorbe(name="tom")




win = Tk()

win.geometry("400x650")
win.configure(bg='yellow')

win.title('گربه پدرسوخته')


picture1 = PhotoImage(file='ol.png')
picture2 = PhotoImage(file='bl.png')





img1= ImageTk.PhotoImage(Image.open("bl.png"))


btnimg = PhotoImage(file='BUTN.PNG')


win.iconphoto(True,picture2)


img = ImageTk.PhotoImage(Image.open('ol.png'))
l=Label(win,image = img)
l.pack()



btn = Button(win,bg="yellow",bd=0,image=btnimg,command=recordandplay,activebackground='yellow')
btn.pack()


img3=ImageTk.PhotoImage(Image.open("ol.png"))
l.configure(image=img3)
l.image=img3

win.mainloop()