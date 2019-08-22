from botkun.lib.database import *


def clear():
    result = clear_db("bot")
    if result:
        print("Clear succeed")
    else:
        print("Error occurred during clearing")
        exit(-1)
