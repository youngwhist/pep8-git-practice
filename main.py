"""Точка входа: вывод статистики по списку оценок."""
from utils import average, max_value, min_value


def main():
    scores = [78, 92, 85, 64, 99]
    print("Средний балл:", average(scores))
    print("Лучший результат:", max_value(scores))
    print("Худший результат:", min_value(scores))


if __name__ == "__main__":
    main()
