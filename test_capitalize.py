def capitalize_string(s):
    if not isinstance(s, str):
        raise TypeError('Please provide a string')
    return s.capitalize()

def add(a,b):
    return a+b;
    
def test_add():
    assert add(3,7) == 10
    
def test_capitalize_string():
    assert capitalize_string('test') == 'Test'
