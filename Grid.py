import numpy
from os.path import exists

import Cell


class colors:
    BLACK  = '\033[30m'
    WHITE  = '\033[37m'
    RED    = '\033[31m'
    BLUE   = '\033[34m'
    GREEN  = '\033[32m'
    YELLOW = '\033[33m'


def openFile():
    filename = input("Please enter a filename with txt extension from folder /ressources.\n")
    while not exists("./ressources/" + filename):
        filename = input("Please enter a valid filename.\n")
    file = open("./ressources/" + filename, "r")
    return file.readlines()


class Grid:
    def __init__(self):
        self.numberGrid = []
        self.cellList = []
        self.lineList = []
        self.columnList = []

    def getNumberGrid(self):
        return self.numberGrid

    def getCellList(self):
        return self.cellList

    def getLineList(self):
        return self.lineList

    def getColumnList(self):
        return self.columnList

    def initNumberGrid(self):
        self.numberGrid = numpy.zeros((9, 9), dtype=int)

    def initCellList(self, cellList):
        self.cellList = cellList

    # Parsing file to fill grid with what we know

    def gridInit(self):
        grid = self.getNumberGrid()
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
    def getCell(self, coordinates):
        for cell in self.getCellList():
            if cell.getCoordinates() == coordinates:
                return cell

    # Printing methods
    def printGrid(self, step):
        txt = ""
        grid = self.getNumberGrid()
        print(colors.YELLOW + "Step", step, "\n")
        for i in range(len(grid)):
            for j in range(len(grid)):
                cell = self.getCell((i, j))
                if cell.getOriginal():
                    txt += colors.GREEN + "|" + str(int(grid[i][j])) + "|"
                elif grid[i][j] == 0:
                    txt += colors.RED + "|" + str(int(grid[i][j])) + "|"
                else:
                    txt += colors.BLUE + "|" + str(int(grid[i][j])) + "|"
            txt += '\n'
        print(txt)

    def printCellList(self):
        cList = self.getCellList()
        for cell in cList:
            cell.printCell()
