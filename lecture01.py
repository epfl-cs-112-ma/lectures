from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

def main() -> None:
    p = Point(5, 7)
    q = p
    print(q)

    p.x = 11
    print(q.x)

    p = Point(15, 17)
    print(q.x)
    q = Point(p.x, p.y)

    x = 5
    print(x)


if __name__ == "__main__":
    main()
