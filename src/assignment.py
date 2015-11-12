class DuplicateExerciseError(Exception):
    pass

class Assignment(object):

    def __init__(self, number = None):
        self._exercises = []
        if self._is_valid_number(number):
            self.number = number

    @property
    def score(self):
        return sum(exercise.score for exercise in self._exercises)

    @property
    def exercises(self):
        return self._exercises 

    def add_exercise(self, exercise):
        if self._not_a_duplicate_exercise(exercise) \
        and self._adding_exercise_does_not_exceed_max_score(exercise):
            self._exercises.append(exercise)

    def _is_valid_number(self, number):
        if number is not None:
            if not isinstance(number, int) or number < 0:
                raise ValueError('Assignment number must be a positive integer.') 
        return True

    def _not_a_duplicate_exercise(self, exercise):
        if exercise in self._exercises:
            raise DuplicateExerciseError()
        return True

    def _adding_exercise_does_not_exceed_max_score(self, exercise):
        if int(self.score + exercise.score) > 100:
            exceeding_score = self.score + exercise.score
            raise ValueError('%d exceeds max score of 100.' % exceeding_score)
        return True

    def remove_exercise(self, exercise):
        self._exercises.remove(exercise)

    def get_exercise(self, index):
        return self._exercises[index - 1]
