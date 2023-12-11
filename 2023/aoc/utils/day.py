class Day:
    def __str__(self):
        return f"{self.day} - {self.title}"

    def __init__(self, day: int, title: str):
        self.day = day
        self.title = title
