from enum import Enum


class Protocol(Enum):
    HTTP = "HTTP"
    HTTPS = "HTTPS"
    FTP = "FTP"
    SSH = "SSH"


class Encryption(Enum):
    TLS = "TLS"
    SSL = "SSL"
    NONE = "NONE"


class IPVersion(Enum):
    V4 = "v4"
    V6 = "v6"


class InternetConnection:
    def __init__(self, protocol=Protocol.HTTP, encryption=None, ip_version=IPVersion.V4, **kwargs):
        self.protocol = protocol
        self.encryption = encryption
        self.ip_version = ip_version
        self.additional_properties = kwargs

    def connect(self):
        connection_info = f"Параметри з'єднання:\n"
        connection_info += f"Протокол: {self.protocol.value}\n"

        if self.encryption:
            connection_info += f"Шифрування: {self.encryption.value}\n"

        connection_info += f"Версія IP адреси: {self.ip_version.value}\n"

        if self.additional_properties:
            connection_info += "Додаткові властивості:\n"
            for key, value in self.additional_properties.items():
                connection_info += f"{key}: {value}\n"

        print(connection_info)


# Приклади створення об'єктів з різними конфігураціями
connection1 = InternetConnection(protocol=Protocol.HTTPS, encryption=Encryption.TLS, ip_version=IPVersion.V6, port=443)
connection2 = InternetConnection(encryption=Encryption.SSL, port=22, username="user123")
connection3 = InternetConnection(ip_version=IPVersion.V4, timeout=30)

# Виклик методу connect для кожного об'єкта
connection1.connect()
connection2.connect()
connection3.connect()
