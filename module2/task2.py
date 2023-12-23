# У даному випадку доцільно використовувати поведінковий шаблон "Стратегія",
# оскільки нам потрібно реалізувати різні стратегії для авторизації (логін та пароль, СМС-код, електронний лист).


from abc import ABC, abstractmethod

# Абстрактний клас стратегії авторизації
class AuthorizationStrategy(ABC):
    @abstractmethod
    def authenticate(self) -> None:
        pass

# Конкретна стратегія для авторизації за допомогою логіну та паролю
class LoginPasswordStrategy(AuthorizationStrategy):
    def authenticate(self) -> None:
        # Логіка авторизації за допомогою логіну та паролю
        print("Авторизація за допомогою логіну та паролю")

# Конкретна стратегія для авторизації за допомогою СМС-коду
class SMSStrategy(AuthorizationStrategy):
    def authenticate(self) -> None:
        # Логіка авторизації за допомогою СМС-коду
        print("Авторизація за допомогою СМС-коду")

# Конкретна стратегія для авторизації за допомогою електронного листа
class EmailStrategy(AuthorizationStrategy):
    def authenticate(self) -> None:
        # Логіка авторизації за допомогою електронного листа
        print("Авторизація за допомогою електронного листа")

# Клас, який використовує стратегію авторизації
class UserAuthorization:
    def __init__(self, strategy: AuthorizationStrategy) -> None:
        self.strategy = strategy

    def perform_authentication(self) -> None:
        self.strategy.authenticate()

# Використання шаблону "Стратегія"
if __name__ == "__main__":
    # Спроба авторизації за допомогою логіну та паролю
    login_password_strategy = LoginPasswordStrategy()
    user_auth = UserAuthorization(login_password_strategy)
    user_auth.perform_authentication()

    # Спроба авторизації за допомогою СМС-коду
    sms_strategy = SMSStrategy()
    user_auth = UserAuthorization(sms_strategy)
    user_auth.perform_authentication()

    # Спроба авторизації за допомогою електронного листа
    email_strategy = EmailStrategy()
    user_auth = UserAuthorization(email_strategy)
    user_auth.perform_authentication()

