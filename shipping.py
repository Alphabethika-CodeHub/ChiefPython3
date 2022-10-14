weight = 50
type_shipping = "BRONZE"
total_cost = 0.0

GROUND_SHIPPING_BRONZE_CHARGE = 20.00
GROUND_SHIPPING_SILVER_CHARGE = 60.00
GROUND_SHIPPING_PLATINUM_CHARGE = 120.00

# 2 Pound or Less
LV1_PRICE_PER_POUND = 4.50

# 6 Pound or Less
LV2_PRICE_PER_POUND = 9.12

# 12 Pound or Less
LV3_PRICE_PER_POUND = 12.37

# 25 Pound or Less
LV4_PRICE_PER_POUND = 15.9

# 50 Pound or Less
LV5_PRICE_PER_POUND = 23.73


def CheckShippingType():
    if type_shipping == "BRONZE":
        total_cost = GROUND_SHIPPING_BRONZE_CHARGE
        return total_cost
    elif type_shipping == "SILVER":
        total_cost = GROUND_SHIPPING_SILVER_CHARGE
        return total_cost
    elif type_shipping == "PLATINUM":
        total_cost = GROUND_SHIPPING_PLATINUM_CHARGE
        return total_cost
    else:
        print("Unknown Type of Shipping.")


# Weight Shipping.
if weight <= 2:
    total_cost = CheckShippingType()
    total_cost += weight * LV1_PRICE_PER_POUND
    print("You're Using: " + type_shipping + " Type of Shipping.")
    print("Estimated Cost: $" + str(total_cost))
elif weight <= 6:
    total_cost = CheckShippingType()
    total_cost += weight * LV2_PRICE_PER_POUND
    print("You're Using: " + type_shipping + " Type of Shipping.")
    print("Estimated Cost: $" + str(total_cost))
elif weight <= 12:
    total_cost = CheckShippingType()
    total_cost += weight * LV3_PRICE_PER_POUND
    print("You're Using: " + type_shipping + " Type of Shipping.")
    print("Estimated Cost: $" + str(total_cost))
elif weight <= 25:
    total_cost = CheckShippingType()
    total_cost += weight * LV4_PRICE_PER_POUND
    print("You're Using: " + type_shipping + " Type of Shipping.")
    print("Estimated Cost: $" + str(total_cost))
elif weight <= 50:
    total_cost = CheckShippingType()
    total_cost += weight * LV5_PRICE_PER_POUND
    print("You're Using: " + type_shipping + " Type of Shipping.")
    print("Estimated Cost: $" + str(total_cost))
else:
    print("Out of Range")
