from tkinter import Tk, ttk, messagebox, Canvas, Menu, Scale, Toplevel
import tkinter as tk
import pyodbc
from tkinter import colorchooser
from tkinter import *

# Создание Обьекта окна
root = Tk()

# Значения по умолчанию
size = 10
color = "red"

# Создание холста
canv = Canvas(bg="white",height=1000, width=1900)
canv.pack()

# Функция для изменения размера
def change_size(val):
    global size
    size = int(float(val))

# Функция для изменения цвета
def change_color():
    global color 
    color = colorchooser.askcolor(initialcolor="black")

# Функция для создания окна с Scale
def show_scale_window():
    scale_win = Toplevel(root)
    scale_win.title("Выберите размер")
    scale = Scale(scale_win, from_=1, to=50, orient=HORIZONTAL, command=change_size)
    scale.set(size)
    scale.pack()

# Создание меню
main_menu = Menu(root)

#Кнопки выбора цвета размера
main_menu.add_cascade(label="Цвет", command=lambda: change_color())
main_menu.add_cascade(label="Размер", command=show_scale_window)

root.config(menu=main_menu)

# Функция для рисования
def draw(event):
    canv.create_oval(event.x - size,
                     event.y - size,
                     event.x + size,
                     event.y + size,
                     fill=color[1], outline=color[1])

# Реакция холста на событие B1-Motion
canv.bind("<B1-Motion>", draw)

root.mainloop()