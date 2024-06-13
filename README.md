# Игра "Перевод слов"

## Обзор

"Перевод слов" — это интерактивная консольная игра на Python, которая получает случайные английские слова и их определения с веб-сайта и переводит их на русский язык. Затем игроку предлагается угадать слово по его переведенному определению. Этот проект демонстрирует использование веб-скрапинга, сервисов перевода и базовой игровой логики на Python.

## Особенности

- Получение случайных английских слов и их определений с веб-источника.
- Перевод полученных слов и определений на русский язык с использованием библиотеки `translate`.
- Интерактивная консольная игра, в которой игроки угадывают слово по его переведенному определению.
- Обратная связь по правильности ответа и возможность играть несколько раундов.

## Установка

1. **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/ваш-имя-пользователя/word-translation-game.git
    cd word-translation-game
    ```

2. **Создайте виртуальное окружение (необязательно, но рекомендуется):**
    ```bash
    python -m venv venv
    source venv/bin/activate   # В Windows: venv\Scripts\activate
    ```

3. **Установите необходимые библиотеки:**
    ```bash
    pip install -r requirements.txt
    ```

## Требования

- Python 3.x
- Библиотека `requests` для выполнения HTTP-запросов.
- Библиотека `beautifulsoup4` для парсинга HTML.
- Библиотека `translate` для переводческих сервисов.

Установите эти библиотеки с помощью pip:
```bash
pip install requests beautifulsoup4 translate
```

## Использование

Запустите игровой скрипт:
```bash
python igra.py
```

## Объяснение кода

Основные компоненты игры:

1. **Получение случайных слов:**
    ```python
    import requests
    from bs4 import BeautifulSoup
    from translate import Translator

    def get_english_words():
        url = "https://randomword.com"
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
            english_word_element = soup.find("div", id="random_word")
            word_definition_element = soup.find("div", id="random_word_definition")

            if english_word_element is None или word_definition_element is None:
                print("Не удалось найти необходимые элементы на странице")
                return None

            english_words = english_word_element.text.strip()
            word_definition = word_definition_element.text.strip()

            translator = Translator(to_lang="ru")
            translated_word = translator.translate(english_words)
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
    ```

2. **Логика игры:**
    ```python
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
    ```

## Лицензия

Этот проект лицензируется по лицензии MIT. Подробности см. в файле [LICENSE](LICENSE).

