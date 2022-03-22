
from tkinter import *

class Lbl_img:
    def __init__(self, master, is_img, text):
        self.master, self.is_img, self.text = master, is_img, text

        if not is_img: return self.get_lbl()
        else: return self.try_img()
        
    def get_lbl(self): return Label(master=self.master, text=self.text, font=("Helvetica",14))

    def get_img(self): return Label(master=self.master, image=PhotoImage('assets/'+self.text))

    def try_img(self):
        try:
            return self.get_img()
        except:
            return self.get_lbl()