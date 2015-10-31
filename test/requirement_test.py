# -*- coding: utf-8 -*-
import unittest 
import mock
from mock import MagicMock
from src.requirement import Requirement

class TestRequirement(unittest.TestCase):

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
