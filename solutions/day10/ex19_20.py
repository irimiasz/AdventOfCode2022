CHECKS = [20, 60, 100, 140, 180, 220]
JUMP = 40


class Register:
    def __init__(self):
        self._clocks = 0
        self._register = 1
        self._signal_count = 0
        self._sprite_position = 1

    def update_signal_count(self):
        self._clocks += 1
        if self._clocks in CHECKS:
            self._signal_count += self._register * self._clocks
        self._draw()

    def add_to_register(self, value: int):
        self._register += value
        self._sprite_position += value

    def get_signal_count(self) -> int:
        return self._signal_count

    def get_sprite_position(self) -> list[int]:
        return [
            self._sprite_position,
            self._sprite_position + 1,
            self._sprite_position + 2,
        ]

    def get_clocks(self) -> int:
        return self._clocks

    def _draw(self):
        end_char = " " if self._clocks % 40 and self._clocks > 0 else "\n"
        print(self._sign(), end=end_char)

    def _sign(self) -> str:
        if (self._clocks % 40) in self.get_sprite_position():
            return "#"
        else:
            return "."


def ex19():
    with open("input.txt", "r") as file:
        register = Register()
        for line in file.readlines():
            register.update_signal_count()
            if line.startswith("addx"):
                register.update_signal_count()
                register.add_to_register(int(line.split(" ")[1]))

    return register.get_signal_count()


if __name__ == "__main__":
    print(ex19())
