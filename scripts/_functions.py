from scripts._config import Config
from scripts._logging import Logging

class Functions:
    def __init__(self) -> None:
        self.config = Config()
        self.log = Logging()._logger(self.__class__)

    # Функция клика

    def click_farm(self):
        self.config.update("clicks", str(int(self.config.get("clicks")) + int(self.config.get("upd_co"))))

    # Функция улучшения кликов

    def upd_clicks(self):
        if int(self.config.get("clicks")) >= 25:
            self.config.update("clicks", str(int(self.config.get("clicks")) - 25))
            self.config.update("upd_co", str(int(self.config.get("upd_co")) + 1))

    # Очистка данных

    def clrall(self):
        self.config.check(nocheck=True)
        self.log.info("Успешное пересоздание конфига по запросу пользователя")
        exit()