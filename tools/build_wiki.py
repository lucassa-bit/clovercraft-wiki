# -*- coding: utf-8 -*-
"""Gera a wiki VitePress a partir do JAR descompilado do Clover Craft 0.4.0."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MODELS = DOCS / "public" / "models"
DECOMP = ROOT / "decompiled" / "dev" / "clovercraft"
LANG_EN = ROOT / "assets" / "clovercraft" / "lang" / "en_us.json"
LANG_PT = ROOT / "assets" / "clovercraft" / "lang" / "pt_br.json"
ACTIONS = ROOT / "clover" / "actions"
QUESTS = ROOT / "clover" / "quests"
KITS = DECOMP / "combat"

RANK_IDS = [
    "aspirant",
    "junior5",
    "junior3",
    "junior1",
    "inter3",
    "inter1",
    "senior3",
    "senior1",
    "vice_captain",
    "captain",
    "grand_knight",
    "wizard_king",
]
RANK_MERITS = [0, 5000, 12000, 20000, 30000, 40000, 55000, 75000, 100000, 130000, 170000, 220000]
FORM_LABELS = {
    "base": "Base",
    "ba": "Black Asta",
    "ba1": "Black Asta I",
    "ba2": "Black Asta II",
    "ba3": "Black Asta III",
    "du": "Devil Union",
    "dive": "Spirit Dive",
    "zephyr": "Complete Spirit Dive",
    "manazone": "Mana Zone",
    "kikongan": "Kikongan",
    "valkyrie": "Valkyrie Dress",
    "saint": "Saint Valkyrie",
    "hellfire": "Hellfire Incarnate",
    "hellfire2": "Hellfire Incarnate II",
    "hellfire3": "Hellfire Incarnate III",
    "leonum": "Exercitus Leonum",
    "zone": "Mana Zone",
    "lucius": "Lucius",
    "canis": "Unite: Canis",
    "fourfold": "Unite: Equinox",
    "awakened": "Licht Desperto",
    "demon": "Forma Demoníaca",
    "lucifero": "Lucifero (50%)",
    "devil": "Manifestação Demoníaca",
    "fiend": "Thunder Fiend",
    "black": "Black Lightning",
    "robe": "Magic Robe",
    "utopia": "Flower Princess Utopia",
    "megicula": "Megicula 50%",
    "megicula70": "Megicula 70%",
    "beelz": "Beelzebub",
    "seal": "Grand Seal",
    "labyrinth": "Ash Labyrinth",
    "fate": "Red Thread of Fate",
    "loom": "Fate's Loom",
    "kaleidoscope": "Kaleidoscope",
    "sea": "Mirror Sea",
}
CHAR_META = {
    "asta": {
        "magic": "Anti-Magia",
        "squad": "Touros Negros",
        "grimoire": "five_leaf_grimoire",
        "role": "Duelista corpo-a-corpo. Cancela magia, troca entre quatro espadas demoníacas e escala com transformações.",
        "color": "#c23b3b",
    },
    "yuno": {
        "magic": "Magia de Vento",
        "squad": "Alvorecer Dourado",
        "grimoire": "four_leaf_grimoire",
        "role": "Mago aéreo. Lâminas de vento, tornados e o espírito Sylph (Bell).",
        "color": "#7fe0b0",
    },
    "yami": {
        "magic": "Magia das Trevas",
        "squad": "Touros Negros (capitão)",
        "grimoire": "three_leaf_grimoire",
        "role": "Espadachim de trevas. Dimension Slash, Black Moon e o modo único Kikongan.",
        "color": "#5b3a8c",
    },
    "noelle": {
        "magic": "Magia de Água",
        "squad": "Touros Negros",
        "grimoire": "noelle_grimoire",
        "role": "Tanque/lanceira. Ninho do Dragão Marinho, Valkyrie Dress e forma santa.",
        "color": "#6ec8ff",
    },
    "mereoleona": {
        "magic": "Magia de Fogo",
        "squad": "Leão Carmesim",
        "grimoire": "mereoleona_grimoire",
        "role": "Brawler de fogo. Calidus Brachium, Hellfire Incarnate e o exército Exercitus Leonum.",
        "color": "#ff8a3a",
    },
    "julius": {
        "magic": "Magia do Tempo",
        "squad": "Rei Mago",
        "grimoire": "julius_grimoire",
        "role": "Controle de tempo. Chrono Stasis, Mana Zone e a forma Lucius.",
        "color": "#c9a227",
    },
    "nacht": {
        "magic": "Magia das Sombras",
        "squad": "Touros Negros (vice-capitão)",
        "grimoire": "nacht_grimoire",
        "role": "Assassino de sombras. Devils Canis/Equinox, Hunting Ground e teleporte por sombra.",
        "color": "#3d3558",
    },
    "licht": {
        "magic": "Magia de Espada / Luz",
        "squad": "Elfos / Olho do Sol da Meia-Noite",
        "grimoire": "licht_grimoire",
        "role": "Espadachim élfico. Origin Flash, espadas invocadas e forma demoníaca de quatro braços.",
        "color": "#f2e6a0",
    },
    "dante": {
        "magic": "Magia Corporal / Gravidade",
        "squad": "Tríade das Trevas (Spade)",
        "grimoire": "dante_grimoire",
        "role": "Bruiser de gravidade. Regeneração, Presence e singularidade de Lucifero.",
        "color": "#8b1e3f",
    },
    "luck": {
        "magic": "Magia de Relâmpago",
        "squad": "Touros Negros",
        "grimoire": "luck_grimoire",
        "role": "Assassino elétrico. Thunder Fiend, Keraunos e Black Lightning.",
        "color": "#ffe566",
    },
    "mimosa": {
        "magic": "Magia de Plantas",
        "squad": "Alvorecer Dourado",
        "grimoire": "mimosa_grimoire",
        "role": "Suporte/curandeira. Cestas de cura, canhões florais e Flower Princess Utopia.",
        "color": "#7bc47b",
    },
    "vanica": {
        "magic": "Magia de Sangue",
        "squad": "Tríade das Trevas (Spade)",
        "grimoire": "vanica_grimoire",
        "role": "Agressora de sangue. Red Beast, maldições de Megicula e manifestação a 70%.",
        "color": "#d02040",
    },
    "zenon": {
        "magic": "Magia de Ossos / Espacial",
        "squad": "Tríade das Trevas (Spade)",
        "grimoire": "zenon_grimoire",
        "role": "Controle espacial. Prisão de ossos, Mana Domination e coração demoníaco.",
        "color": "#cfd8dc",
    },
    "zora": {
        "magic": "Magia de Armadilha (Ash)",
        "squad": "Touros Negros",
        "grimoire": "zora_grimoire",
        "role": "Armadilheiro. Trap Counter, Grand Seal e Ash Labyrinth.",
        "color": "#6b5344",
    },
    "vanessa": {
        "magic": "Magia de Fios",
        "squad": "Touros Negros",
        "grimoire": "vanessa_grimoire",
        "role": "Suporte de destino. Red Thread of Fate, bonecas e tear do destino.",
        "color": "#e070a0",
    },
    "gauche": {
        "magic": "Magia de Espelho",
        "squad": "Touros Negros",
        "grimoire": "gauche_grimoire",
        "role": "Duelista de espelhos. Reflect Ray, Kaleidoscope e Mirror Sea.",
        "color": "#9ad0e8",
    },
}
SQUADS = [
    ("black_bulls", "Touros Negros", "Yami Sukehiro", 1, "+10% maestria"),
    ("golden_dawn", "Alvorecer Dourado", "William Vangeance", 3, "+5% mana, +5% méritos"),
    ("silver_eagle", "Águia Prateada", "Nozel Silva", 3, "+8% mana"),
    ("crimson_lion", "Leão Carmesim", "Fuegoleon Vermillion", 3, "+2 vida"),
    ("blue_rose", "Rosa Azul", "Charlotte Roselei", 2, "+10% regeneração"),
    ("green_mantis", "Louva-a-Deus Verde", "Jack the Ripper", 2, "+10% stamina"),
    ("coral_peacock", "Pavão Coral", "Dorothy Unsworth", 2, "+5% regen, +5% maestria"),
    ("aqua_deer", "Cervo Aqua", "Rill Boismortier", 2, "+2 vida"),
    ("purple_orca", "Orca Púrpura", "Gueldre Poizot", 1, "+10% méritos"),
]
RACES = [
    ("human", "Humano", "61%", "—", "—", "—", "+25% maestria", "—"),
    ("elf", "Elfo", "13%", "-2 vida", "+2% velocidade", "+10% mana", "+5% regen", "—"),
    ("dwarf", "Anão", "13%", "+4 vida", "-4% velocidade", "—", "—", "+10% resistência a knockback"),
    ("witch", "Bruxa", "13%", "—", "—", "—", "+25% regen, +5% maestria", "—"),
]
def load_json(path: Path) -> dict | list:
    return json.loads(path.read_text(encoding="utf-8"))


EN = load_json(LANG_EN)
PT = load_json(LANG_PT)


def t(key: str, fallback: str | None = None) -> str:
    if key in PT:
        return PT[key]
    if key in EN:
        return EN[key]
    return fallback if fallback is not None else key


def pretty(raw: str) -> str:
    name = raw.split("/")[-1]
    return name.replace("_", " ").title()


def skill_name(sid: str) -> str:
    tail = sid.split("/")[-1]
    for prefix in ("unlock.clovercraft.", "title.clovercraft."):
        val = t(prefix + tail, "")
        if val:
            return val
    en = EN.get("unlock.clovercraft." + tail)
    if en:
        return en
    return pretty(tail)


def parse_java_lists(text: str, const: str) -> list[list[str]]:
    m = re.search(rf"{const}\s*=\s*List\.of\((.*?)\)\s*;", text, re.S)
    if not m:
        return []
    groups = re.findall(r"List\.of\((.*?)\)", m.group(1), re.S)
    out = []
    for g in groups:
        items = re.findall(r'"([^"]+)"', g)
        out.append(items)
    return out


def parse_string_list(text: str, const: str) -> list[str]:
    m = re.search(rf"{const}\s*=\s*List\.of\((.*?)\)\s*;", text, re.S)
    if not m:
        return []
    return re.findall(r'"([^"]+)"', m.group(1))


def action_stats(action_id: str) -> dict:
    fname = action_id.replace("/", "__") + ".json"
    path = ACTIONS / fname
    if not path.exists():
        return {}
    data = load_json(path)
    hits = data.get("hits") or []
    dmg = max((h.get("damage") or 0) for h in hits) if hits else 0
    tags = data.get("tags") or []
    return {
        "duration": data.get("duration"),
        "damage": dmg,
        "tags": tags,
        "cancel_at": data.get("cancel_at"),
    }


def extract_kits() -> dict:
    kits = {}
    for path in KITS.glob("*Kit.java"):
        if path.name == "CharacterKit.java":
            continue
        text = path.read_text(encoding="utf-8")
        cid_m = re.search(r'return "([a-z]+)";', text)
        if not cid_m:
            continue
        cid = cid_m.group(1)
        kits[cid] = {
            "forms": parse_string_list(text, "FORMS") or parse_string_list(text, "FORM_NAMES"),
            "skills": parse_java_lists(text, "SKILLS"),
            "unlocks": parse_java_lists(text, "UNLOCKS"),
        }
    return kits


def extract_summons() -> list[dict]:
    units = []
    for path in (DECOMP / "summon" / "pool").glob("*Units.java"):
        text = path.read_text(encoding="utf-8")
        char_m = re.search(r'return "([a-z]+)";', text)
        character = char_m.group(1) if char_m else path.stem.replace("Units", "").lower()
        for m in re.finditer(
            r'new UnitDef\(\s*"([^"]+)"\s*,\s*"([^"]+)"\s*,.*?SummonRules\.Role\.([A-Z]+)\s*,\s*(true|false).*?,\s*(\d+)\s*,',
            text,
            re.S,
        ):
            uid, char, role, unique, tier = m.group(1), m.group(2), m.group(3), m.group(4) == "true", int(m.group(5))
            units.append(
                {
                    "id": uid,
                    "character": char,
                    "role": role.title(),
                    "unique": unique,
                    "tier": tier,
                    "name": t(f"summon.clovercraft.unit.{uid}", pretty(uid)),
                }
            )
        # factories auxiliares (Nacht.devil / Yami.bull)
        for m in re.finditer(
            r'(?:devil|bull)\(\s*"([^"]+)"\s*,\s*SummonRules\.Role\.([A-Z]+)\s*,\s*(\d+)',
            text,
        ):
            uid, role, tier = m.group(1), m.group(2), int(m.group(3))
            units.append(
                {
                    "id": uid,
                    "character": character,
                    "role": role.title(),
                    "unique": True,
                    "tier": tier,
                    "name": t(f"summon.clovercraft.unit.{uid}", pretty(uid)),
                }
            )
        if not any(u["character"] == character for u in units):
            for uid in re.findall(r'new UnitDef\(\s*"([^"]+)"', text):
                units.append(
                    {
                        "id": uid,
                        "character": character,
                        "role": "—",
                        "unique": True,
                        "tier": 1,
                        "name": t(f"summon.clovercraft.unit.{uid}", pretty(uid)),
                    }
                )
    # de-dup
    seen = set()
    out = []
    for u in units:
        if u["id"] in seen:
            continue
        seen.add(u["id"])
        out.append(u)
    return out


def extract_bosses() -> list[dict]:
    bosses = []
    roster = (DECOMP / "boss" / "BossRoster.java").read_text(encoding="utf-8")
    blocks = re.split(r"new BossSpec\(\s*\n\s*\"", roster)
    for block in blocks[1:]:
        bid = block.split('"', 1)[0]
        nums = re.findall(r"\b(\d+)\b", block)
        band = int(nums[1]) if len(nums) > 1 else 0
        moves = []
        for m in re.finditer(r'new BossSpec\.Move\(\s*"([^"]+)"', block):
            mid = m.group(1)
            moves.append({"id": mid, "name": t(f"boss.clovercraft.{bid}.{mid}", pretty(mid))})
        heal_m = re.search(r'new BossSpec\.Heal\(\s*"([^"]+)"', block)
        bosses.append(
            {
                "id": bid,
                "name": t(f"entity.clovercraft.boss_{bid}", pretty(bid)),
                "title": t(f"boss.clovercraft.{bid}.title", ""),
                "magic": t(f"boss.clovercraft.{bid}.magic", ""),
                "heal": t(f"boss.clovercraft.{bid}.heal", "") if heal_m else "",
                "band": band,
                "moves": moves,
                "devil": bid in {"zagred", "megicula", "lilith", "naamah", "beelzebub", "lucifero"},
            }
        )
    return bosses


def extract_relics() -> list[dict]:
    text = (DECOMP / "relic" / "Relic.java").read_text(encoding="utf-8")
    relics = []
    for m in re.finditer(
        r'([A-Z0-9_]+)\(\s*"([^"]+)"\s*,\s*Relic\.Rarity\.([A-Z]+)\s*,\s*Relic\.Canon\.([A-Z_]+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*List\.of\((.*?)\)\s*,\s*(true|false)',
        text,
        re.S,
    ):
        rid = m.group(2)
        bosses = re.findall(r'"([^"]+)"', m.group(7))
        relics.append(
            {
                "id": rid,
                "rarity": m.group(3).title(),
                "canon": "Canônico" if m.group(4) == "CANON_ITEM" else "Inspirado",
                "cooldown": int(m.group(5)),
                "min_band": int(m.group(6)),
                "bosses": bosses,
                "passive": m.group(8) == "true",
                "name": t(f"item.clovercraft.relic_{rid}", pretty(rid)),
                "lore": t(f"item.clovercraft.relic_{rid}.lore", ""),
                "burst": t(f"relic.clovercraft.{rid}.burst", ""),
                "burst_desc": t(f"relic.clovercraft.{rid}.burst.desc", ""),
                "passive_desc": t(f"relic.clovercraft.{rid}.passive", ""),
            }
        )
    return relics


def extract_quests() -> list[dict]:
    index = load_json(QUESTS / "index.json")
    out = []
    for fname in index:
        if fname in ("places.json", "index.json"):
            continue
        data = load_json(QUESTS / fname)
        for chain in data.get("chains", []):
            steps = []
            for s in chain.get("steps", []):
                steps.append(
                    {
                        "id": s.get("id"),
                        "type": s.get("type"),
                        "place": s.get("place"),
                        "min": s.get("min"),
                        "boss": s.get("boss"),
                        "reward": s.get("reward") or {},
                    }
                )
            out.append(
                {
                    "id": chain.get("id"),
                    "kind": chain.get("kind"),
                    "character": chain.get("character") or "",
                    "form": chain.get("form"),
                    "canon": chain.get("canon", ""),
                    "requires": chain.get("requires") or [],
                    "steps": steps,
                    "file": fname,
                }
            )
    return out


def extract_tree() -> list[dict]:
    text = (DECOMP / "progress" / "SkillTree.java").read_text(encoding="utf-8")
    nodes = []
    for kind, regex in (
        ("node", r'n\("([^"]+)",\s*([A-Z]),\s*(\d+),\s*(\d+),\s*SkillTree\.Stat\.([A-Z0-9_]+),\s*([0-9.]+)F\)'),
        ("keystone", r'key\("([^"]+)",\s*([A-Z]),\s*SkillTree\.Stat\.([A-Z0-9_]+),\s*([0-9.]+)F\)'),
        ("capstone", r'cap\("([^"]+)",\s*([A-Z]),\s*SkillTree\.Stat\.([A-Z0-9_]+),\s*([0-9.]+)F\)'),
    ):
        for m in re.finditer(regex, text):
            if kind == "node":
                nid, br, tier, ranks, stat, per = m.groups()
                nodes.append(
                    {
                        "id": nid,
                        "kind": "normal",
                        "branch": br,
                        "tier": int(tier),
                        "ranks": int(ranks),
                        "stat": stat,
                        "per": float(per),
                    }
                )
            else:
                nid, br, stat, per = m.groups()
                nodes.append(
                    {
                        "id": nid,
                        "kind": kind,
                        "branch": br,
                        "tier": 3 if kind == "keystone" else 5,
                        "ranks": 1,
                        "stat": stat,
                        "per": float(per),
                    }
                )
    extra = re.findall(
        r'NODES\.put\("([^"]+)",\s*new SkillTree\.Node\("\1",\s*([A-Z]),\s*(\d+),\s*(\d+),\s*(\d+),\s*SkillTree\.Stat\.([A-Z0-9_]+)',
        text,
    )
    for nid, br, tier, ranks, _cost, stat in extra:
        if not any(n["id"] == nid for n in nodes):
            nodes.append(
                {
                    "id": nid,
                    "kind": "special",
                    "branch": br,
                    "tier": int(tier),
                    "ranks": int(ranks),
                    "stat": stat,
                    "per": 0,
                }
            )
    return nodes


def md_escape(s: str) -> str:
    return s.replace("|", "\\|")


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


def attr_json(obj: object) -> str:
    return json.dumps(obj, ensure_ascii=False).replace("'", "&#39;")


def character_skins(cid: str) -> list[dict]:
    folder = MODELS / "textures" / "character"
    if not folder.exists():
        return []
    out = []
    for path in sorted(folder.glob(f"{cid}_*.png")):
        form = path.stem[len(cid) + 1 :]
        out.append(
            {
                "id": form,
                "label": form_label(form),
                "texture": f"/models/textures/character/{path.name}",
            }
        )
    out.sort(key=lambda s: (0 if s["id"] == "base" else 1, s["id"]))
    return out


def boss_catalog(bosses: list[dict]) -> list[dict]:
    items = []
    for b in bosses:
        geo = MODELS / "geo" / "boss" / f"{b['id']}.geo.json"
        tex = MODELS / "textures" / "entity" / "boss" / f"{b['id']}.png"
        if geo.exists() and tex.exists():
            items.append(
                {
                    "id": b["id"],
                    "label": b["name"],
                    "geo": f"/models/geo/boss/{b['id']}.geo.json",
                    "texture": f"/models/textures/entity/boss/{b['id']}.png",
                }
            )
    return items


def form_label(fid: str) -> str:
    if fid in FORM_LABELS:
        return FORM_LABELS[fid]
    hud = t(f"hud.clovercraft.form.{fid}", "")
    if hud:
        return hud.replace(" %s", "").strip()
    title = t(f"title.clovercraft.{fid}", "")
    return title.title() if title else pretty(fid)


def step_label(step: dict) -> str:
    kind = {
        "talk": "Conversar",
        "goto": "Ir até",
        "boss": "Chefe",
        "trial": "Provação",
    }.get(step["type"], step["type"] or "")
    extra = step.get("boss") or step.get("place") or step["id"]
    return f"{kind}: `{extra}` (força {step.get('min', 0)}+)"


def raw_kit_forms(cid: str) -> list[str]:
    """Names exposed to the client. Staged forms use FORM_NAMES, not only FORMS."""
    path = KITS / f"{cid.title()}Kit.java"
    text = path.read_text(encoding="utf-8")
    return parse_string_list(text, "FORM_NAMES") or parse_string_list(text, "FORMS")


def kit_form_group(cid: str, index: int) -> str:
    """Map the numeric kit group to a player-visible form.

    Some kits expose cosmetic/intermediate names that intentionally reuse one
    numeric action group. They must not shift the final group in the UI.
    """
    groups = {
        "asta": ("base", "ba1", "du"),
        "mereoleona": ("base", "hellfire", "leonum"),
    }.get(cid)
    if groups:
        return groups[min(index, len(groups) - 1)]
    forms = raw_kit_forms(cid)
    return forms[min(index, len(forms) - 1)] if forms else str(index)


def technical_rank(cid: str, sid: str, data: dict) -> int | None:
    """The Asta base kit uses the explicit fallback rules in Ranks.java."""
    if data.get("rank") is not None:
        return data["rank"]
    return {
        "slayer_slash": 1,
        "meteorite": 4,
        "dweller_slash": 3,
        "causality_break": 5,
        "black_divider": 7,
        "du_ultimate": 9,
    }.get(sid) if cid == "asta" else None


def technical_skill_rows(cid: str, kit: dict) -> list[dict]:
    """Action records used by a kit, without translating their effects into prose."""
    rows = []
    for group_index, group in enumerate(kit.get("skills") or []):
        # Kits select groups by numeric form (0 / 1 / 2). A staged visual form
        # such as ba2 remains in group 1.
        form = kit_form_group(cid, group_index)
        for slot, sid in enumerate(group, 1):
            aid = f"{cid}/skill/{sid}"
            path = ACTIONS / (aid.replace("/", "__") + ".json")
            data = load_json(path) if path.exists() else {}
            hits = data.get("hits") or []
            rows.append(
                {
                    "form": form,
                    "slot": slot,
                    "id": aid,
                    "file": f"clover/actions/{path.name}",
                    "duration": data.get("duration"),
                    "rank": technical_rank(cid, sid, data),
                    "hits": len(hits),
                    "max_damage": max((h.get("damage") or 0 for h in hits), default=0),
                    "tags": ", ".join(data.get("tags") or []) or "—",
                }
            )
    if cid == "asta":
        for form, sid in (("ba1–ba3", "black_divider"), ("du", "du_ultimate")):
            aid = f"asta/skill/{sid}"
            path = ACTIONS / (aid.replace("/", "__") + ".json")
            data = load_json(path) if path.exists() else {}
            hits = data.get("hits") or []
            rows.append({"form": form, "slot": 5, "id": aid, "file": f"clover/actions/{path.name}", "duration": data.get("duration"), "rank": technical_rank(cid, sid, data), "hits": len(hits), "max_damage": max((h.get("damage") or 0 for h in hits), default=0), "tags": ", ".join(data.get("tags") or []) or "—"})
    return rows


def fmt_number(value: float | int) -> str:
    return f"{value:.1f}".replace(".", ",")


def skill_damage(data: dict) -> str:
    """Show only damage numbers explicitly declared by the action JSON."""
    parts = []
    hits = [hit.get("damage") for hit in data.get("hits") or [] if (hit.get("damage") or 0) > 0]
    if hits:
        total = sum(hits)
        if len(hits) == 1:
            parts.append(f"{fmt_number(hits[0])} por golpe")
        elif len(set(hits)) == 1:
            parts.append(f"{fmt_number(hits[0])} × {len(hits)} golpes (até {fmt_number(total)})")
        else:
            parts.append(f"{len(hits)} golpes (até {fmt_number(total)})")

    labels = {
        "barrage": "rajada", "binding": "amarra", "dark_slash": "corte à distância",
        "fire_burst": "explosão", "fire_cone": "cone de fogo", "fire_line": "linha de fogo",
        "fire_paw": "garra", "gauche": "raio", "hawk": "investida", "jaws": "mordida",
        "julius": "efeito temporal", "line": "linha", "luck": "contra-ataque",
        "nacht": "golpe de sombra", "sea_dragon": "dragão", "shockwave": "onda de choque",
        "tornado": "tornado", "vanica": "golpe de sangue", "waterball": "orbe de água",
        "wind_blades": "lâmina de vento", "yami": "golpe sombrio", "zenon": "golpe espacial",
        "zora": "armadilha",
    }
    for event in data.get("events") or []:
        if not isinstance(event, dict) or not isinstance(event.get("damage"), (int, float)) or event["damage"] <= 0:
            continue
        count = event.get("count", event.get("passes", 1))
        count = count if isinstance(count, int) and count > 1 else 1
        label = labels.get(event.get("type"), "efeito")
        if count > 1:
            parts.append(f"{label}: {fmt_number(event['damage'])} × {count} (até {fmt_number(event['damage'] * count)})")
        else:
            parts.append(f"{label}: {fmt_number(event['damage'])}")
    return " · ".join(parts)


def skill_effect(data: dict) -> str:
    """A conservative player-facing summary derived only from action events."""
    events = [event for event in data.get("events") or [] if isinstance(event, dict)]
    kinds = {event.get("type") for event in events}
    pieces = []
    if data.get("lunges"):
        pieces.append("avança durante a ação")
    if data.get("hits"):
        pieces.append("atinge em combate direto")
    cancel = next((event for event in events if event.get("type") == "cancel_magic"), None)
    if cancel:
        radius = cancel.get("radius")
        pieces.append(f"cancela magia{f' em raio de {fmt_number(radius)}' if isinstance(radius, (int, float)) else ''}")
    if "anti_field" in kinds:
        pieces.append("cria campo anti-magia")
    if "black_hole" in kinds:
        pieces.append("puxa inimigos em uma zona")
    if "binding" in kinds:
        pieces.append("prende o alvo")
    if "blink" in kinds or "blink_behind" in kinds or "teleport" in kinds:
        pieces.append("se reposiciona")
    if "buff" in kinds:
        pieces.append("aplica um bônus temporário")
    if "mana_skin" in kinds or "water_shell" in kinds or "scutum" in kinds or "cocoon" in kinds:
        pieces.append("gera proteção")
    if "summon" in kinds or "comrades" in kinds:
        pieces.append("chama aliados")
    if "mimosa" in kinds:
        pieces.append("ativa magia de plantas")
    if not pieces:
        pieces.append("não declara dano direto; a action aplica um efeito de kit")
    return "; ".join(pieces).capitalize() + "."


def display_place(raw: str | None) -> str:
    labels = {
        "black_bulls_hideout": "Esconderijo dos Touros Negros",
        "royal_capital": "Capital Real",
        "grimoire_tower": "Torre dos Grimórios",
        "witches_forest": "Floresta das Bruxas",
        "seabed_temple": "Templo Submarino",
        "volcano_camp": "Acampamento do Vulcão",
        "spade_fortress": "Fortaleza de Spade",
        "faust_estate": "Propriedade Faust",
        "shadow_altar": "Altar das Sombras",
        "heart_sanctuary": "Santuário de Heart",
        "wind_shrine": "Santuário do Vento",
        "training_ring": "Arena de treino",
    }
    return labels.get(raw or "", pretty(raw or "local não declarado"))


def display_boss(raw: str | None, bosses: dict[str, str]) -> str:
    if not raw:
        return ""
    if raw.startswith("npc:"):
        cid = raw.split(":", 1)[1]
        return t("character.clovercraft." + cid, pretty(cid))
    if raw.startswith("foe:"):
        return "Onda de inimigos"
    return bosses.get(raw, pretty(raw))


def display_reward(reward: dict) -> str:
    labels = {"strength": "força", "merits": "méritos", "mastery": "maestria"}
    return " · ".join(f"{labels.get(key, key)} +{value}" for key, value in reward.items()) or "Sem recompensa declarada"


def display_unlock(name: str) -> str:
    """Correct the one mastery label whose language file overstates its effect."""
    if name == "forms_mastery":
        return "Domínio das formas (+15% de poder de forma)"
    return skill_name(name)


def write_technical_reference(kits: dict, summons: list, bosses: list, relics: list, quests: list, tree: list) -> None:
    """Write an evidence layer. It deliberately contains no canonical/editorial claims."""
    ref = DOCS / "referencia-tecnica"
    write(
        ref / "index.md",
        """# Referência técnica

Esta seção é a base verificável da wiki. Ela é regenerada por `tools/build_wiki.py` diretamente dos arquivos extraídos do **Clover Craft 0.4.0**.

Não há aqui classificação de papel, esquadrão canônico, interpretação de efeito, nem texto de lore. Cada tabela conserva IDs, números e arquivo de origem para que qualquer afirmação editorial possa ser conferida.

| Área | Fonte primária |
| --- | --- |
| Personagens e kits | `decompiled/dev/clovercraft/combat/*Kit.java` |
| Ações | `clover/actions/*.json` |
| Rank e maestria | `decompiled/dev/clovercraft/combat/Ranks.java` e `Mastery.java` |
| Jornadas | `clover/quests/*.json` |
| Invocações | `decompiled/dev/clovercraft/summon/pool/*Units.java` |

O servidor pode alterar números que dependem de configuração; esta referência descreve os valores presentes no JAR analisado.

- [Personagens e kits](/referencia-tecnica/personagens)
- [Habilidades](/referencia-tecnica/habilidades)
- [Ranks e maestria](/referencia-tecnica/ranks-e-maestria)
- [Mecânicas de kit](/referencia-tecnica/mecanicas)
- [Jornadas](/referencia-tecnica/jornadas)
- [Invocações](/referencia-tecnica/invocacoes)
- [Chefes e relíquias](/referencia-tecnica/chefes-e-reliquias)
- [Árvore](/referencia-tecnica/arvore)
""",
    )
    grimoire_src = (DECOMP / "registry" / "ModItems.java").read_text(encoding="utf-8")
    grimoire_by_char = {character: item for item, character in re.findall(r'ITEMS\.register\("([^"]+)", \(\) -> new GrimoireItem\("([^"]+)"\)', grimoire_src)}
    kit_rows = ["| ID | Grimório registrado | Formas expostas | Grupos de skills | Fonte |", "| --- | --- | --- | ---: | --- |"]
    for cid in kits:
        forms = raw_kit_forms(cid)
        kit_rows.append(f"| `{cid}` | `{grimoire_by_char.get(cid, '—')}` | {', '.join('`' + f + '`' for f in forms)} | {len(kits[cid].get('skills') or [])} | `combat/{cid.title()}Kit.java` |")
    write(ref / "personagens.md", "# Personagens e kits\n\nIDs e estrutura exatamente como o mod registra. Os nomes de forma são IDs internos; não são uma tradução editorial.\n\n" + "\n".join(kit_rows) + "\n\n**Observação sobre estágios:** Asta expõe `ba1`, `ba2` e `ba3`; Mereoleona expõe `hellfire`, `hellfire2` e `hellfire3`. Em ambos os casos o kit mantém três grupos de skills numéricos (base, forma 1, forma 2).")

    skill_md = ["# Habilidades", "", "Uma linha por ação chamada pelo kit. `dano máximo` é o maior campo `hits[].damage` daquele JSON; zero significa que o JSON não declara hit direto, não que a ação não tenha efeito.", "", "| Personagem | Forma/grupo | Slot | Action ID | Rank | Duração (ticks) | Hits | Dano máximo | Tags | Arquivo |", "| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | --- | --- |"]
    for cid, kit in kits.items():
        for row in technical_skill_rows(cid, kit):
            skill_md.append(f"| `{cid}` | `{row['form']}` | {row['slot']} | `{row['id']}` | {row['rank'] if row['rank'] is not None else '—'} | {row['duration'] if row['duration'] is not None else '—'} | {row['hits']} | {row['max_damage'] or '—'} | {md_escape(row['tags'])} | `{row['file']}` |")
    write(ref / "habilidades.md", "\n".join(skill_md))

    rank_rows = ["| Índice | ID | Méritos-base | Desbloqueios genéricos |", "| ---: | --- | ---: | --- |"]
    default_unlocks = [[], ["slayer_slash"], ["flight"], ["dweller", "dweller_slash"], ["meteorite"], ["destroyer", "causality_break"], ["slasher", "third_dash"], ["black_asta", "black_divider"], [], ["devil_union", "du_ultimate"], [], ["forms_mastery"]]
    for index, (rank_id, merits, unlocks) in enumerate(zip(RANK_IDS, RANK_MERITS, default_unlocks)):
        rank_rows.append(f"| {index} | `{rank_id}` | {merits} | {', '.join('`' + x + '`' for x in unlocks) or '—'} |")
    write(ref / "ranks-e-maestria.md", """# Ranks e maestria

## Rank

Tabela de `Ranks.LADDER`. Os limiares efetivos ainda passam por `merit_scale` e dificuldade do servidor.

""" + "\n".join(rank_rows) + """

## Constantes de maestria

| Campo | Valor no código |
| --- | --- |
| Nível máximo | 5 |
| XP acumulado por nível 0–5 | `0, 1000, 3000, 7000, 14000, 25000` |
| Multiplicador de dreno por nível 0–5 | `1.8, 1.45, 1.2, 1.0, 0.85, 0.6` |
| Multiplicador de poder por nível 0–5 | `0.86, 0.92, 0.97, 1.0, 1.05, 1.1` |
| Multiplicador de exaustão por nível 0–5 | `1.6, 1.4, 1.2, 1.0, 0.85, 0.7` |

## Portão de transformação

`formMasteryGate` (`FORM_GATE`) vem **ligado por padrão** no `BalanceConfig`. Nessa configuração, a primeira transformação exige maestria 5★ da forma base; cada transformação seguinte exige 5★ da forma anterior. A checagem usa o XP real salvo para a forma — o piso de nível concedido por rank não a substitui.

O servidor pode desligar `formMasteryGate`; só nesse caso a maestria deixa de bloquear a transformação. `masteryScale` também vem em `4.0`: alcançar 5★ pede `25.000 × escala × custo de dificuldade` XP da forma. Fontes: `config/BalanceConfig.java`, `combat/Mastery.java` e `combat/Ranks.java`.
""")

    mechanic_rows = ["# Mecânicas de kit", "", "Campos que alteram regras do kit, lidos das implementações `CharacterKit`. `true` só aparece quando a classe substitui o comportamento padrão.", "", "| Personagem | Guarda anti-magia | Escudo de mana | Formas de maestria | Fonte |", "| --- | --- | --- | --- | --- |"]
    for cid in kits:
        text = (KITS / f"{cid.title()}Kit.java").read_text(encoding="utf-8")
        anti = "sim" if re.search(r"boolean antiMagicGuard\(\)\s*\{\s*return true", text) else "não"
        shield = "sim" if re.search(r"boolean manaShield\(\)\s*\{\s*return true", text) else "não"
        mastery = re.search(r"masteryForms\(\)\s*\{\s*return List\.of\((.*?)\)", text, re.S)
        keys = ", ".join("`" + key + "`" for key in re.findall(r'"([^"]+)"', mastery.group(1))) if mastery else "formas expostas"
        mechanic_rows.append(f"| `{cid}` | {anti} | {shield} | {keys} | `combat/{cid.title()}Kit.java` |")
    mechanic_rows.extend(["", "## Regras comuns", "", "| Regra | Valor/fonte |", "| --- | --- |", "| Ranks de mérito | 12 degraus, índices `0`–`11`; `Ranks.LADDER` |", "| Força | máximo de 100; `strengthXpFor` usa topo 200000 e expoente 1,5 antes de escalas de configuração |", "| 3º dash | índice de rank 6 (`Sênior 3º`) |", "| Voo padrão do kit | índice de rank 2 (`Júnior 3º`), salvo kits que sobrescrevem `flightRank()` |", "| Transformação e 5★ | a checagem depende da configuração `FORM_GATE` |", "", "Fontes: `combat/CharacterKit.java`, `combat/Ranks.java` e `combat/Mastery.java`."])
    write(ref / "mecanicas.md", "\n".join(mechanic_rows))

    journey = ["# Jornadas", "", "Cadeias lidas dos JSONs. `boss` e `place` são IDs técnicos, preservados sem inferir nome ou local canônico.", "", "| Cadeia | Personagem | Forma | Etapa | Tipo | Place | Força mín. | Boss | Recompensa | Fonte |", "| --- | --- | ---: | --- | --- | --- | ---: | --- | --- | --- |"]
    for chain in quests:
        for step in chain["steps"]:
            reward = ", ".join(f"{key}={value}" for key, value in step["reward"].items()) or "—"
            journey.append(f"| `{chain['id']}` | `{chain['character'] or '—'}` | {chain['form'] if chain['form'] is not None else '—'} | `{step['id']}` | `{step['type']}` | `{step['place'] or '—'}` | {step['min'] or 0} | `{step['boss'] or '—'}` | {reward} | `clover/quests/{chain['file']}` |")
    write(ref / "jornadas.md", "\n".join(journey))

    unit_rows = ["# Invocações", "", "Unidades declaradas nos pools. Função, tier e exclusividade são campos extraídos; a coluna não descreve comportamento em linguagem editorial.", "", "| Personagem | Unidade | ID | Função | Tier | Única |", "| --- | --- | --- | --- | ---: | --- |"]
    for unit in summons:
        unit_rows.append(f"| `{unit['character']}` | {md_escape(unit['name'])} | `{unit['id']}` | `{unit['role']}` | {unit['tier']} | {'sim' if unit['unique'] else 'não'} |")
    write(ref / "invocacoes.md", "\n".join(unit_rows))

    boss_rows = ["# Chefes e relíquias", "", "Registros extraídos, sem descrição de lore. `band` é o campo numérico do `BossSpec` usado pelo mod.", "", "## Chefes", "", "| ID | Nome localizado | Band | Movimentos declarados | Fonte |", "| --- | --- | ---: | --- | --- |"]
    for boss in bosses:
        moves = ", ".join("`" + move["id"] + "`" for move in boss["moves"]) or "—"
        boss_rows.append(f"| `{boss['id']}` | {md_escape(boss['name'])} | {boss['band']} | {moves} | `boss/BossRoster.java` |")
    boss_rows.extend(["", "## Relíquias", "", "| ID | Raridade | Canônica | Cooldown | Band mín. | Passiva | Fonte |", "| --- | --- | --- | ---: | ---: | --- | --- |"])
    for relic in relics:
        boss_rows.append(f"| `{relic['id']}` | {relic['rarity']} | {relic['canon']} | {relic['cooldown']} | {relic['min_band']} | {'sim' if relic['passive'] else 'não'} | `relic/Relic.java` |")
    write(ref / "chefes-e-reliquias.md", "\n".join(boss_rows))

    tree_rows = ["# Árvore", "", "Nós estruturais extraídos da implementação da árvore. Os nomes permanecem IDs para evitar atribuir efeito sem a ação/fonte correspondente.", "", "| ID | Ramo | Tier | Ranks | Stat | Por rank | Fonte |", "| --- | --- | ---: | ---: | --- | --- |"]
    for node in tree:
        tree_rows.append(f"| `{node['id']}` | `{node['branch']}` | {node['tier']} | {node['ranks']} | `{node['stat']}` | {node['per']} | `progress/SkillTree.java` |")
    write(ref / "arvore.md", "\n".join(tree_rows))


def generate(kits: dict, summons: list, bosses: list, relics: list, quests: list, tree: list) -> None:
    chars = list(CHAR_META)
    character_links = {c: f"/personagens/{c}" for c in chars}

    # home
    write(
        DOCS / "index.md",
        """---
layout: home
hero:
  name: Clover Craft
  text: Wiki do mod 0.4.0
  tagline: Black Clover no Minecraft 1.21.1 (NeoForge) — 16 personagens, magia, chefes e o Submundo da Qliphoth.
  actions:
    - theme: brand
      text: Começar a jogar
      link: /guia/comecar
    - theme: alt
      text: Modelos 3D
      link: /galeria
features:
  - title: 16 magos jogáveis
    details: Cada um com grimório, formas, cinco skills por kit e subordinados.
  - title: Jornada de Cavaleiro Mágico
    details: Cerimônia na Torre, exame no Coliseu, esquadrões, ranks até Rei Mago.
  - title: Modelos 3D
    details: Gire os magos e chefes extraídos do GeckoLib — formas e skins no próprio viewer.
  - title: Mundo e Qliphoth
    details: Capital Real, esconderijo dos Touros Negros, masmorras, chefes globais e três camadas do Submundo.
---

<div class="home-note">

Projeto fã não oficial. **Black Clover** pertence a Yūki Tabata / Shueisha. O mod exige **NeoForge 21.1.259+**, **GeckoLib 4.9.3+** e **Photon 2.2.7+** (cliente).

</div>
""",
    )

    write(
        DOCS / "guia" / "comecar.md",
        """# Começar a jogar

Clover Craft começa com a cerimônia do grimório e termina no loop de força, mérito, maestria e jornadas. Esta é a rota prática para a primeira sessão; depois, use as fichas de [personagens](/personagens/) para escolher um kit e acompanhar sua evolução.

> Os passos abaixo descrevem o padrão do 0.4.0. Um servidor pode mudar custos, dificuldade e o portão de maestria nas configurações.

## Requisitos

| Peça | Versão |
| --- | --- |
| Minecraft | 1.21.1 |
| NeoForge | 21.1.259 ou superior |
| GeckoLib | 4.9.3+ |
| Photon | 2.2.7+ (cliente — partículas e pós-FX) |
| O mod | `clovercraft-0.4.0-neoforge-1.21.1.jar` |

## Os primeiros minutos

1. Entre no mundo. **Padre Orsi** fala no overlay (não há NPC no chão) e um marcador aponta a Torre.
2. Chegue a uns 10 blocos do altar. Abre a **Cerimônia do Grimório**: grimório, sangue ([raça](/sistemas/racas)) e berço. É uma vez só.
3. Use o grimório (botão direito) para **vincular**. O mago não troca depois — Grimoire Scroll rerola o grimório; um admin também pode resetar.
4. Complete as **Lições de Hage** no HUD — ou digite `/tutorial skip`.
5. Em **sobrevivência**, digite `/exam`. O jogo te leva ao Coliseu e spawna um examinador (clone NPC de outro mago).
6. Escolha um [esquadrão](/sistemas/squads). O fluxo do exame entrega a **vassoura mágica**; use `J` para voar.

Asta usa o voo próprio liberado após o exame; a vassoura é recusada por ele. Regras de voo: [Combate](/guia/combate#voo).

## Lições de Hage

O tutorial não é conversa com villagers. São cinco ações, nessa ordem:

| # | Lição | O que fazer | Default |
| --- | --- | --- | --- |
| 1 | Combo | Acerte um combo completo (três hits) | clique esquerdo |
| 2 | Dash | Dash | `Alt` esquerdo |
| 3 | Guarda | Segure a guarda | `F` |
| 4 | Heavy | Segure o ataque e solte | clique esquerdo (segurar) |
| 5 | Magia | Lance uma skill | `Z` (`X` `C` `V` ao lado) |

Ao terminar, aparece o convite clicável para `/exam`. Lista completa de teclas: [Controles](/guia/controles).

## Depois do exame

Você já é Cavaleiro Mágico. O resto do jogo é ficar mais forte.

Aperte **K** para abrir a **Jornada**. É o hub: força, rank, maestria, diário de quests, missões, história do reino e árvore. Três coisas diferentes saem daí:

| O quê | Para quê | Como abrir |
| --- | --- | --- |
| **Missões** | Caçadas e defesas, várias diárias. Pagam **méritos** (rank) | `/missions`, quadro de madeira, ou o botão na Jornada |
| **Diário** | Cadeia da **transformação** do seu mago (viajar, trial, boss) | botão de quests na Jornada |
| **História** | Capítulos do reino (Saussey, masmorra, Capital) | `/story` — não é a tela da Jornada |

Combate e jornadas também sobem **força**. A cadeia e os requisitos variam por personagem; veja a seção **Jornada** na ficha de cada [personagem](/personagens/). No padrão do mod, a primeira transformação exige 5★ da Base e as seguintes exigem 5★ da forma anterior.

O primeiro marco comum de voo é **Júnior 3º** (12.000 méritos). A vassoura permite voo a magos com mana; Asta segue a exceção do próprio kit.

Detalhe de força, méritos, maestria e ranks: [Progressão](/guia/progressao).

## Se travar

| Situação | O que fazer |
| --- | --- |
| A roleta não abriu | Vá até a Torre e digite `/roulette` |
| `/exam` recusa | Grimório vinculado, cerimônia feita, modo sobrevivência, chão plano à frente |
| “Treine e volte” | Espere ~2 min e tente de novo |
| Personagem já pego no servidor | Claims — outro jogador vinculou aquele mago |
| Pular o tutorial | `/tutorial skip` |

Admin pode avançar a temporada (`/clover season wipe`): no próximo login todo mundo recomeça na Torre, sem mago. Roleta e claims são configuráveis no servidor.
""",
    )

    write(
        DOCS / "guia" / "controles.md",
        """# Controles

Rebind em **Opções → Controles → Clover Craft**. Abaixo estão os defaults do 0.4.0, definidos em `ClientInput.java`; um servidor não altera essas teclas.

Como se luta com essas teclas: [Combate](/guia/combate).

## Clique vanilla

O mod não troca os botões do Minecraft.

| Botão | Uso |
| --- | --- |
| Clique esquerdo (toque) | Combo |
| Clique esquerdo (segurar) | Heavy / charge |
| Clique direito | Usar item — é assim que você **vincula o grimório** |

## Combate

| Tecla | Ação |
| --- | --- |
| `Z` `X` `C` `V` | Habilidades 1–4 |
| `R` | Skill 5 da forma atual — em geral, a ação de maior impacto do kit |
| `B` | Transformar / avançar forma |
| `Alt` esquerdo | Dash nas quatro direções |
| `F` | Guarda (segurar) ou parry (toque no timing) |
| Botão do meio | Travar alvo (lock-on) |
| `Y` | Meditar (segurar, fora de combate) |

## Movimento e câmera

| Tecla | Ação |
| --- | --- |
| `J` | Voar (vassoura, espada, asas, espírito) |
| `O` | Câmera no ombro |

## Asta e espadachins

| Tecla | Ação |
| --- | --- |
| `H` | Sacar / guardar a arma |
| `G` | Trocar espada (Asta) |

## Menus e subordinados

| Tecla | Ação |
| --- | --- |
| `K` | Jornada (hub de força, rank, quests, missões, árvore) |
| `N` | Subordinado: toque invoca, segurar abre ordens |
| `U` | Forçar despertar dos subordinados |

`N` também está em **minimizar o painel de quest**. As duas ações usam a mesma tecla — rebind uma delas se o summon ou o HUD não responder.

As fichas de [personagens](/personagens/) mostram os cinco slots, seus efeitos e os requisitos relevantes de cada kit.
""",
    )

    write(
        DOCS / "guia" / "combate.md",
        """# Combate

O kit de combate combina combo, heavy, guarda, dash e cinco slots de magia. Transformar (`B`) pode trocar o conjunto de actions disponível.

Teclas: [Controles](/guia/controles). O que destrava cada forma: [Progressão](/guia/progressao).

## Como se luta

1. **Toque no clique esquerdo** — combo de 3–5 hits no chão. No ar, um golpe só. Depois de um dash, o clique vira **dash slash**.
2. **Segure o clique** — heavy / charge. Soltar no timing faz a versão mais forte (*release*).
3. **Segure `F`** — guarda no arco da frente. Gasta **stamina**. Stamina no zero = **guard break**: você fica aberto.
4. **Toque no `F` no timing** — **parry**: atordoa quem bateu e enche a barra de mana.
5. **`Z` `X` `C` `V` `R`** — os cinco slots de magia. Consulte a ficha do seu [personagem](/personagens/) para entender o efeito de cada um.
6. **Botão do meio** — lock-on. Câmera e skills seguem o alvo. Use no exame e em chefe.

Ordem prática: lock-on → combo/guarda → magia. Não fique parado enchendo skill.

## Duas barras

Há dois recursos, e eles não são a mesma coisa.

**Stamina** alimenta a guarda. Acabou = guard break.

**Mana** (a barra do grimório) alimenta skills e transformação. Ela é recuperada por combate e meditação; kits com escudo de mana têm regras próprias. Sem recurso suficiente, a action pode ser recusada.

**Asta** não tem mana: a barra dele é **Anti-Magia**. A guarda **anula magia**. Hits **selam** o alvo por alguns instantes — o selado não lança.

**Meditar (`Y`)** — segurar parado, fora de luta. Recupera mana / anti-magia mais rápido.

**Dash (`Alt`)** — quatro direções, i-frames curtos. O 3º dash só abre no rank Sênior 3º.

## Voo

**Voo (`J`)** — a regra base de voo do kit começa no rank Júnior 3º. Alguns kits sobrescrevem essa regra. A vassoura exige mana e não funciona para Asta; depois do exame, Asta usa o voo próprio. A implementação também recusa voo durante estados inválidos, como exaustão, queda forçada ou uma action cinemática.

## Transformar

Cada kit tem suas próprias formas. Asta e Mereoleona têm estágios internos na primeira transformação; eles não ganham um grupo de skills novo a cada estágio. A ficha de cada personagem separa essas formas de modo jogável.

Rank, jornada, recurso e maestria podem limitar uma transformação. `FORM_GATE` vem ligado na configuração padrão: 5★ da Base abre a primeira forma e 5★ da forma atual abre a próxima. Por isso, não trate força 30, força 80 ou barra 70 como regra universal — nem suponha que o servidor desligou o portão de maestria.

Sair da forma devolve o kit base. Barra no zero pode aplicar `exhausted`; o comportamento final depende da action e da configuração.

## Clash

Dois heavies se encontram: mini-game de círculos (Perfect / Good / Miss). O vencedor atravessa com dano extra. Empate empurra os dois.

Chefes e mobs também clasham. Errar contra boss dói mais.

## PvE e PvP

Dano a mobs e a jogadores escala separado. A [árvore](/sistemas/arvore) rende menos em PvP. Ultimates de forma têm multiplicador próprio contra jogador.

O dano final pode combinar força, forma, rank, árvore, PvE/PvP e configuração do servidor. As fichas de personagem mostram o dano-base quando ele existe; esse número não é o dano final exibido em jogo.
""",
    )

    rank_unlock = {
        2: "Voo do kit",
        6: "3º dash",
        11: "+15% de poder de forma",
    }
    rank_rows = []
    for i, rid in enumerate(RANK_IDS):
        merits = f"{RANK_MERITS[i]:,}".replace(",", ".")
        rank_rows.append(
            f"| {i} | {t('rank.clovercraft.' + rid)} | {merits} | {rank_unlock.get(i, '—')} |"
        )
    write(
        DOCS / "guia" / "progressao.md",
        """# Progressão

A primeira hora (Torre, tutorial, `/exam`) está em [Começar](/guia/comecar). Aqui é o que sobe depois — e as regras do exame.

Quatro sistemas aparecem juntos, mas não são a mesma moeda: **força**, **méritos** (rank), **maestria** e pontos da [árvore](/sistemas/arvore). Entender como eles se combinam evita investir no atributo errado.

## Força (1–100)

É o poder bruto. Sobe com inimigos, chefes e recompensas de quest.

A curva é exponencial: os últimos níveis demoram bem mais. Cada 9 de força equivalem a um “tier” de rank para HP e dano.

Não existe um limiar universal de transformação: cada cadeia de jornada tem seus próprios mínimos de força. Consulte a seção **Jornada** na ficha do seu [personagem](/personagens/).

## Méritos e rank

Méritos de guerra sobem o rank (Aspirante → Rei Mago). Algumas habilidades e transformações também pedem um rank mínimo; a ficha de cada personagem mostra os desbloqueios relevantes.

Limiares do mod (o servidor pode multiplicar por dificuldade):

| # | Rank | Méritos | O que muda para todo mundo |
| --- | --- | ---: | --- |
"""
        + "\n".join(rank_rows)
        + """

O restante dos desbloqueios é por personagem e por action. A tabela de habilidades mostra o rank efetivo que cada JSON declara — incluindo as exceções do kit do Asta.

## Maestria: requisito real das formas

Cada forma tem no máximo 5 níveis. A maestria ganha XP em combate, jornadas e treinos — e é um requisito de transformação no padrão do mod: `formMasteryGate`/`FORM_GATE` vem **ligado**.

Com a configuração padrão, faça nesta ordem:

1. Leve a **forma base a 5★** para liberar a primeira transformação.
2. Conclua a jornada, tenha a força/rank exigidos e o recurso pedido pelo kit.
3. Leve a **forma atual a 5★** antes de tentar a próxima.

O servidor pode desligar esse portão, mas não é seguro presumir isso. A maestria também melhora a forma: no código, 5★ reduz o multiplicador de dreno de `1,8` para `0,6`, eleva o poder de `0,86` para `1,10` e reduz exaustão. O limiar-base de 5★ é 25.000 XP, multiplicado por `masteryScale` (padrão 4,0) e pela dificuldade. Importante: o piso visual concedido por rank não substitui o XP de maestria que o portão testa.

## Árvore

Pontos vêm de força, cadeias concluídas, firsts de chefe e rank. Veja os efeitos e prioridades de cada ramo em [Árvore](/sistemas/arvore).

## Exame de Cavaleiro Mágico

`/exam` teleporta você ao Coliseu. Não existe NPC parado para conversar.

Precisa: grimório vinculado, cerimônia feita, ainda não passou, **sobrevivência**, chão plano. Se a estrutura ainda carrega, espera “Preparando o Coliseu…”.

1. Countdown de ~3 s. O examinador é um **NPC clone** de outro mago jogável, dificuldade Normal.
2. Duelo de **90 s**. O primeiro a cair a **25% de vida** perde — ninguém morre de verdade. No tempo, ganha quem tiver mais % de HP.
3. Nota 0–100. Em seguida você **escolhe qualquer um dos 9 [esquadrões](/sistemas/squads)**; a nota só muda a ordem dos cards.
4. O capitão entrega a **vassoura** (`J`). Se fechar a tela sem escolher, `/exam` reabre a escolha.

Exame anulado (logout, longe demais, sem chão): tente de novo. “Treine e volte” é cooldown de ~2 min.

## O que farmar

Três filas diferentes — não misture:

| Fila | O que é | Onde |
| --- | --- | --- |
| **Missões** | Caçadas, defesas, duelos do quadro. Várias diárias. Méritos | `/missions` ou o quadro |
| **Diário do mago** | Cadeia da transformação (viajar, trial, boss) | Jornada (`K`) → quests |
| **História** | Capítulos do reino: Saussey, masmorra antiga, Capital, ruínas élficas | `/story` |

Treinos globais (`train_spar` na força 8, vulcão da Mereoleona na 25…) repetem e pagam maestria. Lista: [Quests](/sistemas/quests).

## Reroll e temporada

**Race Scroll** (8% em chefe mundial) rerola a [raça](/sistemas/racas). **Grimoire Scroll** (3%) rerola o mago.

Admin: `/clover season wipe`. No próximo login todo cavaleiro recomeça na Torre, sem vínculo. Não é troca de personagem — é reset do servidor.
""",
    )

    # characters index
    cards = []
    for c in chars:
        meta = CHAR_META[c]
        cards.append(
            {
                "id": c,
                "name": t('character.clovercraft.' + c, pretty(c)),
                "magic": meta['magic'],
                "squad": meta['squad'],
                "role": meta['role'].split('. ', 1)[0],
                "color": meta['color'],
                "group": "bulls" if "Touros Negros" in meta['squad'] else "spade" if "Spade" in meta['squad'] else "other",
                "geo": f"/models/geo/character/{c}.geo.json",
                "texture": next((s['texture'] for s in character_skins(c) if s['id'] == 'base'), ''),
            }
        )
    write(
        DOCS / "personagens" / "index.md",
        f"""---
aside: false
---

# Personagens

16 magos jogáveis. O grimório vincula você a um deles — não há troca sem reroll/admin/temporada.

Compare magia, papel e esquadrão canônico. Abra uma ficha para explorar as formas e o kit.

<CharacterRoster :characters='{attr_json(cards)}' />

Cada página tem o **modelo 3D** GeckoLib (gire e troque a forma). Visão geral: [Galeria](/galeria).

Skins: todos têm `own` e `classic`. Asta também tem `spade`. Troca: `/skin <id>`.
""",
    )

    summons_by_char = defaultdict(list)
    for u in summons:
        summons_by_char[u["character"]].append(u)
    quests_by_char = defaultdict(list)
    for q in quests:
        if q["character"]:
            quests_by_char[q["character"]].append(q)
    boss_names = {boss["id"]: boss["name"] for boss in bosses}

    for c in chars:
        meta = CHAR_META[c]
        kit = kits.get(c, {"forms": [], "skills": [], "unlocks": []})
        name = t("character.clovercraft." + c, pretty(c))
        grim = t("item.clovercraft." + meta["grimoire"], meta["grimoire"])

        form_list = raw_kit_forms(c) or kit["forms"] or ["base"]

        skill_cards = []
        for row in technical_skill_rows(c, kit):
            action_path = ACTIONS / Path(row["file"]).name
            action = load_json(action_path) if action_path.exists() else {}
            group_form = row["form"]
            group_label = form_label(group_form)
            if c == "asta" and group_form in {"ba1", "ba1–ba3"}:
                group_form = "ba1"
                group_label = "Black Asta I–III"
            if c == "mereoleona" and group_form == "hellfire":
                group_label = "Hellfire I–III"
            skill_cards.append({
                "form": group_form, "formLabel": group_label, "slot": row["slot"],
                "name": skill_name(row["id"].split("/skill/", 1)[1]),
                "duration": f"{row['duration'] / 20:.1f} s" if row["duration"] else "não declarada",
                "damage": skill_damage(action),
                "mastery": "Base: ×1,00" if group_form == "base" else "Forma: 0★ ×0,86 · 3★ ×1,00 · 5★ ×1,10",
                "effect": skill_effect(action),
                "rank": t("rank.clovercraft." + RANK_IDS[row["rank"]], RANK_IDS[row["rank"]]) if row["rank"] is not None and row["rank"] < len(RANK_IDS) else "",
            })

        unlocks = kit.get("unlocks") or []
        if not unlocks:
            default_u = [
                [],
                ["slayer_slash"],
                ["flight"],
                ["dweller", "dweller_slash"],
                ["meteorite"],
                ["destroyer", "causality_break"],
                ["slasher", "third_dash"],
                ["black_asta", "black_divider"],
                [],
                ["devil_union", "du_ultimate"],
                [],
                ["forms_mastery"],
            ]
            unlocks = default_u
        unlock_cards = []
        for i, group in enumerate(unlocks):
            if not group:
                continue
            rname = t("rank.clovercraft." + RANK_IDS[i], RANK_IDS[i]) if i < len(RANK_IDS) else str(i)
            unlock_cards.append({"rank": rname, "entries": [display_unlock(x) for x in group]})

        journey_cards = []
        for q in quests_by_char.get(c, []):
            steps = []
            for step_index, s in enumerate(q["steps"], 1):
                kind = {"talk": "Converse", "goto": "Vá até", "boss": "Derrote", "trial": "Conclua a provação"}.get(s["type"], s["type"])
                steps.append({"label": f"Etapa {step_index}", "kind": kind, "place": display_place(s.get("place")), "minimum": s.get("min") or 0, "boss": display_boss(s.get("boss"), boss_names), "reward": display_reward(s["reward"])})
            journey_name = form_label(kit_form_group(c, q.get("form") or 0)) if q.get("kind") == "form" else pretty(q["id"])
            journey_cards.append({"name": journey_name, "requires": ["Jornada anterior"] if q["requires"] else [], "steps": steps})

        su = summons_by_char.get(c, [])
        summon_cards = [{"name": u["name"], "role": u["role"], "tier": u["tier"], "unique": u["unique"]} for u in su]
        skins = character_skins(c)
        geo_path = MODELS / "geo" / "character" / f"{c}.geo.json"
        # Keep model choices in gameplay order; alternate outfits follow the forms.
        skins.sort(key=lambda s: form_list.index(s['id']) if s['id'] in form_list else len(form_list))
        progression = []
        for form in (1, 2):
            chain = next((q for q in quests_by_char.get(c, []) if q['kind'] == 'form' and q['form'] == form), None)
            if chain and chain['steps']:
                start = chain['steps'][0].get('min') or 0
                finish = max(s.get('min') or 0 for s in chain['steps'])
                previous = "Base" if form == 1 else "forma anterior"
                progression.append(f"Jornada: força {start}–{finish}. Configuração padrão: 5★ da {previous}.")
        profile = {
            "name": name, "magic": meta['magic'], "squad": meta['squad'],
            "role": meta['role'].split('. ', 1)[0],
            "description": meta['role'].split('. ', 1)[-1],
            "color": meta['color'], "grimoire": grim,
            "forms": [form_label(f) for f in form_list],
            "geo": f"/models/geo/character/{c}.geo.json" if geo_path.exists() else '',
            "skins": skins, "progression": progression,
            "peculiar": "Troque entre 4 espadas com G; a guarda anula magia e os hits selam o alvo." if c == 'asta' else '',
        }
        write(
            DOCS / "personagens" / f"{c}.md",
            f"""---
aside: false
---

# {name}

<CharacterProfile v-bind='{attr_json(profile)}' />

<CharacterDetails v-bind='{attr_json({"skills": skill_cards, "unlocks": unlock_cards, "journeys": journey_cards, "summons": summon_cards})}' />

Os valores mostrados descrevem o comportamento padrão do mod. Configurações do servidor podem ajustar custos, duração e dano.
""",
        )

    gallery = []
    for c in chars:
        skins = character_skins(c)
        geo = MODELS / "geo" / "character" / f"{c}.geo.json"
        if geo.exists() and skins:
            gallery.append(
                {
                    "id": c,
                    "label": t("character.clovercraft." + c, pretty(c)),
                    "geo": f"/models/geo/character/{c}.geo.json",
                    "texture": skins[0]["texture"],
                }
            )
    if gallery:
        write(
            DOCS / "galeria.md",
            f"""# Galeria 3D

Modelos GeckoLib extraídos do JAR. Arraste para orbitar, scroll para zoom. Nas [páginas de personagem](/personagens/) dá para trocar forma/skin; aqui o seletor percorre os 16 magos na pose padrão.

<ClientOnly>
<GeoViewer catalog='{attr_json(gallery)}' :height="520" />
</ClientOnly>

Chefes: viewer na página de [Chefes](/mundo/bosses).
""",
        )

    # world
    places = load_json(QUESTS / "places.json").get("places", [])
    site_notes = {
        "wind_shrine": ("Montanhas, colinas, prados e windswept hills", "Ponto de jornada ligado às rotas de vento."),
        "witches_forest": ("Floresta escura, pântano ou floresta", "Ponto de jornada da Floresta das Bruxas."),
        "heart_sanctuary": ("Flower forest, cherry grove, prado ou floresta", "Ponto de jornada do Reino Heart."),
        "seabed_temple": ("Manguezal, pântano ou costa pedregosa", "Ponto de jornada costeiro; usa o template Heart Spring no JAR."),
        "volcano_camp": ("Badlands, deserto ou savana", "Acampamento de treino e jornadas de fogo."),
        "spade_fortress": ("Biomas nevados, taiga, ice spikes ou grove", "Fortaleza usada nas jornadas finais de Spade."),
        "training_ring": ("Planície, sunflower plains ou prado", "Arena para provas e treino."),
        "faust_estate": ("Floresta escura, taiga antiga ou pântano", "Ponto de jornada da propriedade Faust."),
        "shadow_altar": ("Floresta escura, pântano ou taiga antiga", "Altar e provas de sombra."),
        "gravito_zone": ("Montanhas, colinas de cascalho ou picos rochosos", "Área de gravidade e rochas."),
        "forgotten_obelisk": ("Ponto de site definido pelo servidor", "Obelisco usado por etapas específicas."),
    }
    site_rows = ["| Destino | Terreno preferido | Para que serve |", "| --- | --- | --- |"]
    for p in places:
        if p.get("kind") == "site":
            terrain, purpose = site_notes.get(p["id"], ("Bioma definido pelo site", "Destino de jornada."))
            site_rows.append(f"| {display_place(p['id'])} | {terrain} | {purpose} |")

    write(
        DOCS / "mundo" / "index.md",
        f"""# Mundo

O mundo é a rota prática da progressão: cerimônia e exame no começo, destinos da Jornada para formas e chefes, eventos em grupo e a descida ao [Submundo](/mundo/underworld). Abra a **Jornada** (`K`) para receber o destino da sua própria cadeia.

## Para onde ir

| Momento | Vá para | O que fazer lá |
| --- | --- | --- |
| Começo | Vila de Hage e Torre dos Grimórios | Faça a cerimônia e vincule o grimório. |
| Após o vínculo | Coliseu do Exame | Use `/exam` para iniciar o duelo de admissão; não é uma missão de NPC parada no mapa. |
| Evolução | Capital, Esconderijo e destinos da Jornada | Complete conversas, provas e chefes exigidos pelas transformações. |
| Grupo / endgame | Evento de chefe e Submundo | Enfrente conteúdo escalável, obtenha relíquias e abra camadas da Qliphoth. |

## Estruturas permanentes

| Estrutura | Função prática |
| --- | --- |
| Vila de Hage / Torre dos Grimórios | Início e cerimônia do grimório. |
| Capital Real | Destino recorrente de conversas e jornadas. |
| Esconderijo dos Touros Negros | Destino de cadeias dos Touros, incluindo partes da rota do Asta. |
| Salão de esquadrão | Estrutura de esquadrão no mundo. |
| Coliseu do Exame | Arena do `/exam`. |
| Vila Saussey | Estrutura da história do reino. |
| Masmorra antiga e Ruínas élficas | Estruturas usadas por rotas de história e jornadas. |

## Como funcionam os destinos de jornada

Sites não têm uma coordenada global fixa. Quando uma jornada precisa de um deles, o servidor escolhe um ponto a partir de quem iniciou a etapa, normalmente entre **300 e 1.500 blocos**, tenta respeitar o terreno preferido e guarda aquela posição para o servidor. O template só é construído quando alguém se aproxima a cerca de **112 blocos**. Portanto, siga o marcador da Jornada — procurar uma coordenada publicada por outro servidor não é confiável.

{chr(10).join(site_rows)}

## Ameaças e proteção

No overworld, os biome modifiers colocam facções como bandidos, Diamond, Olho do Sol da Meia-Noite, bruxas, elfos, paladinos, bestas, Spade e rogue knights. As waves da Jornada usam tiers `A`, `B`, `C` e `S`; elites rendem mais méritos.

Capital, esconderijos e outras estruturas protegidas limitam grief de vanilla e usam postos de guarda para preservar NPCs. Para eventos, faixas de força e recompensas, veja [Chefes](/mundo/bosses).
""",
    )

    write(
        DOCS / "mundo" / "underworld.md",
        """# Submundo (Qliphoth)

O Submundo é o ciclo de endgame: três dimensões separadas, só com demônios, mais pressão de inimigos e progressão travada por camadas. Não entre como se fosse uma nova caverna comum: leve cura, rota de retorno e o grupo pronto para uma luta de domínio.

## Antes de atravessar

1. Encontre o santuário/altar da Qliphoth. `/qliphoth` ou `/submundo` mostra o altar, a próxima camada e o que falta para o selo.
2. Coloque no altar os ingredientes do **selo** da próxima camada e realize o ritual. As camadas precisam ser abertas em ordem.
3. Entre pelo portão do altar. Se a camada ainda não estiver liberada para você, o portão recusa a passagem e indica o requisito faltante.
4. Leve um **Return Sigil**. Ele só funciona dentro do Submundo, exige 40 ticks de canalização e é consumido ao levar você de volta.

## Progressão das camadas

| Camada | Dimensão | O que muda | Domínios e chefes |
| ---: | --- | --- | --- |
| 1 · Rim | `clovercraft:underworld_1` | Primeiro contato com imps, low/mid devils, gazers e tendrils. | Zagred — domínio em `(0, -260)`, raio 30. |
| 2 · Depths | `clovercraft:underworld_2` | Sobem mid/high devils, curse wraiths e twin fiends. | Megicula `(280, 0)`, raio 32; Lilith e Nahamah `(-280, 0)`, raio 34. |
| 3 · Throne | `clovercraft:underworld_3` | Mid/high devils e devil hosts; é a camada mais severa. | Belzebu `(0, -270)`, raio 34; Lucifero `(0, 290)`, raio 48. |

Cada domínio é uma arena reservada: o chefe nasce no dais, a luta tem estado próprio por jogador e o domínio entra em descanso após ser concluído. As relíquias e os chefes correspondentes estão em [Chefes](/mundo/bosses).

## Por que vale o risco

Por padrão, as três camadas multiplicam por **3×** os ganhos de força, méritos e maestria. Elas também aumentam a presença de demônios para cada jogador (`capMultiplier` padrão 2,5). Asta, Dante, Vanica, Zenon e Nacht recebem **+5% no dano PvE** enquanto estão no Submundo.

`mana_essence`, raízes e blocos de mana negra sustentam rituais e crafts de endgame. O gerador cria ilhas e santuários; cair no vazio não é uma rota rápida de volta — o Void Guard devolve você ao ponto de chegada.

> Os multiplicadores, vida dos chefes e quantidade de inimigos podem mudar conforme a configuração do servidor. Use estes valores como referência de progressão.
""",
    )

    boss_rows = ["| Chefe | Título | Magia | Força (band) | Tipo |", "| --- | --- | --- | ---: | --- |"]
    for b in bosses:
        kind = "Demônio" if b["devil"] else "Mundo / quest"
        boss_rows.append(
            f"| [{md_escape(b['name'])}](/mundo/bosses#{b['id']}) | {md_escape(b['title'])} | {md_escape(b['magic'])} | {b['band']} | {kind} |"
        )

    boss_pages = []
    for b in bosses:
        moves = ", ".join(f"`{m['name']}`" for m in b["moves"]) or "—"
        boss_pages.append(
            f"## {b['name']} {{#{b['id']}}}\n\n"
            f"- Título: **{b['title'] or '—'}**\n"
            f"- Magia: {b['magic'] or '—'}\n"
            f"- Cura de fase: {b['heal'] or '—'}\n"
            f"- Força recomendada (band): **{b['band']}**\n"
            f"- Moves: {moves}\n"
        )

    write(
        DOCS / "mundo" / "bosses.md",
        """# Chefes

<BossRoster />

## Como uma luta de chefe funciona

Chefes alternam ataques, momentos de pressão e uma janela de recuperação. A luta não é uma sequência de dano livre: golpes pesados, invocações, controle de arena e mobilidade pedem respostas diferentes.

- **Leia a arena.** Zonas no chão, cargas, portais e invocações costumam anunciar o próximo perigo. Dash é uma ferramenta de sobrevivência, não apenas de aproximação.
- **Interrompa a recuperação.** Quando o chefe abre uma janela de cura, concentre dano e controle. É o melhor momento para usar ultimate em grupo.
- **Use stagger e clash.** Guarda, parry e o choque entre ataques ajudam a criar uma abertura; errar contra um chefe deixa menos margem do que contra mobs comuns.
- **Ajuste a equipe.** Um jogador chama o padrão, outro limpa invocações/zonas e os demais evitam gastar tudo ao mesmo tempo. O lock-on facilita acompanhar alvos com teleporte ou voo.

## Eventos do mundo

Eventos selecionam chefes de acordo com a força média dos jogadores online. Os inimigos do Qliphoth pertencem à progressão do Submundo e não entram nos eventos normais do overworld.

| Força média do grupo | Exemplos de encontro |
| --- | --- |
| Abaixo de 40 | Sally, Rades, Heath Graice, Dominante Code |
| 40–61 | Fana, Vetto, Rainha das Bruxas, Ratri |
| 62–84 | Rainha das Bruxas, Vetto, Rhya, Gaderois |
| 85+ | Rainha das Bruxas, Vetto, Damnatio Kira |

As recompensas podem incluir força, méritos, uma relíquia ligada ao chefe e títulos. Servidores podem ajustar vida, dano, frequência de eventos e recompensas.
""",
    )

    # systems
    write(
        DOCS / "sistemas" / "index.md",
        """---
aside: false
---

# Sistemas

<SystemsHub />
""",
    )
    squad_rows = ["| Esquadrão | Capitão | Prestígio | Bônus |", "| --- | --- | ---: | --- |"]
    for key, nome, cap, pres, bonus in SQUADS:
        squad_rows.append(f"| {nome} (`{key}`) | {cap} | {pres} | {bonus} |")
    write(
        DOCS / "sistemas" / "squads.md",
        f"""# Esquadrões

Escolha um esquadrão ao passar no [exame](/guia/progressao). É uma decisão de identidade e bônus leve — não bloqueia personagem, forma ou skill. Prestígio alto (3) marca o “top squad” do cânone, não um multiplicador obrigatório de poder.

{chr(10).join(squad_rows)}

O manto (`SquadRobe`) pinta a capa/roupa na cor do esquadrão. Não é guilda de jogadores — para isso veja [guildas](/sistemas/guildas).
""",
    )

    write(
        DOCS / "sistemas" / "guildas.md",
        """# Guildas de jogadores

Times de até **12** pessoas, prefixo dourado no chat, sem fogo amigo.

```
/guilda criar <nome>     # 3–20 caracteres
/guilda convite <jogador>
/guilda aceitar          # convite vale 2 minutos (2400 ticks)
/guilda sair
```

O líder é o criador; se sair, o próximo membro online herda. Time vazio é dissolvido. Nome vira team `cg_<slug>` no scoreboard.
""",
    )

    race_rows = ["| Raça | Peso na roleta | Vida | Velocidade | Mana | Regen / maestria | Extra |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for row in RACES:
        race_rows.append("| " + " | ".join(row[1:]) + " |")
    write(
        DOCS / "sistemas" / "racas.md",
        f"""# Raças

Sorteadas na cerimônia (pesos somam 100). A raça ajusta atributos passivos desde o começo; ela não troca seu grimório nem suas formas. Reroll com **Race Scroll**.

{chr(10).join(race_rows)}

Humanos são o default e os mais comuns — compensados com maestria mais rápida. Elfos são frágeis e rápidos. Anões tankam. Bruxas regeneram mana.
""",
    )

    branch_name = {"A": "Ataque", "L": "Vida", "R": "Resistência", "S": "Invocação", "M": "Mana"}
    tree_md = []
    for br, title in branch_name.items():
        tree_md.append(f"### {title}\n")
        tree_md.append("| Nó | Tipo | Tier | Ranks | Stat | Por rank |")
        tree_md.append("| --- | --- | ---: | ---: | --- | --- |")
        for n in tree:
            if n["branch"] != br:
                continue
            label = t(f"tree.clovercraft.node.{n['id']}", pretty(n["id"]))
            stat = t(f"tree.clovercraft.stat.{n['stat'].lower()}", n["stat"])
            tree_md.append(
                f"| {md_escape(label)} (`{n['id']}`) | {n['kind']} | {n['tier']} | {n['ranks']} | {md_escape(stat)} | {n['per']} |"
            )
        tree_md.append("")
    write(
        DOCS / "sistemas" / "arvore.md",
        f"""# Árvore de skills

Cinco ramos para escolher uma direção de build: dano, sobrevivência, resistência, subordinados ou recurso. Pontos = `(força - 1) + cadeias concluídas + firsts de chefe (cap) + rank de mérito`, limitados por config.

Tiers abrem com pontos já gastos no ramo: **0 / 6 / 15 / 27 / 42**. Keystone (tier 3, custo 3) muda o playstyle. Capstone (tier 5, custo 12) é **exclusivo** — só um por ramo.

Custo de ramo completo ≈ 60 pontos. Crítico da árvore: **×1.5**. Overload (capstone de mana) encarece skills ≥ 20 de custo em 25% e as fortalece. Commander (capstone de summon) corta 12% do seu dano pessoal.

Em PvP os bônus da árvore são atenuados (`TREE_PVP`). Caps de dano/redução/HP existem nas configs de summon/tree.

{chr(10).join(tree_md)}
""",
    )

    q_idx = ["| Cadeia | Tipo | Personagem | Etapas | Força da 1ª |", "| --- | --- | --- | ---: | ---: |"]
    for q in quests:
        q_idx.append(
            f"| `{q['id']}` | {q['kind']} | {q['character'] or 'todos'} | {len(q['steps'])} | {q['steps'][0]['min'] if q['steps'] else 0} |"
        )
    write(
        DOCS / "sistemas" / "quests.md",
        f"""# Quests

Abra a Jornada (`K`) para acompanhar o objetivo ativo. As cadeias são definidas em JSON: `form` libera transformação, `training` é repetível e `secret` aparece sob uma condição de revelação.

Etapas: `talk`, `goto`, `boss`, `trial` (survive / duel / dodge / nohit). Trials spawnam waves `id@tier*n`.

{chr(10).join(q_idx)}

Treinos globais (qualquer personagem): Ki no ringue, acampamento do vulcão da Mereoleona, e outros em `training.json`.

Segredos em `secrets.json` — exemplos: caçar Ladros à noite, trial sem hit, wanderer. Pagam título e às vezes troféu.

Painel: tecla Journey. `/story` reabre a jornada. `/missions` o quadro de missões diárias (`mission_board`).
""",
    )

    su_rows = ["| Unidade | Personagem | Função | Tier |", "| --- | --- | --- | ---: |"]
    for u in summons:
        owner = t("character.clovercraft." + u["character"], u["character"])
        su_rows.append(f"| {u['name']} | {owner} | {u['role']} | {u['tier']} |")
    write(
        DOCS / "sistemas" / "invocacoes.md",
        f"""# Subordinados (summons)

Cada mago tem um pool próprio (`*Units.java`). Invocação é uma build: pegue **Pact** na árvore (`sum_pact`), escolha a unidade e use ordens para posicioná-la. Toque na tecla Summon chama; segurar abre ordens; Awaken força o próximo estágio.

Unidades têm estágios 1–3, habilidades por estágio, custo de mana e tempo de permanência. Unique = um só (Liebe, Bell, Undine…). Não-únicas empilham até o cap da config.

{chr(10).join(su_rows)}

Capstone **Commander**: subordinados mais fortes, você causa 12% a menos. **Side by Side**: bônus se a unidade luta a ≤ 8 blocos.
""",
    )

    rar_order = {"Rare": 0, "Epic": 1, "Legendary": 2, "Mythic": 3}
    rel_rows = ["| Relíquia | Raridade | Tipo | Band mín. | CD (s) | Origem |", "| --- | --- | --- | ---: | ---: | --- |"]
    for r in sorted(relics, key=lambda x: (rar_order.get(x["rarity"], 9), x["name"])):
        src = ", ".join(r["bosses"]) or "baú / campeão"
        rel_rows.append(
            f"| **{md_escape(r['name'])}** | {r['rarity']} | {r['canon']}{' · passiva' if r['passive'] else ''} | {r['min_band']} | {r['cooldown']} | {src} |"
        )
    rel_detail = []
    for r in relics:
        bits = [f"## {r['name']}\n", f"- `{r['id']}` · {r['rarity']} · {r['canon']}"]
        if r["lore"]:
            bits.append(f"- {r['lore']}")
        if r["burst"]:
            bits.append(f"- Burst **{r['burst']}**: {r['burst_desc']}")
        if r["passive_desc"]:
            bits.append(f"- Passiva: {r['passive_desc']}")
        rel_detail.append("\n".join(bits) + "\n")
    write(
        DOCS / "sistemas" / "reliquias.md",
        f"""# Relíquias

Relíquias são o equipamento de efeito especial: escolha entre um burst ativo, uma passiva ou os dois. Itens `relic_*` vão de Rare a Mythic; ativas disparam um **burst** (cooldown em segundos × 20 ticks), passivas ficam sempre ligadas. A primeira vitória contra um chefe tende a render a relíquia assinatura dele.

{chr(10).join(rel_rows)}

{chr(10).join(rel_detail)}
""",
    )

    write(
        DOCS / "sistemas" / "itens.md",
        f"""# Itens, blocos e crafts

## Grimórios

Um por personagem (ver páginas em [Personagens](/personagens/)). Botão direito vincula se você ainda não tem mago. O grimório vinculado não sai do inventário: ele é a identidade do cavaleiro, não uma arma descartável.

## Espadas de Asta

`slayer_sword`, `dweller_sword`, `destroyer_sword`, `slasher_sword`.

## Utilitários

| Item | Craft | Uso |
| --- | --- | --- |
| Vassoura mágica | gravetos + trigo + lápis | Voo casual fora do kit |
| Mission Board | 3 papéis + 3 tábuas | Missões diárias |
| Altar da Qliphoth | ouro, livro, essência, diamante, obsidiana | Ritual do Submundo |
| Return Sigil | 4 essências + pérola + ouro → 2 | Volta do Submundo |
| Race Scroll | drop de world boss (8%) | Rerola raça |
| Grimoire Scroll | drop de world boss (3%) | Rerola grimório |
| Scroll of Renewal | — | Reseta a árvore do personagem |

## Blocos

| Bloco | Notas |
| --- | --- |
| `mission_board` | madeira, 2.0 hardness |
| `guard_post` | invisível, inquebrável, defende NPCs |
| `qliphoth_altar` / `qliphoth_gate` | entrada do Submundo |
| `qliphoth_root`, `dark_qliphoth_root`, `black_mana` | terreno da Qliphoth |

## Efeitos

`hex`, `sealed` (magia selada por anti-magia), `bound` (trevas), `comrademons`.
""",
    )

    write(
        DOCS / "sistemas" / "comandos.md",
        """# Comandos

## Jogador

| Comando | Função |
| --- | --- |
| `/exam` | Inicia o exame no Coliseu |
| `/missions` | Abre missões |
| `/story` | Jornada / quest tracker |
| `/tutorial skip` | Pula o tutorial |
| `/skin <id>` | Skin do seu mago (`own`, `classic`, Asta também `spade`) |
| `/roulette` | Reabre a roleta se ainda não rolou |
| `/music` | Liga/desliga a trilha |
| `/guilda ...` | Ver [guildas](/sistemas/guildas) |

## Admin (`/clover`)

Requer permissão de operador.

| Subcomando | Função |
| --- | --- |
| `character set <id> [players]` | Define o mago |
| `character clear [players]` | Remove o mago |
| `skin <id> [players]` | Skin |
| `form <nome> [players]` | Força forma (`ba`, `dive`, `kikongan`…) |
| `rank <n> [players]` | Rank 0–11 |
| `strength <n> [players]` | Força 1–100 |
| `merits add <n> [players]` | Méritos |
| `mastery <form> <nível> [players]` | Maestria 0–5 (`all`, `base`, formas) |
| `meter <0–100> [players]` | Barra de mana/anti-magia |
| `autosheathe <true/false>` | Embainhar automático |
| `clash` | Força clash com o alvo próximo |
| `arena [mages] [raio]` | Constrói arena de teste com Test Mages |
| `season wipe` | Nova temporada (zera jornadas) |
| `difficulty <nome>` | Dificuldade do mod |
| `potencial unlock/lock` / `potential ...` | Maxa ou zera o jogador (cheat de kit completo) |
| `exam reset/pass [players]` | Controle do exame |
| `roulette <modo>` | Força modo da roleta |
| `npc spawn/duel/clear/results` | NPCs de treino e duelo |
| `story ...` | Debug da jornada |

Chefes: `/boss` (summon/clear) — ver código `BossCommand`. Subordinados: `/summon` do mod (`SummonCommand`).
""",
    )

    write(
        DOCS / "sobre.md",
        """# Sobre esta wiki

Gerada a partir do JAR **Clover Craft 0.4.0** para NeoForge 1.21.1.

1. O JAR foi aberto (é um ZIP) para lang, datapack, quests e ~1100 actions JSON.
2. As 1216 classes `dev.clovercraft.*` foram descompiladas com **Vineflower 1.12.0**.
          3. Kits, ranks, bosses, relíquias, summons e a árvore saíram desses fontes.
4. Modelos 3D: geos GeckoLib + texturas em `docs/public/models/`, renderizados no browser com Three.js.

Números de dano nas páginas de personagem são o hit cru do JSON — o jogo ainda aplica força, forma, esquadrão, árvore, PvP e config do servidor.

Projeto fã. Black Clover © Yūki Tabata / Shueisha.

Trilha: Kevin MacLeod (incompetech.com), CC BY 4.0 — ver `CREDITS-MUSIC.txt` no JAR.
""",
    )


def write_vitepress(chars: list[str]) -> None:
    char_items = ",\n              ".join(
        f'{{ text: "{t("character.clovercraft." + c, pretty(c))}", link: "/personagens/{c}" }}' for c in chars
    )
    write(
        DOCS / ".vitepress" / "config.mts",
        f"""import {{ defineConfig }} from 'vitepress'

export default defineConfig({{
  title: 'Clover Craft Wiki',
  description: 'Wiki do mod Clover Craft 0.4.0 (NeoForge 1.21.1)',
  lang: 'pt-BR',
  base: process.env.VITEPRESS_BASE || '/',
  cleanUrls: true,
  lastUpdated: true,
  vite: {{
    ssr: {{
      noExternal: ['three'],
    }},
  }},
  themeConfig: {{
    logo: '/clover.svg',
    outline: 'deep',
    search: {{ provider: 'local' }},
    nav: [
      {{ text: 'Guia', link: '/guia/comecar' }},
      {{ text: 'Personagens', link: '/personagens/' }},
      {{ text: 'Galeria 3D', link: '/galeria' }},
      {{ text: 'Mundo', link: '/mundo/' }},
      {{ text: 'Sistemas', link: '/sistemas/' }},
      {{ text: 'Sobre', link: '/sobre' }},
    ],
    sidebar: {{
      '/guia/': [
        {{
          text: 'Guia',
          items: [
            {{ text: 'Começar', link: '/guia/comecar' }},
            {{ text: 'Controles', link: '/guia/controles' }},
            {{ text: 'Combate', link: '/guia/combate' }},
            {{ text: 'Progressão', link: '/guia/progressao' }},
          ],
        }},
      ],
      '/personagens/': [
        {{
          text: 'Personagens',
          items: [
            {{ text: 'Visão geral', link: '/personagens/' }},
            {char_items},
          ],
        }},
      ],
      '/mundo/': [
        {{
          text: 'Mundo',
          items: [
            {{ text: 'Overworld', link: '/mundo/' }},
            {{ text: 'Chefes', link: '/mundo/bosses' }},
            {{ text: 'Submundo', link: '/mundo/underworld' }},
          ],
        }},
      ],
      '/sistemas/': [
        {{
          text: 'Sistemas',
          items: [
            {{ text: 'Visão geral', link: '/sistemas/' }},
            {{ text: 'Esquadrões', link: '/sistemas/squads' }},
            {{ text: 'Guildas', link: '/sistemas/guildas' }},
            {{ text: 'Raças', link: '/sistemas/racas' }},
            {{ text: 'Árvore', link: '/sistemas/arvore' }},
            {{ text: 'Quests', link: '/sistemas/quests' }},
            {{ text: 'Invocações', link: '/sistemas/invocacoes' }},
            {{ text: 'Relíquias', link: '/sistemas/reliquias' }},
            {{ text: 'Itens', link: '/sistemas/itens' }},
            {{ text: 'Comandos', link: '/sistemas/comandos' }},
          ],
        }},
      ],
    }},
    socialLinks: [],
    footer: {{
      message: 'Fan wiki gerada a partir do JAR 0.4.0. Black Clover pertence a Yūki Tabata / Shueisha.',
      copyright: 'Clover Craft 0.4.0 · NeoForge 1.21.1',
    }},
  }},
  head: [
    ['link', {{ rel: 'icon', href: '/clover.svg' }}],
  ],
}})
""",
    )
    write(
        DOCS / ".vitepress" / "theme" / "index.ts",
        """import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import GeoViewer from './GeoViewer.vue'
import CharacterRoster from './CharacterRoster.vue'
import CharacterProfile from './CharacterProfile.vue'
import CharacterDetails from './CharacterDetails.vue'
import SystemsHub from './SystemsHub.vue'
import './custom.css'
import './characters.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('GeoViewer', GeoViewer)
    app.component('CharacterRoster', CharacterRoster)
    app.component('CharacterProfile', CharacterProfile)
    app.component('CharacterDetails', CharacterDetails)
    app.component('SystemsHub', SystemsHub)
  },
} satisfies Theme
""",
    )
    write(
        DOCS / ".vitepress" / "theme" / "custom.css",
        """:root {
  --vp-c-brand-1: #3dba6e;
  --vp-c-brand-2: #2d8a4e;
  --vp-c-brand-3: #1f5c35;
  --vp-c-brand-soft: rgba(61, 186, 110, 0.14);
  --vp-home-hero-name-color: transparent;
  --vp-home-hero-name-background: linear-gradient(120deg, #d4af37 10%, #3dba6e 70%);
}

.dark {
  --vp-c-bg: #0b0f0c;
  --vp-c-bg-alt: #101610;
  --vp-c-bg-elv: #161c16;
  --vp-c-brand-1: #d4af37;
  --vp-c-brand-2: #3dba6e;
  --vp-c-brand-3: #2d8a4e;
}

.home-note {
  max-width: 800px;
  margin: 2rem auto 0;
  padding: 0 24px 48px;
  color: var(--vp-c-text-2);
  font-size: 0.92rem;
}

tr:hover td {
  background: var(--vp-c-brand-soft);
}
""",
    )
    (DOCS / "public").mkdir(parents=True, exist_ok=True)
    write(
        DOCS / "public" / "clover.svg",
        """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <path fill="#2d8a4e" d="M32 8c6 0 10 6 10 12 0 8-10 14-10 14S22 28 22 20c0-6 4-12 10-12zm0 48c-6 0-10-6-10-12 0-8 10-14 10-14s10 6 10 14c0 6-4 12-10 12zM8 32c0-6 6-10 12-10 8 0 14 10 14 10s-6 10-14 10c-6 0-12-4-12-10zm48 0c0 6-6 10-12 10-8 0-14-10-14-10s6-10 14-10c6 0 12 4 12 10z"/>
  <circle cx="32" cy="32" r="5" fill="#d4af37"/>
</svg>
""",
    )
    write(
        ROOT / "package.json",
        """{
  "name": "clovercraft-wiki",
  "private": true,
  "type": "module",
  "scripts": {
    "docs:dev": "vitepress dev docs",
    "docs:build": "vitepress build docs",
    "docs:preview": "vitepress preview docs",
    "wiki:rebuild": "python tools/build_wiki.py",
    "wiki:models": "python tools/extract_models.py"
  },
  "devDependencies": {
    "three": "^0.170.0",
    "vitepress": "^1.6.4"
  }
}
""",
    )
    write(
        ROOT / ".gitignore",
        """node_modules/
docs/.vitepress/cache/
docs/.vitepress/dist/
tools/vineflower-1.12.0.jar
*.jar
decompiled/
assets/
clover/
clovercraft.mixins.json
""",
    )
    write(
        ROOT / "README.md",
        """# Clover Craft Wiki

Wiki do mod **Clover Craft 0.4.0** (NeoForge 1.21.1). Inclui visualizador 3D dos modelos GeckoLib, sem distribuir arquivos de implementação do mod.

## Local

```bash
npm install
npm run docs:dev
```

http://localhost:5173/

## GitHub Pages

1. Crie um repositório (ex.: `clovercraft-wiki`) e envie este projeto.
2. Em **Settings → Pages → Source** escolha **GitHub Actions**.
3. O workflow `.github/workflows/pages.yml` publica a cada push em `main`.

A URL fica `https://<user>.github.io/<repo>/` (o `base` do VitePress é calculado no CI). Se o repo se chamar `<user>.github.io`, o site sobe na raiz.

Os modelos e texturas em `docs/public/models/` vão no git — são o que o visualizador usa. Arquivos do mod, código descompilado e dados de extração ficam excluídos pelo `.gitignore`.

## Manutenção

```bash
python tools/extract_models.py   # atualiza geos + texturas de uma fonte autorizada
python tools/build_wiki.py       # atualiza os markdowns com uma fonte autorizada
```
""",
    )


def main() -> None:
    print("Kits...")
    kits = extract_kits()
    print("  ", list(kits))
    print("Summons...")
    summons = extract_summons()
    print("  ", len(summons))
    print("Bosses...")
    bosses = extract_bosses()
    print("  ", [b["id"] for b in bosses])
    print("Relics...")
    relics = extract_relics()
    print("  ", len(relics))
    print("Quests...")
    quests = extract_quests()
    print("  ", len(quests))
    print("Tree...")
    tree = extract_tree()
    print("  ", len(tree))
    generate(kits, summons, bosses, relics, quests, tree)
    write_vitepress(list(CHAR_META))
    print("Wiki written to docs/")


if __name__ == "__main__":
    main()
