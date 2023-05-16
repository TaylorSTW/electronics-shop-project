import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self) -> str:
        """
        Getter for attribute "name"
        """
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        """Set name property of class instance"""
        try:
            if len(new_name) <= 10:
                self.__name = new_name
            else:
                raise ValueError
        except ValueError:
            print("Name must contain no more than 10 characters")

    @classmethod
    def instantiate_from_csv(cls) -> None:
        with open('../src/items.csv', 'r', encoding='windows-1251') as file:
            cls.all = [] #очистка списков
            item = csv.DictReader(file)
            for i in item:
                name = i["name"]
                price = cls.string_to_number(i["price"])
                quantity = cls.string_to_number(i["quantity"])
                cls(name, price, quantity)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @staticmethod
    def string_to_number(any_string: str) -> int:
        try:
            return int(any_string)
        except ValueError:
            return int(any_string[0: any_string.find('.')])
