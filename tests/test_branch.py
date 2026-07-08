from agile_ci_demo.testbranch import add_numbers, greet


def test_add_numbers():
    assert add_numbers(4, 2) == 2


def test_greet():
    assert greet("Lenglui") == "Hello, Lenglui!"
