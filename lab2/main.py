from typing import List


# Інтерфейс для класу Digit, який відповідає за вивід однієї цифри
class IDigitPrinter:
    def print(self) -> List[str]:
        pass


# Реалізація класу Digit, який представляє одну цифру та виводить її зірочками
class Digit(IDigitPrinter):
    def __init__(self, value: int):
        self.value = value
        self.patterns = [
            ["***", "  *", "  *", "  *", "***"],
            [" * ", "** ", " * ", " * ", "***"],
            ["***", "  *", "***", "*  ", "***"],
            ["***", "  *", "***", "  *", "***"],
            ["* *", "* *", "***", "  *", "  *"],
            ["***", "*  ", "***", "  *", "***"],
            ["***", "*  ", "***", "* *", "***"],
            ["***", "  *", "  *", "  *", "  *"],
            ["***", "* *", "***", "* *", "***"],
            ["***", "* *", "***", "  *", "***"]
        ]

    def print(self) -> List[str]:
        digit_pattern = self.patterns[self.value]
        return digit_pattern


# Реалізація класу Number, який представляє число як масив цифр та виводить його зSSSірочками
class Number:
    def __init__(self, number: int):
        self.digits = [Digit(int(digit)) for digit in str(number)]

    def print(self):
        # Визначимо максимальну кількість рядків серед усіх цифр числа
        max_rows = max(len(digit.print()) for digit in self.digits)

        # Зберігатимемо рядки для виводу кожної цифри
        digit_lines = []

        for digit in self.digits:
            digit_pattern = digit.print()
            # Доповнимо кожну цифру до максимальної кількості рядків
            while len(digit_pattern) < max_rows:
                digit_pattern.insert(0, "   ")

            digit_lines.append(digit_pattern)

        # Виведемо числа рядок за рядком
        for row in range(max_rows):
            for digit_line in digit_lines:
                print(digit_line[row], end="  ")
            print()  # Перехід на новий рядок


# Приклад використання
if __name__ == "__main__":
    number = Number(1234567890)
    number.print()
