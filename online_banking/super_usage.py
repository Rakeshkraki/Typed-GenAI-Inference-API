
class Shape:

    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):

    def __init__(self,color :str, is_filled : bool, radius : float):
        super().__init__(color, is_filled)
        self.radius = radius

    def print_circle(self) -> dict:
        return {"color" : self.color, "is_filled" : self.is_filled, "radius" : self.radius}

tyre = Circle("black", True, 10.5)

print(tyre.print_circle())
