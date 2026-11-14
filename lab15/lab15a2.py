import lab15a1
import math

print("  ДЕМОНСТРАЦІЯ КЛАСУ BIKE (Велосипед)")

bike_a = lab15a1.Bike(weight=12.5, price=8500, wheel_diameter=28, color="Blue")

print("1. Початкові деталі:\n",bike_a.get_details())

bike_a.change_price(9200.50)
print("2. Після зміни ціни:\n",bike_a.get_details())

bike_a.change_color("Red") 
print("3. Після зміни кольору:\n",bike_a.get_details())

print("  ДЕМОНСТРАЦІЯ УСПАДКОВАННЯ (COMPUTER -> TABLET)")

pc_desktop = lab15a1.Computer(cpu="Intel i7", ram=32, os="Linux")
print("\nСтворено об'єкт: PC_DESKTOP (Computer)")
pc_desktop.run_program("IDE")
pc_desktop.display_specs()
print("-" * 15)

tablet_pro = lab15a1.Tablet(cpu="Snapdragon", ram=8, os="Android", 
                               screen_size=10.5, has_cellular=True)
print("\nСтворено об'єкт: TABLET_PRO (Tablet)")

tablet_pro.run_program("Mobile Game") 
tablet_pro.display_specs()
tablet_pro.check_cellular()