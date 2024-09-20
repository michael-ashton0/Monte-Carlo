import random
import math
import time
import tkinter as tk
from tkinter import ttk

class CircleApp:
    def __init__(self, window):

        self.dartNumber = 100
        self.midpoint = 150
        self.circleRadius = 150
        self.isAnimated = tk.IntVar()
        self.hitColors = ['DarkOrange1', 'OliveDrab1', 'Firebrick1']
        self.missColors = ['MediumTurquoise', 'Magenta2', 'Dodger Blue']

        '''window'''
        self.window = window
        #self.window.resizeable(False,False)
        self.window.wm_title('Monte Carlo Simulation')

        '''widgets'''
        self.dartboard = tk.Canvas(window, width=300, height=300, bg="khaki")
        self.draw_circle()
        self.title = tk.Label(self.window, text="Monte Carlo Simulation")
        self.runSimButton = tk.Button(self.window, text="Run Simulation", command=self.runSim)
        self.clearBoardButton = tk.Button(self.window, text="Clear Board", command=self.clearBoard)
        self.sliderLabel = tk.Label(self.window, text="Number of Darts")
        self.dartCount = tk.Scale(self.window, from_=100, to=10000, variable=self.dartNumber, orient=tk.HORIZONTAL)
        self.piValueLabel = tk.Label(self.window, text="π value")
        self.piValueEntry = tk.Entry(self.window, state='readonly')
        self.animatedCheck = tk.Checkbutton(self.window, text="Animate Simulation", variable=self.isAnimated)
        self.hitColor = ttk.Combobox(self.window, values=self.hitColors, state='readonly')
        self.missColor = ttk.Combobox(self.window, values=self.missColors, state='readonly')
        self.hitColorLabel = tk.Label(self.window, text='Hit Color:')
        self.missColorLabel = tk.Label(self.window, text='Miss Color:')
          
        '''positioning'''
        self.title.grid(row=0, column=1, pady=10)
        self.dartboard.grid(row=1, column=1, rowspan=3, padx=10, pady=10)

        '''left side'''
        self.sliderLabel.grid(row=1, column=0, pady=10, padx=10, sticky='e')
        self.dartCount.grid(row=2, column=0, pady=10, padx=10, sticky='n')

        self.runSimButton.grid(row=3, column=0, pady=10, sticky='n')
        self.clearBoardButton.grid(row=3,column=0,pady=10)

        '''right side'''
        self.piValueLabel.grid(row=1, column=2, pady=10, padx=10, sticky='n')
        self.piValueEntry.grid(row=1, column=2, pady=10, padx=10, sticky='w')
        self.animatedCheck.grid(row=2, column=2, pady=10, padx=10, sticky='n')

        self.hitColorLabel.grid(row=2, column=2, pady=10)
        self.hitColor.grid(row=2, column=2, pady=10, sticky='s')
        self.hitColor.set(value='DarkOrange1')

        self.missColorLabel.grid(row=3, column=2, pady=10, sticky='n')
        self.missColor.grid(row=3, column=2, pady=20)
        self.missColor.set(value='MediumTurquoise')

    '''Handles the button press and runs the simulation.''' 
    def runSim(self):
        self.total = 0
        self.yesCounter = 0
        self.dartNumber = self.dartCount.get()
        self.animated = self.isAnimated.get()

        if self.animated == 1: #if the animated box is checked
            for i in range(0,self.dartNumber):
                x = random.randint(0,300) 
                y = random.randint(0,300)

                if self.isInCircle(x,y) == True:
                    self.yesCounter+=1
                    self.total+=1
                    self.Color = self.hitColor.get()
                else:
                    self.total+=1
                    self.Color = self.missColor.get()

                self.piValue = (self.yesCounter / self.total)
                self.piValue *= 4

                self.piValueEntry.config(text=f"{self.piValue:.5f}")

                self.dartboard.create_oval(x-3, y-3, x+3, y+3, fill=self.Color)
                self.piValueEntry.config(state="normal")
                self.piValueEntry.delete(0, tk.END)
                self.piValueEntry.insert(0, f"{self.piValue:.5f}")
                self.piValueEntry.config(state="readonly")
                time.sleep(0.01)
                self.dartboard.update()
        else:
            for i in range(0,self.dartNumber):
                x = random.randint(0,300) 
                y = random.randint(0,300)

                if self.isInCircle(x,y) == True:
                    self.yesCounter+=1
                    self.total+=1
                    self.Color = self.hitColor.get()
                else:
                    self.total+=1
                    self.Color = self.missColor.get()

                self.piValue = (self.yesCounter / self.total)
                self.piValue *= 4

                self.piValueEntry.config(text=f"{self.piValue:.5f}")

                self.dartboard.create_oval(x-3, y-3, x+3, y+3, fill=self.Color)
                self.piValueEntry.config(state="normal")
                self.piValueEntry.delete(0, tk.END)
                self.piValueEntry.insert(0, f"{self.piValue:.5f}")
                self.piValueEntry.config(state="readonly")
   
    '''Handles the button press and resets the board and values to 0.'''
    def clearBoard(self):
        self.dartboard.delete('all')
        self.piValue = 0

        self.draw_circle()
        self.piValueEntry.config(state="normal")
        self.piValueEntry.delete(0, tk.END)
        self.piValueEntry.insert(0, f"{self.piValue}")
        self.piValueEntry.config(state="readonly")

    '''Draws the circle and axes.'''
    def draw_circle(self):
        x0 = self.midpoint - self.circleRadius
        y0 = self.midpoint - self.circleRadius
        x1 = self.midpoint + self.circleRadius
        y1 = self.midpoint + self.circleRadius

        self.dartboard.create_oval(x0, y0, x1, y1, outline="black", width=1, fill="SkyBlue1")
        self.dartboard.create_line(0,150,300,150, fill='linen')
        self.dartboard.create_line(150,0,150,300, fill='linen')

    '''Checks if a point at the given coordinates is inside of the circle.'''
    def isInCircle(self, x, y):
        #if distance between point and center is less than radius then it is within the circle
        self.distance = math.sqrt((x - self.midpoint)**2 + (y - self.midpoint)**2)
        if self.distance <= self.circleRadius:
            return True
        else:
            return False

root = tk.Tk()
app = CircleApp(root)
root.mainloop()
