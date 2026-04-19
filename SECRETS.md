# Secrets Policy

**This repository is a key-free zone by design.** Credentials of any kind — API keys, tokens, passwords, private keys, `.env` assignments, connection strings with passwords, signed URLs with embedded auth — must **never** be committed to this repo.

This repo holds literature-survey and community-survey notes. None of those workflows require credentials in tracked files.

## Where secrets belong

The **only** sanctioned location is:

```
~/.claude/<service>_api_key
```

One key per file, key value on line 1, loaded at runtime by a launcher script (see `~/.claude/run-gemini-chat-mcp.sh`). Those files are gitignored in `~/.claude/.gitignore`.

## Enforcement at checkpoint

The `save-to-github` skill runs `~/.claude/tools/secret-scan.sh` over the union of (modified-vs-HEAD) and (untracked) files **before** staging. Any match aborts the commit until reviewed.

The scanner honors:

- **`.secret-scan-allowlist`** at the repo root — newline-separated paths to skip entirely.
- **Inline marker `secret-scan: example`** on the same line — for documentation that legitimately shows a pattern (this file is itself an example).

## If you encounter a secret in this repo

1. Stop. Do not commit.
2. Move the secret to `~/.claude/<service>_api_key`.
3. Rotate the key.
4. Scrub the file (or `git rm` it) before any push.

## Related

- `~/.claude/CLAUDE.md` § "Secrets Policy — One Sanctioned Home"
- `~/.claude/skills/save-to-github/SKILL.md`
- `~/.claude/tools/secret-scan.sh`
