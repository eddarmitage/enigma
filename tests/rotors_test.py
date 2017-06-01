from enigma.components import Rotor

def test_position_of_default_rotor_advances():
    rotor = Rotor()
    assert rotor.position == 'A'
    rotor.advance()
    assert rotor.position == 'B'

def test_position_wraps_around():
    rotor = Rotor('Z')
    assert rotor.position == 'Z'
    rotor.advance()
    assert rotor.position == 'A'

def test_default_rotor_has_all_notches():
    rotor = Rotor()
    assert rotor.is_on_notch()
    rotor.advance()
    assert rotor.is_on_notch()

def test_rotor_reports_on_notch_correctly():
    rotor = Rotor(notches={'B'})
    assert not rotor.is_on_notch()
    rotor.advance()
    assert rotor.is_on_notch()
    rotor.advance()
    assert not rotor.is_on_notch()
