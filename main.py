from tkinter import Tk, ttk, messagebox, Canvas, Menu, Scale, Toplevel, filedialog
import tkinter as tk
from tkinter import colorchooser
from PIL import ImageGrab, Image



# Создание Обьекта окна
root = Tk()

# Значения по умолчанию
size = 10
color = "red"

# Создание холста
canv = Canvas(bg="white", height=1000, width=1900)
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
    scale = Scale(scale_win, from_=1, to=50, orient=tk.HORIZONTAL, command=change_size)
    scale.set(size)
    scale.pack()

# Функция сохранения холста
def save_canvas():
    # подменю для выбора формата
    format_menu = Menu(root, tearoff=0)
    format_menu.add_command(label="PNG", command=lambda: save_as("png"))
    format_menu.add_command(label="JPEG", command=lambda: save_as("jpg"))
    
    # меню "Сохранить" с подменю выбора формата
    save_menu = Menu(root, tearoff=0)
    save_menu.add_cascade(label="Выберите формат", menu=format_menu)
    
    # Показываем меню
    save_menu.post(root.winfo_pointerx(), root.winfo_pointery())

def save_as(file_format):
    file_path = filedialog.asksaveasfilename(
        defaultextension=f".{file_format}",
        filetypes=[(f"{file_format.upper()} files", f"*.{file_format}")]
    )
    
    if not file_path:  # Если пользователь отменил сохранение
        return
    
    if file_format in ["png", "jpg"]:
        # Получаем координаты холста
        x = root.winfo_rootx() + canv.winfo_x()
        y = root.winfo_rooty() + canv.winfo_y()
        x1 = x + canv.winfo_width()
        y1 = y + canv.winfo_height()
        
        # скриншот холста и сохраняем
        ImageGrab.grab(bbox=(x, y, x1, y1)).save(file_path)
        messagebox.showinfo("Успех", f"Изображение сохранено как {file_path}")
    
# Создание меню
main_menu = Menu(root)

# Кнопки выбора цвета размера и сохраниения
main_menu.add_cascade(label="Цвет", command=lambda: change_color())
main_menu.add_cascade(label="Размер", command=show_scale_window)
main_menu.add_cascade(label="Сохранить", command=save_canvas)

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