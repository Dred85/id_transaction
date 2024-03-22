from utils import print_last_5_transaction
from utils import get_json
import json


def test_format_operation():
    assert print_last_5_transaction.format_operation(
        {
            'date': '2020-01-01',
            'description': 'test',
          'source': 'test',
            'destination': 'test',
            'amount': 100,
            'currency': 'test'
        }
    ) == '2020-01-01 test\ntest -> test\n100 test'

def test_print_last_5_operations():
    pass