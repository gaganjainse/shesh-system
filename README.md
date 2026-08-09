# ⚙️ sesha-system

**Sesha Soma — system control MCP server.** Power profiles, GPU/MUX status, battery/RAM/CPU
telemetry, and backup triggers, exposed over stdio MCP for the agent.

- License: GPL-3.0
- Layer: Soma
- Provides: `mcp:system`, `power`, `gpu-mux`, `backup`, `maintenance`
- Target: MSI Sword 16 HX on CachyOS (but runs on any Linux with `powerprofilesctl`)
- Part of: [Sesha ecosystem](https://github.com/gaganjainse/sesha-ecosystem)

## Develop

```bash
uv sync --extra dev
uv run pytest -q
uv run ruff check .
uv run sesha-system-mcp
```

All hardware access is wrapped in `_run()` so tests mock subprocess and never touch the real GPU/battery.
