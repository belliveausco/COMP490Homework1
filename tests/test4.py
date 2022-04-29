import math
from dataclasses import dataclass
import pytest
import main


# good path test

def test():
    @dataclass
    class Items:
        name: str
        price: int
        type: str

    milk = Items('Milk', 0, 'wic eligible food')
    shirt = Items('Shirt', 0, 'clothing')
    pen = Items('Pen', 0, 'everything else')

    nh_tax = 0
    ma_tax = 0.00625
    me_tax = 0.0055

    items = [milk, shirt, pen]

    main.calc_total(ma_tax, items)
    assert (main.calc_total(ma_tax, items)) == 0
    main.calc_total(me_tax, items)
    assert (main.calc_total(me_tax, items)) == 0
    main.calc_total(nh_tax, items)
    assert (main.calc_total(nh_tax, items)) == 0
