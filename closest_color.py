import webcolors

class ClosestColor(object):

    def __init__(self, rgb):
        self.rgb = (rgb[0], rgb[1], rgb[2]) if rgb else None

    def get_name(self):
        if self.rgb:
            actual, closest = self.get_colour_name()
            return closest
        else:
            return None

    def closest_colour(self):
        min_colours = {}
        for key, name in webcolors.css3_hex_to_names.items():
            r_c, g_c, b_c = webcolors.hex_to_rgb(key)
            rd = (r_c - self.rgb[0]) ** 2
            gd = (g_c - self.rgb[1]) ** 2
            bd = (b_c - self.rgb[2]) ** 2
            min_colours[(rd + gd + bd)] = name
        return min_colours[min(min_colours.keys())]

    def get_colour_name(self):
        try:
            closest_name = actual_name = webcolors.rgb_to_name(self.rgb)
        except ValueError:
            closest_name = self.closest_colour()
            actual_name = None
        return actual_name, closest_name
