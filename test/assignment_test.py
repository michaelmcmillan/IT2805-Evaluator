# -*- coding: utf-8 -*-
import unittest 
import mock
from mock import MagicMock
from src.assignment import Assignment

class TestAssignment(unittest.TestCase):

    def test_has_zero_exercises_by_default(self):
        assignment = Assignment()
        number_of_exercises = len(assignment.exercises)
        assert number_of_exercises == 0

    def test_can_have_exercises_added(self):
        assignment = Assignment()
        exercise = MagicMock()
        assignment.add_exercise(exercise)
        number_of_exercises = len(assignment.exercises)
        assert number_of_exercises == 1

    def test_can_remove_exercise(self):
        assignment = Assignment()
        exercise = MagicMock()
        assignment.add_exercise(exercise)
        assignment.remove_exercise(exercise)
        number_of_exercises = len(assignment.exercises)
        assert number_of_exercises == 0
    
    def test_can_get_exercise(self):
        assignment = Assignment()
        exercise = MagicMock()
        assignment.add_exercise(exercise)
        retrieved_exercise = assignment.get_exercise(1)
        assert retrieved_exercise == exercise

    def test_has_a_default_score_of_zero(self):
        assignment = Assignment()
        assert assignment.score == 0

    def test_score_is_same_as_score_on_exercise_if_there_is_only_one_exercise(self):
        assignment = Assignment()
        exercise = MagicMock()
        exercise.score = 50
        assignment.add_exercise(exercise)
        assert assignment.score == 50

    def test_score_is_a_sum_of_all_the_added_exercises(self):
        assignment = Assignment()
        first_exercise = MagicMock()
        second_exercise = MagicMock()
        first_exercise.score = 10
        second_exercise.score = 10
        assignment.add_exercise(first_exercise)
        assignment.add_exercise(second_exercise)
        assert assignment.score == 20

    def test_score_is_updated_when_exercises_are_removed(self):
        assignment = Assignment()
        exercise = MagicMock()
        exercise.score = 30 
        exercise_to_be_removed = MagicMock()
        exercise_to_be_removed.score = 10 
        assignment.add_exercise(exercise)
        assignment.add_exercise(exercise_to_be_removed)
        assignment.remove_exercise(exercise_to_be_removed)
        assert assignment.score == 30

    def test_score_can_not_exceed_one_hundred_by_adding_exercises(self):
        with self.assertRaisesRegexp(ValueError, '110'):
            assignment = Assignment()
            first_exercise = MagicMock()
            first_exercise.score = 55 
            second_exercise = MagicMock()
            second_exercise.score = 55 
            assignment.add_exercise(first_exercise)
            assignment.add_exercise(second_exercise)
