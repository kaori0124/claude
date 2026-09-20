from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Ingredient:
    name: str
    amount: str
    section: str


@dataclass
class Dish:
    name: str
    category: str  # main / side / soup
    effort: str  # easy / normal / hard
    time_minutes: int
    tags: list[str] = field(default_factory=list)
    ingredients: list[Ingredient] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict) -> Dish:
        ingredients = [
            Ingredient(name=i["name"], amount=i["amount"], section=i["section"])
            for i in data.get("ingredients", [])
        ]
        return cls(
            name=data["name"],
            category=data["category"],
            effort=data.get("effort", "normal"),
            time_minutes=data.get("time_minutes", 30),
            tags=data.get("tags", []),
            ingredients=ingredients,
        )


@dataclass
class MealSlot:
    """一食分の献立（主菜 + 副菜 + 汁物 など）"""

    date: str  # YYYY-MM-DD
    day_of_week: str  # 月〜日
    main: Dish | None = None
    sides: list[Dish] = field(default_factory=list)
    soup: Dish | None = None

    @property
    def all_dishes(self) -> list[Dish]:
        dishes = []
        if self.main:
            dishes.append(self.main)
        dishes.extend(self.sides)
        if self.soup:
            dishes.append(self.soup)
        return dishes

    @property
    def total_time(self) -> int:
        return sum(d.time_minutes for d in self.all_dishes)

    @property
    def all_ingredients(self) -> list[Ingredient]:
        result = []
        for dish in self.all_dishes:
            result.extend(dish.ingredients)
        return result

    def summary(self) -> str:
        parts = []
        if self.main:
            parts.append(self.main.name)
        for side in self.sides:
            parts.append(side.name)
        if self.soup:
            parts.append(self.soup.name)
        return " / ".join(parts)


@dataclass
class WeeklyPlan:
    meals: list[MealSlot] = field(default_factory=list)

    def all_ingredients(self) -> list[Ingredient]:
        result = []
        for meal in self.meals:
            result.extend(meal.all_ingredients)
        return result
