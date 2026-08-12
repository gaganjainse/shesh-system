# shesh-system

**system control MCP** — Power profiles, GPU/MUX status, backup, maintenance.

- Layer: Soma (Soma)
- License: GPL-3.0
- Part of: [Shesh ecosystem](https://github.com/gaganjainse/shesh-ecosystem)

---
**Shesh Soma — system control MCP server.** Power profiles, GPU/MUX status, battery/RAM/CPU
telemetry, and backup triggers, exposed over stdio MCP for the agent.

- License: GPL-3.0
- Layer: Soma
- Provides: `mcp:system`, `power`, `gpu-mux`, `backup`, `maintenance`
- Target: MSI Sword 16 HX on CachyOS (but runs on any Linux with `powerprofilesctl`)
- Part of: [Shesh ecosystem](https://github.com/gaganjainse/shesh-ecosystem)

## Develop

```bash
uv sync --extra dev
uv run pytest -q
uv run ruff check .
uv run shesh-system-mcp
```

All hardware access is wrapped in `_run()` so tests mock subprocess and never touch the real GPU/battery.