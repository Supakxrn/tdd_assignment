def validate_weight(weight_total, weight_truck):
    weight = weight_total
    if type(weight) != int:
        if type(weight) == str:
            return "input integer"
        elif weight >= 1 and weight <= 3000:
            return "input integer"
        else:
            return "out of range"
    elif weight >= 1 and weight <= 3000:
        return weight
    else:
        return "out of range"
    weight_oil = weight_total - weight_truck

def display_cost(weight_total, weight_truck, weight_oil, price):
    weight = validate_weight(weight_total, weight_truck)
    if type(weight) == int:
        cost = weight_oil * price
        result = cost
        return result
    else:
        return weight