"""献立生成エンジン。平日5日分の献立を提案する。"""

from __future__ import annotations

import random
from datetime import date, timedelta

from .models import Dish, MealSlot, WeeklyPlan

WEEKDAY_JA = ["月", "火", "水", "木", "金", "土", "日"]

MONTH_TO_SEASON = {
    3: "spring", 4: "spring", 5: "spring",
    6: "summer", 7: "summer", 8: "summer",
    9: "autumn", 10: "autumn", 11: "autumn",
    12: "winter", 1: "winter", 2: "winter",
}


def _is_fish(dish: Dish) -> bool:
    return "魚" in dish.tags or any(
        i.section == "魚" for i in dish.ingredients
    )


def _is_in_season(dish: Dish, season: str) -> bool:
    if not dish.seasons:
        return True
    return season in dish.seasons


def _seasonal_sort_key(dish: Dish, season: str) -> int:
    if dish.seasons and season in dish.seasons:
        return 0
    if not dish.seasons:
        return 1
    return 2


def generate_weekly_plan(
    dishes: list[Dish],
    rules: dict,
    start_date: date | None = None,
) -> WeeklyPlan:
    if start_date is None:
        today = date.today()
        days_until_monday = (7 - today.weekday()) % 7
        if days_until_monday == 0:
            start_date = today
        else:
            start_date = today + timedelta(days=days_until_monday)

    season = MONTH_TO_SEASON.get(start_date.month, "spring")
    prefer_seasonal = rules.get("prefer_seasonal", True)

    mains = [d for d in dishes if d.category == "main"]
    salads = [d for d in dishes if d.category == "salad"]
    sides = [d for d in dishes if d.category == "side"]

    max_same = rules.get("max_same_main_per_week", 1)
    avoid_consecutive = rules.get("avoid_consecutive_same_protein", True)
    max_time = rules.get("weekday_max_total_time_minutes", 30)
    min_fish = rules.get("min_fish_per_week", 1)

    if prefer_seasonal:
        mains = [m for m in mains if _is_in_season(m, season)]
        salads_in_season = [s for s in salads if _is_in_season(s, season)]
        if salads_in_season:
            salads = salads_in_season
        sides = [s for s in sides if _is_in_season(s, season)]

    plan = WeeklyPlan()
    used_mains: dict[str, int] = {}
    used_salads: list[str] = []
    prev_was_fish: bool | None = None
    fish_count = 0

    num_days = rules.get("days", 5)
    dates = [start_date + timedelta(days=i) for i in range(num_days)]

    for i, d in enumerate(dates):
        slot = MealSlot(
            date=d.isoformat(),
            day_of_week=WEEKDAY_JA[d.weekday()],
        )

        # --- メインを選ぶ ---
        candidates = [
            c for c in mains if used_mains.get(c.name, 0) < max_same
        ]

        main_budget = max_time - 5
        fast = [c for c in candidates if c.time_minutes <= main_budget]
        if fast:
            candidates = fast

        if avoid_consecutive and prev_was_fish is not None:
            if prev_was_fish:
                non_fish = [c for c in candidates if not _is_fish(c)]
                if non_fish:
                    candidates = non_fish

        remaining_days = num_days - i
        fish_needed = min_fish - fish_count
        if fish_needed > 0 and remaining_days <= fish_needed:
            fish_cands = [c for c in candidates if _is_fish(c)]
            if fish_cands:
                candidates = fish_cands

        if not candidates:
            candidates = [
                c for c in mains if c.time_minutes <= main_budget
            ] or list(mains)

        if prefer_seasonal:
            candidates.sort(key=lambda d: _seasonal_sort_key(d, season))
            best_tier = _seasonal_sort_key(candidates[0], season)
            candidates = [
                c for c in candidates
                if _seasonal_sort_key(c, season) == best_tier
            ]

        main_dish = random.choice(candidates)
        slot.main = main_dish
        used_mains[main_dish.name] = used_mains.get(main_dish.name, 0) + 1
        prev_was_fish = _is_fish(main_dish)
        if prev_was_fish:
            fish_count += 1

        remaining_time = max_time - main_dish.time_minutes

        # --- サラダを選ぶ（必須）---
        salad_candidates = [
            s for s in salads if s.time_minutes <= remaining_time
        ]
        recent = set(used_salads[-2:]) if len(used_salads) >= 2 else set()
        varied = [s for s in salad_candidates if s.name not in recent]
        if varied:
            salad_candidates = varied

        if not salad_candidates:
            salad_candidates = list(salads)

        if prefer_seasonal:
            salad_candidates.sort(key=lambda d: _seasonal_sort_key(d, season))
            best_tier = _seasonal_sort_key(salad_candidates[0], season)
            salad_candidates = [
                c for c in salad_candidates
                if _seasonal_sort_key(c, season) == best_tier
            ]

        salad = random.choice(salad_candidates)
        slot.salad = salad
        used_salads.append(salad.name)
        remaining_time -= salad.time_minutes

        # --- 副菜を選ぶ（余裕があれば）---
        if remaining_time > 0:
            side_candidates = [
                s for s in sides if s.time_minutes <= remaining_time
            ]
            if prefer_seasonal:
                in_season = [
                    s for s in side_candidates
                    if s.seasons and season in s.seasons
                ]
                if in_season:
                    side_candidates = in_season

            if side_candidates:
                slot.side = random.choice(side_candidates)

        plan.meals.append(slot)

    return plan
