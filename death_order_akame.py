import tkinter as tk
from tkinter import messagebox as mb
import random
import pygame

class AkameGaKill:
    #create a class and a constructor
    def __init__(self):
        #make sure you enter the death order characters only within this range
        self.proper_order = "Sayo,Ieyasu,Sheele,Bulat,Chelsea,Lubbock,Susanoo,Mine,Kurome,Tatsumi,Esdeath,Leone".upper().split(',')
        self.deaths_list = list()
        #self.death_list is the user entered list

    def submit(self):
        #once you press the next button, clear the entry box and enter new character
        received = enter_name.get().upper()
        #received data name should be in characters list

        if received not in self.proper_order:
            mb.showerror("Name Unknown","Check name")
        else:
            self.deaths_list.append(received)
            enter_name.delete(0,"end")

    def result(self):
        #once you have entered all names
        #check the result

        if self.proper_order == self.deaths_list:
            mb.showinfo("Sugoi","Besto Friend")
        elif len(self.deaths_list) != len(self.proper_order):
            mb.showerror("Didn't match","You missed to enter \n Character names")
        elif len(self.deaths_list) == 0:
            mb.showerror("Enter names","No Name entered")
        else:
            mb.showinfo("Try Again","Check names properly, Ganbatte \n start over")
        self.deaths_list.clear()   #its good to clear the death order list, for trying text time

    def main(self,parent):
        #geometry and structure of root directory

        global character_names,enter_name
        character_names = tk.StringVar()
        parent.title("Akame Ga Kill")
        parent.geometry("490x480+400+150")
        parent.resizable(False,False)

        canva = tk.Canvas(parent,bg="black")
        canva.pack(expand=True, fill= "both")  #the background design is done using Canvas
        #the rest widgets commands are simple to understand

        head = tk.Label(parent,text="Enter AKAME GA KILL Death Order",font=("arial",20,"bold")).place(x=15,y=15)
        characters = tk.Label(parent,text="Characters \n\n{}".format('| '.join(sorted(self.proper_order[:6]))),font=("arial",12,"bold"),fg="white",bg="black").place(x=30,y=75)
        next = tk.Label(parent,text='| '.join(sorted(self.proper_order[6:])),font=("arial",12,"bold"),fg="white",bg="black").place(x=25,y=130)
        foot = tk.Label(parent,text="Check spelling before clicking next\nDON'T CHEAT\nGanbatte",font=("arial",15,"italic")).place(x=100,y=380)
        name = tk.Label(parent,text="Enter one at a time:",font=("arial",13,"bold"),fg="white",bg="black").place(x=20,y=170)
        enter_name = tk.Entry(parent,textvariable=character_names,font=("arial",15,"bold"),bd=5)
        enter_name.place(x=200,y=160,width=200,height=50)
        enter_name.focus_set()
        btn = tk.Button(parent,text="Next",command=self.submit,font=("arial",11,"bold"),bg="grey",fg="black",bd=5).place(x=195,y=230,width=60,height=40)
        exit = tk.Button(parent,text="If done: Check Your Result",command=self.result,font=("arial",11,"bold"),bg="grey",fg="black",bd=5).place(x=135,y=295,width=200,height=40)

if __name__ == '__main__':
    pygame.mixer.init()
    death = AkameGaKill()
    root = tk.Tk()
    death.main(root)
    pygame.mixer.music.load('bg.ogg')
    pygame.mixer.music.play(loops=-1)
    root.mainloop()