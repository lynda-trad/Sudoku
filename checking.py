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


"""
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

"""


# Calls updateBoxes, Lines, Columns
def updateAll(numberGrid, grid):
    updateBoxes(numberGrid, grid)
    updateLines(numberGrid, grid)
    updateColumns(numberGrid, grid)


def updateBoxes(numberGrid, grid):
    checkSolo(boxMembers(0, 0), numberGrid, grid)
    checkSolo(boxMembers(0, 3), numberGrid, grid)
    checkSolo(boxMembers(0, 6), numberGrid, grid)
    checkSolo(boxMembers(3, 0), numberGrid, grid)
    checkSolo(boxMembers(3, 3), numberGrid, grid)
    checkSolo(boxMembers(3, 6), numberGrid, grid)
    checkSolo(boxMembers(6, 0), numberGrid, grid)
    checkSolo(boxMembers(6, 3), numberGrid, grid)
    checkSolo(boxMembers(6, 6), numberGrid, grid)


def updateLines(numberGrid, grid):
    for i in range(9):
        checkSolo(lineMembers(i), numberGrid, grid)


def updateColumns(numberGrid, grid):
    for j in range(9):
        checkSolo(columnMembers(j), numberGrid, grid)


# If a number is only possible in one cell depending on its box, line or column then we place it
def checkSolo(memberList, numberGrid, grid):
    cellMemberList = []
    for member in memberList:
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


##############################################################
# Calls updateBoxTuple, LineTuple and ColumnTuple
def updateTuples(numberGrid, grid):
    updateBoxTuple(numberGrid, grid)
    updateLineTuple(numberGrid, grid)
    updateColumnTuple(numberGrid, grid)


def updateBoxTuple(numberGrid, grid):
    checkTuple(boxMembers(6, 3), numberGrid, grid)
    checkTuple(boxMembers(6, 3), numberGrid, grid)
    checkTuple(boxMembers(6, 3), numberGrid, grid)
    checkTuple(boxMembers(6, 3), numberGrid, grid)
    checkTuple(boxMembers(6, 3), numberGrid, grid)
    checkTuple(boxMembers(6, 3), numberGrid, grid)
    checkTuple(boxMembers(6, 3), numberGrid, grid)
    checkTuple(boxMembers(6, 3), numberGrid, grid)
    checkTuple(boxMembers(6, 6), numberGrid, grid)


def updateLineTuple(numberGrid, grid):
    for i in range(9):
        checkTuple(lineMembers(i), numberGrid, grid)


def updateColumnTuple(numberGrid, grid):
    for j in range(9):
        checkTuple(columnMembers(j), numberGrid, grid)


# If 2 cells in a line, column or box have the same numbers as hypothesis then we remove them from the other hypothesis
def checkTuple(memberList, numberGrid, grid):
    indexList = []
    for member in memberList:
        if numberGrid[member[0]][member[1]] == 0:
            cell = grid.getCell(member)
            if len(cell.getHypothesis()) == 2:
                indexList.append(member)
    if len(indexList) == 0:
        return

    # get cells with only 2 numbers as hypothesis
    if len(indexList) == 2:
        # 2 cells have hypothesis = 2
        cellx1 = grid.getCell(indexList[0])
        cellx2 = grid.getCell(indexList[1])

        if cellx1.getHypothesis() == cellx2.getHypothesis():  # if they have the same hypothesis
            hypothesisTuple = cellx1.getHypothesis()
            for member in memberList:
                if member not in indexList:
                    cell = grid.getCell(member)
                    if hypothesisTuple[0] in cell.getHypothesis():
                        cell.delHypothesis(hypothesisTuple[0])
                    if hypothesisTuple[1] in cell.getHypothesis():
                        cell.delHypothesis(hypothesisTuple[1])
