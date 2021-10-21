import time
from os.path import exists
import numpy
import Cell
import Grid
import checking


class colors:
    GREEN = '\033[0;32m'
    BLUE = '\033[34m'
    BLACK = '\033[33m'
    RED = '\033[31m'


def openFile():
    filename = input("Please enter a filename with txt extension from folder /ressources.\n")
    while not exists("./ressources/" + filename):
        filename = input("Please enter a valid filename.\n")
    file = open("./ressources/" + filename, "r")
    return file.readlines()


# Parsing file to fill grid with what we know
def gridInit(grid):
    lines = openFile()
    cellList = []
    for i in range(len(lines)):  # for each line = i
        for j in range(len(lines[i])):  # for each column in line = j
            if lines[i][j] == '_':
                c = Cell.Cell(i, j, 0, False)
            elif lines[i][j].isdigit():
                c = Cell.Cell(i, j, int(lines[i][j]), True)
            elif lines[i][j] != '\n':
                print("ERROR, cell has to be either _ or a digit, please check the file again")
                return 0
            if i != 9 and j != 9:
                cellList.append(c)
                grid[i, j] = c.getNumber()
    return cellList


# Returns cell object when given its coordinates
def getCell(list, coordinates):
    for cell in list:
        if cell.getCoordinates() == coordinates:
            return cell


# While cell has 0 as number, game is not finished
def finished(numberGrid):
    for i in range(len(numberGrid)):
        for j in range(len(numberGrid)):
            if numberGrid[i][j] == 0:
                return False
    return True


# Solving algorithm
def solving(numberGrid, cellList):
    step = 0
    printGrid(numberGrid, cellList, step)
    while not finished(numberGrid):
        for i in range(len(numberGrid)):
            for j in range(len(numberGrid)):
                cursor = (i, j)
                if numberGrid[i][j] == 0:
                    print("Working on: (", i, ",", j, ")")
                    hypothesis = checking.getHypothesis(numberGrid, cursor)
                    currentCell = getCell(cellList, cursor)
                    currentCell.setHypothesis(hypothesis)
                    numberGrid[i][j] = currentCell.placeNumber()
                    print("final hypothesis:", currentCell.getHypothesis())
        step += 1
        printGrid(numberGrid, cellList, step)


def printCellList(list):
    for cell in list:
        cell.printCell()


def printGrid(grid, cellList, step):
    txt = ""
    print(colors.BLACK + "Step", step, "\n")
    for i in range(len(grid)):
        for j in range(len(grid)):
            cell = getCell(cellList, (i, j))
            if cell.getOriginal():
                txt += colors.GREEN + "|" + str(int(grid[i][j])) + "|"
            elif grid[i][j] == 0:
                txt += colors.RED + "|" + str(int(grid[i][j])) + "|"
            else:
                txt += colors.BLUE + "|" + str(int(grid[i][j])) + "|"
        txt += '\n'
    print(txt)


grid = Grid.Grid()
grid.initNumberGrid()
grid.initCellList(gridInit(grid.getNumberGrid()))
if grid.getCellList() == 0:
    print("Parsing failed, script will now stop")
else:
    solving(grid.getNumberGrid(), grid.getCellList())
