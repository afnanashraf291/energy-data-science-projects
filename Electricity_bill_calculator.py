
price_below_100units=0.05
price_for_next_200units=0.10
price_for_remaining_unit=0.15
vat=0.19

def bill_calculator(units_consumed):
    bill=0
    for unit in range(1,units_consumed+1):
        if unit<=100:
            bill+=price_below_100units
        elif unit<=300:
            bill+=price_for_next_200units
        else:
            bill+=price_for_remaining_unit
    total_bill=bill+bill*vat
    return total_bill


    


print(bill_calculator(450))