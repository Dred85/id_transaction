from utils.format_operation import format_operation


def test_format_operation1():
    """
    Тестирование функции format_operation: Перевод со счета на счет
    """
    date = "2019-11-13T10:30:00.000"
    description = "Перевод со счета на счет"
    source = "Счет 19708645243227259794"
    destination = "Счет 19708645243227258125"
    amount = 31957.58
    currency = {"name": "руб."}

    expected_output = '13.11.2019 Перевод со счета на счет\nСчет **9794 -> Счет **8125\n31957.58 руб.'

    assert format_operation(date, description, source, destination, amount, currency) == expected_output

def test_format_operation2():
    """
    Тестирование функции format_operation: Перевод с карты на карту
    """
    date = "2018-12-03T10:30:00.000"
    description = "Перевод с карты на карту"
    source = "MasterCard 1796816785869527"
    destination = "Visa Classic 7699855375169288"
    amount = 31957.58
    currency = {"name": "руб."}

    expected_output = '03.12.2018 Перевод с карты на карту\nMasterCard 1796 81** **** 9527 -> Visa Classic 7699 85** **** 9288\n31957.58 руб.'

    assert format_operation(date, description, source, destination, amount, currency) == expected_output

def test_format_operation3():
    """
    Тестирование функции format_operation: открытие нового счета
    """
    date = "2019-12-03T10:30:00.000"
    description = "Открытие вклада"
    source = ""
    destination = "Счет 19708645243227258125"
    amount = 31957.58
    currency = {"name": "USD"}

    expected_output = '03.12.2019 Открытие вклада\nОткрытие вклада -> Счет **8125\n31957.58 USD'

    assert format_operation(date, description, source, destination, amount, currency) == expected_output

