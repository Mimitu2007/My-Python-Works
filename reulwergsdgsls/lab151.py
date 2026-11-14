import math

class Paralelogram:
    """Клас для представлення паралелограма."""
    
    def __init__(self, side_a, side_b, angle_alpha_deg):
        """
        Конструктор класу Paralelogram.
        Приймає сторони a, b та кут alpha в градусах.
        """
        self.a = float(side_a)
        self.b = float(side_b)
        self.alpha_deg = float(angle_alpha_deg)
        self.alpha_rad = math.radians(self.alpha_deg) 
        print(f"-> Створено паралелограм зі сторонами {self.a}, {self.b} та кутом {self.alpha_deg}°.")

    def calculate_perimeter(self):
        """Обчислює периметр паралелограма: P = 2 * (a + b)."""
        perimeter = 2 * (self.a + self.b)
        return perimeter

    def calculate_area(self):
        """Обчислює площу паралелограма: S = a * b * sin(alpha)."""
        area = self.a * self.b * math.sin(self.alpha_rad)
        return area

    def get_details(self):
        """Повертає рядок з деталями паралелограма."""
        return (f"Сторони: {self.a}, {self.b} | Кут: {self.alpha_deg}°")

class Mess:
    """Базовий клас для представлення текстового повідомлення."""
    
    def __init__(self, sender, recipient, content):
        """Конструктор класу Mess."""
        self.sender = str(sender)
        self.recipient = str(recipient)
        self.content = str(content)
        self.is_read = False
        
    def mark_as_read(self):
        """Метод, який позначає повідомлення як прочитане."""
        self.is_read = True
        print(f"   Повідомлення від {self.sender} позначено як прочитане.")

    def preview(self):
        """Метод для попереднього перегляду повідомлення."""
        status = " (Не прочитано)" if not self.is_read else " (Прочитано)"
        return (f"[{self.recipient}] Від {self.sender}: "
                f"{self.content[:30]}..." + status)

class MailMess(Mess):
    """Похідний клас для поштового повідомлення (електронний лист)."""
    
    def __init__(self, sender, recipient, content, subject):
        """
        Конструктор класу MailMess.
        Викликає конструктор батьківського класу (Mess).
        """
        super().__init__(sender, recipient, content)
        self.subject = str(subject)
        self.attachments = []
        
    def add_attachment(self, filename):
        """Додатковий метод: додає вкладення до поштового повідомлення."""
        self.attachments.append(filename)
        print(f"   Додано вкладення: {filename}")
        
    def preview(self):
        """
        Перевизначений метод (Поліморфізм). 
        Додає тему листа до попереднього перегляду.
        """
        status = " (Не прочитано)" if not self.is_read else " (Прочитано)"
        attachment_count = len(self.attachments)
        
        return (f"[EMAIL до {self.recipient}] Тема: {self.subject} (Вкладень: {attachment_count}) "
                f"Від: {self.sender}. {self.content[:30]}..." + status)