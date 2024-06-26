import requests
from bs4 import BeautifulSoup
from googletrans import Translator


def get_english_words():
    url = "https://randomword.com"
    try:
        response = requests.get(url)
        #print(response.text)
        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        translator = Translator()
        #translated_word = translator.translate(english_words, src='en', dest='ru').text.strip()
        #translated_definition = translator.translate(word_definition, src='en', dest='ru').text.strip()

        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except:
        print("Произошла ошибка")

def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово?")
        if user == word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, правильное слово - {word}")

        play_again = input("Хотите сыграть еще раз? y/n")
        if play_again != "y":
            print("Спасибо за игру!")
            break

word_game()


