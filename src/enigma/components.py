from string import ascii_uppercase
import itertools

from six import next

from enigma.mappings import IDENTITY

class Rotor(object):

    def __init__(self, initial_position='A', mappings=IDENTITY, notches=ascii_uppercase):
        idx = ascii_uppercase.index(initial_position)
        self._positions = itertools.cycle(ascii_uppercase[idx:] + ascii_uppercase[:idx])
        self._position = next(self._positions)
        self._mappings = mappings
        self._notches = notches

    def map_forward(self, input_char):
        return self._mappings.map_forward(input_char)

    def map_back(self, input_char):
        return self._mappings.map_back(input_char)

    def advance(self):
        self._position = next(self._positions)

    @property
    def position(self):
        return str(self._position)

    def is_on_notch(self):
        return self._position in self._notches
