import sys
from decimal import Decimal


def dot_clac(dot, circle_dot, r):
    x1, y1 = circle_dot
    x2, y2 = dot
    d = (x2 - x1) ** 2 + (y2 - y1) ** 2
    r = r ** 2
    if d == r:
        print(0)
    elif d < r:
        print(1)
    else:
        print(2)


if __name__ == "__main__":
    circle_path = sys.argv[1]
    dots_path = sys.argv[2]

    with open(circle_path, "r") as file:
        circle_dot = tuple(map(Decimal, file.readline().strip().split()))
        r = Decimal(file.readline().strip())

    with open(dots_path, "r") as file:
        for line in file:
            dot = tuple(map(Decimal, line.strip().split()))
            dot_clac(dot, circle_dot, r)
