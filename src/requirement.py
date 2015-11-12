from score import Score

class Requirement(object):
    
    def __init__(self):
        self.text = "Unknown requirement."
        self._score = Score(0)
        self.fulfilled = False

    @property
    def score(self):
        return self._score._points

    @score.setter
    def score(self, score):
        self._score = Score(score)
