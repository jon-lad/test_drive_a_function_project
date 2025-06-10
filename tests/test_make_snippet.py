from lib.make_snippet import *


"""
With an empty string 
returns an empty string
"""
def test_with_empty_string_return_empty():
    
    actual = make_snippet("hello world")

    expected = "hello world"

    assert actual == expected

"""
With a string less than 5 words
returns the same string
"""
def test_with_string_less_than_5_words_return_same_string():
    
    actual = make_snippet("hello world")

    expected = "hello world"

    assert actual == expected

"""
With a string more than 5 words
returns the shortened string
"""
def test_with_string_more_than_5_words_return_shortened_string():
    
    actual = make_snippet("hello world how are you doing")

    expected = "hello world how are you..."

    assert actual == expected