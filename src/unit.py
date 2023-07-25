from typing import List, Set


class Unit:
    def __init__(self, unit: List[str]):
        if len(unit) != 9:
            raise ValueError("Invalid unit length. A unit should contain 9 cells.")
        self.unit: List[str] = unit

    def is_valid(self) -> bool:
        seen: Set[str] = set()
        for cell in self.unit:
            if cell not in (".", "0"):
                if cell in seen or not cell.isdigit() or int(cell) < 1 or int(cell) > 9:
                    return False
                seen.add(cell)
        return True
