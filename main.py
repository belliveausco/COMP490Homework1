import math
from dataclasses import dataclass


@dataclass
class Items:
    name: str
    price: int
    type: str


milk = Items('Milk', 3, 'wic eligible food')
shirt = Items('Shirt', 180, 'clothing')
pen = Items('Pen', 2, 'everything else')

nh_tax = 0
ma_tax = 0.00625
me_tax = 0.0055

items = [milk, shirt, pen]


def calc_total(user_state, list_of_records):
    calculation = 0
    calculation_two = 0
    if not len(list_of_records):
        total = "cart is empty, total equals zero"
        return total
    else:
        for i in range(len(list_of_records)):
            if list_of_records[i].type == 'clothing' and list_of_records[i].price < 175:
                calculation += list_of_records[i].price * (1 + user_state)
                total = math.ceil(calculation * 100) / 100
            if list_of_records[i].type == 'clothing' and list_of_records[i].price > 175:
                calculation += list_of_records[i].price
                total = math.ceil(calculation * (1 + user_state) * 100) / 100
            if list_of_records[i].type == 'clothing' and list_of_records[i].price < 0:
                total = "We don't offer refunds"
            elif list_of_records[i].type != 'clothing':
                calculation_two += list_of_records[i].price
        if total == int:
            total = total + calculation_two
            return total
        else:
            return total


calc_total(nh_tax, items)
