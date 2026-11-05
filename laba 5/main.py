# main.py
from alchemy_logic import play_alchemy_game

if __name__ == "__main__":
    try:
        play_alchemy_game()
    except Exception as e:
        print(f"Фатальна помилка програми: {e}")