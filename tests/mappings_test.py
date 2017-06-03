from string import ascii_uppercase
import codecs
from enigma.mappings import IDENTITY, ROT13

def test_identity_mapping():
    for c in ascii_uppercase:
        assert IDENTITY.map_forward(c) == c
        assert IDENTITY.map_back(c) == c

def test_rot13_mapping():
    for c in ascii_uppercase:
        assert ROT13.map_forward(c) == codecs.encode(c, 'rot13')
        assert ROT13.map_back(codecs.encode(c, 'rot13')) == c
