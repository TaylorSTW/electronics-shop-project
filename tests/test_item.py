import pytest
from src.item import Item


@pytest.fixture()
def tv_obj():
    return Item("name", 20000, 10)


def test_function(tv_obj):
    assert tv_obj.name == "name"


def test_calculate_total_price(tv_obj):
    assert tv_obj.calculate_total_price() == 200000


def test_apply_discount(tv_obj):
    tv_obj.apply_discount()
    assert tv_obj.price == 20000