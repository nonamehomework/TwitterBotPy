from botkun.lib.twitter_handler import *
from botkun.lib.markov import *
from botkun.lib.database import *
import random

max_try = 100


def tweet(local: bool, use_database: bool):
    db_entries = []
    if use_database:
        db_entries += get_db_entries("bot")
        print("got {} entries from database".format(len(db_entries)))
    else:
        filtered_tweets = get_filtered_tweets("bottokuxn")

        print("got {} tweets".format(len(filtered_tweets)))

        if len(filtered_tweets) == 0:
            return

        mecab = create_mecab()
        for tw in filtered_tweets:
            db_entries += create_db_entries(tw, mecab)

        print("created {} entries".format(len(db_entries)))

    word_blocks = [[e["word1"], e["word2"], e["word3"]] for e in db_entries]
    candidates = []
    for i in range(max_try):
        indexes = connect_word_blocks(word_blocks)
        candidate = create_list_from_indexes(db_entries, indexes)
        if is_enough_quality(candidate):
            candidates.append(candidate)

    if len(candidates) == 0:
        print("Couldn't create enough quality tweet")
        exit(-1)

    choice = random.choice(candidates)

    text = create_string_from_blocks(choice)
    authors = [([e["word1"], e["word2"], e["word3"]], e["user"]) for e in choice]

    for e in authors:
        print(e)
    print("text: {}".format(text))

    if not local:
        res = post_tweet_with_session(text)
        if res:
            print("Post succeed")
        else:
            print("Twitter Error Occurred")
            exit(-1)


def is_enough_quality(candidate: [dict]) -> bool:
    cost = 0
    length = len(candidate)
    for i in range(length - 1):
        if candidate[i]["id"] == candidate[i + 1]["id"]:
            cost += 1

    return length <= 15 and cost < length / 3
