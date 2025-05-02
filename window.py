from tkinter import Tk, BOTH, Canvas

class Window():
    
    # constructor sets the root and canvas widget
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack()
        self.__running = False

    # renders the visuals, must be called
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    # simulates the "reactive" framework of other libraries
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")
    
    # closes the window
    def close(self):
        self.__running = False