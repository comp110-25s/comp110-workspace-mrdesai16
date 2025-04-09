"""Testing dictionary exercise functions"""

__author__: str = "730652974"

import pytest
from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import bin_len


def test_invert_simple_case():
    """Test with a simple dictionary of unique values."""
    result = invert({"a": "z", "b": "y", "c": "x"})
    assert result == {"z": "a", "y": "b", "x": "c"}


def test_invert_single_key_value():
    """Test with a dictionary containing only one key-value pair."""
    result = invert({"apple": "cat"})
    assert result == {"cat": "apple"}


def test_invert_key_error_case():
    """Test where there are duplicate values causing a KeyError."""
    with pytest.raises(KeyError):
        invert({"kris": "jordan", "michael": "jordan"})


def test_count_simple_case():
    """Test with a list of words that are unique and repeated."""
    result = count(["apple", "banana", "apple", "orange", "banana", "banana"])
    assert result == {"apple": 2, "banana": 3, "orange": 1}


def test_count_empty_list():
    """Test with an empty list."""
    result = count([])
    assert result == {}


def test_count_single_word():
    """Test with a list containing only one word."""
    result = count(["apple"])
    assert result == {"apple": 1}


def test_favorite_color_simple_case():
    """Test with multiple names and their favorite colors."""
    result = favorite_color(
        {
            "Alice": "blue",
            "Bob": "red",
            "Charlie": "blue",
            "David": "green",
            "Eve": "red",
        }
    )
    assert result == "blue"  # 'blue' appears first in a tie


def test_favorite_color_single_color():
    """Test with multiple names all having the same favorite color."""
    result = favorite_color({"Alice": "blue", "Bob": "blue", "Charlie": "blue"})
    assert result == "blue"


def test_favorite_color_tie_case():
    """Test where two colors are tied, the first one should be returned."""
    result = favorite_color(
        {"Alice": "red", "Bob": "blue", "Charlie": "blue", "David": "red"}
    )
    assert result == "red"  # 'red' appears first


def test_bin_len_simple_case():
    """Test with a list of words of varying lengths."""
    result = bin_len(["the", "quick", "fox"])
    assert result == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_empty_list():
    """Test with an empty list."""
    result = bin_len([])
    assert result == {}


def test_bin_len_repeated_words():
    """Test with a list containing repeated words."""
    result = bin_len(["the", "the", "fox"])
    assert result == {3: {"the", "fox"}}
