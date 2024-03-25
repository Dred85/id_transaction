import os

from config import ROOT_DIR
from utils.sorted_json import sorted_json
from utils.get_json import get_json
import pytest

path_to_file = os.path.join(ROOT_DIR, 'data', 'operations.json')
# Создаем фикстуру, которая запускается перед каждым тестом
@pytest.fixture
def coll():  # имя фикстуры
    return get_json(path_to_file)


expected_output_sort_0 = 863064926
expected_output_sort_1 = 114832369
expected_output_sort_2 = 154927927
expected_output_sort_3 = 482520625
expected_output_sort_4 = 801684332




def test_sorted_json(coll):
    assert sorted_json(coll)[0]['id'] == expected_output_sort_0
    assert sorted_json(coll)[1]['id'] == expected_output_sort_1
    assert sorted_json(coll)[2]['id'] == expected_output_sort_2
    assert sorted_json(coll)[3]['id'] == expected_output_sort_3
    assert sorted_json(coll)[4]['id'] == expected_output_sort_4
