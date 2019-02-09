from Tkinter import *
z=Tk()
z.title("AboutUs")
d=PhotoImage(file="splash.gif")
 
def des2():
    z.destroy()

b=Label(z,image=d,compound='center',text='Name:- Amlend Singh Jadaun\n Enrollment NO.:-161B031\nBatch:-B2(BX)\nTitle:-Train Ticketing System',bg='blue',font=" times 35 bold italic",fg='black')

b.after(5000,des2)
b.pack()
z.mainloop()
