import tempfile

from src.decorators import log


def test_log(capsys):
    @log(filename="test_log.txt")
    def my_function(x: str, y: str) -> str:
        """Тестирует корректное выполнение функции"""
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert "my_function called with args: (1, 2), kwargs:{}. Result: 3\n" in captured.out
    # Проверка ошибки
    try:
        my_function(0, 2)
    except TypeError:
        captured = capsys.readouterr()
        assert "my function error: " in captured.out


def test_log_2() -> None:
    """Тестирует запись в файл после успешного выполнения"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_2 = tmp_file.name

    @log(filename=log_2)
    def func(x: str, y: str) -> str:
        return x + y

    func(1, 2)
    with open(log_2, "r", encoding="utf-8") as file:
        logs = file.read()

    assert "func called with args: (1, 2), kwargs:{}. Result: 3" in logs


def test_log_3() -> None:
    """Тестирует запись в файл после ошибки"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_3 = tmp_file.name

    @log(filename=log_3)
    def func(x: str, y: str) -> str:
        return x + y

    func(1, "2")
    with open(log_3, "r", encoding="utf-8") as file:
        logs = file.read()

    assert "func error: unsupported operand type(s) for +: 'int' and 'str'. Inputs:(1, '2'), {}" in logs
