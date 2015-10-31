from score import Score

class Requirement(object):
    
    def __init__(self):
        self.text = "Unknown requirement."
        self._counts = Score(0)

    @property
    def counts(self):
        return self._counts._points

    @counts.setter
    def counts(self, score):
        self._counts = Score(score)
