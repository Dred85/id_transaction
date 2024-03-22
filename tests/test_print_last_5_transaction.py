from utils.print_last_5_transaction import format_operation
import pytest

# Создаем фикстуру, которая запускается перед каждым тестом
@pytest.fixture
def coll(): # имя фикстуры
    return [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }]



def test_format_operation(coll):
    assert format_operation(coll) == '13.11.2019 Перевод со счета на счет\
                                              Счет ** 9794 -> Счет ** 8125\
                                              31957.58 руб.'


# def test_print_last_5_operations():
#     pass
