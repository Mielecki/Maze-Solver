import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells_list_length1(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )
    
    def test_maze_create_cells_list_length2(self):
        num_cols = 30
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 10, 5)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_break_entrance_and_exit(self):
        num_cols = 5
        num_rows = 6
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1.cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m1.cells[num_cols-1][num_rows-1].has_bottom_wall,
            False
        )

    def test_reset_cells_visited(self):
        m1 = Maze(0, 0, 12, 10, 10, 10)

        cells_visited = [[True for _ in range(12)] for _ in range(10)]
        for i in range(10):
            for j in range(12):
                cells_visited[i][j] = m1.cells[i][j].visited

        self.assertEqual(
            cells_visited,
            [[False for _ in range(12)] for _ in range(10)]
        )        


if __name__ == "__main__":
    unittest.main()