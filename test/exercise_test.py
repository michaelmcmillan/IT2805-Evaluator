# -*- coding: utf-8 -*-
import unittest 
import mock
from mock import MagicMock
from src.exercise import Exercise

class TestExercise(unittest.TestCase):

    def test_exercise_has_a_default_score_of_zero(self):
        exercise = Exercise()
        assert exercise.score == 0 

    def test_exercise_has_no_requirements_by_default(self):
        exercise = Exercise()
        requirements = exercise.requirements
        number_of_requirements = len(requirements)
        assert number_of_requirements == 0 

    def test_exercise_score_can_not_be_over_one_hundred(self):
        with self.assertRaisesRegexp(ValueError, '\s100'):
            exercise = Exercise()
            exercise.score = 101

    def test_exercise_score_can_not_be_over_one_hundred(self):
        with self.assertRaisesRegexp(ValueError, '\s0'):
            exercise = Exercise()
            exercise.score = -1 

    def test_exercise_score_must_be_an_integer(self):
        with self.assertRaisesRegexp(TypeError, 'number'):
            exercise = Exercise()
            exercise.score = "50"

    def test_exercise_has_a_default_text(self):
        exercise = Exercise()
        assert 'Unknown' in exercise.text

    def test_exercise_can_set_text_in_constructor(self):
        exercise = Exercise()
        exercise.text = """
            You are to create HTML code that displays an img.
        """
        assert 'HTML' in exercise.text

    def test_exercise_subtracts_unfilled_requirements_from_score(self):
        exercise = Exercise()
        exercise.score = 50
        requirement = MagicMock()
        requirement.fulfilled = False
        requirement.counts = 10
        exercise.add_requirement(requirement)
        assert exercise.score == 40

    def test_exercise_does_not_subtract_fulfilled_requirements_from_score(self):
        exercise = Exercise()
        exercise.score = 50
        requirement = MagicMock()
        requirement.fulfilled = True 
        requirement.counts = 10
        exercise.add_requirement(requirement)
        assert exercise.score == 50
