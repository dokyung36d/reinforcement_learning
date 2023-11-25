from tkinter import Tk, Canvas, Frame, BOTH


class MovingBall(Frame):
    ball_r = 25
    x, y = 0, 0  # ball last coords

    def __init__(self):
        super().__init__()
        self.ball = None
        self.initUI()

    def initUI(self):
        self.master.title("Moving Ball")
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self)
            
        self.ball = self.paint_ball(self.x, self.y)
        self.canvas.pack(fill=BOTH, expand=1)
        # Left click on canvas moves the ball
        self.canvas.bind("<Button-1>", self.move)
        # Right click on canvas reset ball position
        self.canvas.bind("<Button-3>", self.reset)

    def paint_ball(self, x, y):
        return self.canvas.create_oval(x - self.ball_r, y - self.ball_r, x + self.ball_r, y + self.ball_r, fill="red",
                                       outline="silver", width=1)

    def paint_path(self, x, y):
        return self.canvas.create_line(self.x, self.y, x, y, fill="silver", width=1)

    def move(self, event):
        # Remove last painted ball
        self.canvas.delete(self.ball)
        # Add new line to the path
        self.paint_path(event.x, event.y)
        # Paint new ball at new position
        self.ball = self.paint_ball(event.x, event.y)
        self.canvas.pack(fill=BOTH, expand=1)
        # Store current ball coords
        self.x, self.y = event.x, event.y

    def reset(self, event):
        """Reset whole scene and put ball to 0,0"""
        self.x, self.y = 0, 0
        self.canvas.delete("all")
        self.ball = self.paint_ball(self.x, self.y)
        self.canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    MovingBall()
    root.geometry("1024x768")
    root.mainloop()


if __name__ == '__main__':
    main()