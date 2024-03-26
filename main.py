import os

from config import ROOT_DIR
from utils.get_executed_only import get_executed_only
from utils.sorted_json import sorted_json
from utils.get_json import get_json
from utils.format_operation import format_operation


def main():
    """" Окончательный Вывод 5 ближайших к нашай дате транзакции """


# Путь до файла operations.json через абсолютный путь ROOT_DIR
path_to_file = os.path.join(ROOT_DIR, 'data', 'operations.json')

# все транзакции без фильтрации и сортировки
all_operations = get_json(path_to_file)
# фильтруем по EXECUTED
executed_operations = get_executed_only(all_operations)
# сортируем по дате операции ближайшей к нам
sorted_operations = sorted_json(executed_operations)
# В цикле выводим первые пять операций и формируем вывод как по ТЗ
five_for_formating = sorted_operations[:5]
for operation in five_for_formating:
    print(format_operation(operation['date'], operation['description'], operation.get('from', ''),
                           operation.get('to', ''), operation['operationAmount']['amount'],
                           operation['operationAmount']['currency']))
    print()

if __name__ == '__main__':
    main()
