from tkinter import Tk, ttk, messagebox, Canvas
import tkinter as tk
import pyodbc

# Подключение к БД
connection_string = (
    "DRIVER={SQL Server};"
    "SERVER=DESKTOP-OGAMHE4\\MSSQLSERVER01;"
    "DATABASE=UserAuthDB;"
    "Trusted_Connection=yes;"
)

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Рисовалка")
        
        # Значения по умолчанию
        self.size = 10
        self.color = "red"
        
        # Создание холста
        self.canvas = Canvas(root, bg="white")
        self.canvas.pack(fill="both", expand=True)
        
        # Привязка событий
        self.canvas.bind("<B1-Motion>", self.draw)
    
    def draw(self, event):
        self.canvas.create_oval(event.x - self.size,
                               event.y - self.size,
                               event.x + self.size,
                               event.y + self.size,
                               fill=self.color, outline=self.color)

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

    def create_login_tab(self):
        """Создает интерфейс вкладки для входа"""
        # Поле для логина
        ttk.Label(self.login_tab, text="Логин:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.login_username_entry = ttk.Entry(self.login_tab)
        self.login_username_entry.grid(row=0, column=1, padx=10, pady=5)

        # Поле для пароля
        ttk.Label(self.login_tab, text="Пароль:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.login_password_entry = ttk.Entry(self.login_tab, show="*")
        self.login_password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Кнопка входа
        ttk.Button(
            self.login_tab, 
            text="Войти", 
            command=self.login
        ).grid(row=2, column=0, columnspan=2, pady=10)

    def create_register_tab(self):
        """Создает интерфейс вкладки для регистрации"""
        # Поле для логина
        ttk.Label(self.register_tab, text="Логин:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.reg_username_entry = ttk.Entry(self.register_tab)
        self.reg_username_entry.grid(row=0, column=1, padx=10, pady=5)

        # Поле для пароля
        ttk.Label(self.register_tab, text="Пароль:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.reg_password_entry = ttk.Entry(self.register_tab, show="*")
        self.reg_password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Кнопка регистрации
        ttk.Button(
            self.register_tab, 
            text="Зарегистрироваться", 
            command=self.register
        ).grid(row=2, column=0, columnspan=2, pady=10)
    
    def register(self):
        """Регистрирует нового пользователя в БД"""
        username = self.reg_username_entry.get()
        password = self.reg_password_entry.get()

        if not username or not password:
            messagebox.showerror("Ошибка", "Все поля обязательны!")
            return

        try:
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()

            # Проверка существующего пользователя
            cursor.execute("SELECT Username FROM Users WHERE Username = ?", username)
            if cursor.fetchone():
                messagebox.showerror("Ошибка", "Пользователь уже существует!")
                return

            # Добавление нового пользователя
            cursor.execute(
                "INSERT INTO Users (Username, Password) VALUES (?, ?)",
                username, password
            )
            conn.commit()
            messagebox.showinfo("Успех", "Регистрация завершена!")

        except pyodbc.Error as e:
            messagebox.showerror("Ошибка БД", f"Ошибка: {e}")
        finally:
            if 'conn' in locals():
                conn.close()

    def login(self):
        """Авторизует пользователя"""
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()

        try:
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()

            cursor.execute(
                "SELECT Username FROM Users WHERE Username = ? AND Password = ?",
                username, password
            )
            if cursor.fetchone():
                messagebox.showinfo("Успех", f"Добро пожаловать, {username}!")
                self.root.destroy()  # Закрываем окно авторизации
                
                # Создаем новое окно для рисования
                drawing_root = Tk()
                DrawingApp(drawing_root)
                drawing_root.mainloop()
            else:
                messagebox.showerror("Ошибка", "Неверный логин или пароль")

        except pyodbc.Error as e:
            messagebox.showerror("Ошибка БД", f"Ошибка: {e}")
        finally:
            if 'conn' in locals():
                conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = AuthApp(root)
    root.mainloop()