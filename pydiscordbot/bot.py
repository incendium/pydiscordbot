from pydiscordbot.util import get_timestamp

import irc.bot
import re


class Hostname(object):
    def __init__(self, hostname):
        tokens = re.split(r"[!@]", hostname)
        self.username = tokens[0]
        self.ident = tokens[1]
        self.host = tokens[2]


class PyDiscordBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, password, server, port):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, password)], nickname, nickname)
        self.channel = channel

    def on_welcome(self, client, event):
        print("[%s] Connected." % (get_timestamp(), ))
        print("[%s] Joining %s..." % (get_timestamp(), self.channel))
        client.join(self.channel)

    def on_join(self, client, event):
        print("[%s] Joined %s." % (get_timestamp(), event.target))

    def on_pubmsg(self, client, event):
        print("[%s] <%s> %s" % (get_timestamp(), Hostname(event.source).username, event.arguments[0]))
