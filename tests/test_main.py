from utils.main import main
from utils.sorted_json import sorted_json

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out != ""
