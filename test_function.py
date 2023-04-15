from function import display_cost, validate_weight
import pytest

@pytest.mark.code # pytest -m code
def test_palm_oil_with_truck1500kg_price_32():
    weight_total = 1500
    weight_truck = 800
    weight_oil = 700
    price = 32
    expected_result = 22400
    actual_result = display_cost(weight_total, weight_truck, weight_oil, price)
    assert expected_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_out_of_range_weight_total_0_price_32():
    weight_total = 0
    weight_truck = 0
    weight_oil = 0
    price = 32
    expected_result = "out of range"
    actual_result = display_cost(weight_total, weight_truck, weight_oil, price)
    assert expected_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_out_of_range_weight_total_minus_10_price_32():
    weight_total = -10
    weight_truck = 0
    weight_oil = -10
    price = 32
    expected_result = "out of range"
    actual_result = display_cost(weight_total, weight_truck, weight_oil, price)
    assert expected_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_input_integer_weight_char_a():
    weight_total = "a"
    weight_truck = "a"
    weight_oil = ''
    price = ''
    expected_result = "input integer"
    actual_result = display_cost(weight_total, weight_truck, weight_oil, price)
    assert expected_result == actual_result
