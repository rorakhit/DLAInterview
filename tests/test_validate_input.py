from project import validate_input
import pytest

def test_letter_input():
    with pytest.raises(TypeError) as e:
        wrong_text = validate_input('x*5')

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        wrong = validate_input('10/0')

def test_lots_of_spaces():
    result = validate_input('      10      *      50       ')
    assert result == '10*50'

def test_bad_numbers():
    with pytest.raises(TypeError) as e:
        wrong = validate_input('-3*4')

def test_bad_operation():
    with pytest.raises(TypeError) as e:
        wrong = validate_input('3x5')

def test_working_plus():
    result = validate_input('10+4')
    assert result == '10+4'

def test_working_minus():
    result = validate_input('10-3')
    assert result == '10-3'

def test_working_multiplication():
    result = validate_input('234*234')
    assert result == '234*234'

def test_working_division():
    result = validate_input('283904762835/237645238764')
    assert result == '283904762835/237645238764'