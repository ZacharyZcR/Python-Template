# Python 项目模板

一个高度工程化的 Python 项目模板，具备严格的质量控制和自动化 CI/CD 流程。

[![CI](https://github.com/ZacharyZcR/Python-Template/workflows/CI/badge.svg)](https://github.com/ZacharyZcR/Python-Template/actions)
[![codecov](https://codecov.io/gh/ZacharyZcR/Python-Template/branch/main/graph/badge.svg)](https://codecov.io/gh/ZacharyZcR/Python-Template)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

## 特性

**质量控制：**
- 🚀 **Ruff** - 极快的代码检查和格式化工具（替代 Black、Flake8、isort）
- 🔍 **Mypy** - 静态类型检查
- 📊 **Pytest** - 测试框架，要求 80%+ 覆盖率
- 📝 **Interrogate** - 文档字符串覆盖率强制检查（80%+）
- 🔬 **Radon** - 代码复杂度分析
- 🎯 **Pre-commit hooks** - 提交前自动质量检查

**CI/CD：**
- ✅ GitHub Actions 自动化测试（支持 Python 3.9-3.12）
- 🔄 Dependabot 自动依赖更新
- 📦 自动发布到 PyPI
- 📈 代码覆盖率报告（Codecov）

**开发体验：**
- 📋 Makefile 提供常用命令
- 🎨 现代化的 `pyproject.toml` 配置
- 📚 最佳实践示例代码
- 🔧 兼容 VS Code 和 PyCharm

## 快速开始

### 使用本模板

1. 在 GitHub 上点击 "Use this template"
2. 克隆你的新仓库
3. 更新 `pyproject.toml` 中的项目元数据
4. 安装依赖：

```bash
make install-dev
```

### 项目结构

```
python-template/
├── src/                    # 源代码
│   ├── core/              # 核心功能
│   └── utils/             # 工具函数
├── tests/                 # 测试
│   ├── unit/             # 单元测试
│   └── integration/      # 集成测试
├── .github/
│   └── workflows/        # CI/CD 流程
├── pyproject.toml        # 项目配置
├── .pre-commit-config.yaml
├── Makefile              # 常用命令
└── README.md
```

## 开发指南

### 环境设置

```bash
# 创建虚拟环境
python -m venv .venv
source .venv/bin/activate  # Windows 用户: .venv\Scripts\activate

# 安装开发依赖
make install-dev
```

### 常用命令

```bash
make help              # 显示所有可用命令
make test              # 运行测试（含覆盖率）
make lint              # 代码质量检查
make format            # 自动格式化代码
make quality           # 运行所有质量检查
make clean             # 清理构建产物
```

### 质量标准

本模板强制执行严格的质量标准：

| 检查项 | 工具 | 标准 |
|-------|------|----------|
| 代码风格 | Ruff | 符合 PEP 8，100 字符/行 |
| 类型注解 | Mypy | 所有函数必需 |
| 测试覆盖率 | Pytest | ≥ 80% |
| 文档覆盖率 | Interrogate | ≥ 80% |
| 复杂度 | Radon | 循环复杂度 ≤ 10 (B 级) |

### Pre-commit Hooks

Hooks 会在 `git commit` 时自动运行：

```bash
# 手动运行所有文件检查
make pre-commit

# 更新 hook 版本
pre-commit autoupdate
```

### 编写测试

```python
# tests/unit/test_example.py
import pytest
from src.core.calculator import Calculator

def test_addition() -> None:
    """测试加法功能是否正常工作。"""
    assert Calculator.add(2, 3) == 5
```

运行测试：
```bash
make test              # 含覆盖率
make test-fast         # 不含覆盖率
```

## CI/CD

### 持续集成

每次 push 和 PR 时会运行：
- ✅ 代码质量检查（lint、format、type）
- ✅ 多版本测试（Python 3.9-3.12）
- ✅ 覆盖率报告
- ✅ 构建验证

### 发布流程

创建版本标签时自动发布：

```bash
# 创建并推送标签
git tag v1.0.0
git push origin v1.0.0
```

触发流程：
1. 构建发布包
2. 创建 GitHub Release
3. 发布到 PyPI（需配置 `PYPI_API_TOKEN` secret）

## 配置说明

### pyproject.toml

所有工具配置集中在一个文件：
- 项目元数据
- 依赖管理
- Ruff 配置
- Mypy 配置
- Pytest 配置
- Coverage 配置
- Interrogate 配置

### 自定义配置

在 `pyproject.toml` 中调整质量阈值：

```toml
# 示例：降低覆盖率要求
[tool.pytest.ini_options]
addopts = ["--cov-fail-under=70"]

# 示例：调整行长度
[tool.ruff]
line-length = 120
```

## 工具说明

### 为什么选择 Ruff？

Ruff 比传统 Python linter 快 10-100 倍：
- **替代**：Black（格式化）+ Flake8（检查）+ isort（导入排序）
- **实现语言**：Rust（性能极快）
- **优势**：一个工具，一份配置，即时反馈

### 为什么这些覆盖率阈值？

- **80% 代码覆盖率**：能捕获大部分 bug，同时避免边际效益递减
- **80% 文档覆盖率**：确保公共 API 有文档
- **复杂度 ≤ 10**：保持函数可测试和可维护

## 故障排查

### Pre-commit Hook 失败

```bash
# 查看失败原因
git commit -m "message"

# 修复问题
make format        # 自动修复格式问题
make lint-fix      # 自动修复 lint 问题

# 重新提交
git commit -m "message"
```

### 类型检查错误

```bash
# 运行类型检查
make type-check

# 常见修复：添加类型注解
def my_function(x: int) -> str:
    return str(x)
```

### 测试失败

```bash
# 运行特定测试
pytest tests/unit/test_calculator.py::test_add

# 查看详细输出
pytest -vv

# 使用 print 调试
pytest -s
```

## 贡献指南

1. 创建功能分支：`git checkout -b feature-name`
2. 修改代码并提交（hooks 会自动运行）
3. 推送并创建 PR
4. CI 必须通过才能合并

详见 [CONTRIBUTING.md](CONTRIBUTING.md)

## 许可证

本模板使用 MIT 许可证发布，可自由使用！

---

**以质量为本，自信交付代码。**
