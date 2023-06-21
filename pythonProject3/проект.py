from tkinter import *
import random


window = Tk()
window.geometry('800x500')
window.title('Приложение')
points=0
def check():
    global points
    b.place(x=random.randint(1, 550), y=random.randint(1, 350))
    points += 1
    point_show['text'] =str('Количество очков:')+str(points)
def clicker():
    b.place(x=200, y=130)
    point_show.place(x=0, y=0)



b = Button(text='нажми меня', font=('Arial', 20), fg='black', bg='white', command=check)
point_show=Label(text='Количество очков: '+str(points), fg='black', font=('Courier New', 16))
point_show.place(x=0,y=0)
first_butt=Button(text='Кликер',bg='lime',font=('Courier New', 16),command=clicker,height=5,width=15)
first_butt.place(x=125,y=100)
window.mainloop()
