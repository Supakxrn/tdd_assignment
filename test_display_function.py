from function import display_cost
import pytest

@pytest.mark.display # pytest -m display
@pytest.mark.parametrize('weight_total, weight_truck, weight_oil, price, expected_result', [
    (1500,800,700,32,22400),
    (0,0,0,32,"out of range"),
    (-10,0,-10,32,"out of range"),
    ("a","a",'','',"input integer"),
])

def test_display(weight_total, weight_truck, weight_oil, price, expected_result):
    actual_result = display_cost(weight_total, weight_truck, weight_oil, price)
    assert expected_result == actual_result
