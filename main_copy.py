# import sys
import tkinter as tk
import turtle
import random
# from browser import document ---> bryton
# from browser import html -----> brython

### Brython HTML Stuff

# form_container = document['form-container']

# newdiv = html.DIV(id="new-div")

# form = HTML.FORM()

# label1 = html.LABEL("Simulation Speed")
# input1 = html.INPUT(type='range', min='10', max='1000', value='50', Class='slider', id='sim_speed', name='sim_speed')
# label2 = html.LABEL("Cell Color")
# input2 = html.INPUT(type='color', value='#191cc2', id='color', name='color')
# label3 = html.LABEL("Continuous Simulation")
# input3 = html.INPUT(type='radio', id='cont', name='cont', Class='radio')
# button = html.BUTTON("Play Simulation", Class='btn btn-primary')
# form <= label1 + html.BR() + input1 + html.BR() + label2 + html.BR() + input2 + html.BR() + label3 + html.BR() + input3 + button

# newdiv <= form

# button.bind("click", main)

### GOL Stuff

CELL_SIZE = 10

class Board(tk.Frame):
    def __init__(self, xsize, ysize):
        self.state = set()
        self.xsize, self.ysize = xsize, ysize
        self.master = master

    def set_key(self, x, y):
      
        key = (x, y)
        self.state.add(key)

    def makeRandom(self):
        self.erase()
        for i in range(0, self.xsize):
            for j in range(0, self.ysize):
                if random.random() > 0.5:
                    self.set_key(i, j)

    def toggle(self, x, y):
        key = (x, y)
        if key in self.state:
            self.state.remove(key)
        else:
            self.state.add(key)

    def erase(self):
        # Clear the board
        self.state.clear()

    def step(self):
        # Compute one generation, update the display
        d = set()
        for i in range(self.xsize):
            x_range = range(max(0, i - 1), min(self.xsize, i + 2))
            for j in range(self.ysize):
                s = 0
                live = ((i, j) in self.state)
                for yp in range(max(0, j - 1), min(self.ysize, j + 2)):
                    for xp in x_range:
                        if (xp, yp) in self.state:
                            s += 1

                # Subtract the central cell's value; it doesn't count.
                s -= live
                # print(d)
                ##print(i, j, s, live)
                if s == 3:
                    # Birth
                    d.add((i, j))
                elif s == 2 and live:
                    # Survival
                    d.add((i, j))
                elif live:
                    # Death
                    pass

        self.state = d

    def draw(self, x, y):
        # Update the cell (x,y) on the display
        turtle.penup()
        key = (x, y)
        if key in self.state:
            turtle.setpos(x * CELL_SIZE, y * CELL_SIZE)
            turtle.color('blue')
            turtle.pendown()
            turtle.setheading(0)
            turtle.begin_fill()
            for i in range(4):
                turtle.forward(CELL_SIZE)
                turtle.left(90)
            turtle.end_fill()

    def display(self):
        # Draw board
        turtle.clear()
        for i in range(self.xsize):
            for j in range(self.ysize):
                self.draw(i, j)
        turtle.update()

    def pause(self):
        print("I am pausing")

    def next_gen(self):
        pass

    def color(self):
        pass

    def speed(self):
        pass

    def reset(self):
        self.erase()
        print("i am resetting?")
        main()

    def main(self):

        xsize, ysize = 800, 800

        board = Board(xsize // CELL_SIZE, 1 + ysize // CELL_SIZE)

        root = tk.Tk()
        canvas = tk.Canvas(master = root, width = xsize, height = ysize)
        # turtle = turtle.RawTurtle(canvas)
        topframe = tk.Frame(root)
        topframe.pack()
        middleframe = tk.Frame(root)
        middleframe.pack()
        bottomframe = tk.Frame(root)
        bottomframe.pack()

        button1 = tk.Button(topframe, text = "Pause", fg="red")
        button2 = tk.Button(middleframe, text = "Next Generation", fg="red")
        button3 = tk.Button(middleframe, text = "Speed", fg="red")
        button4 = tk.Button(bottomframe, text = "Color", fg="red")
        button5 = tk.Button(bottomframe, text = "Reset", fg="red")

        button1.bind("<Button-1>", board.pause())
        button2.bind("<Button-2>", board.next_gen)
        button3.bind("<Button-3>", board.color)
        button4.bind("<Button-4>", board.speed)
        button5.bind("<Button-5>", board.reset)
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        scr = turtle.TurtleScreen(canvas)
        turtle.mode('standard')
        xsize, ysize = scr.screensize()
        print(xsize, ysize)
        turtle.setworldcoordinates(0, 0, xsize, ysize)

        turtle.hideturtle()
        # turtle.speed('fastest')
        turtle.tracer(0, 0)
        turtle.penup()


        board.makeRandom()
        board.display()

        # Continuous movement
        continuous = False

        def step_continuous():
            nonlocal continuous
            continuous = True
            perform_step()

        def perform_step():
            board.step()
            board.display() 
            # Setting timer to display another generation N ms
            if continuous:
                turtle.ontimer(perform_step, 5)

        turtle.ontimer(step_continuous)

        # Tk loop
        turtle.listen()
        
app = Board()

# if __name__ == '__main__':
#     main()
