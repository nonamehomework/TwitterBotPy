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
    words.insert(0, "")  # head of string
    words.append("")  # last of string
    for i in range(len(words) - 2):
        word_block.append([words[i], words[i + 1], words[i + 2]])

    return word_block


def connect_word_blocks(word_blocks: [[str]], connected_indexes=None) -> [int]:
    if connected_indexes is None:
        connected_indexes = []

    last_word = ""
    if len(connected_indexes) != 0:
        last_word = word_blocks[connected_indexes[-1]][2]
        if last_word == "":  # in case last word is end of string
            return connected_indexes

    next_candidate = []
    for index, word_block in enumerate(word_blocks):
        if (word_block[0] == last_word) and (index not in connected_indexes):
            next_candidate.append(index)

    if len(next_candidate) == 0:
        return connected_indexes
    else:
        i = randint(0, len(next_candidate) - 1)
        return connect_word_blocks(word_blocks, connected_indexes + [next_candidate[i]])


def create_list_from_indexes(lst: list, indexes: [int]) -> list:
    return [lst[i] for i in indexes]


def create_db_entries(tweet: dict, mecab: Tagger) -> [dict]:
    db_entries = []
    words = parse_string(tweet["text"], mecab)
    word_block = create_word_block(words)  # [['', 'hello', 'world'],['hello', 'world', '!']]
    for block in word_block:
        db_entries.append({
            "word1": block[0],
            "word2": block[1],
            "word3": block[2],
            "id": tweet["id"],
            "user": tweet["user"]["screen_name"]
        })

    return db_entries


def create_string_from_blocks(blocks: [dict]) -> str:
    string = ""
    for e in blocks:
        string += e["word2"] + e["word3"]

    return string
