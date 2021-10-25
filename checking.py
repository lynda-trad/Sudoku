# Returns number possibilities of given cell depending of line
import time


# Return lists of coordinates on lines, columns or boxes
def boxMembers(i, j):
    return [(i, j), (i + 1, j), (i + 2, j),
            (i, j + 1), (i + 1, j + 1), (i + 2, j + 1),
            (i, j + 2), (i + 1, j + 2), (i + 2, j + 2)
            ]


def lineMembers(i):
    list = []
    for j in range(9):
        list.append((i, j))
    return list


def columnMembers(j):
    list = []
    for i in range(9):
        list.append((i, j))
    return list


# Returns number possibilities of given cell depending of line
def checkLine(numberGrid, coordinates):
    i = coordinates[0]
    hypothesis = []
    for number in range(1, 10):
        boolean = False  # not on line
        for jx in range(len(numberGrid[i])):
            if number == numberGrid[i][jx]:  # found number on line
                boolean = True
        if not boolean:
            hypothesis.append(number)
        elif boolean and number in hypothesis:  # if number was placed after hypothesis init
            hypothesis.remove(number)
    return hypothesis


# Returns number possibilities of given cell depending of column
def checkColumn(numberGrid, coordinates):
    j = coordinates[1]
    hypothesis = []
    for number in range(1, 10):
        boolean = False  # not on column
        for ix in range(len(numberGrid[j])):
            if number == numberGrid[ix][j]:  # found number on column
                boolean = True
        if not boolean:
            hypothesis.append(number)
        elif boolean and number in hypothesis:  # if number was placed after hypothesis init
            hypothesis.remove(number)
    return hypothesis


# Functions to find neighbours coordinates in the box
def getIList(i):
    if i % 3 == 0:
        return [i, i + 1, i + 2]
    elif i % 3 == 1:
        return [i, i - 1, i + 1]
    elif i % 3 == 2:
        return [i, i - 1, i - 2]


def getJList(j):
    if j % 3 == 0:
        return [j, j + 1, j + 2]
    elif j % 3 == 1:
        return [j, j - 1, j + 1]
    elif j % 3 == 2:
        return [j, j - 1, j - 2]


def mergeLists(iList, jList):
    checkingList = []
    for i in iList:
        for j in jList:
            checkingList.append((i, j))
    return checkingList


# Returns number possibilities of given cell depending of box
def checkBox(numberGrid, coordinates):
    i = coordinates[0]
    j = coordinates[1]
    iList = getIList(i)
    jList = getJList(j)
    checkingList = mergeLists(iList, jList)
    checkingList.remove((i, j))
    checkingList.sort()
    hypothesis = []
    for number in range(1, 10):
        boolean = False  # not in box
        for cell in checkingList:
            ix = cell[0]
            jx = cell[1]
            if number == numberGrid[ix][jx]:  # found number in box
                boolean = True
        if not boolean and number not in hypothesis:
            hypothesis.append(number)
        elif boolean and number in hypothesis:  # if number was placed after hypothesis init
            hypothesis.remove(number)
    return hypothesis


# Returns numbers that are common to 3 checking lists
def getHypothesis(numberGrid, cursor):
    lineHypo = checkLine(numberGrid, cursor)
    columnHypo = checkColumn(numberGrid, cursor)
    boxHypo = checkBox(numberGrid, cursor)
    hypothesis = []
    for hypo in lineHypo:
        if hypo in columnHypo and hypo in boxHypo:
            hypothesis.append(hypo)
    return hypothesis


# When a number is placed in main, function updates hypothesis of line and column members
def updateHypothesis(grid, number, i, j):
    iList = getIList(i)
    jList = getJList(j)
    boxList = mergeLists(iList, jList)
    lineList = lineMembers(i)
    columnList = columnMembers(j)

    boxList.sort()
    lineList.sort()
    columnList.sort()

    for coord in boxList:
        cell = grid.getCell(coord)
        cell.delHypothesis(number)

    for coord in lineList:
        cell = grid.getCell(coord)
        cell.delHypothesis(number)

    for coord in columnList:
        cell = grid.getCell(coord)
        cell.delHypothesis(number)


def boxSolo(numberGrid, grid, i, j):
    members = boxMembers(i, j)

    cellMemberList = []
    for member in members:
        if numberGrid[member[0]][member[1]] == 0:
            cellMemberList.append(grid.getCell(member))

    if len(cellMemberList) != 0:
        for number in range(1, 10):
            count = 0
            for cell in cellMemberList:
                if len(cell.getHypothesis()) != 0:
                    if number in cell.getHypothesis():
                        count += 1
            if count == 1:
                for cell in cellMemberList:
                    if number in cell.getHypothesis():
                        cell.setNumber(number)
                        coord = cell.getCoordinates()
                        numberGrid[coord[0]][coord[1]] = number
                        updateHypothesis(grid, numberGrid[coord[0]][coord[1]], coord[0], coord[1])


def lineSolo(numberGrid, grid, i):
    members = lineMembers(i)
    cellMemberList = []
    for member in members:
        if numberGrid[member[0]][member[1]] == 0:
            cellMemberList.append(grid.getCell(member))

    if len(cellMemberList) != 0:
        for number in range(1, 10):
            count = 0
            for cell in cellMemberList:
                if len(cell.getHypothesis()) != 0:
                    if number in cell.getHypothesis():
                        count += 1
            if count == 1:
                for cell in cellMemberList:
                    if number in cell.getHypothesis():
                        cell.setNumber(number)
                        cell.setHypothesis([])
                        coord = cell.getCoordinates()
                        numberGrid[coord[0]][coord[1]] = number
                        updateHypothesis(grid, numberGrid[coord[0]][coord[1]], coord[0], coord[1])


def columnSolo(numberGrid, grid, j):
    members = columnMembers(j)
    cellMemberList = []
    for member in members:
        if numberGrid[member[0]][member[1]] == 0:
            cellMemberList.append(grid.getCell(member))

    if len(cellMemberList) != 0:
        for number in range(1, 10):
            count = 0
            for cell in cellMemberList:
                if len(cell.getHypothesis()) != 0:
                    if number in cell.getHypothesis():
                        count += 1
            if count == 1:
                for cell in cellMemberList:
                    if number in cell.getHypothesis():
                        cell.setNumber(number)
                        cell.setHypothesis([])
                        coord = cell.getCoordinates()
                        numberGrid[coord[0]][coord[1]] = number
                        updateHypothesis(grid, numberGrid[coord[0]][coord[1]], coord[0], coord[1])


##############################################################
def boxTuple(numberGrid, grid, i, j):
    members = boxMembers(i, j)
    cellMemberList = []
    for member in members:
        if numberGrid[member[0]][member[1]] != 0:
            cellMemberList.append(grid.getCell(members))

    # on recupere tt les cellules qui ont 2 numbers en hypothese
    hypothesisTuple = {}
    for cell in cellMemberList:
        if len(cell.getHypothesis()) == 2:  # cell.getCoordinates() == value ; # hypothesis[] == key
            hypothesisTuple[cell.getCoordinates()] = str(cell.getHypothesis())

    duplicate = {}
    for key, value in hypothesisTuple.items():
        duplicate.setdefault(value, set()).add(key)
    result = filter(lambda x: len(x) > 1, duplicate.values())
    resList = list(result)
    print(resList)
    print(len(resList))
    print(resList[0])
    print(resList[0][0])
    print(resList[0][1])

    print(resList[1])

    # result == list des coordonnees des 2 cells qui ont hypotheses en commun
    if len(list(result)) == 2:
        return

