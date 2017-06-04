from string import ascii_uppercase
import codecs
from enigma.mappings import IDENTITY, ROT13

def test_identity_mapping():
    """Ensure IDENTITY mapping maps every uppercase ASCII letter to itself"""
    assert_mappings(IDENTITY, ascii_uppercase, ascii_uppercase)

def test_rot13_mapping():
    """Ensure ROT13 mapping works, and is symmetric"""
    expected_output = [codecs.encode(c, 'rot13') for c in ascii_uppercase]

    assert_mappings(ROT13, ascii_uppercase, expected_output)
    assert_mappings(ROT13, expected_output, ascii_uppercase)

def assert_mappings(mapping, input_sequence, output_sequence):
    """
    Ensure that map mapping works as expected.

    For every character in the input sequence, ensure that map_forward produces
    the corresponding character in output_sequence. Also ensure that map_back
    produces the correct result when mapping characters from output_sequence.
    """
    for i, o in zip(input_sequence, output_sequence):
        assert mapping.map_forward(i) == o
        assert mapping.map_back(o) == i
