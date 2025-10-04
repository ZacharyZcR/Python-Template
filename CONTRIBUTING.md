# 贡献指南

感谢你考虑为本项目做出贡献！

## 开始之前

1. Fork 本仓库
2. 克隆你的 fork：`git clone https://github.com/your-username/python-template.git`
3. 创建功能分支：`git checkout -b feature/your-feature-name`

## 开发环境设置

```bash
# 创建虚拟环境
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 安装开发依赖
make install-dev

# 或手动安装
pip install -e ".[dev]"
pre-commit install
```

## 开发工作流

### 1. 编写代码

遵循项目的代码规范：
- 所有函数必须有类型注解
- 所有公共 API 必须有中文文档字符串
- 保持函数简洁（复杂度 ≤ 10）
- 遵循 PEP 8 规范

### 2. 运行质量检查

```bash
# 运行所有检查
make quality

# 或单独运行
make lint          # 代码检查
make format        # 代码格式化
make type-check    # 类型检查
make test          # 运行测试
```

### 3. 编写测试

- 新功能必须包含测试
- 测试覆盖率不得低于 80%
- 测试必须有清晰的中文文档字符串

```python
def test_new_feature(self) -> None:
    """测试新功能是否正常工作。"""
    result = new_function(input_data)
    assert result == expected_output
```

### 4. Commit 规范

本项目使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

```bash
# 设置 commit 模板（可选）
git config commit.template .gitmessage

# Commit 格式
<type>(<scope>): <subject>

# 示例
feat(core): 添加数据验证功能
fix(utils): 修复邮箱验证正则表达式
docs(readme): 更新安装说明
```

**Type 类型：**
- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档变更
- `style`: 代码格式（不影响功能）
- `refactor`: 重构
- `perf`: 性能优化
- `test`: 测试相关
- `build`: 构建系统变更
- `ci`: CI 配置变更
- `chore`: 其他杂项

### 5. 提交 Pull Request

1. 确保所有检查通过：`make quality`
2. 推送到你的 fork：`git push origin feature/your-feature-name`
3. 在 GitHub 上创建 Pull Request
4. 填写 PR 模板，说明你的改动
5. 等待 CI 检查通过
6. 等待代码审查

## 质量标准

你的 PR 必须满足以下条件才能被合并：

- ✅ 所有 CI 检查通过
- ✅ 代码覆盖率 ≥ 80%
- ✅ 文档覆盖率 ≥ 80%
- ✅ 代码复杂度 ≤ 10
- ✅ 类型检查通过
- ✅ 代码格式正确
- ✅ 至少一位维护者审核通过

## Pre-commit Hooks

提交时会自动运行以下检查：

1. **Ruff** - 代码格式化和 linting
2. **Mypy** - 类型检查
3. **标准检查** - 去除尾随空格、文件结尾换行等
4. **Interrogate** - 文档字符串覆盖率
5. **Gitlint** - Commit 信息格式

如果检查失败，commit 会被拒绝。修复问题后重新提交。

## 常见问题

### Pre-commit 检查失败怎么办？

```bash
# 查看失败原因
git commit -m "your message"

# 自动修复格式问题
make format

# 自动修复 lint 问题
make lint-fix

# 重新提交
git add .
git commit -m "your message"
```

### 如何跳过 Pre-commit 检查？

**不推荐！** 但如果确实需要：

```bash
git commit --no-verify -m "message"
```

注意：CI 仍然会运行所有检查，跳过只是延后了问题。

### 如何更新 Pre-commit Hooks？

```bash
pre-commit autoupdate
```

### 测试覆盖率不够怎么办？

```bash
# 查看覆盖率报告
make test

# 查看详细的 HTML 报告
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows

# 找到未覆盖的代码，添加测试
```

## 行为准则

- 尊重他人
- 建设性地提出批评
- 专注于技术问题，不针对个人
- 帮助新手成长

## 需要帮助？

- 查看 [README.md](README.md) 了解项目使用
- 在 [Issues](../../issues) 中提问
- 查看现有的 [Pull Requests](../../pulls) 学习

---

再次感谢你的贡献！🎉
