from pydiscordbot.bot import PyDiscordBot

import argparse
import os
import signal
import yaml


DEFAULT_CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.yml")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config-file", type=argparse.FileType("r"), default=DEFAULT_CONFIG_FILE)

    args = parser.parse_args()

    config = yaml.load(args.config_file)

    bot = PyDiscordBot(**config)
    bot.start()

    signal.signal(signal.SIGINT, lambda: bot.disconnect())
