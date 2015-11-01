class Assignment(object):

    def __init__(self):
        self._score = 0
        self._exercises = []

    @property
    def score(self):
        return self._score 

    @property
    def exercises(self):
        return self._exercises 

    def add_exercise(self, exercise):
        if self._adding_exercise_does_not_exceed_max_score(exercise):
            self._score += exercise.score
            self._exercises.append(exercise)

    def _adding_exercise_does_not_exceed_max_score(self, exercise):
        if int(self._score + exercise.score) > 100:
            exceeding_score = self._score + exercise.score
            raise ValueError('%d exceeds max score of 100.' % exceeding_score)
        return True

    def remove_exercise(self, exercise):
        self._score -= exercise.score
        self._exercises.remove(exercise)

    def get_exercise(self, index):
        return self._exercises[index - 1]
