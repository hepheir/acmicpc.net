# 6088번: Scrabble

from collections import Counter
from pathlib import Path


DICT_FILE = Path(__file__).parent.resolve() / 'dict.txt'


VALUE_LETTER_MAP = {
    0: '#',
    1: 'AEILNORSTU',
    2: 'DG',
    3: 'BCMP',
    4: 'FHVWY',
    5: 'K',
    8: 'JX',
    10: 'QZ',
}

LETTER_VALUE_MAP = {}

for value, letters in VALUE_LETTER_MAP.items():
    for letter in letters:
        LETTER_VALUE_MAP[letter] = value


def main():
    input_file = open(0, 'rt')
    dict_file = DICT_FILE.open('rt')
    try:
        T = int(input_file.readline())
        user_letters = [input_file.readline().strip() for _ in range(T)]
        user_counter = Counter(user_letters)

        max_score = 0
        max_word = ''

        while (word := dict_file.readline().strip()):
            dict_counter = Counter(word)
            score = get_score(user_counter, dict_counter)
            if max_score < score:
                max_score = score
                max_word = word

        print(max_word)
    except:
        pass
    finally:
        input_file.close()
        dict_file.close()


def get_score(user_counter: Counter[str], dict_counter: Counter[str]) -> int:
    unmatched = 0
    score = 0
    for letter in dict_counter:
        unmatched += max(0, dict_counter[letter] - user_counter[letter])
        score += LETTER_VALUE_MAP[letter] * min(dict_counter[letter], user_counter[letter])
    unmatched -= min(unmatched, user_counter['#'])

    if unmatched > 0:
        return -1

    return score


if __name__ == '__main__':
    main()
