from function import display_cost

#น้ำหนักปาล์มน้ำมันพร้อมรถ
weight_palm_truck = input("Enter weight of palm oil with truck (kg): ")

#น้ำหนักรถเปล่า
weight_truck = input("Enter weight of the truck (kg): ")

#น้ำหนักปาล์มน้ำมัน
if any(c.isalpha() for c in weight_palm_truck) or any(c.isalpha() for c in weight_truck):
    print("input integer")
    exit()
elif float(weight_palm_truck) < 0 or float(weight_truck) < 0:
    weight_oil = float(weight_palm_truck) - float(weight_truck)
    print("Weight of palm oil (kg): ", weight_oil)
else:
    weight_oil = float(weight_palm_truck) - float(weight_truck)
    print("Weight of palm oil (kg): ", weight_oil)

#ราคาปาล์มน้ำมัน
price = None
while price is None or not price.isdigit():
    price = input("Enter price of the oil (THB/kg): ")
    if any(c.isalpha() for c in price) or (float(price) < 0):
        print("input integer")
        price = None
        continue

try:
    try:
        weight_palm_truck  = int(weight_palm_truck)
        weight_truck = int(weight_truck)
        weight_oil = int(weight_oil)
        price  = int(price )
    except:
        weight_palm_truck = float(weight_palm_truck)
        weight_truck = float(weight_truck)
        weight_oil = float(weight_oil)
        price = float(price)
except:
    weight_palm_truck = str(weight_palm_truck)
    weight_truck = str(weight_truck)
    weight_oil = str(weight_oil)
    price = str(price)

#ค่าสินค้าทั้งหมด
result = display_cost(weight_palm_truck, weight_truck, weight_oil, price )
print("Cost: " ,result)