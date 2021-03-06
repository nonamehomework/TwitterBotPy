from argparse import ArgumentParser
from botkun.add import add
from botkun.tweet import tweet
from botkun.clear import clear
from botkun.info import info
from botkun.config import *


def main():
    options = parse_argument()
    bot_config = get_config(options["config"])
    bot_config.save_arguments(options)

    if options["action"] == "add":
        if bot_config.use_database:
            add(bot_config)
        else:
            print("no database mode detected.")
            print("nothing to do")

    elif options["action"] == "tweet":
        tweet(bot_config)

    elif options["action"] == "clear":
        if bot_config.use_database:
            clear(bot_config)
        else:
            print("no database mode detected.")
            print("nothing to do")

    elif options["action"] == "info":
        info(bot_config)

    else:
        exit(-1)  # unreachable code


def parse_argument() -> dict:
    parser = ArgumentParser()
    parser.add_argument("action",
                        choices=["add", "tweet", "clear", "info"])
    parser.add_argument("-c", "--config",
                        type=str,
                        default="",
                        help="custom config path")
    parser.add_argument("-l", "--local",
                        action="store_true",
                        help="don't post tweet.py, only to console output")
    parser.add_argument("--no-database",
                        action="store_true",
                        help="no database mode")

    args = parser.parse_args()

    return {"action": args.action,
            "config": args.config,
            "local": args.local,
            "database": not args.no_database
            }


if __name__ == "__main__":
    main()
