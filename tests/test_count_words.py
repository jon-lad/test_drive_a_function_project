from lib.count_words import *

"""
Test an empty string
should return 0
"""
def test_empty_string_returns_zero():
    actual = count_words("")

    expected = 0

    assert actual == expected

"""
Test an string with 1 word
should return 1
"""
def test_empty_string_returns_zero():
    actual = count_words("hello")

    expected = 1

    assert actual == expected

"""
Test an string with 5 words
should return 5
"""
def test_empty_string_returns_zero():
    actual = count_words("one two three four five")

    expected = 5

    assert actual == expected