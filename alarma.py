import vlc
import time, threading
import requests
from tkinter import *

p = vlc.MediaPlayer("file:///siren.wav", "input-repeat=-1")

alarmaup = 0
alarmadown = 0
upto = 0
downto = 0

# Button functions to activate or deactivate alarm
def activarup():
    global upto
    upto = up_to.get()
    global alarmaup
    alarmaup = 1
    up_to_number.config(state=DISABLED)
    up_button.config(text ='Desactivar', command=desactivarup)
    win.update()
    
def desactivarup():
    global alarmaup
    alarmaup = 0
    p.stop()
    up_to_number.config(state=NORMAL)
    up_button.config(text ='Activar', command=activarup)
    win.update()

def activardown():
    global downto
    downto = down_to.get()
    global alarmadown
    alarmadown = 1
    down_to_number.config(state=DISABLED)
    down_button.config(text ='Desactivar', command=desactivardown)
    win.update()
    
def desactivardown():
    global alarmadown
    alarmadown = 0
    p.stop()
    down_to_number.config(state=NORMAL)
    down_button.config(text ='Activar', command=activardown)
    win.update()

# Creating tkinter window
win = Tk()
win.title("Alarma para Bitcoin")
win.geometry('400x150')

# Updated btc value data
lastbtc = Label(win, text="-")
lastbtc.grid(column=3, row=0)
lastbtc.config(fg="white",    # Foreground
             bg="black",   # Background
             font=("Verdana",24))


# Create labels
up_label = Label(win, text="Alarma si sube de:")
up_label.grid(row=1, column=0, sticky=W)

down_label = Label(win, text="Alarma si baja de:")
down_label.grid(row=2, column=0, sticky=W)

# Create entry box
up_to = DoubleVar(win, value="")
up_to_number = Entry(win, width=16, textvariable=up_to)
up_to_number.grid(row=1, column=3)
up_to_number.focus()

down_to = DoubleVar(win, value="")
down_to_number = Entry(win, width=16, textvariable=down_to)
down_to_number.grid(row=2, column=3)

# Create button
up_button = Button(win, text='Activar', command=activarup, width = 10)
up_button.grid(row=1, column=5)

down_button = Button(win, text='Activar', command=activardown, width = 10)
down_button.grid(row=2, column=5)


# Function that takes the values and activates or deactivates the alarm
def btcprice():
    r = requests.get('https://www.bitstamp.net/api/ticker/').json()
    realbtc = float(r["last"])
    btc = '%.2f' %realbtc
    lastbtc.config(text = str(btc))
    win.update()
    
    if float(btc) > upto and alarmaup == 1:
        p.play()
    elif float(btc) < downto and alarmadown == 1:
        p.play()
        

    threading.Timer(2, btcprice).start()

btcprice()




win.mainloop()
