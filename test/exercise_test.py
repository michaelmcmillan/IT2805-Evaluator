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

    def test_exercise_has_a_default_text(self):
        exercise = Exercise()
        assert 'Unknown' in exercise.text

    def test_exercise_can_set_text_in_constructor(self):
        exercise = Exercise()
        exercise.text = """
            You are to create HTML code that displays an img.
        """
        assert 'HTML' in exercise.text
