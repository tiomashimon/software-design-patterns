from typing import List

# Інтерфейс для класу Digit
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

# Реалізація класу Number, який представляє число як масив цифр та виводить його
class Number:
    _singleton_instance = None

    def __new__(cls, *args, **kwargs):
        if cls._singleton_instance is None:
            cls._singleton_instance = super(Number, cls).__new__(cls)
        return cls._singleton_instance

    def __init__(self, number: int):
        if not hasattr(self, "initialized"):
            self.initialized = True
            self.digits = [Digit(int(digit)) for digit in str(number)]

    def print(self):
        # Визначимо максимальну кількість рядків серед усіх цифр числа
        max_rows = max(len(digit.print()) for digit in self.digits)

        # Виводимо числа рядок за рядком
        for row in range(max_rows):
            for digit in self.digits:
                digit_pattern = digit.print()
                # Доповнимо кожну цифру до максимальної кількості рядків
                while len(digit_pattern) < max_rows:
                    digit_pattern.insert(0, "   ")
                print(digit_pattern[row], end="  ")
            print()  # Перехід на новий рядок

# Приклад використання
if __name__ == "__main__":
    number1 = Number(1234567890)
    number1.print()

    # Тут number2 буде посилатися на той самий об'єкт, що і number1
    number2 = Number(9876543210)
    number2.print()
