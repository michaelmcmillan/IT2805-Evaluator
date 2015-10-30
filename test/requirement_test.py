# -*- coding: utf-8 -*-
import unittest 
import mock
from mock import MagicMock
from src.requirement import Requirement

class TestRequirement(unittest.TestCase):

    def test_requirement_is_by_default_not_met(self):
        requirement = Requirement()
        assert requirement.fulfilled == False

    def test_requirement_can_be_set_to_be_fulfilled(self):
        requirement = Requirement()
        requirement.fulfilled = True

    def test_requirement_has_default_text(self):
        requirement = Requirement()
        assert "Unknown" in requirement.text

    def test_requirement_can_change_text(self):
        requirement = Requirement()
        requirement.text = "The student calls window.setInterval every 10 ms"
        assert "window.setInterval" in requirement.text

    def test_requirement_counts_zero_as_default(self):
        requirement = Requirement()
        assert requirement.counts == 0

    def test_requirement_has_score_penalty_when_not_fulfilled(self):
        requirement = Requirement()
        requirement.counts = 5
        requirement.fulfilled = False
        assert requirement.penalty == 5

    def test_requirement_does_not_have_score_penalty_when_fulfilled(self):
        requirement = Requirement()
        requirement.counts = 15
        requirement.fulfilled = True 
        assert requirement.penalty == 0
