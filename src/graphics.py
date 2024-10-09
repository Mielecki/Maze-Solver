from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(width=width, height=height, background="white")
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__running = False
        self.close()
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_cords(self):
        return self.x, self.y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2


    def draw(self, canvas: Canvas, fill_color):
        canvas.create_line(*self.point1.get_cords(), *self.point2.get_cords(), fill=fill_color, width=2)