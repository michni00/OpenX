from backend.methods import fahrenheit_to_celsius
from backend.methods_ai import fahrenheit_to_celsius_ai

def test_conversion_int_web():
    assert fahrenheit_to_celsius(50.0) == 10.0
    
def test_conversion_int_tf():
    assert fahrenheit_to_celsius_ai(50.0) == 10.0
    
def test_conversion_float_web():
    assert fahrenheit_to_celsius(30.0) == -1.11111
    
def test_conversion_float_tf():
    assert fahrenheit_to_celsius_ai(30.0) == -1.11111
    