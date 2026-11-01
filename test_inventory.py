"""
Project name:Ecommerce_Profit_and_Inventory_calculator
Author:Adhanet Gebretensay
Purpouse:Automated testing using pytest
Date:10/30/2026

"""

import pytest

from product import Product
from inventory import Inventory

def test_product_attributes():
    p = Product("Candle", "AD-001",  "Home", 5.0, 10.0, 20)
    assert p.product_id == "AD-001"
    assert p.name == "Candle"
    assert p.stock_quantity == 20


def test_record_sales():
    my_inventory = Inventory()
    p = Product("Candle", "AD-001",  "Home", 5.0, 10.0, 20)
    my_inventory.add_product(p)
    success = my_inventory.record_sales("AD-001", 5)

    assert success is True
    assert p.stock_quantity == 15