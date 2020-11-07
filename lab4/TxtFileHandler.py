from collections import defaultdict


def generate_tokens_from_txt(filename):
    tokens = []
    with open(filename, encoding='utf-8') as infile:
        infile = "".join(line for line in infile if not line.isspace())
        infile = ''.join(c for c in infile if c not in """,.?!-;()"'""")
        for line in infile.split():
            for token in line.split():
                tokens.append(token.lower())

    return tokens

def count_words(tokens):
    counted_words = defaultdict(int)
    for token in tokens:
        counted_words[token] += 1

    counted_words = sorted(counted_words.items(), key=lambda x: x[1], reverse=True)

    return counted_words

def generate_digram(tokens):
    two_words = defaultdict(int)
    for index in range(len(tokens) - 1):
        two_words[tokens[index] + " " + tokens[index + 1]] += 1

    two_words = sorted(two_words.items(), key=lambda x: x[1], reverse=True)
    return two_words

def generate_trigram(tokens):
    three_words = defaultdict(int)
    for index in range(len(tokens) - 2):
        three_words[tokens[index] + " " + tokens[index + 1] + " " + tokens[index + 2]] += 1

    three_words = sorted(three_words.items(), key=lambda x: x[1], reverse=True)
    return three_words

def get_x_records(words_dictionary, x=20):
    # words_dictionary = sorted(words_dictionary.items(), key=lambda x: x[1], reverse=True)
    top_x = []
    for i in range(x):
        top_x.append((words_dictionary[i][0], words_dictionary[i][1]))

    i=x
    while(words_dictionary[i][1] == top_x[x-1][1]):
        top_x.append((words_dictionary[i][0], words_dictionary[i][1]))
        i += 1

    print(top_x)







tokens = generate_tokens_from_txt("potop.txt")
print(count_words(tokens))
print(generate_digram(tokens))
print(generate_trigram(tokens))
trigram = generate_trigram(tokens)

print(get_x_records(trigram))

