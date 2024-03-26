def get_executed_only(operations):
    """Фильтрую по статусу выполнения операции 'EXECUTED'"""

    exectuted_operations = filter(lambda x: x.get("state") == "EXECUTED", operations)
    return exectuted_operations
