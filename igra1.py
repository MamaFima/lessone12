import requests
from bs4 import BeautifulSoup
from translate import Translator

def get_english_words():
    url = "https://randomword.com"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        if english_word is None or word_definition is None:
            print("Не удалось найти необходимые элементы на странице")
            return None

        translator = Translator(to_lang="ru")
        translated_word = translator.translate(english_word)
        translated_definition = translator.translate(word_definition)

        return {
            "english_words": translated_word,
            "word_definition": translated_definition
        }
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



