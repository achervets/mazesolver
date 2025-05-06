from cell import Cell
import time
import random

class Maze():

    def __init__(self, x, y, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cells = []
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x + i * self._cell_size_x
        y1 = self._y + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_list = []
            # finding the next cell
            if i > 0 and self._cells[i - 1][j].visited == False:
                next_list.append((i - 1, j))
            if i < self._num_cols - 1 and self._cells[i + 1][j].visited == False:
                next_list.append((i + 1, j))
            if j > 0 and self._cells[i][j-1].visited == False:
                next_list.append((i, j - 1))
            if j < self._num_rows - 1 and self._cells[i][j + 1].visited == False:
                next_list.append((i, j + 1))

            # if you don't have more paths to make from this cell
            if len(next_list) == 0:
                self._draw_cell(i, j)
                return
            
            # random direction
            next_cell = next_list[random.randrange(len(next_list))]

            # break the wall down between origin and next cell
            if next_cell[0] == i + 1:
                self._cells[i][j].has_right = False
                self._cells[i + 1][j].has_left = False
            if next_cell[0] == i - 1:
                self._cells[i][j].has_left = False
                self._cells[i - 1][j].has_right = False
            if next_cell[1] == j + 1:
                self._cells[i][j].has_bottom = False
                self._cells[i][j + 1].has_top = False
            if next_cell[1] == j - 1:
                self._cells[i][j].has_top = False
                self._cells[i][j - 1].has_bottom = False
            self._break_walls_r(next_cell[0], next_cell[1])

    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        # end check, if reached then the maze is solved
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        # go left
        if i > 0 and self._cells[i][j].has_left == False and self._cells[i - 1][j].visited == False:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)
        
        # go right
        if i < self._num_cols - 1 and self._cells[i][j].has_right == False and self._cells[i + 1][j].visited == False:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        
        # go up
        if j > 0 and self._cells[i][j].has_top == False and self._cells[i][j - 1].visited == False:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        
        # go down
        if j < self._num_rows - 1 and self._cells[i][j].has_bottom == False and self._cells[i][j + 1].visited == False:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)
        
        # dead end, line goes grey on previous cell
        return False