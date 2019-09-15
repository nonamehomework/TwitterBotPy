from twitter import Api
from twitter import TwitterError
from typing import List, Dict, Any

Tweet = Dict[str, Any]


def get_filtered_tweets(consumer_key: str,
                        consumer_secret: str,
                        access_token: str,
                        access_secret: str,
                        my_screen_name="") -> List[Tweet]:
    session = create_session(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_secret=access_secret)
    timeline = get_home_timeline(session)

    filtered = [t for t in timeline if can_tweet_be_used(t, my_screen_name)]

    return filtered

def can_tweet_be_used(t: Tweet, my_screen_name: str) -> bool:
    return (t["user"]["screen_name"] != my_screen_name and
            "http" not in t["text"] and
            "RT" not in t["text"] and
            "#" not in t["text"] and
            "@" not in t["text"]
            )


def get_home_timeline(session: Api) -> List[Tweet]:
    try:
        timeline = session.GetHomeTimeline(count=200, exclude_replies=True, include_entities=False)
        return [status.AsDict() for status in timeline]
    except TwitterError:
        return []


def post_tweet(status: str, session: Api) -> bool:
    try:
        session.PostUpdate(status=status)
        return True
    except TwitterError:
        return False


def post_tweet_with_session(status: str,
                            consumer_key: str,
                            consumer_secret: str,
                            access_token: str,
                            access_secret: str,
                            ) -> bool:
    session = create_session(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_secret=access_secret)
    return post_tweet(status, session)


def create_session(consumer_key: str, consumer_secret: str, access_token: str, access_secret: str) -> Api:
    api = Api(consumer_key=consumer_key,
              consumer_secret=consumer_secret,
              access_token_key=access_token,
              access_token_secret=access_secret)
    return api
