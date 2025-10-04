"""演示组件交互的集成测试。"""

from src.core.calculator import Calculator
from src.utils.validators import is_positive


class TestCalculatorWorkflow:
    """计算器与验证器的工作流测试。"""

    def test_divide_with_validation(self) -> None:
        """测试带正数验证的除法运算。"""
        dividend = 10
        divisor = 2

        # 验证输入为正数
        assert is_positive(dividend)
        assert is_positive(divisor)

        # 执行计算
        result = Calculator.divide(dividend, divisor)

        # 验证结果
        assert result == 5.0
        assert is_positive(result)

    def test_calculation_chain(self) -> None:
        """测试链式计算。"""
        # (10 + 5) * 2 / 3 = 10
        step1 = Calculator.add(10, 5)
        step2 = Calculator.multiply(step1, 2)
        result = Calculator.divide(step2, 3)

        assert result == 10.0
