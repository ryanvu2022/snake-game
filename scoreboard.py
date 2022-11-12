from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Roboto", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("#15f045")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)
