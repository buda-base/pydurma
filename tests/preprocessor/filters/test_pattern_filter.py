import re
from pydurma.bo.tokenizer_bo import TibetanTokenizer
from pydurma.bo.normalizer_bo import TibetanNormalizer
from pydurma.encoder import Encoder
from pydurma.input_filters.pattern_filter import PatternInputFilter


def test_pattern_filter():
    test_string = "གི་ཚེ་རང་ཉིད༌        ཉིད་སྐྱེ་ན་རྒྱུའི། །"
    expected_string = "གི་ཚེ་རང་ཉིད་ཉིད་སྐྱེ་ན་རྒྱུའི༎ "

    filtered = PatternInputFilter(test_string, re.compile("། །"), "༎ ")
    filtered = PatternInputFilter(filtered, re.compile("༌"), "་")
    filtered = PatternInputFilter(filtered, re.compile("་ +"), "་")
    
    assert filtered.get_string() == expected_string
