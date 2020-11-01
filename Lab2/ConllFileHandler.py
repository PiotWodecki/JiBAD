import os

class ConllFileHandler:
    path = os.getcwd()

    def __init__(self):
        self.path = os.path.join(self.path, "nkjp.conll")

    def get_path(self):
        return self.path


    @staticmethod
    def get_tokens_from_conll_file(path_to_file):
        f = open(path_to_file, "r", encoding="utf-8")
        lines = f.readlines()
        result = []
        for x in lines:
            result.append(x.split(' \"')[0])
        f.close()
        result = [i.replace('"', '') for i in result]
        return result

    @staticmethod
    def get_sentence_from_tokens(tokens):
        sentences = []
        sentence = ""
        end_of_sentence = ['.', '?', '!']
        for token in tokens:
            if sentence == "" or token == ',' or token == ';' or token in end_of_sentence:
                sentence += token
            elif token != ',':
                sentence += " " + token

            if token in end_of_sentence:
                sentences.append(sentence)
                sentence = ""

        print(sentences)


handler = ConllFileHandler()
tokens = handler.get_tokens_from_conll_file(handler.get_path())
handler.get_sentence_from_tokens(tokens)
