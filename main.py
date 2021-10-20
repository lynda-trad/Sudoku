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
                c = Cell.Cell(i, j, 0, True)
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
def findCell(list, coordinates):
    for cell in list:
        if cell.getCoordinates() == coordinates:
            return cell


def printCellList(list):
    for cell in list:
        cell.printCell()


def solving(numberGrid, cellList):
    cursor = (0, 0)
    for i in range(len(numberGrid)):
        for j in range(len(numberGrid)):
            hypothesis = checking.getHypothesis(numberGrid, cursor)


    # with cursor, move in numberGrid, for each cell, if number == 0:
    # for every number from 1 to 9 check if you can place it:
    # check line of the coordinates, check column, check box too
    # if so, put said number in hypothesis of cell with coordinates
    # once every number from 1 to 9 was tested, if hypothesis.len == 1, place the number in numberGrid and Cell.number
    # else move forward to the next cell with double for loop in numberGrid
    # once you are done with the whole numberGrid, reset cursor to 0,0 and start again until every cell is filled


numberGrid = numpy.zeros((9, 9))
cellList = gridInit(numberGrid)
printCellList(cellList)
