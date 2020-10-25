import os
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

class TxtFileHandler:
    path = os.getcwd()

    def __init__(self):
        self.path = os.path.join(self.path, "nkjp.txt")

    def get_path(self):
        return self.path

    @staticmethod
    def read_txt_file(pathToFile):
        file = open(pathToFile, "r", encoding='utf-8')
        text = file.read()
        file.close()
        return text

    @staticmethod
    def tokenize_txt_file(txt_file):
        tokenized_text = word_tokenize(txt_file)
        print(tokenized_text)

    @staticmethod
    def sentence_tokenize_txt_file(txt_file):
        tokenized_text = sent_tokenize(txt_file)
        print(tokenized_text)


handler = TxtFileHandler()
text = handler.read_txt_file(handler.get_path())
handler.tokenize_txt_file(text)
handler.sentence_tokenize_txt_file(text)

# Żeby odczytać cały tekst w konsoli musimy zwiększyć bufer konsoli, można to zrobić w File > Settings > Editor >
# > Console  > Override console cycle buffer