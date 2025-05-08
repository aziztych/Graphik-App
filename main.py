from tkinter import Tk, ttk, messagebox, Canvas, Menu, Scale, Toplevel
import tkinter as tk
import pyodbc
from tkinter import *

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

# Создание Обьекта окна
root = Tk()

# Значения по умолчанию
size = 10
color = "red"

# Создание холста
canv = Canvas(bg="white")
canv.pack()

# Функция для изменения размера
def change_size(val):
    global size
    size = int(float(val))

# Функция для изменения цвета
def change_color(new_color):
    global color
    color = new_color

# Функция для создания окна с Scale
def show_scale_window():
    scale_win = Toplevel(root)
    scale_win.title("Выберите размер")
    scale = Scale(scale_win, from_=1, to=50, orient=HORIZONTAL, command=change_size)
    scale.set(size)
    scale.pack()

# Создание меню
main_menu = Menu(root)

# Меню цвета
color_menu = Menu(main_menu, tearoff=0)
color_menu.add_command(label="Красный", command=lambda: change_color("red"))
color_menu.add_command(label="Зеленый", command=lambda: change_color("green"))
color_menu.add_command(label="Синий", command=lambda: change_color("blue"))
color_menu.add_separator()
color_menu.add_command(label="Exit", command=root.quit)

# Меню размера
size_menu = Menu(main_menu, tearoff=0)
size_menu.add_command(label="Изменить размер", command=show_scale_window)

main_menu.add_cascade(label="Цвет", menu=color_menu)
main_menu.add_cascade(label="Размер", menu=size_menu)

root.config(menu=main_menu)

# Функция для рисования
def draw(event):
    canv.create_oval(event.x - size,
                     event.y - size,
                     event.x + size,
                     event.y + size,
                     fill=color, outline=color)

# Реакция холста на событие B1-Motion
canv.bind("<B1-Motion>", draw)

root.mainloop()