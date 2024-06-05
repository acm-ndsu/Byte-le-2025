from game.common.game_object import GameObject
from game.common.enums import ObjectType
from typing import Self, Tuple


class Vector(GameObject):
    """
    `Vector Class Notes:`

    This class is used universally in the project to handle anything related to coordinates. There are a few useful
    methods here to help in a few situations.

    -----

    Add Vectors Method:
        This method will take two Vector objects, combine their (x, y) coordinates, and return a new Vector object.

        Example:
            vector_1: (1, 1)
            vector_2: (1, 1)

            Result:
            vector_result: (2, 2)

    -----

    Add to Vector method:
        This method will take a different Vector object and add it to the current Self reference; that is, this method
        belongs to a Vector object and is not static.

        Example:
            self_vector: (0, 0)
            vector_1: (1, 3)

            Result:
            self_vector: (1, 3)

    -----

    Add X and Add Y methods:
        These methods act similarly to the ``add_vector()`` method, but instead of changing both the x and y, these
        methods change their respective variables.

        Add X Example:
            self_vector: (0, 0)
            vector_1: (1, 3)

            Result:
            self_vector: (1, 0)

        Add Y Example:
            self_vector: (0, 0)
            vector_1: (1, 3)

            Result:
            self_vector: (0, 3)

    -----

    As Tuple Method:
        This method returns a tuple of the Vector object in the form of (x, y). This is to help with storing it easily
        or accessing it in an immutable structure.
    """

    def __init__(self, x: int = 0, y: int = 0):
        super().__init__()
        self.object_type: ObjectType = ObjectType.VECTOR
        self.x = x
        self.y = y

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int) -> None:
        if x is None or not isinstance(x, int):
            raise ValueError(f"The given x value, {x}, is not an integer.")
        self.__x = x

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int) -> None:
        if y is None or not isinstance(y, int):
            raise ValueError(f"The given y value, {y}, is not an integer.")
        self.__y = y

    @staticmethod
    def from_xy_tuple(xy_tuple: Tuple[int, int]) -> 'Vector':
        return Vector(*xy_tuple)

    @staticmethod
    def from_yx_tuple(yx_tuple: Tuple[int, int]) -> 'Vector':
        return Vector(*yx_tuple[::-1])

    def add_to_vector(self, other_vector: Self) -> 'Vector':
        return Vector(
            self.x + other_vector.x,
            self.y + other_vector.y
        )

    def add_x_y(self, x: int, y: int) -> 'Vector':
        return self.add_to_vector(Vector(x, y))

    def add_x(self, x: int) -> 'Vector':
        return self.add_to_vector(Vector(x))

    def add_y(self, y: int) -> 'Vector':
        return self.add_to_vector(Vector(y=y))

    def as_tuple(self) -> Tuple[int, int]:
        """Returns (x: int, y: int)"""
        return self.x, self.y

    def to_json(self) -> dict:
        data = super().to_json()
        data['x'] = self.x
        data['y'] = self.y

        return data

    def from_json(self, data) -> Self:
        super().from_json(data)
        self.x = data['x']
        self.y = data['y']

        return self

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __hash__(self):
        return hash(self.as_tuple())

    def __eq__(self, other) -> bool:
        return self.as_tuple() == other.as_tuple()
