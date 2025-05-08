from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#РЕГИСТРАЦИЯ

#Подключение к БД
connection_string = (
    "DRIVER={SQL Server};"
    "SERVER=DESKTOP-OGAMHE4\MSSQLSERVER01;"
    "DATABASE=UserAuthDB;"
    "UID=Azizi_admin;"
    "PWD=9110084399;"
)

#Базовый интерфейс

class AuthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auth System")
        self.root.geometry("300x200")

        # Создаем вкладки
        self.notebook = ttk.Notebook(root)
        self.login_tab = ttk.Frame(self.notebook)
        self.register_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.login_tab, text="Вход")
        self.notebook.add(self.register_tab, text="Регистрация")
        self.notebook.pack(expand=True, fill="both")

        # Инициализация вкладок
        self.create_login_tab()
        self.create_register_tab()

    # ...




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ОСНОВНОЙ ФУНКЦИОНАЛ






#Создание Обьекта окна
root = Tk()

#Значения по умолчанию
size = 10
color = "red"

#Создание холста
canv = Canvas(bg="white")
canv.pack()

#Функция для риосвания
def draw(event):
        canv.create_oval(event.x - size,
                              event.y - size,
                              event.x + size,
                              event.y + size,
                              fill=color, outline=color)
        
#Реакция холста на событие B1-Motion(Движение выши с зажатой лкм)
canv.bind("<B1-Motion>",draw)
root.mainloop()
