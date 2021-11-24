#masterspin
#sos
#11/22/2021

import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print("Bot is ready!")
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('--repeat'):
    m = message.content.split(" ", 1)
    newMessage = m[1]
    m = newMessage.split(" ",1)
    for i in range(int(m[0])):
      await message.channel.send(m[1])

client.run(os.getenv('TOKEN'))
