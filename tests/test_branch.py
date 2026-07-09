from agile_ci_demo.testbranch import add_numbers, greet


def test_add_numbers():
    assert add_numbers(3, 1) == 4


def test_greet():
    assert greet("LengZai") == "Hello, LengZai!"
