from botkun.lib.database import *
from botkun.config import BotConfig


def clear(config: BotConfig):
    result = clear_db(config.database_path)
    if result:
        print("Clear succeed")
    else:
        print("Error occurred during clearing")
        exit(-1)
