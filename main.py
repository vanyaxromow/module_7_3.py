class WordsFinder:
    def __init__(self, *args):
        self.file_name = args

    def get_all_words(self):
        all_words = {}
        str_ = ''
        lst = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in self.file_name:
            with open(i, encoding='utf-8') as file:
                for i in file:
                    if i not in lst:
                        str_ += i.lower()

        all_words[self.file_name] = str_.split()
        return all_words

    def find(self, word):
        dict_ = {}
        fl = 1
        for name, words in self.get_all_words().items():
            for i in words:
                if i == word.lower():
                    break
                else:
                    fl += 1
        dict_[self.file_name] = fl
        return dict_

    def count(self, word):
        dict_ = {}
        fl = 0
        for name, words in self.get_all_words().items():
            for i in words:
                if i == word.lower():
                    fl += 1
        dict_[self.file_name] = fl
        return dict_


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
