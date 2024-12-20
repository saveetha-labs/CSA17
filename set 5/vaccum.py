class Vacuum:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cleaned = []
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def clean(self):
        if (self.x, self.y) not in self.cleaned:
            self.cleaned.append((self.x, self.y))
            print(f"Cleaned spot ({self.x}, {self.y})")

vacuum = Vacuum(0, 0)

vacuum.move(1, 1)
vacuum.clean()
vacuum.move(1, 0)
vacuum.clean()
vacuum.move(0, -1)
vacuum.clean()
