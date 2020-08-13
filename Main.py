import Config
from twitchio.ext import commands
from colorama import init
from discord import Webhook, AsyncWebhookAdapter, Embed
import aiohttp
import asyncio
import datetime

class Bot(commands.Bot):

    def __init__(self):
        init()
        super().__init__(irc_token = Config.TOKEN, nick = Config.NICK, prefix = Config.PREFIX, initial_channels = [Config.NICK])
        self.default = "\033[1;0;4m"
        self.green = "\033[1;32;40m"
        self.magenta = "\033[1;35;40m"
        self.blue = "\033[1;34;40m"

    async def event_ready(self):
        print(f"{self.green}[Success]{self.default} Twitch Bot has started!")

        channel = self.get_channel("polar_dev")
        while True:
            await asyncio.sleep(1)
            for message in Config.CLUSTER["bridge"]["messages"].find({}):
                await channel.send("From Discord - " + message["author"] + ": " + message["content"])
                Config.CLUSTER["bridge"]["messages"].delete_one({"_id": message["_id"]})

    async def event_message(self, message):
        if "From Discord - " not in message.content:
            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url(Config.WEBHOOK, adapter = AsyncWebhookAdapter(session))
                embed = Embed(
                    description = message.content,
                    timestamp = datetime.datetime.utcnow(),
                    color = 0x6441A5,
                )
                embed.set_author(name = message.author.name)
                embed.set_footer(text = "Sent From Twitch")
                await webhook.send(embed = embed)
                print(f"{self.green}[Posted to Discord]{self.default} {self.magenta}{message.author.name}{self.default}: {self.blue}{message.content}{self.default}")

bot = Bot()
bot.run()