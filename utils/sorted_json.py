def sorted_json(operations):
    """
    Cортируем все данные из файла json по дате транзакции ближайшей к нашей дате
    """

    # Сортирую по дате транзакции ближайшей к нашей дате уже отфильтрованные данные
    sorted_operations = sorted(operations, key=lambda x: x.get('date', '0'), reverse=True)
    return sorted_operations
