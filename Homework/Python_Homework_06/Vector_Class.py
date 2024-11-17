import math

class Vector:
    def __init__(self, *components):
        self.components = components

    def __str__(self):
        return f"Vector({', '.join(map(str, self.components))})"

    def __bool__(self):
        return any(value != 0 for value in self.components)

    def __len__(self):
        return len(self.components)

    def __getitem__(self, index):
        return self.components[index]

    def __setitem__(self, index, value):
        components_as_list = list(self.components)
        components_as_list[index] = value
        self.components = tuple(components_as_list)

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension for addition")
        return Vector(*[a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension for subtraction")
        return Vector(*[a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Vectors must have the same dimension for multiplication")
            return Vector(*[a * b for a, b in zip(self.components, other.components)])
        elif isinstance(other, (int, float)):
            return Vector(*[value * other for value in self.components])

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError("Cannot divide by zero")
        return Vector(*[value / scalar for value in self.components])

    def __eq__(self, other):
        return self.components == other.components

    def __abs__(self):
        return math.sqrt(sum(value ** 2 for value in self.components))

    def __neg__(self):
        return Vector(*[-value for value in self.components])
# v1 = Vector(1, 4, 6)
# print(v1)

# print(bool(v1))
# print(bool(Vector(0, 0)))

# print(len(v1))

# print(v1[1])
# v1[1] = 10
# print(v1)

# v2 = Vector(3, 7, 2)
# print(v1 + v2)
# print(v1 - v2)
# print(v1 * v2)

# print(v1 * 3)
# print(v1 / 2)

# print(abs(v1))

# print(v1 == Vector(1, 10, 6))

# print(-v1)
