class Ball(object):
    # your code goes here
    def __init__(self, ball = "regular"):
        self.ball = ball

    def ball_type(self):
        return self.ball


b = Ball()
print(b.ball_type())