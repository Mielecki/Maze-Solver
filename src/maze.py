from cell import Cell
from time import sleep

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self.cells = []
        self.create_cells()
        self.break_entrance_and_exit()

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
        sleep(0.01)

    def break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self.draw_cell(0, 0)
        self.cells[self.num_rows-1][self.num_cols-1].has_bottom_wall = False
        self.draw_cell(self.num_rows-1, self.num_cols-1)
