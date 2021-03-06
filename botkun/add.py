from botkun.lib.twitter_handler import *
from botkun.lib.markov import *
from botkun.lib.database import *
from botkun.config import BotConfig


def add(config: BotConfig):
    filtered_tweets = get_filtered_tweets(
        config.consumer_key,
        config.consumer_secret,
        config.access_token,
        config.access_secret,
        config.twitter_user_name
    )

    latest = get_latest_tweet(config.database_path)
    filtered_tweets = [t for t in filtered_tweets if t["id"] > latest]
    print("got {} tweets".format(str(len(filtered_tweets))))

    if len(filtered_tweets) == 0:
        return

    mecab = create_mecab()
    db_entries = []
    for tweet in filtered_tweets:
        db_entries += create_db_entries(tweet, mecab)

    print("created {} entries".format(str(len(db_entries))))

    count = add_to_database(config.database_path, db_entries)
    print("database {} entries".format(str(count)))
