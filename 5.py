import re 
from collections import Counter 

def count_words (path):
    with open (path, encoding='utf-8') as file:
        all_words = re.findall(r'[0-9a-zA-Z-]+', file.read())
        all_words = [words.upper() for words in all_words]
        print('\nTotalWords:', len(all_words))

        word_counts = Counter()
        for word in all_words:
            word_counts[word] +=1

        print('\nTop 50 words:')
        for word in word_counts.most_common(50):
            print(word[0], '\t\t', word[1])

name_of_file = str(input())
count_words(name_of_file)
