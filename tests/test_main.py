from main import main


def test_main(capsys):
    """проверяю вывод нa соответствие ТЗ"""
    main()
    # захват вывода функции main()
    captured = capsys.readouterr()
    assert captured.out == """08.12.2019 Открытие вклада
Открытие вклада -> Счет **5907
41096.24 USD

07.12.2019 Перевод организации
Visa Classic 2842 87** **** 9012 -> Счет **3655
48150.39 USD

19.11.2019 Перевод организации
Maestro 7810 84** **** 5568 -> Счет **2869
30153.72 руб.

13.11.2019 Перевод со счета на счет
Счет **9794 -> Счет **8125
62814.53 руб.

05.11.2019 Открытие вклада
Открытие вклада -> Счет **8381
21344.35 руб.

"""
