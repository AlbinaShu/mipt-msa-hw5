import requests
from collections import Counter


def get_text(url):
    response = requests.get(url)
    return response.text.lower()  # приведение к нижнему регистру


def count_word_frequencies(text):  # подсчет всех слов сразу
    words = text.split()
    return Counter(words)  # один проход по тексту


def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    words_to_count = []
    with open(words_file, 'r') as file:
        for line in file:
            word = line.strip().lower()  # приведение к нижнему регистру
            if word:
                words_to_count.append(word)

    text = get_text(url)  # загрузка сайта один раз

    all_counts = count_word_frequencies(text)  # получение частоты всех слов сразу

    frequencies = {}
    for word in words_to_count:
        frequencies[word] = all_counts[word]   # берётся уже посчитанное количество этого слова
    
    print(frequencies)


if __name__ == "__main__":
    main()