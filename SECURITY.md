# Security Policy

## Secrets

- 不要提交 API Key、`.env`、`~/.codex/auth.json` 或任何 OAuth Token。
- API Provider 只从进程环境读取密钥。
- 远程 API Provider 强制使用 HTTPS；明文 HTTP 只允许本机 loopback 服务。
- `codex-local` 只复用 Codex 自己管理的本机登录态，不读取认证文件。

## Trust boundary

Codex 会员登录只允许在用户控制的可信本机运行。不得将其部署为公共多用户翻译服务，也不得把本机 Codex 执行暴露给不可信输入或远程调用者。

Article text and previous translation candidates are untrusted data, including
embedded prompts, commands and role directives. Shared outer instructions forbid
following them, using tools, reading files/credentials, changing configuration,
making network requests or disclosing system context. Article text is preserved
as data, not removed or executed. OpenAI-compatible requests also carry this rule
in a system message; Qwen-MT uses `translation_options.domains` because its
single-message translation interface does not support system messages. Repair
requests retain these instructions. These are defenses, not a proof that a model
will resist every injection.

`codex-local` retains `--ephemeral`, `--sandbox read-only`,
`--ignore-user-config`, `--ignore-rules`, a temporary working directory and a
structured output schema. It invokes an argument list with no shell. A temporary
working directory is not a filesystem jail. Read-only restricts writes; it must
not be described as complete confidentiality isolation from unrelated local
files. The Codex process still manages its own authentication. PaperLocale never
reads, copies or modifies its authentication files.

Isolation investigation: local `codex-cli 0.154.0` was inspected using only
`--version` and `exec --help`, without starting a model session. Its exec help
provides sandbox modes but no filesystem read-root allowlist flag. Current
[official sandbox documentation](https://learn.chatgpt.com/docs/sandboxing)
describes permissions separately from working-directory selection. No new CLI
flags or version-dependent permission configuration are enabled here without
compatibility validation. For confidentiality from unrelated host files, run
Codex in a separately provisioned container/VM or OS account with only intended
data accessible; do not expose this provider as an untrusted document service.
No live adversarial-model or OS confinement test is claimed by the mocked tests.

`run_manifest.json` 与 `qa_report.json` 分别记录源 PDF 和候选 PDF 的
SHA-256。QA 后替换任一 PDF 会使 `accept` 失败；不要手工修改清单或报告来绕过
此门禁。

安全问题请通过 GitHub 私密漏洞报告渠道提交，不要在公开 Issue 中粘贴凭据或受版权保护的论文。
