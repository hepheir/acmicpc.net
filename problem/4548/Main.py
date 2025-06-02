import sys


PREFIX = {
    'anti': 'against {word}',
    'post': 'after {word}',
    'pre': 'before {word}',
    're': '{word} again',
    'un': 'not {word}',
}

SUFFIX = {
    'er': 'one who {word}s',
    'ing': 'to actively {word}',
    'ize': 'change into {word}',
    's': 'multiple instances of {word}',
    'tion': 'the process of {word}ing',
}

def split_prefix(word: str):
    for prefix in PREFIX:
        if word.startswith(prefix):
            return prefix, word[len(prefix):]
    return None, word


def split_suffix(word: str):
    for suffix in SUFFIX:
        if word.endswith(suffix):
            return suffix, word[:-len(suffix)]
    return None, word


N = int(sys.stdin.readline())
for _ in range(N):
    word = sys.stdin.readline().strip()
    prefix, word = split_prefix(word)
    suffix, word = split_suffix(word)

    definition = word
    if suffix is not None:
        definition = SUFFIX[suffix].format(word=definition)
    if prefix is not None:
        definition = PREFIX[prefix].format(word=definition)
    print(definition)
