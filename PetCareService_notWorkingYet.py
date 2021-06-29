# Project Tkinter
# December 16, 2020
# Tyler Decaro


"""
The code mildly works as long as you click Dog, despite it being technically selected, and enter a name.
It shows all 6 services rather than what I intended which was that only checked boxes worked. This was hard for me to wrap my head around.
"""


from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Project 4: Decaro")
root.geometry("450x600")





welcome = Label(root,
                text="Welcome to Petcare\n",
                font=("helvetica",20),
                fg="blue",
                padx=100,
               ).grid(row=0, column=0, columnspan=2)

petName = Label(root,text="What is the pet name?")
petName.grid(row=1, column=0)

petNameEntry = Entry(root,bg="blue", fg="white")
petNameEntry.grid(row=1, column=1)



# Getting the radiobuttons working
r=StringVar()
r.set("dog")
dogButton = Radiobutton(root, text="DOG (Service fee $20)", variable=r, value="dog")
dogButton.deselect()
dogButton.grid(row=2, column=0)

# I cannot figure out how to just display the value "Dog" here.

p=StringVar()
p.set("cat")
catButton = Radiobutton(root, text="CAT (Service fee $12)", value="Cat")
catButton.deselect()
catButton.grid(row=2, column=1)

dash1 = Label(root,text="\n----------------------------------------\n").grid(row=3,column=0, columnspan=2)

groomCare = Label(root, text="Select the grooming care service. (min 2 choices)\n").grid(row=4, column=0, columnspan=2)

total = 0

# Start Checkbuttons

bath1 = IntVar()
bath1.set(20)
bath = Checkbutton(root,text="Bath\t$20", variable=lambda:bath1, onvalue=20, offvalue=0)
bath.grid(row=5, column=0)

haircut1 = IntVar()
haircut1.set(25)
haircut = Checkbutton(root,text="Haircut\t$25", onvalue=25, offvalue=0)
haircut.grid(row=6, column=0)

hairbrush1= IntVar()
hairbrush1.set(18)
hairbrush = Checkbutton(root,text="Brush\t$18", onvalue=18, offvalue=0)
hairbrush.grid(row=7, column=0)

trim1= IntVar()
trim1.set(22)
trim = Checkbutton(root,text="Trimming\t$22", onvalue=22, offvalue=0)
trim.grid(row=5, column=1)

toothbrush1=IntVar()
toothbrush1.set(17)
toothbrush = Checkbutton(root,text="Brush Teeth\t$17", onvalue=17, offvalue=0)
toothbrush.grid(row=6, column=1)

nails1 = IntVar()
nails1.set(16)
nails = Checkbutton(root,text="Cut Nails\t$16", onvalue=16, offvalue=0)
nails.grid(row=7, column=1)

dash2 = Label(root,text="\n----------------------------------------\n")
dash2.grid(row=8,column=0, columnspan=2)

def submitCalc():
    if len(petNameEntry.get()) == 0:
        response = messagebox.showwarning("Warning!", "Please type a name and SUBMIT again")
    # selection = Label(root, text=str(r.get()).grid())
    if (len(petNameEntry.get()) >= 1) & (r.get() == "dog"):
        welcome = Label(root, text="Welcome to Petcare Service: For your pet %s, %s."%(r.get(), petNameEntry.get()))
        welcome.grid(row=10, column=0, columnspan=2)
        if bath1.get() == 20:
            bathcheck = Label(root, text="Bath: $20").grid(row=11, column=0, columnspan=2)
        elif bath1.get() == 0:
            bathcheck = Label(root, text="").grid(row=11, column=0, columnspan=2)
        if haircut1.get() == 25:
            haircheck = Label(root, text="Haircut: $25").grid(row=12, column=0, columnspan=2)
        elif haircut1.get() == 0:
            haircheck = Label(root, text="").grid(row=12, column=0, columnspan=2)
        if hairbrush1.get() == 18:
            brushcheck = Label(root, text="Hairbrush: $18").grid(row=13, column=0, columnspan=2)
        elif hairbrush1.get() == 0:
            brushcheck = Label(root, text="").grid(row=13, column=0, columnspan=2)
        if trim1.get() == 22:
            trimcheck = Label(root, text="Trim: $22").grid(row=14, column=0, columnspan=2)
        elif trim1.get() == 0:
            trimcheck = Label(root, text="").grid(row=14, column=0, columnspan=2)
        if toothbrush1.get() == 17:
            toothcheck = Label(root, text="Toothbrush: $17").grid(row=15, column=0, columnspan=2)
        elif toothbrush1.get() == 0:
            toothcheck = Label(root, text="").grid(row=15, column=0, columnspan=2)
        if nails1.get() == 16:
            nailcheck = Label(root, text="Nails: $16").grid(row=16, column=0, columnspan=2)
        elif nails1.get() == 0:
            nailcheck = Label(root, text="").grid(row=16, column=0, columnspan=2)
        if bath1.get() == 20:
            service_num = 6
            cost = 138
            subtotal = Label(root, text="Your subtotal for %s service(s) comes to $%s."%(service_num, cost)).grid(row=17, column=0, columnspan=2)
            sales = (cost * 0.0875) + cost
            round(sales, 2)
            total= Label(root, text="Your total with sales tax comes to $%s."%sales).grid(row=18, column=0, columnspan=2)

sumbit = Button(root,
                text="Sumbit",
                bg="blue",
                fg="white",
                padx=50,
                pady=10,
                command=submitCalc
                ).grid(row=9, column=0,columnspan=2)

root.mainloop()
