import datetime

from utils.get_json import get_json
from utils.format_operation import format_operation


def print_last_5_operations(operations):
    """
    Сортируем по дате  и выводим 5 самых близких к нам по дате операций
    """
    sorted_operations = sorted(operations,
                               key=lambda x: datetime.datetime.strptime(x.get('date', '1900-08-26T10:50:58.294041'),
                                                                        "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)

    for operation in sorted_operations[:5]:
        print(format_operation(operation['date'], operation['description'], operation.get('from', ''),
                               operation.get('to', ''), operation['operationAmount']['amount'],
                               operation['operationAmount']['currency']))
        print()


print_last_5_operations(get_json())
