# Text-based adventure game

'''
Directions:

- RPG (Fantasy)
- Puzzle/Riddles
- Scenario (see RPG)

'''

'''
My game:

- Solve puzzles to make the lives of those in the village better, and increase you 'honour'
- You can also speak to them, also affecting your honour, and other stats.

- Stats will will be show in a seperate window (top-right)

'''

# https://docs.python.org/3/library/tkinter/tkinter.messagebox.html

'''
tkinter stuff:

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

WN = tk.Tk()
WN.geometry('600x400')
WN.title('Here\'s a title')

button1 = ttk.Button(WN, text = "Open main window", command = create_window) --> command links a declared function to the button press
button1.pack(expand = True)

button2 = ttk.Button(WN, text = "Close main window")
button2.pack(expand = True)

button3 = ttk.Button(WN, text = "Create Y/N window", command = ask_y_n)
button3.pack(expand = True)

def ask_y_n():
    answer = messagebox.askquestion('Title', 'Body') --> Title is pop-up title, body is question (text)
    print(answer)

def create_window():
    WN = tk.Toplevel()

    width, height = 200, 500
    screen_width = WN.winfo_screenwidth()
    x = screen_width - width
    y = 0

    WN.title('Stats')
    WN.geometry(f'{width}x{height}+{x}+{y}')

    ttk.Label(WN, text = 'Line 1').pack()
    ttk.Label(WN, text = 'Line 2').pack()

'''


# Imports
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import random
import time

playerStats = {'Strength': 0, 'Intelligence': 0, 'Agility': 0, 'Charisma': 0}
playerHonour = 0

def generate_random_playerStats():

    global playerStats

    totalStatsPoints = 12 # The max points that can be shared across player stats
    baseList = [totalStatsPoints // len(playerStats)]*4 # Avg points per stat (ensure is integer)

    tamperList = [1, 1, 1, 1]

    while sum(tamperList) != 0:
        tamperList[0] = random.randint(-2, 2)
        tamperList[1] = random.randint(-2, 2)
        tamperList[2] = random.randint(-2, 2)
        tamperList[3] = random.randint(-2, 2)


    for i in range(len(baseList)):
        baseList[i] += tamperList[i]
    
    pairs = playerStats.items()

    for pair in pairs:
        pair = list(pair)
        pair[1] += 2
        print(pair)



playerStats = generate_random_playerStats()
print(playerStats)


def create_stats_window():

    global playerStats
    global playerHonour

    WN = tk.Toplevel()

    width, height = 200, 300
    screen_width = WN.winfo_screenwidth()
    x = screen_width - width
    y = 0

    WN.title('Player stats')
    WN.geometry(f'{width}x{height}+{x}+{y}')

    ttk.Label(WN, text = " ").pack()

    for stat in playerStats:
        ttk.Label(WN, text= f'{stat}: {playerStats[stat]}').pack()
    
    ttk.Label(WN, text = f'\nHonour: {playerHonour}').pack()

# Main window
WN = tk.Tk()
WN.geometry('600x400')
WN.title('Text-based adventure game!')

statsButton = ttk.Button(WN, text = "Open player stats", command = create_stats_window)
statsButton.pack(expand = True)

# Run
WN.mainloop()

