# Game of life Algorithm - Max Malacari 08/03/2017

import pygame as pg
import sys # to handle quit event
import random as rand
from math import *

# Some colours
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
white = (255,255,255)
black = (0,0,0)

# Some options to set!
wWidth = 700 # dimensions of the drawing window
wHeight = 700
cols = 100 # number of cells in each dimension
rows = 100
onFraction = 0.01
B = "25"
S = "4"
deadColour = black
liveColour = green

w = wWidth / cols
h = wHeight / rows

pg.init()
screen = pg.display.set_mode((wWidth,wHeight))
screen.fill(deadColour)

# Class to hold the properties of a cell
class Cell():
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.currentState = False # on or off
        self.nextState = False

    def show(self, colour):
        pg.draw.rect(screen, colour, (self.i*w, self.j*h, w, h), 0)

    def showCellBoundary(self):
        pg.draw.rect(screen, black, (self.i*w, self.j*h, w, h), 1)

    def countActiveNeighbours(self, grid):
        activeNeighbours = 0
        if self.j < rows-1:
            if grid[self.i][self.j+1].currentState == True:
                activeNeighbours += 1
        if self.j > 0:
            if grid[self.i][self.j-1].currentState == True:
                activeNeighbours += 1
        if self.i < cols-1:
            if grid[self.i+1][self.j].currentState == True:
                activeNeighbours += 1
        if self.i > 0:
            if grid[self.i-1][self.j].currentState == True:
                activeNeighbours += 1
        if self.i > 0 and self.j > 0:
            if grid[self.i-1][self.j-1].currentState ==True:
                activeNeighbours += 1
        if self.i > 0 and self.j < rows-1:
            if grid[self.i-1][self.j+1].currentState == True:
                activeNeighbours += 1
        if self.i < cols-1 and self.j < rows-1:
            if grid[self.i+1][self.j+1].currentState == True:
                activeNeighbours += 1
        if self.i < cols-1 and self.j > 0:
            if grid[self.i+1][self.j-1].currentState == True:
                activeNeighbours += 1
        return activeNeighbours

    def updateState(self):
        self.currentState = self.nextState
        if self.currentState == True:
            self.show(liveColour)
                

def main():

    grid = []
    initialize(grid, cols, rows)

    while True:

        for i in range(0,cols):
            for j in range(0,rows):
                activeNeighbours = grid[i][j].countActiveNeighbours(grid)
                evaluateRuleset(B, S, activeNeighbours, grid[i][j])
                    
        screen.fill(deadColour) # reset the board and draw new state
        for i in range(0,cols):
            for j in range(0,rows):
                grid[i][j].updateState()
        pg.display.update()

        
# Set up the grid of cell objects, init. state
def initialize(grid, cols, rows):
    for i in range(0,cols):
        grid.append([])
        for j in range(0,rows):
            grid[i].append(Cell(i,j))

    for i in range(0,cols):
        for j in range(0,rows):
            if rand.random() < onFraction:
                grid[i][j].currentState = True


def evaluateRuleset(born, survive, activeNeighbours, gridPoint):
    gridPoint.nextState = gridPoint.currentState # set to current state by default
    
    if gridPoint.currentState == False:
        if str(activeNeighbours) in born:
            gridPoint.nextState = True
    if gridPoint.currentState == True:
        if str(activeNeighbours) in survive:
            gridPoint.nextState = True
        else:
            gridPoint.nextState = False
    
                
main()
