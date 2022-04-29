import math
from dataclasses import dataclass
import pytest
import main


# corner path test

def test():
    @dataclass
    class Items:
        name: str
        price: int
        type: str

    nh_tax = 0
    ma_tax = 0.00625
    me_tax = 0.0055

    records = []

    main.calc_total(ma_tax, records)
    assert (main.calc_total(ma_tax, records)) == "cart is empty, total equals zero"
    main.calc_total(me_tax, records)
    assert (main.calc_total(me_tax, records)) == "cart is empty, total equals zero"
    main.calc_total(nh_tax, records)
    assert (main.calc_total(nh_tax, records)) == "cart is empty, total equals zero"
