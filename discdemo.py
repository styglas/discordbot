import discord
import re
import configparser
import os

tokenfile = 'token.cfg'
client = discord.Client()

@client.event
async def on_message(message):
    print(message.content)
    # we do not want the bot to reply to itself
    print("Author: {}, User:{}".format(message.author, client.user))
    if message.author == client.user:
        return

    if re.match(r'.*peng.*',message.content):
        msg = 'Jeg elsker penge'
        await client.send_message(message.channel, msg)

    if re.match(r'.*klog.*',message.content.lower()):
        msg = 'Jeg er meget klog'
        await client.send_message(message.channel, msg)

    if message.content.lower().startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

if __name__ == '__main__':
    cfg = configparser.ConfigParser()
    cfg.read(tokenfile)
    token = cfg.get (option='token', section='DEFAULT')
    client.run(token)