class WordFinder:

    def __init__(self):
        self.word = input(' Введите искомое слово: ')
        self.path = input('\n Введите путь к файлу: ')

    def count_word(self):
        while True:
            try:
                with open(self.path, 'r') as file:
                    raw_text = file.read()
                text = raw_text.strip().lower()  # :D
                answer = text.count(self.word.strip().lower())
                print("\n Найдено вхождений слова '{1}': {0}".format(answer, self.word))
                break
            except:
                print('\n Ошибка!')
                self.path = input('\n Попробуйте ввести путь еще раз или введите exit для выхода: ')
                if self.path == 'exit':
                    break


if __name__ == '__main__':
    finder = WordFinder()
    finder.count_word()
