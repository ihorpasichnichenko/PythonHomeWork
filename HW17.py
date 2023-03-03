from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self) -> None:
        pass


class triangle(Shape):
    def __init__(self, width: int) ->None:
        self.width = width

    def draw(self) -> None:
        for i in range(self.width):
            print('*'*(i+1))


class rectangle(Shape):
    def __init__(self, width: int,height: int) -> None:
        self.width = width
        self.height = height

    def draw(self) -> None:
        for i in range(self.height):
            print('*'* self.width)


shapes = [triangle(45),rectangle(2, 2)]
for shape in shapes:
    shape.draw()