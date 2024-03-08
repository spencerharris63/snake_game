from turtle import Turtle, ontimer
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("gold")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.choice(range(-280, 280, 20))
        random_y = random.choice(range(-280, 280, 20))
        self.goto(random_x, random_y)


class SuperFood(Food):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("hot pink")
        self.speed("fastest")

    def show_hide_cycle(self):
        self.show()
        ontimer(self.hide, 3000)
        ontimer(self.show_hide_cycle, 5000)  # Repeat the cycle after 5 seconds

    def show(self):
        self.refresh()
        self.showturtle()

    def hide(self):
        self.hideturtle()
