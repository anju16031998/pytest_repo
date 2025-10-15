import pytest

from myapp.app import multiply_by_two, divide_by_two


@pytest.fixture
def numbers():
    a = 10
    b = 20
    return [a,b]


class TestApp:
    def test_multiplication(self, numbers):
        res = multiply_by_two(numbers[0])
        assert res == numbers[1]

    def test_division(self, numbers):
        res = divide_by_two(numbers[1])
        assert res == numbers[0]
    def test_divide_by_two_studentid(self):
        input_value = 171           # 178 ÷ 2 = 89
        expected_output = 89        # last two digits of your student ID
        result = divide_by_two(input_value)
        assert result == expected_output