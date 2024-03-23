from utils.sorted_json import sorted_json
from utils.get_json import get_json
from utils.format_operation import format_operation


def main():
    """" Выводим 5 ближайших к нашай дате транзакции """

    for operation in sorted_json(get_json())[:5]:
        print(format_operation(operation['date'], operation['description'], operation.get('from', ''),
                               operation.get('to', ''), operation['operationAmount']['amount'],
                               operation['operationAmount']['currency']))
        print()

main()
