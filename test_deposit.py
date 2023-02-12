import library
import pytest


"""Тесты на копейки"""


def test_get_national_ua_coins_int():
    assert type(library.get_national_ua_coins(5)) == str


def test_get_national_ua_coins_negative():
    assert type(library.get_national_ua_coins(-5)) == str


def test_get_national_ua_coins_value_01():
    assert library.get_national_ua_coins(39) == 'копеек'


def test_get_national_ua_coins_value_02():
        assert library.get_national_ua_coins(41) == 'копейка'


def test_get_national_ua_coins_value_03():
        assert library.get_national_ua_coins(4) == 'копейки'


"""Тесты на гривни"""


def test_get_national_ua_money_value_1():
    assert library.get_national_ua_money(30) == 'гривень'


def test_get_national_ua_money_value_2():
    assert library.get_national_ua_money(72) == 'гривни'


def test_get_national_ua_money_value_3():
    assert library.get_national_ua_money(91) == 'гривня'


def test_get_national_ua_money_value_int():
    assert type(library.get_national_ua_money(30)) == str


def test_get_national_ua_money_float():
    assert type(library.get_national_ua_money(5.5)) == str


def test_get_national_ua_money_value_negative():
    assert type(library.get_national_ua_money(-30)) == str



"""Тест на список"""


def test_get_user_numbers_for_list_type():
    assert  type(library.get_user_numbers_for_list(456)) == list


"""Тест на температуру"""

def test_is_hot_today():
    assert library.is_hot_today(34) == 'The weather is hot today!'


def test_is_hot_today_01():
    assert library.is_hot_today(24) == 'The weather is cold today!'


"""Тест на логическое значение"""


def test_get_bool_from_user_false():
    assert library.get_bool_from_user(False)(5) == -5


def test_get_bool_from_user_true():
    assert library.get_bool_from_user(True)(-2) == 2


def test_get_bool_from_user_false_1():
    assert library.get_bool_from_user(False)(-5) == -5


def test_get_bool_from_user_true_1():
    assert library.get_bool_from_user(True)(5) == 5























# check_list = [(5, 'копеек'),(0, 'копеек'),(2, 'копейки'),(99, 'копеек')]
#
#
# @pytest.mark.parametrize('test_input,expected', check_list)
# def test_get_national_ua_coins_value(test_input, expected):
#     assert library.get_national_ua_coins(test_input) == expected