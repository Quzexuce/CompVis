import tkinter as tk
from tkinter import messagebox

def show_menu(menu):
    for dish, price in menu.items():
        menu_listbox.insert(tk.END, f"{dish}: {price} руб.")

def add_to_order():
    selected_dish = menu_listbox.get(tk.ACTIVE)
    if selected_dish:
        dish_name = selected_dish.split(":")[0]
        quantity = int(quantity_entry.get())
        if dish_name in order:
            order[dish_name] += quantity
        else:
            order[dish_name] = quantity
        update_order_listbox()

def update_order_listbox():
    order_listbox.delete(0, tk.END)
    for dish, quantity in order.items():
        order_listbox.insert(tk.END, f"{dish}: {quantity} порций")

def calculate_total(menu):
    total = 0
    for dish, quantity in order.items():
        total += menu[dish] * quantity
    return total

def show_total():
    total = calculate_total(menu)
    messagebox.showinfo("Итого", f"Итого к оплате: {total} руб.")

menu = {
    "Салат Цезарь": 300,
    "Борщ": 150,
    "Паста Карбонара": 450,
    "Пицца Маргарита": 500,
    "Стейк Рибай": 1200,
    "Чизкейк": 350
}

order = {}

root = tk.Tk()
root.title("Счет, пожалуйста!")

menu_frame = tk.Frame(root)
menu_frame.pack(side=tk.LEFT, padx=10, pady=10)

order_frame = tk.Frame(root)
order_frame.pack(side=tk.RIGHT, padx=10, pady=10)

menu_label = tk.Label(menu_frame, text="Ресторанное меню")
menu_label.pack()

menu_listbox = tk.Listbox(menu_frame)
menu_listbox.pack()

show_menu(menu)

quantity_label = tk.Label(menu_frame, text="Количество")
quantity_label.pack()

quantity_entry = tk.Entry(menu_frame)
quantity_entry.pack()
quantity_entry.insert(0, "1")

add_button = tk.Button(menu_frame, text="Добавить в заказ", command=add_to_order)
add_button.pack()

order_label = tk.Label(order_frame, text="Ваш заказ")
order_label.pack()

order_listbox = tk.Listbox(order_frame)
order_listbox.pack()

total_button = tk.Button(order_frame, text="Показать итоговую сумму", command=show_total)
total_button.pack()

root.mainloop()
