"""Offline tests for maintenance/health/update tools."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from shesh_system import maintenance as m  # noqa: E402


def test_check_updates_no_updates(monkeypatch):
    monkeypatch.setattr(m.shutil, "which", lambda x: "/usr/bin/checkupdates")
    monkeypatch.setattr(m, "_run", lambda cmd, timeout=60: (2, ""))
    s = m.check_updates()
    assert s.available is False


def test_check_updates_lists_packages(monkeypatch):
    monkeypatch.setattr(m.shutil, "which", lambda x: "/usr/bin/checkupdates")
    monkeypatch.setattr(m, "_run", lambda cmd, timeout=60: (0, "linux 6.0\nvim 9.0"))
    s = m.check_updates()
    assert s.available is True and s.count == 2
    assert "never auto" in s.note.lower()


def test_cache_size_reports(monkeypatch, tmp_path):
    monkeypatch.setattr(m, "_run", lambda cmd, timeout=60: (0, "123\t/some/path"))
    sizes = m.cache_size()
    assert any(k.endswith("_mb") for k in sizes)


def test_clean_user_cache(monkeypatch):
    called = {}

    def fake_run(cmd, timeout=60):
        called["cmd"] = cmd
        return 0, ""

    monkeypatch.setattr(m, "_run", fake_run)
    m.clean_caches("user")
    assert "rm" in " ".join(called["cmd"])


def test_health_report_has_sections(monkeypatch, tmp_path):
    # Stub du and systemctl
    monkeypatch.setattr(m, "_run", lambda cmd, timeout=60: (0, "0 failed."))
    report = m.health_report()
    assert "failed_units" in report
    assert "caches" in report


def test_mcp_tools_exist():
    import shesh_system.server as srv  # noqa: F401
    # The tools are registered on the MCP instance; ensure functions exist.
    assert hasattr(srv, "check_system_updates")
    assert hasattr(srv, "clean_system_caches")
    assert hasattr(srv, "system_health")
