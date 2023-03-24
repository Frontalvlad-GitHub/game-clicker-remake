import sys, os
from scripts._logging import Logging
from configparser import ConfigParser
'''
Класс, включающий в себя __init__ а так же
методы управления ini конфигом.
'''
class Config:
    '''
    Включает в себя важные данные для дальнейшего
    использования и редактирования конфига.
    :param self:
    '''
    def __init__(self) -> None:
        self.settings = {
            'clicks': '0',
            'upd_co': '1',
            'price': '25',
        }
        self.config = ConfigParser()
        self.config_path = "config.ini"
        self.log = Logging()._logger(self.__class__)


    '''
    Проверка наличия а так же действительности конфига.
    :param self: 
    '''
    def check(self, nocheck = False) -> bool:
        if os.path.isfile(self.config_path) and nocheck != True:
            self.config.read("config.ini")
            if self.config["settings"].keys() == self.settings.keys():
                self.log.info("Конфиг найден") 
                return True
            else:
                self.log.error("Конфиг имеет ошибки и не соответствует шаблону, удалите конфиг или исправьте ошибку")
                exit()
        else:
            self.log.info("Создание конфига")
            try: 
                self.create()
                self.log.info("Успешно!")
                return True
            except: 
                self.log.error("Не получилось создать конфиг")
                self.log.exception("exception")
                return False


    '''
    Создание конфига, а так же заполнение его стандартными данными.
    :param self:
    '''
    def create(self) -> None:
        self.config["settings"] = self.settings
        with open('config.ini', 'w') as cfg:
            self.config.write(cfg)


    '''
    Изменение определенного параметра в конфиге
    на пользовательское значение.
    :param self:
    :param param: Получение параметра.
    :param value: Получение нового значения параметра.
    '''
    def update(self, param, value) -> bool:
        if param in self.settings.keys():
            self.config.read("config.ini")
            self.config["settings"][param] = value

            with open('config.ini', 'w') as conf:
                self.config.write(conf)
            self.log.info("Успешное обновление данных параметра {0} на {1} в конфиге".format(param, value))
            return True    
        else:
            self.log.error("Не удалось найти и перезаписать параметр {0} на значение {1}".format(param, value))
            return False
        

    '''
    Получение уже имеющихся данных из конфига.
    :param self:
    :param value: Получение параметра.
    '''
    def get(self, param) -> str or int or bool:
        if param in self.settings.keys():
            self.config.read("config.ini")
            self.log.info("Успешно получены данные из параметра {}".format(param))
            return self.config["settings"][param]
        else:
            self.log.error("Не удалось найти параметр со значением {}".format(param))
