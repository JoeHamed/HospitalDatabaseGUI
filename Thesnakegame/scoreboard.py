from turtle import Turtle

AlIGNMENT = "center"
FONT = ("Courier new", 15, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.high_score = 0
        self.speed(0)   # Fastest Speed
        self.hideturtle()
        self.penup()
        self.setposition(-10, 270)
        self.write(arg="Score : 0", align=AlIGNMENT, font=FONT)

    def update_score(self, score):
        self.clear()
        self.write(arg="Score : " + str(score), align=AlIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER ! ", align=AlIGNMENT, font=FONT)




