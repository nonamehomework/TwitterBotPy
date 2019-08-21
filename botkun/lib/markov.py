from MeCab import Tagger
from random import randint


def create_mecab(arg="") -> Tagger:
    mecab = Tagger(arg)
    mecab.parse("")  # dummy
    return mecab


def parse_string(string: str, mecab: Tagger) -> [str]:
    parsed = []
    node = mecab.parseToNode(string)
    while node:
        if node.surface != "":
            parsed.append(node.surface)

        node = node.next

    return parsed


def create_word_block(words: [str]) -> [[str]]:
    word_block = []
    for i in range(len(words) - 2):
        word_block.append([words[i], words[i + 1], words[i + 2]])

    return word_block


def connect_word_blocks(word_blocks: [[str]], connected_indexes=None) -> [int]:
    if connected_indexes is None:
        connected_indexes = []
    last_word = "" if len(connected_indexes) == 0 else word_blocks[connected_indexes[-1]][2]

    next_candidate = []
    for index, word_block in enumerate(word_blocks):
        if index not in connected_indexes and word_block[0] == last_word:
            next_candidate.append(index)

    if len(next_candidate) == 0:
        return []
    else:
        next_index = randint(0, len(next_candidate) - 1)
        connect_word_blocks(word_blocks, connected_indexes + [next_index])
