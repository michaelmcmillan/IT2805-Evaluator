class Assignment(object):

    def __init__(self):
        self._exercises = []

    @property
    def score(self):
        return sum(exercise.score for exercise in self._exercises)

    @property
    def exercises(self):
        return self._exercises 

    def add_exercise(self, exercise):
        if self._adding_exercise_does_not_exceed_max_score(exercise):
            self._exercises.append(exercise)

    def _adding_exercise_does_not_exceed_max_score(self, exercise):
        if int(self.score + exercise.score) > 100:
            exceeding_score = self.score + exercise.score
            raise ValueError('%d exceeds max score of 100.' % exceeding_score)
        return True

    def remove_exercise(self, exercise):
        self._exercises.remove(exercise)

    def get_exercise(self, index):
        return self._exercises[index - 1]
