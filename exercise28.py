def fuel_price(litres, price_per_liter):
    dicount = (litres // 2) * 0.05
    if dicount > 0.25:
        dicount = 0.25

    return round(litres * (price_per_liter - dicount),2)


print(fuel_price(10, 21.5))
print(fuel_price(40, 10))
print(fuel_price(15, 5.83))