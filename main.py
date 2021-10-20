import numpy
from os.path import exists
import Cell

# Opens input file
import checking


def openFile():
    filename = 'sudoku.txt'
    # input("Please enter a filename with txt extension from folder /ressources.\n")
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
                return
            if i != 9 and j != 9:
                cellList.append(c)
                grid[i, j] = c.getNumber()
    c.printCell()
    print(grid)
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
                print(False)
                return False
    print(True)
    return True


# Solving algorithm
def solving(numberGrid, cellList):
    step = 0
    while not finished(numberGrid):
        # step != 10
        for i in range(len(numberGrid)):
            for j in range(len(numberGrid)):
                cursor = (i, j)
                hypothesis = checking.getHypothesis(numberGrid, cursor)
                currentCell = getCell(cellList, cursor)
                currentCell.setHypothesis(hypothesis)
                numberGrid[i][j] = currentCell.placeNumber()
        print("Step", step, "\n", numberGrid)
        step += 1


def printCellList(list):
    for cell in list:
        cell.printCell()


numberGrid = numpy.zeros((9, 9))
cellList = gridInit(numberGrid)

solving(numberGrid, cellList)

