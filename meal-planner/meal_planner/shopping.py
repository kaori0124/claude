"""買い物リスト生成。1週間分の食材を売り場セクション別に集計する。"""

from __future__ import annotations

from collections import defaultdict

from .models import Ingredient, WeeklyPlan

SECTION_ORDER = [
    "野菜",
    "肉",
    "肉加工品",
    "魚",
    "卵・乳製品",
    "豆腐",
    "乾物",
    "缶詰",
    "冷凍食品",
    "調味料",
    "お惣菜",
    "その他",
]


def generate_shopping_list(plan: WeeklyPlan) -> dict[str, list[dict]]:
    """売り場セクション別に食材を集計して返す。"""
    grouped: dict[str, dict[str, list[str]]] = defaultdict(
        lambda: defaultdict(list)
    )

    for ingredient in plan.all_ingredients():
        section = ingredient.section
        grouped[section][ingredient.name].append(ingredient.amount)

    result: dict[str, list[dict]] = {}
    for section in SECTION_ORDER:
        if section not in grouped:
            continue
        items = []
        for name, amounts in sorted(grouped[section].items()):
            merged = _merge_amounts(amounts)
            items.append({"name": name, "amount": merged})
        result[section] = items

    for section in grouped:
        if section not in result:
            items = []
            for name, amounts in sorted(grouped[section].items()):
                merged = _merge_amounts(amounts)
                items.append({"name": name, "amount": merged})
            result[section] = items

    return result


def _merge_amounts(amounts: list[str]) -> str:
    if len(amounts) == 1:
        return amounts[0]

    if all(a == amounts[0] for a in amounts):
        return f"{amounts[0]} x{len(amounts)}"

    return " + ".join(amounts)


def format_shopping_list(shopping_list: dict[str, list[dict]]) -> str:
    lines = []
    lines.append("=" * 40)
    lines.append("  買い物リスト")
    lines.append("=" * 40)

    for section, items in shopping_list.items():
        lines.append("")
        lines.append(f"【{section}】")
        for item in items:
            lines.append(f"  [ ] {item['name']}  ... {item['amount']}")

    lines.append("")
    lines.append("=" * 40)
    return "\n".join(lines)
