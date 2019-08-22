from botkun.lib.twitter_handler import *
from botkun.lib.markov import *
from botkun.lib.database import *
from botkun.config import BotConfig
import random

max_try = 100


def tweet(config: BotConfig):
    db_entries = []
    if config.use_database:
        db_entries += get_db_entries(config.database_path)
        print("got {} entries from database".format(len(db_entries)))
    else:
        filtered_tweets = get_filtered_tweets(
            config.consumer_key,
            config.consumer_secret,
            config.access_token,
            config.access_secret,
            config.twitter_user_name
        )

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

    for e in choice:
        print(([e["word1"], e["word2"], e["word3"]], e["user"]))
        delete_success = delete_db_entries_by_id(config.database_path, e["id"])
        if not delete_success:
            print("Failed to delete entry from database")

    print("text: {}".format(text))

    if not config.local:
        res = post_tweet_with_session(
            text,
            config.consumer_key,
            config.consumer_secret,
            config.access_token,
            config.access_secret
        )
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
