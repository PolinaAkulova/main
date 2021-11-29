def sort_sentence(sentence):
    words = sentence.split()            # выполняем слова через пробел и используем список words
    words = sorted(words, key=len)      # Распределение слов по списку
    return " ".join(words).capitalize() # Совмещение слов через пробел в список. соответственно меняем список и вводим в Words


if __name__ == '__main__':
    while True:
        sentence = input("Вход: ")
        print("Вывод:", sort_sentence(sentence))
