import pytest
from string_utils import StringUtils

utils = StringUtils()


# capitalize

@pytest.mark.parametrize("value, expected", [
    ("skypro", "Skypro"),
    ("тест", "Тест"),
    ("123", "123"),
])
def test_capitalize_positive(value, expected):
    assert utils.capitalize(value) == expected


def test_capitalize_empty_string():
    assert utils.capitalize("") == ""


def test_capitalize_none_raises():
    # дефект/особенность: метод не обрабатывает None
    with pytest.raises(AttributeError):
        utils.capitalize(None)


# trim

@pytest.mark.parametrize("value, expected", [
    ("   skypro", "skypro"),
    ("   04 апреля 2023", "04 апреля 2023"),
    ("skypro", "skypro"),
])
def test_trim_positive(value, expected):
    assert utils.trim(value) == expected


@pytest.mark.parametrize("value, expected", [
    ("", ""),
    (" ", ""),
    ("     ", ""),
])
def test_trim_empty_and_spaces(value, expected):
    assert utils.trim(value) == expected


def test_trim_none_raises():
    # дефект/особенность: метод не обрабатывает None
    with pytest.raises(AttributeError):
        utils.trim(None)


# contains

@pytest.mark.parametrize("string, symbol", [
    ("SkyPro", "S"),
    ("123", "2"),
    ("04 апреля 2023", " "),
])
def test_contains_positive(string, symbol):
    assert utils.contains(string, symbol) is True


@pytest.mark.parametrize("string, symbol", [
    ("SkyPro", "U"),
    ("", "a"),
    (" ", "a"),
])
def test_contains_negative(string, symbol):
    assert utils.contains(string, symbol) is False


def test_contains_none_raises():
    # дефект/особенность: метод не обрабатывает None
    with pytest.raises(AttributeError):
        utils.contains(None, "a")


# delete_symbol

@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("04 апреля 2023", " ", "04апреля2023"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected


def test_delete_symbol_when_symbol_not_found_returns_original():
    assert utils.delete_symbol("SkyPro", "Z") == "SkyPro"


def test_delete_symbol_empty_string():
    assert utils.delete_symbol("", "a") == ""


def test_delete_symbol_none_raises():
    # дефект/особенность: метод не обрабатывает None
    with pytest.raises(AttributeError):
        utils.delete_symbol(None, "a")
