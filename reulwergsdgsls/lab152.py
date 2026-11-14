import lab151 as geometry 

print("=========================================")
print("  ДЕМОНСТРАЦІЯ КЛАСУ PARALELOGRAM")
print("=========================================")

p1 = geometry.Paralelogram(side_a=5.0, side_b=8.0, angle_alpha_deg=30)
p2 = geometry.Paralelogram(side_a=10.0, side_b=10.0, angle_alpha_deg=90)

print(f"\nПаралелограм 1 ({p1.get_details()}):")
p1_perimeter = p1.calculate_perimeter()
print(f"  - Периметр (P): {p1_perimeter}")
p1_area = p1.calculate_area()
print(f"  - Площа (S): {p1_area:.2f}")

print(f"\nПаралелограм 2 ({p2.get_details()}):")
p2_perimeter = p2.calculate_perimeter()
print(f"  - Периметр (P): {p2_perimeter}")
p2_area = p2.calculate_area()
print(f"  - Площа (S): {p2_area:.2f}")

print("\n" + "="*45)
print("  ДЕМОНСТРАЦІЯ УСПАДКОВАННЯ (MESS -> MAILMESS)")
print("="*45)

sms1 = geometry.Mess("Mom", "Me", "Купи хліб і молоко, будь ласка.")
print("\nСтворено об'єкт: SMS1 (Mess)")
print("  Попередній перегляд:", sms1.preview())
sms1.mark_as_read()
print("  Попередній перегляд:", sms1.preview())
print("-" * 15)

email_work = geometry.MailMess("Manager", "User", 
                                "Нагадую про сьогоднішній мітинг о 15:00. Будь ласка, підготуйте звіт.", 
                                "Нагадування про мітинг")
email_work.add_attachment("meeting_agenda.pdf")
print("\nСтворено об'єкт: EMAIL_WORK (MailMess)")

print("  Попередній перегляд:", email_work.preview()) 

email_work.mark_as_read()

print("  Попередній перегляд:", email_work.preview())