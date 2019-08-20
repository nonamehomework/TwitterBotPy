from twitter import Api
from twitter import TwitterError


def get_home_timeline(session: Api) -> [dict]:
    try:
        timeline = session.GetHomeTimeline(count=200, exclude_replies=True, include_entities=False)
        return [status.AsDict for status in timeline]
    except TwitterError:
        return []


def send_tweet(status: str, session: Api) -> bool:
    try:
        response = session.PostUpdate(status=status)
        return True
    except TwitterError:
        return False


def create_session(consumer_key: str, consumer_secret: str, access_token: str, access_secret: str) -> Api:
    api = Api(consumer_key=consumer_key,
              consumer_secret=consumer_secret,
              access_token_key=access_token,
              access_token_secret=access_secret)
    return api
