import requests


def get_english_words():
    url = "https://random-word-api.herokuapp.com/word?number=1"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на успешный ответ от сервера
        words = response.json()

        if words:
            english_words = words[0]
            word_definition = "Definition not available"  # Фиктивное определение

            return {
                "english_words": english_words,
                "word_definition": word_definition
            }
        else:
            print("Не удалось получить слово")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка при запросе: {e}")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_dict = get_english_words()
        if word_dict is None:
            print("Не удалось получить слово, попробуйте еще раз.")
            continue

        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово? ")
        if user.lower() == word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, правильное слово - {word}")

        play_again = input("Хотите сыграть еще раз? y/n ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break


word_game()
