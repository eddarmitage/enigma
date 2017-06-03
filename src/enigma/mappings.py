from abc import ABCMeta, abstractmethod
import codecs

class Mapping(object):
    """A reversible function that can be applied to an input."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def map_forward(self, input_char):
        """Return the result of applying the mapping in the forwards direction."""
        pass

    @abstractmethod
    def map_back(self, input_char):
        """Return the result of applying the mapping in the reverse direction."""
        pass

class SymmetricMapping(Mapping):
    """A mapping that uses a symmetric relationship between input and output.

    That is, one whereby if a mapping exists from A -> B, a corresponding
    mapping will exist from B -> A."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def _map(self, input_char):
        """Return the result of mapping the input in either direction."""
        pass

    def map_forward(self, input_char):
        return self._map(input_char)

    def map_back(self, input_char):
        return self._map(input_char)

class IdentityMapping(SymmetricMapping):
    """A Mapping where every value is mapped to itself."""
    def _map(self, input_char):
        return input_char

class Rot13Mapping(SymmetricMapping):
    def _map(self, input_char):
        return codecs.encode(input_char, 'rot13')

IDENTITY = IdentityMapping()
ROT13 = Rot13Mapping()
