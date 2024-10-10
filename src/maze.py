from cell import Cell
from time import sleep
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self.cells = []
        if seed is not None:
            seed = random.seed(seed)
        self.create_cells()
        self.break_entrance_and_exit()
        self.break_walls_r(0, 0)
        self.reset_cells_visited()

    def create_cells(self):
        for col in range(self.num_cols):
            col_cells = []
            for row in range(self.num_rows):
                col_cells.append(Cell(self.window))
            self.cells.append(col_cells)

        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self.draw_cell(col, row)

    def draw_cell(self, i, j):
        cell_x1 = self.x1 + i * self.cell_size_x
        cell_x2 = cell_x1 + self.cell_size_x
        cell_y1 = self.y1 + j * self.cell_size_y
        cell_y2 = cell_y1 + self.cell_size_y

        self.cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self.animate()

        
    def animate(self):
        if self.window:
            self.window.redraw()
        sleep(0.02)

    def break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self.draw_cell(0, 0)
        self.cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self.draw_cell(self.num_cols-1, self.num_rows-1)

    def break_walls(self, i, j, new_i, new_j):
        if i > new_i:
            self.cells[i][j].has_left_wall = False
            self.cells[new_i][new_j].has_right_wall = False
            self.draw_cell(i, j)
            self.draw_cell(new_i, new_j)
        elif i < new_i:
            self.cells[i][j].has_right_wall = False
            self.cells[new_i][new_j].has_left_wall = False
            self.draw_cell(i, j)
            self.draw_cell(new_i, new_j)
        elif j > new_j:
            self.cells[i][j].has_top_wall = False
            self.cells[new_i][new_j].has_bottom_wall = False
            self.draw_cell(i, j)
            self.draw_cell(new_i, new_j)
        elif j < new_j:
            self.cells[i][j].has_bottom_wall = False
            self.cells[new_i][new_j].has_top_wall = False
            self.draw_cell(i, j)
            self.draw_cell(new_i, new_j)

    def break_walls_r(self, i=0, j=0):
        self.cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0 and not self.cells[i-1][j].visited:
                to_visit.append((i-1, j))
            if j > 0 and not self.cells[i][j-1].visited:
                to_visit.append((i, j-1))
            if i < self.num_cols - 1 and not self.cells[i+1][j].visited:
                to_visit.append((i+1, j))
            if j < self.num_rows - 1 and not self.cells[i][j+1].visited:
                to_visit.append((i, j+1))
            
            if not to_visit:
                return
            
            direction = to_visit[random.randrange(0, len(to_visit))]
            self.break_walls(i, j, *direction)
            self.break_walls_r(*direction)


    def reset_cells_visited(self):
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self.cells[col][row].visited = False
    
    def __solve_move(self, i, j, new_i, new_j):
        current_cell = self.cells[i][j]
        new_cell = self.cells[new_i][new_j]
        current_cell.draw_move(new_cell)
        if self.solve_r(new_i, new_j):
            return True
        current_cell.draw_move(new_cell, True)
        return False

    def solve_r(self, i, j):
        self.animate()
        self.cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True

        if i > 0 and not self.cells[i-1][j].visited and not self.cells[i][j].has_left_wall:
            if self.__solve_move(i, j, i-1, j):
                return True
        if j > 0 and not self.cells[i][j-1].visited and not self.cells[i][j].has_top_wall:
            if self.__solve_move(i, j, i, j-1):
                return True
        if i < self.num_cols - 1 and not self.cells[i+1][j].visited and not self.cells[i][j].has_right_wall:
            if self.__solve_move(i, j, i+1, j):
                return True
        if j < self.num_rows - 1 and not self.cells[i][j+1].visited and not self.cells[i][j].has_bottom_wall:
            if self.__solve_move(i, j, i, j+1):
                return True

        return False
    
    def solve(self):
        if self.solve_r(0, 0):
            print("Solved")
        else:
            print("Path not found")
        
             