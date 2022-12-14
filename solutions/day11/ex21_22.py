from __future__ import annotations
from math import prod


MONKEYS = {}


OPERATIONS = {
    "*": lambda a, b: a * int(b) if b != "old" else a * a,
    "+": lambda a, b: a + int(b) if b != "old" else a * 2,
}


class Item:
    def __init__(self, worry_level: int):
        self.worry_level = worry_level

    def pass_by_monkey(self, operation):
        self.worry_level = operation(self.worry_level) // 3

    def pass_by_monkey_but_worried(self, operation):
        self.worry_level = operation(self.worry_level)

    def set_modular_worry_level(self, test_val: int):
        self.worry_level = self.worry_level % test_val

    def check_test_pass(self, test: int):
        return self.worry_level % test == 0


class Monkey:
    def __init__(
        self,
        id: int,
        items: list,
        op_sign: str,
        op_val: str,
        test_val: int,
        test_true: int,
        test_false: int,
    ):
        self.id = id
        self.items = [Item(lvl) for lvl in items]
        self.hold_count = 0
        self.operation = lambda x: OPERATIONS[op_sign](x, op_val)
        self.test_val = test_val
        self.test_true = test_true
        self.test_false = test_false

    def get_passed_test_receiver(self):
        return MONKEYS[self.test_true]

    def get_failed_test_receiver(self):
        return MONKEYS[self.test_false]

    def get_monkey_receiver(self, item: Item):
        return (
            self.get_passed_test_receiver()
            if item.check_test_pass(self.test_val)
            else self.get_failed_test_receiver()
        )

    def pass_item_to_other_monkey(self, item: Item):
        monkey = self.get_monkey_receiver(item)
        monkey.items.append(item)
        self.items.remove(item)

    def pass_item_to_other_monkey_with_decreasing_value(self, item: Item):
        monkey = self.get_monkey_receiver(item)
        monkey.items.append(item)
        self.items.remove(item)


def get_monkeys():
    with open("input.txt", "r") as file:
        for line in file.readlines():
            line = line.strip()
            if line.startswith("Monkey"):
                monkey = {}
                monkey_id = int(line.split(" ")[1][:-1])
                monkey["id"] = monkey_id
            if line.startswith("Starting items"):
                monkey["items"] = [
                    int(val) for val in line.replace(",", "").split(" ")[2:]
                ]
            if line.startswith("Operation"):
                monkey["op_sign"] = line.split(" ")[-2]
                monkey["op_val"] = line.split(" ")[-1]
            if line.startswith("Test"):
                monkey["test_val"] = int(line.split(" ")[-1])
            if line.startswith("If true"):
                monkey["test_true"] = int(line.split(" ")[-1])
            if line.startswith("If false"):
                monkey["test_false"] = int(line.split(" ")[-1])
                MONKEYS[monkey_id] = Monkey(**monkey)


def get_max_hold_counts_v1() -> int:
    get_monkeys()
    for _ in range(20):
        for monkey in MONKEYS.values():
            for item in monkey.items.copy():
                item.pass_by_monkey(monkey.operation)
                monkey.pass_item_to_other_monkey(item)
                monkey.hold_count += 1
    max_hold_counts = sorted(
        [monkey.hold_count for monkey in MONKEYS.values()], reverse=True
    )[:2]
    return max_hold_counts[0] * max_hold_counts[1]


def get_max_hold_counts_v2() -> int:
    get_monkeys()
    lcd = prod([m.test_val for m in MONKEYS.values()])
    for _ in range(10000):
        for monkey in MONKEYS.values():
            for item in monkey.items.copy():
                item.pass_by_monkey_but_worried(monkey.operation)
                monkey.pass_item_to_other_monkey_with_decreasing_value(item)
                monkey.hold_count += 1
                item.set_modular_worry_level(lcd)
    max_hold_counts = sorted(
        [monkey.hold_count for monkey in MONKEYS.values()], reverse=True
    )[:2]
    return max_hold_counts[0] * max_hold_counts[1]


if __name__ == "__main__":
    print(get_max_hold_counts_v1())
    MONKEYS.clear()
    print(get_max_hold_counts_v2())
