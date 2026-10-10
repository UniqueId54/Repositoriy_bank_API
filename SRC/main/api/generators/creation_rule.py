from dataclasses import dataclass

@dataclass
class CreationRule:
    regex: str | None = None
    min_value: int | float | None = None
    max_value: int | float | None = None
