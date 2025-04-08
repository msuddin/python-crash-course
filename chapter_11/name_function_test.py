import pytest

from name_function import name_function

def test_name_function_pass():
    name = name_function('sam', 'holland')
    assert name == 'Sam Holland'

def test_name_function_fail():
    name = name_function('sam', 'holland')
    #assert name == 'Sam Hollands'