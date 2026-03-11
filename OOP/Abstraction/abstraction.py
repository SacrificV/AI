from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract Class
    def __init__(self, c: str):
        self.color = c

    def get_color(self) -> str:
        return self.color

    @abstractmethod
    def get_area(self) -> float:
        pass

class Square(Shape):
    def __init__(self, c: str, side: float):
        super().__init__(c)
        self.side = side

    def get_area(self) -> float:
        return self.side * self.side

s = Square("blue", 6.0)
print(s.get_color())
print(s.get_area())
