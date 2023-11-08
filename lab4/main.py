from abc import ABC, abstractmethod


# Абстрактний клас для всіх датчиків
class Sensor(ABC):
    @abstractmethod
    def activate(self):
        pass

    @abstractmethod
    def deactivate(self):
        pass


# Класи для конкретних типів датчиків

class SmokeSensor(Sensor):
    def activate(self):
        print("Датчик диму активований")
        # Вимикаємо всі інші датчики
        self.deactivate_other_sensors()

    def deactivate(self):
        print("Датчик диму вимкнений")

    def deactivate_other_sensors(self):
        print("Вимикаємо всі інші датчики")


class LightSensor(Sensor):
    def activate(self):
        print("Датчик освітлення активований")
        self.deactivate_noise_sensor()
        self.activate_curtain_sensor()

    def deactivate(self):
        print("Датчик освітлення вимкнений")

    def deactivate_noise_sensor(self):
        print("Вимикаємо датчик шуму")

    def activate_curtain_sensor(self):
        print("Вмикаємо штори")


class NoiseSensor(Sensor):
    def activate(self):
        print("Датчик шуму активований")
        # Вимикаємо інші датчики, якщо необхідно

    def deactivate(self):
        print("Датчик шуму вимкнений")


class CurtainSensor(Sensor):
    def activate(self):
        print("Датчик штор активований")

    def deactivate(self):
        print("Датчик штор вимкнений")


class WaterLeakSensor(Sensor):
    def activate(self):
        print("Датчик протікання води активований")
        # Вимикаємо інші датчики, якщо необхідно

    def deactivate(self):
        print("Датчик протікання води вимкнений")


# Клас для керування системою

class SmartHomeSystem:
    def __init__(self):
        self.sensors = []

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def activate_sensor(self, sensor_type):
        for sensor in self.sensors:
            if isinstance(sensor, sensor_type):
                sensor.activate()

    def deactivate_sensor(self, sensor_type):
        for sensor in self.sensors:
            if isinstance(sensor, sensor_type):
                sensor.deactivate()


if __name__ == "__main__":
    home_system = SmartHomeSystem()

    smoke_sensor = SmokeSensor()
    light_sensor = LightSensor()
    noise_sensor = NoiseSensor()
    curtain_sensor = CurtainSensor()
    water_leak_sensor = WaterLeakSensor()

    home_system.add_sensor(smoke_sensor)
    home_system.add_sensor(light_sensor)
    home_system.add_sensor(noise_sensor)
    home_system.add_sensor(curtain_sensor)
    home_system.add_sensor(water_leak_sensor)

    # Сценарій а) - активуємо датчик диму
    home_system.activate_sensor(SmokeSensor)

    # Сценарій б) - активуємо датчик освітлення
    home_system.activate_sensor(LightSensor)
