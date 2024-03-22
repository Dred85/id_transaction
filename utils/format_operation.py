import datetime


def format_operation(date, description, source, destination, amount, currency):
    """
    Фоматирует данные из json файла по шаблону:
- Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018).
- Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX (видны первые 6 цифр и последние 4,
разбито по блокам по 4 цифры, разделенных пробелом).
- Номер счета замаскирован и не отображается целиком в формате  **XXXX
(видны только последние 4 цифры номера счета).
    """
    # форматирование даты совершения операции
    formatted_date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f").strftime('%d.%m.%Y')

    # форматирование источника денег (from)
    if 'счет' in source.lower():
        masked_source = 'Счет **' + source[-4:]
    elif source == '':
        masked_source = 'Открытие вклада'
    else:
        masked_source = ' '.join(source.split()[:-1]) + ' ' + source.split()[-1][:4] + ' ' + source.split()[-1][4:6] + \
                        '**' + ' ' + '****' + ' ' + source.split()[-1][-4:]

    # форматирование приемника денег (to)
    if 'счет' in destination.lower():
        masked_destination = 'Счет **' + destination[-4:]
    elif destination == '':
        masked_destination = 'закрытие вклада'
    else:
        masked_destination = ' '.join(destination.split()[:-1]) + ' ' + destination.split()[-1][:4] + ' ' + \
                             destination.split()[-1][4:6] + '**' + ' ' + '****' + ' ' + destination.split()[-1][-4:]

    # форматирование количества и наименования валюты
    formatted_amount = f'{amount} {currency["name"]}'
    # собираем все отформатированные данные в один вывод и возвращаем его из функции
    operation_string = f'{formatted_date} {description}\n{masked_source} -> {masked_destination}\n{formatted_amount}'

    return operation_string
