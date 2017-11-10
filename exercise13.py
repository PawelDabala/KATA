"""
Imagine you are creating a game where the user has to guess the correct number. But there is a limit of how many guesses the user can do.

If the user tries to guess WRONG more than the limit the function should throw an error
If the user guess wrong it should lose a life and return false (if you guess correctly you shouldn't remove a life)
If the user guess right it should return true
Can you finish the game so all the rules are met?
"""


class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives

    def guess(self, n):
        if n == self.number:
            return True
        else:
            self.lives -= 1
            if self.lives == 0:
                raise Exception('error')
            else:
                return False

class Guesser2:
  def __init__(self, number, lives):
    self.number = number
    self.lives = lives
  def guess(self, n):
    if self.lives < 1: raise "Too many guesses!"
    if self.number == n: return True
    self.lives -= 1
    return False

g = Guesser2(10,2)
print(g.guess(10))
print(g.guess(1))
print(g.guess(2))
print(g.guess(10))