from graphics import Line, Point
from graphics import Window

class Cell:
    def __init__(self, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.__window = window
        self.visited = False
    
    def draw(self, x1, y1, x2, y2):
        if not self.__window:
            return
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        if self.has_left_wall:
            left_wall = Line(Point(x1, y1), Point(x1, y2))
            self.__window.draw_line(left_wall)
        else:
            left_wall = Line(Point(x1, y1), Point(x1, y2))
            self.__window.draw_line(left_wall, "white")
        if self.has_right_wall:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            self.__window.draw_line(right_wall)
        else:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            self.__window.draw_line(right_wall, "white")
        if self.has_top_wall:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self.__window.draw_line(top_wall)
        else:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self.__window.draw_line(top_wall, "white")
        if self.has_bottom_wall:
            bottom_wall = Line(Point(x1, y2), Point(x2, y2))
            self.__window.draw_line(bottom_wall)
        else:
            bottom_wall = Line(Point(x1, y2), Point(x2, y2))
            self.__window.draw_line(bottom_wall, "white")

    def draw_move(self, to_cell, undo=False):
        wall_length1 = abs(self.x1 - self.x2)//2
        center_point1 = Point(self.x1 + wall_length1//2, self.y1 + wall_length1//2)


        wall_length2 = abs(to_cell.x1 - to_cell.x2)//2
        center_point2 = Point(to_cell.x1 + wall_length2//2, to_cell.y1 + wall_length2//2)

        connecting_line = Line(center_point1, center_point2)
        color = "grey" if undo else "red"
        if self.__window:
            self.__window.draw_line(connecting_line, color)
