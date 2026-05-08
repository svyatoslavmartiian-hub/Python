import os

ORDERS_DATABASE = "orders.txt" 

def create_new_order():
    order_id = input("ID замовлення: ")
    product_name = input("Назва товару: ")
    item_quantity = input("Кількість: ")
    unit_price = input("Ціна за одиницю: ")
    
    order_entry = f"{order_id};{product_name};{item_quantity};{unit_price}\n"
    
    with open(ORDERS_DATABASE, "a", encoding="utf-8") as db_file:
        db_file.write(order_entry)

def display_all_orders():
    if not os.path.exists(ORDERS_DATABASE):
        print("База даних порожня.")
        return
        
    with open(ORDERS_DATABASE, "r", encoding="utf-8") as db_file:
        for current_line in db_file:
            clean_record = current_line.strip().replace(";", " | ")
            print(clean_record)

def update_order_details():
    target_id = input("Введіть ID замовлення для редагування: ")
    updated_records_list = []
    is_order_found = False
    
    if os.path.exists(ORDERS_DATABASE):
        with open(ORDERS_DATABASE, "r", encoding="utf-8") as db_file:
            for line in db_file:
                record_data = line.strip().split(";")
                
                if record_data[0] == target_id:
                    record_data[2] = input("Нова кількість: ")
                    record_data[3] = input("Нова ціна: ")
                    is_order_found = True
                
                updated_records_list.append(";".join(record_data) + "\n")
        
        if is_order_found:
            with open(ORDERS_DATABASE, "w", encoding="utf-8") as db_file:
                db_file.writelines(updated_records_list)
            print("Дані успішно оновлено.")
        else:
            print("Замовлення з таким ID не існує.")

def start_application():
    while True:
        print("\n--- СИСТЕМА ЗАМОВЛЕНЬ ---")
        print("1. Створити | 2. Переглянути | 3. Оновити | 4. Вихід")
        user_choice = input("Ваш вибір: ")
        
        if user_choice == "1": create_new_order()
        elif user_choice == "2": display_all_orders()
        elif user_choice == "3": update_order_details()
        elif user_choice == "4": break

start_application()