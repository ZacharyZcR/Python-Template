"""计算器模块，演示良好的编码实践。

本模块提供基础算术运算，包含正确的类型注解、文档字符串和错误处理。
"""

from typing import Union

Number = Union[int, float]


class Calculator:
    """简单的计算器类，提供基础算术运算。

    本类演示了正确的文档编写、类型注解和简洁的代码组织。
    """

    @staticmethod
    def add(a: Number, b: Number) -> Number:
        """两数相加。

        Args:
            a: 第一个加数
            b: 第二个加数

        Returns:
            a 和 b 的和

        Examples:
            >>> Calculator.add(2, 3)
            5
            >>> Calculator.add(2.5, 3.5)
            6.0
        """
        return a + b

    @staticmethod
    def subtract(a: Number, b: Number) -> Number:
        """从 a 中减去 b。

        Args:
            a: 被减数
            b: 减数

        Returns:
            a 和 b 的差

        Examples:
            >>> Calculator.subtract(5, 3)
            2
        """
        return a - b

    @staticmethod
    def multiply(a: Number, b: Number) -> Number:
        """两数相乘。

        Args:
            a: 第一个乘数
            b: 第二个乘数

        Returns:
            a 和 b 的积

        Examples:
            >>> Calculator.multiply(3, 4)
            12
        """
        return a * b

    @staticmethod
    def divide(a: Number, b: Number) -> float:
        """a 除以 b。

        Args:
            a: 被除数
            b: 除数

        Returns:
            a 除以 b 的商

        Raises:
            ValueError: 当 b 为零时抛出

        Examples:
            >>> Calculator.divide(10, 2)
            5.0
        """
        if b == 0:
            raise ValueError("不能除以零")
        return a / b
