from graphics import Line, Point

class Cell:
    def __init__(self, win=None):
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.has_left = True
        self.has_right = True
        self.has_top = True
        self.has_bottom = True
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        # left edge
        line = Line(Point(x1, y1), Point(x1, y2))
        if self.has_left:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")
        # top edge
        line = Line(Point(x1, y1), Point(x2, y1))
        if self.has_top:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")
        # right edge
        line = Line(Point(x2, y1), Point(x2, y2))
        if self.has_right:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")
        # bottom edge
        line = Line(Point(x1, y2), Point(x2, y2))
        if self.has_bottom:     
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        origin = Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)
        end = Point((to_cell._x1 + to_cell._x2) // 2, (to_cell._y1 + to_cell._y2) // 2)
        line = Line(origin, end)
        self._win.draw_line(line, color)