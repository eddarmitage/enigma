from string import ascii_uppercase
import codecs
from enigma.mappings import IDENTITY, ROT13, AsciiMapping

ROT13_OUTPUT = [codecs.encode(c, 'rot13') for c in ascii_uppercase]

def test_identity_mapping():
    """Ensure IDENTITY mapping maps every uppercase ASCII letter to itself"""
    assert_mappings(IDENTITY, ascii_uppercase, ascii_uppercase)

def test_rot13_mapping():
    """Ensure ROT13 mapping works, and is symmetric"""
    assert_mappings(ROT13, ascii_uppercase, ROT13_OUTPUT)
    assert_mappings(ROT13, ROT13_OUTPUT, ascii_uppercase)

def test_ascii_mapping():
    """Test the AsciiMapping using a ROT13 output encoding"""
    mapping = AsciiMapping(ROT13_OUTPUT)
    assert_mappings(mapping, ascii_uppercase, ROT13_OUTPUT)
    assert_mappings(mapping, ROT13_OUTPUT, ascii_uppercase)

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
