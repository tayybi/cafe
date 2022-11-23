# from src.main import main_menu
from unittest.mock import patch
from unittest import mock
from src.products import Products
# from src.products import Products


def test_add_product():
    # assembly
    lst = [{'ali',11}]
    # # action 
    products = Products(lst)
    result = products.add_product("lst")
    # # asserttion
    axpectation = 'null'
    assert result == axpectation


# def test_get_country_code():
#     test_countries = [
#         {"name": "United Kingdom", "alpha3Code": "UK"},
#         {"name": "United States", "alpha3Code": "USA"}
#     ]

#     test_name = "United Kingdom"
#     expected = "UK"
#     actual = get_country_code(test_countries, test_name)

#     assert expected == actual

