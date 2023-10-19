class Rectangle:

  def __init__(self, width: int, height: int) -> None:
    self.width = width
    self.height = height

  def __str__(self) -> str:
    return f"Rectangle(width={int(self.width)}, height={int(self.height)})"

  def set_width(self, width: int):
    self.width = width

  def set_height(self, height: int):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return ((self.width**2 + self.height**2)**.5)

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."

    rectangle = ("*" * self.width + "\n") * self.height
    return rectangle

  def get_amount_inside(self, shape):
    max_width = self.width // shape.width
    max_height = self.height // shape.height
    return max_width * max_height


class Square(Rectangle):

  def __init__(self, side: int):
    self.width = side
    self.height = side

  def __str__(self):
    return "Square(side=" + str(self.width) + ")"

  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, side):
    self.width = side
    self.height = side

  def set_height(self, side):
    self.width = side
    self.height = side