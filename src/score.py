class Score(object):
    
    def __init__(self, points):
        if self._is_valid(points):
            self._points = points 

    def _is_valid(self, points):
        if isinstance(points, int) == False:
            raise TypeError('Points must be a number.')
        elif points > 100:
            raise ValueError('Score is over 100.')
        elif points < 0:
            raise ValueError('Points is under 0.')
        else:
            return True

    @property
    def points(self):
        return self._points

    def subtract(self, points):
        self._points = self._points - points
