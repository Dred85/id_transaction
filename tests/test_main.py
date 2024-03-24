from utils.main import main


def test_main(capsys):
    """проверяю, что вывод не пустой"""
    main()
    captured = capsys.readouterr()
    assert captured.out != ""
