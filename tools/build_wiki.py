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
KEYS = [
    ("skill_1–5", "Habilidades 1 a 5 (a 5ª é o ultimate da forma)"),
    ("transform", "Transformar / avançar forma"),
    ("dash", "Dash nas quatro direções"),
    ("guard", "Guardar (segurar) / parry (toque no timing)"),
    ("lock_on", "Travar alvo"),
    ("stance", "Empunhar / embainhar (Asta e espadachins)"),
    ("swap", "Trocar espada (Asta)"),
    ("fly", "Voar (espada, asas, espírito, etc.)"),
    ("meditate", "Meditar para regenerar mana (segurar, fora de combate)"),
    ("summon", "Toque: invocar subordinado · Segurar: ordens"),
    ("awaken", "Forçar despertar dos subordinados"),
    ("journey", "Tela da jornada / missões"),
    ("quest_hud", "Minimizar painel de quest"),
    ("shoulder_camera", "Câmera no ombro"),
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
        f"""# Começar a jogar

Clover Craft transforma o mundo vanilla num Reino Clover: você nasce sem grimório, é chamado à **Torre dos Grimórios** em Hage, gira a roleta e recebe um dos 16 magos.

## Requisitos

| Peça | Versão |
| --- | --- |
| Minecraft | 1.21.1 |
| NeoForge | 21.1.259 ou superior |
| GeckoLib | 4.9.3+ |
| Photon | 2.2.7+ (cliente — partículas e pós-FX) |
| O mod | `clovercraft-0.4.0-neoforge-1.21.1.jar` |

## Loop inicial

1. Entre no mundo. A **cerimônia** aponta o altar da Torre dos Grimórios.
2. Chegue perto do altar: a **roleta** sorteia personagem, raça e potencial.
3. Use o grimório (botão direito) para se **vincular** — isso é permanente até a próxima temporada ou comando de admin.
4. Siga o tutorial e fale com os NPCs de Hage.
5. Vá ao **Coliseu do Exame** (`/exam`) para virar Cavaleiro Mágico e escolher um esquadrão.
6. Suba **força** (combate) e **méritos de guerra** (ranks). Cadeias de quest liberam a primeira e a segunda transformação.

## O que sobe com você

- **Força (1–100)** — poder bruto. Quests, chefes e inimigos pagam XP de força.
- **Méritos** — definem o [rank](/guia/progressao) (Aspirante → Rei Mago) e desbloqueiam skills/formas.
- **Maestria** — 5 estrelas por forma. A forma seguinte só abre com 5★ na anterior (configurável).
- **Árvore de skills** — pontos vindos de força, cadeias, firsts de chefes e rank de mérito.

## Dificuldade e temporada

O servidor tem dificuldade própria (`/clover difficulty`) além da vanilla. Uma **nova temporada** zera a jornada de todo cavaleiro na Torre.

Personagens já escolhidos por outro jogador no servidor podem ficar bloqueados (claims). Roleta e claims são configuráveis.
""",
    )

    key_rows = "\n".join(f"| `{k}` | {d} |" for k, d in KEYS)
    write(
        DOCS / "guia" / "controles.md",
        f"""# Controles

Categoria no Minecraft: **Clover Craft**. Rebind no menu vanilla.

| Tecla (id) | Função |
| --- | --- |
{key_rows}

## Combate básico

- **Ataque básico** — combo de 3–5 hits no chão. No ar, um air attack. Depois de um dash, **dash slash**.
- **Segurar ataque** — charge / heavy. Soltar no timing faz a versão *release*.
- **Guard** — reduz dano no arco frontal e gasta stamina. No frame certo, **parry** (atordoa o atacante e gera meter).
- **Guard break** — stamina zerada: você fica aberto.
- **Lock-on** — câmera e skills seguem o alvo. Essencial contra chefes.
- **Clash** — dois golpes pesados se encontram: mini-game de círculos (Perfect / Good / Miss). O vencedor perpassa com dano extra.

## Meter (mana / anti-magia)

A barra enche com hits, dano sofrido (exceto quem usa escudo de mana) e meditação. Transformar e skills caras gastam a barra. Sem meter, skills recusam (`Out of mana`).

Asta não tem mana: a barra é **Anti-Magia**. Guard dele **anula magia** em vez de só bloquear.

## Câmera e feedback

Câmera no ombro, shake e FOV são opções de cliente. Personagens têm braços em primeira pessoa com motion própria.
""",
    )

    write(
        DOCS / "guia" / "combate.md",
        """# Combate

O combate é de ação, não de cooldown de hotbar. Cada personagem tem um **kit** (`CharacterKit`) com combo, charge, dash, guard, 4–5 skills e 2 transformações.

## Estrutura de um kit

| Slot | O que é |
| --- | --- |
| Combo 1–4 (às vezes 5) | String leve. Cancela no `cancel_at` para o próximo hit |
| Charge / tap / release | Heavy. Segurar aumenta o golpe |
| Dash F/L/B/R | I-frames curtos + deslocamento |
| Air | Um golpe aéreo |
| Dash slash | Conversão depois do dash |
| Skill 1–4 | Magias do grimório |
| Skill 5 | Ultimate da forma atual |
| Transform | Gasta meter e troca o kit inteiro |
| Exhausted | Stun curto se a forma acabar no zero |

Dano dos hits vem dos JSON em `clover/actions/` (campo `hits[].damage`), depois multiplicado por **força**, **forma**, **rank**, **esquadrão**, **árvore** e **PvE/PvP**.

## Formas

Quase todo mago tem forma 0 (base), 1 e 2. Mereoleona e Asta têm **estágios** internos (Black Asta 1–3, Hellfire 1–3). A forma 2 em geral pede:

- forma 1 com **maestria 5★**
- meter ≥ 70
- ainda não gasta nesta vida (várias ultimates são *once per life*)

Sair da forma (`revert`) devolve o kit base. Meter no zero aplica **exhausted**.

## Guard, parry, selo

- Guard reduz dano (config `guard_reduction`) num arco em graus.
- Parry na janela (`parry_ticks`) stagger o atacante.
- Hits de Asta **selam** magia do alvo por alguns ticks — o selado não lança.

## Clash

Dois fighters com charge suficiente entram no minigame. Círculos aparecem; timing Perfect vence. Empate empurra os dois. Chefes e mobs têm “skill” de clash própria (mais fácil errar contra boss).

## Meditação

Segurar fora de combate, depois de alguns ticks de calma. Regenera mana/anti-magia mais rápido.

## PvP vs PvE

A config separa dano a mobs e a jogadores, e a árvore aplica só uma fração dos bônus em PvP (`TREE_PVP`). Ultimates de forma têm multiplicador PvP próprio.
""",
    )

    rank_rows = []
    for i, rid in enumerate(RANK_IDS):
        rank_rows.append(
            f"| {i} | {t('rank.clovercraft.' + rid)} | {RANK_MERITS[i]:,} |".replace(",", ".")
        )
    write(
        DOCS / "guia" / "progressao.md",
        f"""# Progressão

Há três eixos que sobem juntos — força, méritos/rank e maestria — mais a [árvore](/sistemas/arvore) e as [quests](/sistemas/quests).

## Ranks (méritos de guerra)

Limiares vanilla do mod (multiplicados por `merit_scale` e pela dificuldade):

| # | Rank | Méritos |
| --- | --- | ---: |
{chr(10).join(rank_rows)}

Cada rank desbloqueia skills/formas **do seu personagem** (veja a página dele). Coisas comuns a todos:

- **Junior 3º** — voo do kit (rank 2)
- **Senior 3º** — 3º dash
- **Rei Mago** — *Form mastery* (+15% poder, forma drena mais devagar)

## Força (1–100)

XP de força vem de inimigos, chefes e recompensas de quest. A curva é exponencial (`STRENGTH_TOP = 200000`, expoente 1.5). Cada 9 níveis de força equivalem a um “tier” de rank para scaling de HP/dano.

HP, regen, resistência e dano PvE/PvP interpolam entre o valor do Aspirante e o do Rei Mago (configs `health_min/max`, `damage_pve_*`, etc.).

## Maestria

Cada forma tem 5 níveis. Combate na forma, quests (`mastery` nas recompensas) e treinos enchem a barra. A config `form_gate` impede pular formas.

## Cerimônia e roleta

Na Torre, a roleta escolhe personagem + [raça](/sistemas/racas). Há pergaminhos para rerolar raça (`race_scroll`) e grimório (`grimoire_scroll`) — drops raros de chefes mundiais (8% e 3%).

## Exame de Cavaleiro Mágico

Comando `/exam` (ou o NPC no Coliseu). Requisitos: personagem vinculado, cerimônia feita, ainda não passou, modo sobrevivência, cooldown de retry (~2 min).

Você luta contra um examinador NPC. Vitória oferece **três esquadrões**. A escolha aplica o bônus permanente do [esquadrão](/sistemas/squads).

## Temporada

Admin pode avançar a temporada (`/clover season wipe`). Todo mundo recomeça na Torre no próximo login.
""",
    )

    # characters index
    cards = []
    for c in chars:
        meta = CHAR_META[c]
        cards.append(
            f"| [{t('character.clovercraft.' + c, pretty(c))}](/personagens/{c}) | {meta['magic']} | {meta['squad']} |"
        )
    write(
        DOCS / "personagens" / "index.md",
        f"""# Personagens

16 magos jogáveis. O grimório vincula você a um deles — não há troca sem reroll/admin/temporada.

| Personagem | Magia | Esquadrão canônico |
| --- | --- | --- |
{chr(10).join(cards)}

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

    for c in chars:
        meta = CHAR_META[c]
        kit = kits.get(c, {"forms": [], "skills": [], "unlocks": []})
        name = t("character.clovercraft." + c, pretty(c))
        grim = t("item.clovercraft." + meta["grimoire"], meta["grimoire"])
        grim_desc = t("item.clovercraft." + meta["grimoire"] + ".desc", "")

        form_list = kit["forms"] or ["base"]
        forms_md = ", ".join(f"**{form_label(f)}** (`{f}`)" for f in form_list)

        skill_md = []
        for i, group in enumerate(kit.get("skills") or []):
            form_name = form_list[min(i, len(form_list) - 1)] if form_list else f"kit {i}"
            # map ba1/dive etc: skills groups are base / form1 / form2
            if i == 0:
                form_name = "base"
            elif i == 1 and len(form_list) > 1:
                form_name = form_list[1]
            elif i == 2 and len(form_list) > 2:
                form_name = form_list[-1]
            rows = ["| Slot | ID | Nome | Dano (hit) | Duração (ticks) |", "| ---: | --- | --- | ---: | ---: |"]
            for slot, sid in enumerate(group, 1):
                aid = f"{c}/skill/{sid}"
                st = action_stats(aid)
                dmg = f"{st['damage']:.1f}" if st.get("damage") else "—"
                dur = str(st["duration"]) if st.get("duration") else "—"
                rows.append(f"| {slot} | `{sid}` | {md_escape(skill_name(sid))} | {dmg} | {dur} |")
            skill_md.append(f"### {form_label(form_name)}\n\n" + "\n".join(rows))

        unlock_md = ["| Rank | Desbloqueios |", "| --- | --- |"]
        unlocks = kit.get("unlocks") or []
        if not unlocks:
            # Asta usa a ladder global
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
        for i, group in enumerate(unlocks):
            rname = t("rank.clovercraft." + RANK_IDS[i], RANK_IDS[i]) if i < len(RANK_IDS) else str(i)
            names = ", ".join(skill_name(x) for x in group) if group else "—"
            unlock_md.append(f"| {rname} | {md_escape(names)} |")

        q_md = []
        for q in quests_by_char.get(c, []):
            q_md.append(f"### {q['id']}\n")
            if q["canon"]:
                q_md.append(f"> {q['canon']}\n")
            if q["requires"]:
                q_md.append(f"Requer: {', '.join('`' + r + '`' for r in q['requires'])}\n")
            q_md.append("| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |")
            q_md.append("| --- | --- | --- | ---: | --- | --- |")
            for s in q["steps"]:
                rew = s["reward"]
                bits = []
                for k in ("strength", "merits", "mastery"):
                    if k in rew:
                        bits.append(f"{k} {rew[k]}")
                q_md.append(
                    f"| `{s['id']}` | {s['type']} | `{s.get('place') or '—'}` | {s.get('min') or 0} | `{s.get('boss') or '—'}` | {', '.join(bits) or '—'} |"
                )
            q_md.append("")

        su = summons_by_char.get(c, [])
        if su:
            srows = ["| Unidade | Função | Tier | Única |", "| --- | --- | ---: | --- |"]
            for u in su:
                srows.append(f"| {u['name']} (`{u['id']}`) | {u['role']} | {u['tier']} | {'sim' if u['unique'] else 'não'} |")
            summons_md = "\n".join(srows)
        else:
            summons_md = "_Este personagem não tem pool de subordinados listado._"

        extras = ""
        if c == "asta":
            extras = """
## Espadas demoníacas

Asta troca quatro armas (`swap`). Cada uma muda o combo, o dash slash e skills ligadas:

| Espada | Item | Notas |
| --- | --- | --- |
| Demon-Slayer | `slayer_sword` | Kit inicial. One-Horn / Bull Thrust |
| Demon-Dweller | `dweller_sword` | Absorve e devolve magia — Black Slash |
| Demon-Destroyer | `destroyer_sword` | Causality Break (campo que anula magia) |
| Demon-Slasher | `slasher_sword` | Katana. Black Divider, 5º hit no combo |

Guard de Asta é **anti-magia**: selo no oponente em vez de escudo de mana.
"""
        skins = character_skins(c)
        geo_path = MODELS / "geo" / "character" / f"{c}.geo.json"
        geo_block = ""
        if geo_path.exists() and skins:
            geo_block = (
                "<ClientOnly>\n"
                f'<GeoViewer geo="/models/geo/character/{c}.geo.json" '
                f"skins='{attr_json(skins)}' />\n"
                "</ClientOnly>\n"
            )
        write(
            DOCS / "personagens" / f"{c}.md",
            f"""# {name}

**{meta['magic']}** · {meta['squad']}

{geo_block}
{meta['role']}

- Grimório: **{grim}**
- {grim_desc}
- Formas: {forms_md}
- Vincular: use o grimório (mensagem `{t('message.clovercraft.bound_' + c, '')}`)

## Skills por forma

Dano é o maior hit do JSON da action, **antes** dos multiplicadores de força/forma/árvore.

{chr(10).join(skill_md) if skill_md else "_Kit sem lista SKILLS (ver actions JSON)._"}

## Desbloqueio por rank

{chr(10).join(unlock_md)}

{extras}

## Subordinados

{summons_md}

## Quests da jornada

{chr(10).join(q_md) if q_md else "_Sem cadeia própria além dos treinos globais._"}

Veja também: [combate](/guia/combate) · [progressão](/guia/progressao) · [invocações](/sistemas/invocacoes)
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
    place_rows = ["| ID | Tipo | Alvo |", "| --- | --- | --- |"]
    for p in places:
        place_rows.append(f"| `{p['id']}` | {p.get('kind','')} | `{p.get('target','')}` |")

    write(
        DOCS / "mundo" / "index.md",
        f"""# Mundo

O overworld ganha estruturas do Reino Clover, sites de quest e eventos de **world boss**. Três dimensões extras formam o [Submundo](/mundo/underworld).

## Estruturas (worldgen)

| Estrutura | Onde aparece |
| --- | --- |
| `hage_village` | Vila inicial, Torre dos Grimórios |
| `royal_capital` | Capital Real |
| `black_bulls_hideout` | Esconderijo dos Touros Negros |
| `squad_hall` | Salão de esquadrão |
| `exam_colosseum` | Coliseu do exame |
| `saussey_village` | Vila Saussey |
| `ancient_dungeon` | Masmorra antiga (primeiro dungeon do anime) |
| `elf_ruins` | Ruínas élficas |

## Locais de quest

Sites são peças templated (`quest_wind_shrine`, `quest_witch_grove`, `quest_heart_spring`, `quest_volcano_camp`…) plantadas em biomas certos, 300–1500 blocos da origem.

{chr(10).join(place_rows)}

## Inimigos de mundo

Factions spawnam via biome modifiers: bandidos, Reino Diamond, Olho do Sol da Meia-Noite, bruxas, elfos, paladinos, bestas, Spade e rogue knights. No Submundo, só demônios (imp → high devil / devil host).

Tiers de foe `A/B/C/S` nas waves de quest. Elites dropam mais méritos.

## Proteção

Áreas de estrutura são `Protected`: grief de vanilla é limitado para não destruir capital/esconderijo. Guard posts invisíveis defendem NPCs.
""",
    )

    write(
        DOCS / "mundo" / "underworld.md",
        """# Submundo (Qliphoth)

Três dimensões: `clovercraft:underworld_1` (Rim), `underworld_2` (Depths), `underworld_3` (Throne). Entrada pelo **Altar da Qliphoth**.

## Como entrar

1. Crafte o altar (`qliphoth_altar`: ouro, livro, essência de mana, diamante, obsidiana).
2. Realize o **ritual** com o item de ritual e selos (`SealRecipes`) — cada camada pede materiais mais raros.
3. O portão (`QliphothGate`) abre para a camada correspondente.
4. **Return Sigil** (`return_sigil`: 4 essências + ender pearl + ouro → 2 sigilos) traz de volta ao overworld.

Hosts de demônio no elenco jogável (Asta, Dante, Vanica, Zenon, Nacht) têm +5% de vantagem (`HOST_EDGE`) no Submundo.

## Camadas

| Camada | Dimensão | Bioma | Chefes de domínio |
| ---: | --- | --- | --- |
| 1 Rim | `underworld_1` | `qliphoth_rim` | **Zagred** |
| 2 Depths | `underworld_2` | `qliphoth_depths` | **Megicula**, **Lilith / Nahamah** |
| 3 Throne | `underworld_3` | `qliphoth_throne` | **Beelzebub**, **Lucifero** |

Cada domínio é uma arena circular com raio 30–48 e um dais. Baús `domain_*` dropam relíquias temáticas.

## Ilhas, santuários, essência

O gerador cria ilhas de `black_mana` / `qliphoth_root` / `dark_qliphoth_root`. Santuários e landmarks servem de âncora. `mana_essence` é o recurso de craft do conteúdo endgame.

Void guard teleporta de volta se você cair no vazio (`The void spat you back onto the landing`).
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

    catalog = boss_catalog(bosses)
    catalog_block = ""
    if catalog:
        catalog_block = (
            "<ClientOnly>\n"
            f"<GeoViewer catalog='{attr_json(catalog)}' :height=\"460\" />\n"
            "</ClientOnly>\n"
        )
    write(
        DOCS / "mundo" / "bosses.md",
        f"""# Chefes

{catalog_block}
Chefes de quest, eventos mundiais e senhores da Qliphoth compartilham o mesmo cérebro (`BossBrain`): fases, cura interrompível, stagger, clash e persona (agressivo, caster, summoner…).

## Eventos mundiais

Com `clovercraft-world.toml` → `boss_events`. A cada ciclo o servidor escolhe um headliner conforme a força média dos online:

| Força dos jogadores | Headliners (peso 6×) |
| --- | --- |
| &lt; 40 | Sally, Rades, Heath Graice, Dominante Code |
| 40–61 | Vetto, Fana, Witch Queen, Ratri |
| 62–84 | Witch Queen, Vetto, Rhya, Gaderois |
| 85+ | Witch Queen, Vetto, Damnatio Kira |

Outros bosses cujo `band` está entre `força-25` e `força+6` entram com peso 1. Demônios da Qliphoth **não** spawnam no overworld.

Recompensas: força, méritos, chance de `race_scroll` (8%) e `grimoire_scroll` (3%), relíquia assinatura do chefe, título *Vanquisher of X*. Duo (dois chefs) paga 60% extra. Sair da arena faz o chefe *withdraw*.

## Roster

{chr(10).join(boss_rows)}

{chr(10).join(boss_pages)}

IA: o boss lê ki (percepts), evita cheese (teto, pillar, kiting infinito) e troca de move por utilidade (`BossUtility`). Fairness reduz dano se o grupo está muito abaixo do band.
""",
    )

    # systems
    squad_rows = ["| Esquadrão | Capitão | Prestígio | Bônus |", "| --- | --- | ---: | --- |"]
    for key, nome, cap, pres, bonus in SQUADS:
        squad_rows.append(f"| {nome} (`{key}`) | {cap} | {pres} | {bonus} |")
    write(
        DOCS / "sistemas" / "squads.md",
        f"""# Esquadrões

Escolhidos no [exame](/guia/progressao). Prestígio alto (3) é o “top squad” do cânone; o bônus é pequeno de propósito.

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

Sorteadas na cerimônia (pesos somam 100). Reroll com **Race Scroll**.

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

Cinco ramos. Pontos = `(força - 1) + cadeias concluídas + firsts de chefe (cap) + rank de mérito`, limitados por config.

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

Definidas em JSON (`clover/quests/`). Tipos de cadeia: `form` (libera transformação), `training` (repeatable), `secret` (condição `reveal`).

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

Cada mago tem um pool (`*Units.java`). Precisa do nó **Pact** na árvore (`sum_pact`) para invocar. Toque na tecla Summon chama; segurar abre ordens; Awaken força o próximo estágio.

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

Itens `relic_*` com raridade Rare → Mythic. Ativas disparam um **burst** (cooldown em segundos × 20 ticks). Passivas ficam sempre ligadas. First kill de um chefe tende a dropar a relíquia assinatura dele.

{chr(10).join(rel_rows)}

{chr(10).join(rel_detail)}
""",
    )

    write(
        DOCS / "sistemas" / "itens.md",
        f"""# Itens, blocos e crafts

## Grimórios

Um por personagem (ver páginas em [Personagens](/personagens/)). Botão direito vincula se você ainda não tem mago. Bound items não saem do inventário.

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
      {{ text: 'Sistemas', link: '/sistemas/squads' }},
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
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('GeoViewer', GeoViewer)
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
classes/
tools/vineflower-1.12.0.jar
extracted/
tmp_geo/
*.jar
decompiled/
assets/
clover/
data/
META-INF/
clovercraft.mixins.json
""",
    )
    write(
        ROOT / "README.md",
        """# Clover Craft Wiki

Wiki do mod **Clover Craft 0.4.0** (NeoForge 1.21.1), gerada a partir do JAR descompilado. Inclui viewer 3D dos modelos GeckoLib.

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

Não commite o `.jar` nem `decompiled/` (já estão no `.gitignore`). Os modelos em `docs/public/models/` (~11 MB) vão no git — são o que o viewer usa.

## Regenerar conteúdo

```bash
python tools/extract_models.py   # geos + texturas do JAR
python tools/build_wiki.py       # markdown a partir do descompilado
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
    dump = {
        "kits": kits,
        "summons": summons,
        "bosses": [{"id": b["id"], "band": b["band"], "name": b["name"]} for b in bosses],
        "relics": len(relics),
        "quests": len(quests),
        "tree": len(tree),
    }
    (ROOT / "tools" / "extract-summary.json").write_text(json.dumps(dump, indent=2, ensure_ascii=False), encoding="utf-8")
    print("Wiki written to docs/")


if __name__ == "__main__":
    main()
