from utils.sorted_json import sorted_json
from utils.get_json import get_json
import pytest


# Создаем фикстуру, которая запускается перед каждым тестом
@pytest.fixture
def coll():  # имя фикстуры
    return get_json()


expected_output_sort = """08.12.2019 Открытие вклада
открытие нового счета -> Счет **5907
41096.24 USD

07.12.2019 Перевод организации
Visa Classic 2842 87** **** 9012 -> Счет **3655
48150.39 USD

03.12.2019 Перевод с карты на карту
MasterCard 1796 81** **** 9527 -> Visa Classic 7699 85** **** 9288
17628.50 USD

19.11.2019 Перевод организации
Maestro 7810 84** **** 5568 -> Счет **2869
30153.72 руб.

13.11.2019 Перевод со счета на счет
Счет **9794 -> Счет **8125
62814.53 руб."""


def test_print_last_5_operations(coll):
    assert sorted_json(coll) == expected_output_sort
