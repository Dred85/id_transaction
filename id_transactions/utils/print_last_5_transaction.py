import datetime

from get_json import get_json

def print_last_5_transaction():
    """Print the last 5 transactions"""
    sorted_operations = sorted(get_json(), key=lambda x: datetime.datetime.strptime(x['date'], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    return sorted_operations


print(print_last_5_transaction())