"""Dictionary exercise!"""

__author__: str = "730652974"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Invert keys and values of a dictionary and raise KeyError if duplicates exist"""
    inverted_dict = {}
    for key, value in d.items():
        if value in inverted_dict:
            raise KeyError(f"Duplicate key found when inverting: {value}")
        inverted_dict[value] = key
    return inverted_dict


def count(values: list[str]) -> dict[str, int]:
    result = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def favorite_color(people: dict[str, str]) -> str:
    color_counts = count(list(people.values()))
    most_popular = ""
    highest_count = 0
    for color in color_counts:
        if color_counts[color] > highest_count:
            most_popular = color
            highest_count = color_counts[color]
    return most_popular


def bin_len(words: list[str]) -> dict[int, set[str]]:
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = set()
        result[length].add(word)
    return result
