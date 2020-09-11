# Bridge between Twitch and Discord

![Twitch Banner](https://cdn.discordapp.com/attachments/701315125428355124/754055286544793650/twitch.jpg)

[View Live](https://discord.gg/yYUYPr)

Bridge between Discord and Twitch developed using Python, and MongoDB. Frameworks used for the project include discord.py, twitchio, and pymongo.

## Installation

To use the Bridge follow the following steps.

### Install All Required Libraries

```cmd
pip3 install dnspython
```

```cmd
pip3 install pymongo
```

```cmd
pip3 install twitchio
```

```cmd
pip3 install discord.py
```

### Setting up the configuration file

Generate your Twitch oauth token [here](https://twitchapps.com/tmi/) which will be used to read messages from the Twitch chat. After you've generated your token copy and paste it into the `TOKEN` field within `Config.py` file. (You must use the account you copied the token for as the bridged channel.)

After you set up your Twitch OAUTH settings enter the Twitch channel name you would like to build a bridge with into the `NICK` field of the `Config.py` file.

Once you set up the Twitch side of things you need to create a Mongo URI, google how to do so if you don't know how already. Once created copy and paste the Mongo URI into the `CLUSTER` field of `Config.py`.

Once you have set up a Mongo URI go to the Discord channel you want Twitch messages to be sent to create a webhook to the channel and copy and paste the link for the webhook into the `WEBHOOK` field inside of the `Config.py` file.

Then create a Discord bot application and copy and paste the token into the `TOKEN2` field of the `Config.py` file.


### Starting the bot

Once all has been said and done run the following commands in separate terminals to create the bridge.

```cmd
python3 Main.py
```

```cmd
python3 Bot.py
```

Now that you've created the bridge these two programs must stay on for as long as you want to have a bridge running, if you would only like the Twitch to Discord bridge turn off the `Bot.py` program.
