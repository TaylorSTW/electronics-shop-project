import pytest
from src.item import Item


@pytest.fixture()
def item_book():
    return Item("Book", 500, 10)


@pytest.fixture
def item_bag():
    return Item("Bag", 1000, 5)


def test_show_all(item_book, item_bag):
    """
    Checks total number of class instances
    """
    assert len(Item.all) == 2


def test_item_init(item_book):
    """
    Checks correct Item class instance initialization
    """
    assert item_book.name == "Book"
    assert item_book.price == 500
    assert item_book.quantity == 10


def test_calculate_total_price(item_book):
    """
    Checks correct calculation of total price of item
    """
    assert item_book.calculate_total_price() == 5000


def test_apply_discount(item_book):
    """
    Checks that correct discount is applied
    """
    item_book.pay_rate = 0.65
    item_book.apply_discount()
    assert item_book.price == 325


def test_string_to_number(item_bag):
    """
        Checks conversion of string to integer
        """
    assert item_bag.string_to_number('7') == 7
    assert item_bag.string_to_number('7.0') == 7
    assert item_bag.string_to_number('7.5') == 7


def test_name_getter(item_bag):
    """
        Checks name getter
        """
    assert item_bag.name == 'Bag'


def test_name_setter(item_bag):
    """
        Checks name setter
        """
    item_bag.name = 'Box'
    assert item_bag.name == 'Box'
    # Check exception for >10 chars
    item_bag.name = 'SuperPuperBag'
    assert item_bag.name == 'Box'
