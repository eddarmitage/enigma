from string import ascii_uppercase
from enigma.mappings import IDENTITY

def test_identity_mapping():
    for c in ascii_uppercase:
        assert IDENTITY.map_forward(c) == c
        assert IDENTITY.map_back(c) == c
