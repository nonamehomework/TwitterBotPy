from botkun.config import *
from botkun.lib.database import get_db_entries


def info(config: BotConfig):
    print("config: " + config.file_path)
    print(str(config))
    if config.use_database:
        entries = get_db_entries(config.database_path)
        print("database {} entries".format(len(entries)))
