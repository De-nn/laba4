from collections import Counter
import os

def load_dictionary():
    # Путь к файлу nouns.txt 
    file_path = os.path.join(os.path.dirname(__file__), "nouns.txt")
    with open(file_path, encoding='utf-8') as f:
        words = [line.strip() for line in f if line.strip()]
    return words

def find_anagrams(input_word, words_list):
    input_counter = Counter(input_word)
    valid_words = []
    for word in words_list:
        if len(word) <= len(input_word) and Counter(word) <= input_counter:
            valid_words.append(word)
    valid_words.sort(key=len, reverse=True)
    return valid_words

def main():
    # Загрузка словаря
    dictionary = load_dictionary()

    while True:
        # Ввод от пользователя
        query = input("Введите слово ").strip().lower()
        if query in ('выход', 'exit', ''):
            print("Выход из программы.")
            break

        # Поиск подходящих слов
        anagrams = find_anagrams(query, dictionary)

        # Вывод результатов
        print("\nНайденные слова:")
        for word in anagrams:
            print(word)
        print()

if __name__ == "__main__":
    main()

