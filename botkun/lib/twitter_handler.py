from twitter import Api
from twitter import TwitterError


def get_filtered_tweets(consumer_key: str,
                        consumer_secret: str,
                        access_token: str,
                        access_secret: str,
                        my_screen_name="") -> [dict]:
    session = create_session(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_secret=access_secret)
    timeline = get_home_timeline(session)

    tweet_filter = (lambda s:
                    s["user"]["screen_name"] != my_screen_name and
                    "http" not in s["text"] and
                    "RT" not in s["text"] and
                    "#" not in s["text"])

    filtered = [s for s in timeline if tweet_filter(s)]

    return filtered


def get_home_timeline(session: Api) -> [dict]:
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
