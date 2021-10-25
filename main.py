import time
import Grid
import checking


# While cell has 0 as number, game is not finished
def finished(numberGrid):
    for i in range(len(numberGrid)):
        for j in range(len(numberGrid)):
            if numberGrid[i][j] == 0:
                return False
    return True


# Solving algorithm
def solving(grid, cellList):
    step = 0
    numberGrid = grid.getNumberGrid()
    grid.printGrid(step)
    while not finished(numberGrid):
        for i in range(len(numberGrid)):
            for j in range(len(numberGrid)):
                cursor = (i, j)
                if numberGrid[i][j] == 0:
                    # print(Grid.colors.YELLOW + "Working on: (", i, ",", j, ")")
                    hypothesis = checking.getHypothesis(numberGrid, cursor)
                    currentCell = grid.getCell(cursor)
                    currentCell.setHypothesis(hypothesis)
                    numberGrid[i][j] = currentCell.placeNumber()
                    checking.updateHypothesis(grid, numberGrid[i][j], i, j)
                    # print(Grid.colors.YELLOW + "final hypothesis:", currentCell.getHypothesis())

        updateBoxes(numberGrid, grid)
        updateLines(numberGrid, grid)
        updateColumns(numberGrid, grid)
        step += 1
        grid.printGrid(step)


def updateBoxes(numberGrid, grid):
    checking.boxSolo(numberGrid, grid, 0, 0)
    checking.boxSolo(numberGrid, grid, 0, 3)
    checking.boxSolo(numberGrid, grid, 0, 6)
    checking.boxSolo(numberGrid, grid, 3, 0)
    checking.boxSolo(numberGrid, grid, 3, 3)
    checking.boxSolo(numberGrid, grid, 3, 6)
    checking.boxSolo(numberGrid, grid, 6, 0)
    checking.boxSolo(numberGrid, grid, 6, 3)
    checking.boxSolo(numberGrid, grid, 6, 6)


def updateLines(numberGrid, grid):
    for i in range(9):
        checking.lineSolo(numberGrid, grid, i)


def updateColumns(numberGrid, grid):
    for j in range(9):
        checking.columnSolo(numberGrid, grid, j)


##################################################
grid = Grid.Grid()
grid.initNumberGrid()
grid.initCellList(grid.gridInit())
if grid.getCellList() == 0:
    print("Parsing failed, script will now stop")
else:
    solving(grid, grid.getCellList())
    print()
