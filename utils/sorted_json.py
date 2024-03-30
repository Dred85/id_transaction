import datetime


def sorted_json(operations):
    """
    Cортируем все данные из файла json по дате транзакции ближайшей к нашей дате
    """

    # Сортирую по дате транзакции ближайшей к нашей дате уже отфильтрованные данные
    sorted_operations = sorted(operations,
                               key=lambda x: datetime.datetime.strptime(x.get('date', '1900-08-26T10:50:58.294041'),
                                                                        "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    return sorted_operations
