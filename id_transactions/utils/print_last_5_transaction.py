import datetime

from get_json import get_json


def format_operation(date, description, source, destination, amount, currency):
    """
    Formats operation string
    """
    formatted_date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f").strftime('%d.%m.%Y')

    # форматирование источника from
    if 'счет' in source.lower():
        masked_source = 'Счет **' + source[-4:]
    elif source == '':
        masked_source = 'открытие нового счета'
    else:
        masked_source = ' '.join(source.split()[:-1]) + ' ' + source.split()[-1][:4] + ' ' + source.split()[-1][4:6] + '**' + ' ' + '****' + ' ' + source.split()[-1][-4:]

    if 'счет' in destination.lower():
        masked_destination = 'Счет **' + destination[-4:]
    else:
        masked_destination = ' '.join(destination.split()[:-1]) + ' ' + destination.split()[-1][:4] + ' ' + destination.split()[-1][4:6] + '**' + ' ' + '****' + ' ' + destination.split()[-1][-4:]

    formatted_amount = f'{amount} {currency["name"]}'

    operation_string = f'{formatted_date} {description}\n{masked_source} -> {masked_destination}\n{formatted_amount}'

    return operation_string


def print_last_5_operations(operations):
    """
    Prints last 5 operations
    """

    # sorted_operations = sorted(operations, key=lambda x: datetime.datetime.strptime(x['date'], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    sorted_operations = operations


    for operation in sorted_operations[:5]:
        print(format_operation(operation['date'], operation['description'], operation.get('from', ''),
                               operation.get('to', ''), operation['operationAmount']['amount'],
                               operation['operationAmount']['currency']))
        print()


operations = get_json()

print_last_5_operations(operations)
