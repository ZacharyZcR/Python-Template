"""验证工具的单元测试。"""

import pytest

from src.utils.validators import is_not_empty, is_positive, is_valid_email


class TestEmailValidation:
    """邮箱验证测试套件。"""

    @pytest.mark.parametrize(
        "email",
        [
            "user@example.com",
            "test.user@example.com",
            "user+tag@example.co.uk",
            "123@test.com",
        ],
    )
    def test_valid_emails(self, email: str) -> None:
        """测试有效的邮箱能被识别。"""
        assert is_valid_email(email) is True

    @pytest.mark.parametrize(
        "email",
        [
            "invalid.email",
            "@example.com",
            "user@",
            "user@.com",
            "user name@example.com",
            "",
        ],
    )
    def test_invalid_emails(self, email: str) -> None:
        """测试无效的邮箱会被拒绝。"""
        assert is_valid_email(email) is False


class TestPositiveValidation:
    """正数验证测试套件。"""

    @pytest.mark.parametrize("value", [1, 5, 100, 0.1, 999.99])
    def test_positive_numbers(self, value: float) -> None:
        """测试正数能被识别。"""
        assert is_positive(value) is True

    @pytest.mark.parametrize("value", [-1, -0.1, 0, "not a number", None, []])
    def test_non_positive_values(self, value: object) -> None:
        """测试非正数会被拒绝。"""
        assert is_positive(value) is False


class TestNotEmptyValidation:
    """非空字符串验证测试套件。"""

    @pytest.mark.parametrize("value", ["hello", "a", "  text  "])
    def test_non_empty_strings(self, value: str) -> None:
        """测试非空字符串能被识别。"""
        assert is_not_empty(value) is True

    @pytest.mark.parametrize("value", ["", "   ", "\t", "\n"])
    def test_empty_strings(self, value: str) -> None:
        """测试空字符串会被拒绝。"""
        assert is_not_empty(value) is False
