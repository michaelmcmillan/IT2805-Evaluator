from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from closest_color import ClosestColor
import re
import unittest

class RequirementRunner(object):

    def __init__(self):
        self.browser = webdriver.Firefox()

    def run(self, url, requirement):
        requirement.browser = self.browser
        self.browser.get(url)

        for test in self.get_tests(requirement):
            getattr(requirement, test)()
        self.cleanup()

    def get_tests(self, requirement):
        methods = dir(requirement) 
        return filter(lambda method: method.startswith('test'), methods)

    def cleanup(self):
        self.browser.quit()

class Requirement(object):

    def get_background_color_from_element(self, element):
        background_style = element.value_of_css_property('background-color')
        rgb_values = re.findall(r'\d+', background_style) 
        return [int(rgb_value) for rgb_value in rgb_values]

    def get_closest_color_name(self, rgb):
        return ClosestColor(rgb).get_name()

    def all_images_loaded_successfully(self):
        return self.browser.execute_script("""
            for (var i = 0; i < document.images.length; i++)
                if (document.images[i].naturalWidth === 0)
                    return false;
            return true;
        """)

class ThreeSquaresRequirement(Requirement):

    def get_squares(self):
        return self.browser.find_elements_by_css_selector('div#one > div')
    
    def test_three_squares_exists(self):
        squares = self.get_squares()
        assert len(squares) == 3

    def test_two_squares_have_the_same_width_and_height(self):
        squares = self.get_squares()
        squares_with_correct_dimensions = 0
        for square in squares:
            if square.size['height'] == square.size['width']:
                squares_with_correct_dimensions += 1
        assert squares_with_correct_dimensions >= 2

    def test_two_squares_are_brown_and_blue(self):
        squares = self.get_squares()
        color_values = map(self.get_background_color_from_element, squares)
        color_names = map(self.get_closest_color_name, color_values)
        assert 'peru' in color_names and 'cornflowerblue' in color_names

    def test_bear_image_loaded_successfully(self):
        assert self.all_images_loaded_successfully()

    def test_all_squares_have_different_y_coordinates(self):
        squares = self.get_squares()
        y_coordinates = [square.location['y'] for square in squares]
        duplicate_coordinates = len(y_coordinates) != len(set(y_coordinates))
        assert not duplicate_coordinates

    def test_two_squares_have_the_same_x_coordinates(self):
        squares = self.get_squares()
        x_coordinates = [square.location['x'] for square in squares]
        unique_coordinates = len(squares) - len(set(x_coordinates))
        assert unique_coordinates == 1

runner = RequirementRunner()
#runner.run("http://folk.ntnu.no/michaedm/it2805/5/exercise-2/positioning.html", ThreeSquaresRequirement())
#runner.run("http://folk.ntnu.no/eiriknf/it2805/homework5/2/positioning.html", ThreeSquaresRequirement())
runner.run("http://folk.ntnu.no/adrianjs/%C3%98ving%203/2.%20Posisjonering%20med%20CSS/positioning.html", ThreeSquaresRequirement())
