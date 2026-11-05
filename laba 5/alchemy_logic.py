# alchemy_logic.py
import random


def play_alchemy_game():
    print("=== АЛХІМІЧНА ЛАБОРАТОРІЯ ===")
    print("Вам потрібно вгадати секретний номер інгредієнта (від 1 до 20), щоб зварити легендарне зілля!")

    while True:  # Зовнішній цикл для повторення гри
        secret_ingredient = random.randint(1, 20)
        attempts = 3
        game_won = False

        while attempts > 0:
            try:
                print(f"\nЗалишилось спроб: {attempts}")
                user_input = input("Введіть номер інгредієнта (або 'q' для виходу): ").strip()

                if user_input.lower() == 'q':
                    print("Ви залишили лабораторію.")
                    return

                guess = int(user_input)

                if guess < 1 or guess > 20:
                    print("⚠️ Помилка: Інгредієнт має бути в межах від 1 до 20!")
                    continue

                if guess == secret_ingredient:
                    print("\n🎉 ВИГРАШ! Ви успішно підібрали інгредієнт і зварили еліксир!")
                    game_won = True
                    break
                elif guess < secret_ingredient:
                    print("📈 Занадто малий номер інгредієнта.")
                else:
                    print("📉 Занадто великий номер інгредієнта.")

                attempts -= 1

            except ValueError:
                print("❌ Помилка вводу! Потрібно ввести ціле число.")
            except Exception as e:
                print(f"❌ Сталася непередбачена помилка: {e}")

        if not game_won:
            print(f"\n❌ ПРОГРАШ! Спроби скінчилися. Правильний інгредієнт був: {secret_ingredient}")

        # Запит на повторну гру
        try:
            choice = input("\nБажаєте зіграти ще раз? (так/ні або t/n): ").strip().lower()
            if choice not in ['так', 'т', 'y', 'yes']:
                print("Дякуємо за гру! До зустрічі.")
                break
            print("\n" + "=" * 30 + "\nНОВА ГРА РОЗПОЧАЛАСЬ!\n" + "=" * 30)
        except Exception:
            break