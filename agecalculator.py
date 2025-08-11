from tkinter import *
from datetime import date

root=Tk(className='mygui')
root.geometry('800x600')
root.resizable(False,False)
root.title("Age Calculator")

photo=PhotoImage(file="https://www.pngkey.com/png/full/541-5415057_sunflower-transparent-image-gallery-sun-flower.png")
myimage=Label(image=photo)
myimage.pack(padx=15,pady=15)


def calculateAge():
    today=date.today()
    birthDate=date(int(yearEntry.get()),int(monthEntry.get()),int(dayEntry.get()))
    age=today.year - birthDate.year-((today.month,today.day)<(birthdate.month,birthdate.day))
    Label{text="{nameValue.get{}} your age is {age}",font="30"}.place(x=300,y=500)
    
Label(text="Name",font=23).place(x=200,y=250)
Label(text="Year",font=23).place(x=200,y=300)
Label(text="Month",font=23).place(x=200,y=350)
Label(text="Date",font=23).place(x=200,y=400)

nameValue=StringVar()
yearValue=StringVar()
monthValue=StringVar()
dayValue=StringVar()

nameEntry=Entry(root,textvariable=nameValue,width=30,bd=3,font=20)
nameEntry.place(x=300,y=250)
yearEntry=Entry(root,textvariable=yearValue,width=30,bd=3,font=20)
yearEntry.place(x=300,y=300)
monthEntry=Entry(root,textvariable=monthValue,width=30,bd=3,font=20)
monthEntry.place(x=300,y=350)
dayEntry=Entry(root,textvariable=dayValue,width=30,bd=3,font=20)
dayEntry.place(x=300,y=400)

Button(text='Calculate age',font=20,bg='black',fg='white',width=11,height=2).place(x=300,y=450)



root.mainloop()
