from score import Score

class Exercise(object):
    
    def __init__(self):
        self._score = Score(0)
        self._text = "Unknown exercise description."
        self._requirements = [] 

    @property
    def requirements(self):
        return self._requirements 

    def _sum_requirement_count(self):
        return sum(requirement.counts for requirement in self._requirements)

    def add_requirement(self, requirement):
        if int(self._sum_requirement_count() + requirement.counts) > self.score:
            raise ValueError('Requirement count exceeds exercise score.')
        if not requirement.fulfilled:
            self._score.subtract(requirement.counts)
        self._requirements.append(requirement)

    @property
    def score(self):
        return self._score.points

    @score.setter
    def score(self, points):
        self._score = Score(points)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text
