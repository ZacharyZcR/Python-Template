"""输入验证工具模块。

本模块提供常用的验证函数，包含适当的错误处理。
"""

import re
from typing import Any


def is_valid_email(email: str) -> bool:
    """检查字符串是否为有效的电子邮件地址。

    Args:
        email: 要验证的电子邮件字符串

    Returns:
        如果邮箱有效返回 True，否则返回 False

    Examples:
        >>> is_valid_email("user@example.com")
        True
        >>> is_valid_email("invalid.email")
        False
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def is_positive(value: Any) -> bool:
    """检查值是否为正数。

    Args:
        value: 要检查的值

    Returns:
        如果值是正数返回 True，否则返回 False

    Examples:
        >>> is_positive(5)
        True
        >>> is_positive(-1)
        False
        >>> is_positive("not a number")
        False
    """
    try:
        return float(value) > 0
    except (ValueError, TypeError):
        return False


def is_not_empty(value: str) -> bool:
    """检查字符串在去除空白后是否非空。

    Args:
        value: 要检查的字符串

    Returns:
        如果字符串非空返回 True，否则返回 False

    Examples:
        >>> is_not_empty("hello")
        True
        >>> is_not_empty("   ")
        False
    """
    return bool(value.strip())
