import datetime
def format_operation(date, description, source, destination, amount, currency):
    """
    Formats operation string
    """
    formatted_date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f").strftime('%d.%m.%Y')

    # форматирование источника денег (from)
    if 'счет' in source.lower():
        masked_source = 'Счет **' + source[-4:]
    elif source == '':
        masked_source = 'открытие нового счета'
    else:
        masked_source = ' '.join(source.split()[:-1]) + ' ' + source.split()[-1][:4] + ' ' + source.split()[-1][4:6] + \
                        '**' + ' ' + '****' + ' ' + source.split()[-1][-4:]

    # форматирование приемника денег (to)
    if 'счет' in destination.lower():
        masked_destination = 'Счет **' + destination[-4:]
    elif destination == '':
        masked_destination = 'закрытие счета'
    else:
        masked_destination = ' '.join(destination.split()[:-1]) + ' ' + destination.split()[-1][:4] + ' ' + \
                             destination.split()[-1][4:6] + '**' + ' ' + '****' + ' ' + destination.split()[-1][-4:]

    formatted_amount = f'{amount} {currency["name"]}'

    operation_string = f'{formatted_date} {description}\n{masked_source} -> {masked_destination}\n{formatted_amount}'

    return operation_string
