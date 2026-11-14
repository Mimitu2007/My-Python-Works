class Bike:
    """Клас для представлення велосипеда."""
    
    default_manufacturer = "Generic Bikes Co" 

    def __init__(self, weight, price, wheel_diameter, color):
        """Конструктор класу Bike."""
        self.weight = float(weight) 
        self.__price = float(price) 
        self.wheel_diameter = int(wheel_diameter)
        self.color = str(color)
        print(f"-> Створено новий велосипед: {self.color}, {self.wheel_diameter}\" колеса.")

    def change_price(self, new_price):
        """Метод для зміни ціни велосипеда."""
        if new_price > 0:
            self.__price = new_price
            print(f"   Ціну змінено. Нова ціна: {self.__price} грн.")
        else:
            print("   Помилка: Ціна має бути додатною.")

    def change_color(self, new_color):
        """Метод для зміни кольору велосипеда."""
        self.color = new_color
        print(f"   Колір змінено на {self.color}.")
        
    def get_details(self):
        """Виведення всіх відомостей."""
        return (f"Характеристики: Вага: {self.weight} кг, Колір: {self.color}, "
                f"Колеса: {self.wheel_diameter}\", Ціна: {self.__price} грн.")

class Computer:
    """Базовий клас для представлення комп'ютерного пристрою."""
    
    def __init__(self, cpu, ram, os="Windows"):
        self.cpu = str(cpu)
        self.ram = int(ram)
        self.os = str(os)
        
    def run_program(self, program_name):
        """Метод для запуску програми."""
        print(f"-> Computer (CPU: {self.cpu}) запускає програму '{program_name}'.")

    def display_specs(self):
        """Метод для відображення основних характеристик."""
        print(f"   Специфікації: OS: {self.os}, CPU: {self.cpu}, RAM: {self.ram}GB.")

class Tablet(Computer):
    """Похідний клас Tablet (планшет), успадковує від Computer."""
    
    def __init__(self, cpu, ram, os, screen_size, has_cellular=False):
        super().__init__(cpu, ram, os)
        self.screen_size = float(screen_size)
        self.has_cellular = has_cellular
        
    def check_cellular(self):
        """Додатковий метод: перевіряє наявність мобільного зв'язку."""
        status = "встановлений" if self.has_cellular else "відсутній"
        print(f"   Для цього планшета мобільний зв'язок {status}.")
        
    def display_specs(self):
        """Перевизначений метод."""
        super().display_specs()
        print(f"   Додатково: Екран {self.screen_size}\".")