# -*- coding: utf-8 -*-
"""Copia geos GeckoLib + texturas do JAR para docs/public/models."""

from __future__ import annotations

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JAR = ROOT / "clovercraft-0.4.0-neoforge-1.21.1.jar"
DEST = ROOT / "docs" / "public" / "models"

KEEP_CHAR_TEX = True
SKIP_TEX_MARKERS = ("_face_", "_glow")


def want(name: str) -> bool:
    n = name.replace("\\", "/")
    if not n.startswith("assets/clovercraft/"):
        return False
    rest = n[len("assets/clovercraft/") :]
    if rest.startswith("geo/character/") and rest.endswith(".geo.json"):
        stem = Path(rest).name
        if stem.startswith("squad_") or stem.startswith("player_"):
            return False
        if stem.endswith("_parts.geo.json"):
            return False
        return True
    if rest.startswith("geo/boss/") and rest.endswith(".geo.json"):
        return True
    if rest.startswith("textures/character/") and rest.endswith(".png"):
        if any(m in Path(rest).name for m in SKIP_TEX_MARKERS):
            return False
        return KEEP_CHAR_TEX
    if rest.startswith("textures/entity/boss/") and rest.endswith(".png"):
        if "_glow" in Path(rest).name:
            return False
        return True
    return False


def dest_path(name: str) -> Path:
    rest = name.replace("\\", "/")[len("assets/clovercraft/") :]
    return DEST / rest


def main() -> None:
    if not JAR.exists():
        raise SystemExit(f"JAR não encontrado: {JAR}")
    copied = 0
    total = 0
    with zipfile.ZipFile(JAR) as z:
        for info in z.infolist():
            if info.is_dir() or not want(info.filename):
                continue
            out = dest_path(info.filename)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(z.read(info.filename))
            copied += 1
            total += info.file_size
    mb = total / (1024 * 1024)
    print(f"Copied {copied} files ({mb:.1f} MB) -> {DEST}")


if __name__ == "__main__":
    main()
