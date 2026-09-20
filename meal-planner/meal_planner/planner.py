"""献立生成エンジン。設定ファイルのルールに従い、1週間分の献立を提案する。"""

from __future__ import annotations

import random
from datetime import date, timedelta

from .models import Dish, MealSlot, WeeklyPlan

WEEKDAY_JA = ["月", "火", "水", "木", "金", "土", "日"]


def _is_weekend(d: date) -> bool:
    return d.weekday() >= 5  # 土=5, 日=6


def _is_fish(dish: Dish) -> bool:
    return "魚" in dish.tags or dish.ingredients and any(
        i.section == "魚" for i in dish.ingredients
    )


def generate_weekly_plan(
    dishes: list[Dish],
    rules: dict,
    start_date: date | None = None,
    dishes_per_meal_config: dict | None = None,
) -> WeeklyPlan:
    if start_date is None:
        today = date.today()
        days_until_monday = (7 - today.weekday()) % 7
        if days_until_monday == 0:
            start_date = today
        else:
            start_date = today + timedelta(days=days_until_monday)

    config = dishes_per_meal_config or {}
    weekday_count = config.get("weekday_dinner", 3)
    weekend_count = config.get("weekend_dinner", 4)

    mains = [d for d in dishes if d.category == "main"]
    sides = [d for d in dishes if d.category == "side"]
    soups = [d for d in dishes if d.category == "soup"]

    max_same = rules.get("max_same_main_per_week", 1)
    avoid_consecutive = rules.get("avoid_consecutive_same_protein", True)
    weekday_max_time = rules.get("weekday_max_total_time_minutes", 60)
    min_fish = rules.get("min_fish_per_week", 1)
    hard_weekend_only = rules.get("hard_dishes_on_weekend_only", True)

    plan = WeeklyPlan()
    used_mains: dict[str, int] = {}
    prev_was_fish = None
    fish_count = 0

    dates = [start_date + timedelta(days=i) for i in range(7)]

    for i, d in enumerate(dates):
        weekend = _is_weekend(d)
        target_dishes = weekend_count if weekend else weekday_count
        side_count = target_dishes - 2  # 主菜1 + 汁物1 を引く

        slot = MealSlot(
            date=d.isoformat(),
            day_of_week=WEEKDAY_JA[d.weekday()],
        )

        # --- 主菜を選ぶ ---
        candidates = list(mains)

        if hard_weekend_only and not weekend:
            candidates = [c for c in candidates if c.effort != "hard"]

        if not weekend:
            soup_time = 10
            main_budget = weekday_max_time - soup_time
            fast = [c for c in candidates if c.time_minutes <= main_budget]
            if fast:
                candidates = fast

        candidates = [
            c for c in candidates if used_mains.get(c.name, 0) < max_same
        ]

        if avoid_consecutive and prev_was_fish is not None:
            if prev_was_fish:
                non_fish = [c for c in candidates if not _is_fish(c)]
                if non_fish:
                    candidates = non_fish

        remaining_days = 7 - i
        fish_needed = min_fish - fish_count
        if fish_needed > 0 and remaining_days <= fish_needed:
            fish_candidates = [c for c in candidates if _is_fish(c)]
            if fish_candidates:
                candidates = fish_candidates

        if not candidates:
            candidates = list(mains)

        main_dish = random.choice(candidates)
        slot.main = main_dish
        used_mains[main_dish.name] = used_mains.get(main_dish.name, 0) + 1
        prev_was_fish = _is_fish(main_dish)
        if prev_was_fish:
            fish_count += 1

        # --- 副菜を選ぶ（調理時間を考慮）---
        remaining_time = (weekday_max_time - main_dish.time_minutes - 10
                          if not weekend else 999)
        available_sides = list(sides)
        random.shuffle(available_sides)
        chosen_sides = []
        used_side_names: set[str] = set()
        for s in available_sides:
            if len(chosen_sides) >= max(side_count, 1):
                break
            if s.name in used_side_names:
                continue
            if not weekend and s.effort == "hard":
                continue
            if not weekend and s.time_minutes > remaining_time:
                continue
            chosen_sides.append(s)
            used_side_names.add(s.name)
            remaining_time -= s.time_minutes
        slot.sides = chosen_sides

        # --- 汁物を選ぶ ---
        available_soups = list(soups)
        if not weekend:
            available_soups = [
                s for s in available_soups if s.time_minutes <= remaining_time
            ]
        random.shuffle(available_soups)
        if available_soups:
            slot.soup = available_soups[0]

        plan.meals.append(slot)

    return plan
