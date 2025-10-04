"""Calculator 类的单元测试。"""

import pytest
from src.core.calculator import Calculator


class TestCalculator:
    """Calculator 类的测试套件。"""

    def test_add_integers(self) -> None:
        """测试两个整数相加。"""
        assert Calculator.add(2, 3) == 5

    def test_add_floats(self) -> None:
        """测试两个浮点数相加。"""
        assert Calculator.add(2.5, 3.5) == 6.0

    def test_add_negative(self) -> None:
        """测试负数相加。"""
        assert Calculator.add(-5, 3) == -2

    def test_subtract_integers(self) -> None:
        """测试两个整数相减。"""
        assert Calculator.subtract(5, 3) == 2

    def test_subtract_result_negative(self) -> None:
        """测试减法结果为负数的情况。"""
        assert Calculator.subtract(3, 5) == -2

    def test_multiply_integers(self) -> None:
        """测试两个整数相乘。"""
        assert Calculator.multiply(3, 4) == 12

    def test_multiply_by_zero(self) -> None:
        """测试乘以零的情况。"""
        assert Calculator.multiply(5, 0) == 0

    def test_divide_integers(self) -> None:
        """测试两个整数相除。"""
        assert Calculator.divide(10, 2) == 5.0

    def test_divide_floats(self) -> None:
        """测试两个浮点数相除。"""
        result = Calculator.divide(7.5, 2.5)
        assert result == pytest.approx(3.0)

    def test_divide_by_zero_raises_error(self) -> None:
        """测试除以零时抛出 ValueError。"""
        with pytest.raises(ValueError, match="不能除以零"):
            Calculator.divide(10, 0)
