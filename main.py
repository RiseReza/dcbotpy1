import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'z')

@client.event
async def on_ready():
  print('Bot is online!')

client.run('TOKEN')
# now lets run the bot,
# and by the way, this means part 1 is done.
# bot is online, lets see from discord!
# the bot is online, thank you for watching!
