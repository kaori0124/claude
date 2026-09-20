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
    category: str  # main / salad / side
    effort: str  # easy / normal
    time_minutes: int
    tags: list[str] = field(default_factory=list)
    seasons: list[str] = field(default_factory=list)
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
            effort=data.get("effort", "easy"),
            time_minutes=data.get("time_minutes", 0),
            tags=data.get("tags", []),
            seasons=data.get("seasons", []),
            ingredients=ingredients,
        )


@dataclass
class MealSlot:
    date: str
    day_of_week: str
    main: Dish | None = None
    salad: Dish | None = None
    side: Dish | None = None

    @property
    def all_dishes(self) -> list[Dish]:
        dishes = []
        if self.main:
            dishes.append(self.main)
        if self.salad:
            dishes.append(self.salad)
        if self.side:
            dishes.append(self.side)
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
        if self.salad:
            parts.append(self.salad.name)
        if self.side:
            parts.append(self.side.name)
        return " / ".join(parts)


@dataclass
class WeeklyPlan:
    meals: list[MealSlot] = field(default_factory=list)

    def all_ingredients(self) -> list[Ingredient]:
        result = []
        for meal in self.meals:
            result.extend(meal.all_ingredients)
        return result
