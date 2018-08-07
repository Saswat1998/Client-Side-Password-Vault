from tkinter import *
from PIL import Image, ImageTk

def load_window():                              # method definition to load  our software window
    window=Tk()                                 # creates a window to work on in tkinter stuff
    image=Image.open('tkbg.jpg')                # our image in the directory this program is in
    photo=ImageTk.PhotoImage(image)             # converts it into usable form to use in tkinter
    window.title("Client Side Password Vault")  # name that appears on statusbar
    canvas=Canvas(window,width=500,height=500)  # creates a canvas in window , canvas only does work of showing an image
    canvas.create_image(100,150,image=photo)    # we load our background image
    canvas.pack()                               # pack() method adds the widget into our window

    #Username
    label_user=Label(window,text="Hello, Username",font=("Hekvetica",25),fg='blue')       #label widget , fg means foreground color, bg means background color
    label_user.configure(activebackground="#33B5E5",relief=FLAT)                          #the hex color value doesnt make sense to me as it works fine without it
    label_user_window=canvas.create_window(125,120,anchor=NW,window=label_user)           #we add the widget over canvas rather than directly window because if we add
                                                                                          #directly to window it would get hidden behind canvas

    #Password
    mPass=Entry(show='*',font=('Helvetika',10),bg='#d3d3d3')                              #same thing except widget is entry type means takes text input
    mPass.configure(relief=FLAT)
    mPass_window = canvas.create_window(175, 190, anchor=NW, window=mPass)

    #Enter Pass                                                                                        #label widget
    enter_pass=Label(window, text="Enter Password", font=("TimesNewRoman", 10),fg='grey',bg='black')
    enter_pass.configure(relief=FLAT)
    enter_pass_window = canvas.create_window(200,210, anchor=NW, window=enter_pass)

    #submit_button                                                                        #button widget , here command=submit means when we press this button submit method will be called
    mButton=Button(window,text='SUBMIT',command=submit,bg='green')
    mButton.configure(width=10, activebackground="#33B5E5", relief=FLAT)
    mButton_window = canvas.create_window(210, 245, anchor=NW, window=mButton)

    #window_launch
    f1=Frame(window, height=0, width=250)                                                 #the height and width here doesnt make much sense to me
    f1.pack()                                                                             # better way take approx values , add background image then reduce values till satisfied
    window.mainloop()                                                                     # keeps window open till not closed by user

def submit():
    print("Submit button pressed")                                                         #method for when submit button is pressed

load_window()