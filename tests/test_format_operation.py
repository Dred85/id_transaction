from utils.print_last_5_transaction import format_operation

def test_format_operation():
    date = "2019-11-13T10:30:00.000"
    description = "Перевод со счета на счет"
    source = "Счет 19708645243227259794"
    destination = "Счет 19708645243227258125"
    amount = 31957.58
    currency = {"name": "руб."}

    expected_output = '13.11.2019 Перевод со счета на счет\nСчет **9794 -> Счет **8125\n31957.58 руб.'



    assert format_operation(date, description, source, destination, amount, currency) == expected_output
