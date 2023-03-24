from tkinter import *
from tkinter import ttk
from scripts._config import Config
from scripts._logging import Logging
from scripts._functions import Functions
import threading

class Main:
    def __init__(self) -> None:
        self.config = Config()
        self.log = Logging()._logger(self.__class__)
        self.func = Functions()

        # Создание и настройка окна
        self.root = Tk()
        self.root.geometry('250x200+800+400')

        # Создание набора вкладок

        tab_control = ttk.Notebook(self.root)
        tab_control.pack(expand=True, fill=BOTH)

        # Создание вкладок

        game = ttk.Frame(tab_control)
        magaz = ttk.Frame(tab_control)
        options = ttk.Frame(tab_control)

        # Основное окно
        self.root.title('Игра "Кликер"')
        # self.root.iconbitmap(default='logo.ico') 
        self.root.resizable(False,False)

        def update_clicks():
            self.lb_cl['text'] = f'Золота: {self.config.get("clicks")}'
            self.func.click_farm()
        def update_co():
            self.lb_prr['text'] = f'Текущий множитель: {self.config.get("upd_co")}'
            self.func.upd_clicks()

        btnf = ttk.Button(game, text='Кликай!', command=update_clicks)
        btn_upd_plus = ttk.Button(magaz, text='Улучшение кирки', command=update_co)
        self.lb_cl = ttk.Label(game, text= f'Золота: {self.config.get("clicks")}')
        self.lb_prr = ttk.Label(magaz, text=f'Текущий множитель: {self.config.get("upd_co")}')
        self.lb_pr = ttk.Label(magaz, text=f'Цена улучшения: {self.config.get("price")} золота')
        clear_btn = ttk.Button(options, text=f'Очистка всех данных (Откат невозможен!)', command=self.func.clrall)

        self.lb_prr.pack(anchor='s', padx=55, ipady=20, fill=X)
        self.lb_pr.pack(anchor='s', padx=45, ipady=5, fill=X)
        self.lb_cl.pack(anchor=S)

        btnf.pack(anchor='s',fill = X, ipady=5, pady = 1)
        btn_upd_plus.pack(anchor='sw', fill=X, expand=True, ipady=5)
        clear_btn.pack(expand=True, fill=X)

        tab_control.add(game, text='Игра')
        tab_control.add(magaz, text='Магазин')
        tab_control.add(options, text='Настройки')

'''
Запуск главного файла
'''
if __name__ == "__main__":
    Main().root.mainloop()
