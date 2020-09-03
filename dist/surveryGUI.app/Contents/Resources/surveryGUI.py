import sys
sys.path.append("/Users/tristansinclair/Documents/CovidSurveyScript/AnimatedGif.py")
sys.path.append("/Users/tristansinclair/Documents/CovidSurveyScript/CovidSurvey.py")
from AnimatedGif import *
from CovidSurvey import *

from selenium.webdriver.support.ui import Select
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from tkinter import ttk
from tkinter import *
import time
"""
surveryGUI.py
Creates a GUI for the CovidSurvery Script
When ran, enables user to fill out data quickly and efficiently for the
Stanford Student-Athlete COVID-19 screening survey
* Only to be used when a user does not have any symptoms *
created by: Tristan Sinclair
"""

"""
Tkinter creates the master window for application to be built in
master is used for the tkinter frame
"""
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

"""
run
Called when the run button is pressed. Takes user input data and calls
the CovidSurvery function fillSurvery to open a browser page and fill
the survey using the data.
"""
def run():
    locations = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(), var8.get()]
    data = User(e1.get(), e2.get(), e3.get(), e4.get(), locations)

    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    print("Email: %s\nPhone: %s" % (e3.get(), e4.get()))
    print("Yesterday:\nMaples: %s\n Field: %s\n Training Room: %s\n PT: %s\n" % (var1.get(), var2.get(), var3.get(), var4.get()))
    print("Today:\nMaples: %s\n Field: %s\n Training Room: %s\n PT: %s\n" % (var5.get(), var6.get(), var7.get(), var8.get()))

    fillSurvey(data)
    return

# Ste up the master window, window title and title
master = Tk()
master.title("Not this time COVID")
title = Label(master, text="COVID Survey \nAutomation", font=("Verdana", 20, "bold"))
title.pack(side=TOP, expand=True, fill=BOTH, padx=30, pady=1)

# Nate Peck GIF :)
filename = "/Users/tristansinclair/Documents/CovidSurveyScript/assets/nate3.gif"
lbl_with_my_gif = AnimatedGif(master, filename, 0.1)
lbl_with_my_gif.pack(side=TOP, expand=True, fill=BOTH, padx=50, pady=1)
lbl_with_my_gif.start_thread()

# Data Entry
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e1.insert(END, "First Name")
e2.insert(END, "Last Name")
e3.insert(END, "Email")
e4.insert(END, "Phone Number")
e1.pack(side=TOP, expand=True, fill=BOTH, padx=50, pady=1)
e2.pack(side=TOP, expand=True, fill=BOTH, padx=50, pady=1)
e3.pack(side=TOP, expand=True, fill=BOTH, padx=50, pady=1)
e4.pack(side=TOP, expand=True, fill=BOTH, padx=50, pady=1)

# Check Boxes
# Where were you last?
text1 = Label(master, text="Where were you last?", font=("Verdana", 10, "bold"))
text1.pack(side=TOP, expand=True, fill=BOTH, padx=5, pady=1)
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
c1 = ttk.Checkbutton(master, text="Maples", variable=var1)
c2 = ttk.Checkbutton(master, text="Football Field", variable=var2)
c3 = ttk.Checkbutton(master, text="Training Room", variable=var3)
c4 = ttk.Checkbutton(master, text="Physical Therapy", variable=var4)
c1.pack(side=TOP, expand=True, fill=BOTH, padx=50, pady=1)
c2.pack(side=TOP, expand=True, fill=BOTH, padx=50, pady=1)
c3.pack(side=TOP, expand=True, fill=BOTH, padx=50, pady=1)
c4.pack(side=TOP, expand=True, fill=BOTH, padx=50, pady=1)

# Where are you going today?
text2 = Label(master, text="Where are you going today?", font=("Verdana", 10, "bold"))
text2.pack(side=TOP, expand=True, fill=BOTH, padx=5, pady=1)
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
c5 = ttk.Checkbutton(master, text="Maples", variable=var5)
c6 = ttk.Checkbutton(master, text="Football Field", variable=var6)
c7 = ttk.Checkbutton(master, text="Training Room", variable=var7)
c8 = ttk.Checkbutton(master, text="Physical Therapy", variable=var8)
c5.pack(side=TOP, expand=True, fill=BOTH, padx=50, pady=1)
c6.pack(side=TOP, expand=True, fill=BOTH, padx=50, pady=1)
c7.pack(side=TOP, expand=True, fill=BOTH, padx=50, pady=1)
c8.pack(side=TOP, expand=True, fill=BOTH, padx=50, pady=1)

# Command Buttons
ttk.Button(master, text="Run", command=run).pack(
    side=TOP, expand=FALSE, fill=BOTH, padx=50, pady=1
)
ttk.Button(master, text="Quit", command=master.quit).pack(
    side=TOP, expand=FALSE, fill=BOTH, padx=50, pady=1
)

master.mainloop()