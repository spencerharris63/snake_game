from turtle import Turtle, ontimer
ALIGNMENT = "center"
GLOBAL_FONT = ("Courier", 20, "normal")
BONUS_FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("lime")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.update_scoreboard()

    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=GLOBAL_FONT)

    def show_hide_bonus(self):
        bonus_message = self.display_bonus_message()
        ontimer(lambda: self.hide_bonus_message(bonus_message), 3000)

    def bonus_score(self):
        self.bonus_update()
        self.show_hide_bonus()

    def bonus_update(self):
        self.score += 3
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=GLOBAL_FONT)

    def display_bonus_message(self):
        bonus_message = Turtle()
        bonus_message.color("hot pink")
        bonus_message.penup()
        bonus_message.hideturtle()
        bonus_message.goto(0, 240)
        bonus_message.write("BONUS SCORE", align=ALIGNMENT, font=BONUS_FONT)
        return bonus_message

    def hide_bonus_message(self, bonus_message):
        bonus_message.clear()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")
        self.write("GAME OVER", align=ALIGNMENT, font=GLOBAL_FONT)

