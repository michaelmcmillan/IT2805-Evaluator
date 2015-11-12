from score import Score

class Exercise(object):
    
    def __init__(self):
        self.text = "Unknown exercise description."
        self._requirements = [] 

    @property
    def requirements(self):
        return self._requirements 

    @property
    def score(self):
        return sum(requirement.score for requirement in self._requirements)

    def add_requirement(self, requirement):
        self._requirements.append(requirement)
