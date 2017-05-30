from string import ascii_uppercase

class Rotor(object):

    def __init__(self, initial_position = 'A', mappings = None, notches = ascii_uppercase):
        idx = ascii_uppercase.index(initial_position)
        self._positions = itertool.cycle(ascii_uppercase[idx:] + ascii_uppercase[:idx])
        self._position = initial_position
        self._mappings = mappings
        self._notches = notches

    def map_forward(self, input):
        return input

    def map_back(self, input):
        return input

    def advance(self):
        self._position = _positions.next()

    @property
    def position(self):
        return self._position

    def is_on_notch(self):
        return self._position in self._notches
