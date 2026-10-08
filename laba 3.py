# Клас для опису товару
class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id  # Унікальний ID товару
        self.name = name  # Назва
        self.price = price  # Ціна (число)
        self.quantity = quantity  # Кількість на складі

    # Лямбда-функція для форматування ціни у форматі xxx.xxгрн
    format_price = lambda self: f"{self.price:.2f}грн"


# Клас магазину, що керує товарами та покупками
class Store:
    def __init__(self):
        #каталог товарів
        self.products = [
            Product(1, "Яблука", 25.50, 50),
            Product(2, "Молоко", 38.00, 20),
            Product(3, "Хліб", 18.25, 30),
            Product(4, "Шоколад", 45.00, 15)
        ]
        self.cart = []  # Кошик покупця

    def show_catalog(self):
        print("\n--- КАТАЛОГ ТОВАРІВ ---")
        for p in self.products:
            print(f"ID: {p.product_id} | {p.name} — {p.format_price()} | В наявності: {p.quantity} шт.")

    def add_to_cart(self):
        self.show_catalog()
        try:
            p_id = int(input("Введіть ID товару, який хочете додати в кошик: "))
            qty = int(input("Введіть кількість: "))

            # Товар за ід
            product = next((p for p in self.products if p.product_id == p_id), None)

            if product and product.quantity >= qty:
                # Перевірка кошика
                existing_item = next((item for item in self.cart if item["product"].product_id == p_id), None)

                if existing_item:
                    # Якшо є то додаєм +
                    existing_item["qty"] += qty
                else:
                    # якшо нема добавляєм нове
                    self.cart.append({"product": product, "qty": qty})

                print(f"Товар '{product.name}' (шт: {qty}) успішно додано до кошика!")
            else:
                print("Помилка: такого товару немає або недостатньо на складі.")
        except ValueError:
            print("Будь ласка, вводьте тільки числа!")

    # Перегляд кошику
    def show_cart(self):
        if not self.cart:
            print("\nВаш кошик наразі порожній.")
            return

        print("\n--- ВАШ КОШИК ---")
        total = 0
        for index, item in enumerate(self.cart):
            p = item["product"]
            q = item["qty"]
            cost = p.price * q
            total += cost
            print(f"[{index}] {p.name} — {p.format_price()} x {q} шт. = {cost:.2f}грн")
        print(f"Загальна сума в кошику: {total:.2f}грн")

    def remove_from_cart(self):
        # показ що є в кошику
        if not self.cart:
            print("\nВаш кошик порожній, нічого видаляти.")
            return

        self.show_cart()

        try:
            idx = int(input("Введіть номер товару в кошику (в квадратних дужках), який хочете видалити: "))
            if 0 <= idx < len(self.cart):
                removed = self.cart.pop(idx)
                print(f"Товар '{removed['product'].name}' видалено з кошика.")
            else:
                print("Невірний індекс товару.")
        except ValueError:
            print("Введіть числове значення.")

    def checkout(self):
        if not self.cart:
            print("\nВаш кошик порожній, нічого купувати.")
            return

        print("\n--- ОФОРМЛЕННЯ ПОКУПКИ ---")
        total = 0
        for item in self.cart:
            p = item["product"]
            q = item["qty"]
            cost = p.price * q
            total += cost
            # - залишок на складі
            p.quantity -= q
            print(f"- {p.name} x {q} = {cost:.2f}грн")

        # функція знижки якщо товар 100+ грн
        apply_discount = lambda sum_val: sum_val * 0.95 if sum_val > 100 else sum_val
        final_total = apply_discount(total)

        if final_total < total:
            print(f"Застосовано знижку 5%! Разом до сплати: {final_total:.2f}грн")
        else:
            print(f"Разом до сплати: {total:.2f}грн")

        # очищеня кошика
        self.cart.clear()
        print("Дякуємо за покупку!")

    def admin_panel(self):
        password = input("Введіть пароль адміністратора: ")
        if password == "admin123":
            print("\n--- ПАНЕЛЬ АДМІНІСТРАТОРА (ЗАЛИШКИ) ---")
            for p in self.products:
                print(f"Товар: {p.name} | Залишок на складі: {p.quantity} шт. | Ціна: {p.format_price()}")
        else:
            print("Неправильний пароль!")


# Менюха йоу
def main():
    store = Store()

    while True:
        print("\n=== МІНІ-МАГАЗИН ===")
        print("1. Переглянути каталог товарів")
        print("2. Додати товар у кошик")
        print("3. Переглянути мій кошик")  # Новий пункт
        print("4. Видалити товар з кошика")
        print("5. Купити товари з кошика")
        print5_num = 6  # Зміщеня пунктів
        print("6. Увійти як адміністратор")
        print("7. Вихід")

        choice = input("Оберіть дію (1-7): ")

        if choice == "1":
            store.show_catalog()
        elif choice == "2":
            store.add_to_cart()
        elif choice == "3":
            store.show_cart()  # Перегляд кошику
        elif choice == "4":
            store.remove_from_cart()
        elif choice == "5":
            store.checkout()
        elif choice == "6":
            store.admin_panel()
        elif choice == "7":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()