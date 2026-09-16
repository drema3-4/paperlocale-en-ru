# PaperLocale 领域包指南

领域包把专业翻译规则与 PDF/Provider 核心分开。它只包含四个数据文件，不加载 Python 代码，因此可以独立审查和贡献。

## 目录合同

```text
your-domain/
├── manifest.json
├── prompt.txt
├── glossary.tsv
└── eval_cases.jsonl
```

`manifest.json` 必须声明唯一 `id`、语义化 `version`、`source_language` 和 `target_language`。运行语言必须与领域包一致，否则 PaperLocale 会拒绝翻译。

核心已测试 `en` → `zh-CN`、`en` → `ru` / `ru-RU`。内置领域包仍为中文；
俄语必须提供对应语言的提示、术语及案例，不能把中文包只改语言标签后使用。
标签统一大小写并接受下划线；`ru` 与 `ru-RU` 在语言匹配时等价，但领域包
原始文件哈希不变，不能借别名绕过断点身份校验。`run` 新建时默认 en→zh-CN，
俄语请指定 `--target-language ru`；续跑省略语言参数时沿用清单，显式冲突则拒绝。

公式、样式、标识符、数字、单位配对、缩写、URL/DOI 等硬合同与语言启发式独立。
中文保持既有长正文门禁；俄语只保守识别明显未译的长英语正文，不要求每个片段
都有西里尔字符，允许公式、人名、拉丁学名、软件名和混合术语。其他合法语言标签
采用通用保守策略：仍执行硬合同和术语检查，不套用中文规则，也不保证 Provider
或排版引擎支持。单位请保留标准 SI 符号；不猜测未登记俄语单位的等价性。
这些规则不替代人工语义复核或逐页视觉验收。

加载时会用固定文件名和四个文件的原始字节生成内容 SHA-256，并写入运行清单。
因此相同 `id/version` 下修改提示词、术语或案例也会改变身份，旧断点会明确拒绝续跑。

`prompt.txt` 只写本领域的消歧规则和表达要求。公式、数字、单位等通用完整性要求由核心合同统一注入，不需要复制。

`glossary.tsv` 必须恰好有四列：

```text
source\ttarget\trequired\tnote
```

- `source`：源语言术语；
- `target`：要求出现的目标术语；
- `required`：只能为 `true` 或 `false`；
- `note`：适用范围、易混词或必须保留的缩写。

当 `required=true` 且原文命中 `source` 时，译文必须包含 `target`。相同源术语不允许重复。

`eval_cases.jsonl` 每行只允许 `source` 和 `target` 两个字段。至少提供：正常术语、缩写、数值单位、容易混淆概念和公式占位案例。

## 创建与验证

复制内置包后修改：

```bash
cp -R src/paperlocale/packs/atmospheric-science /tmp/your-domain
paperlocale domain-check /tmp/your-domain
```

检查数据文件后，再用计划采用的真实 Provider 运行公开案例：

```bash
paperlocale provider-eval \
  --provider codex-local \
  --model gpt-5.6-sol \
  --reasoning-effort high \
  --domain /tmp/your-domain \
  --output tmp/your-domain-provider-eval.json
```

命令会原子写入每条原文、参考译文、候选译文、内容合同错误和逐字匹配结果。合同失败时报告仍会保留，但命令返回非零。逐字不匹配不等于语义错误；报告始终标记 `manual_semantic_review_required=true`，必须由理解该领域的人逐条判断术语、限定词、因果强度和专业含义。

提交新领域包时，还应在 `tests/` 增加一个加载测试，并说明术语来源与专业边界。不要提交受版权保护的整篇论文、完整译文或数据库导出。
