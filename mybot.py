# Import discord package
import discord
from discord.ext import commands

# Client bot
client = commands.Bot(command_prefix='!')

@client.command(name='yo')
async def version(context):




   # DO STUFF

   general_channel = client.get_channel(817706086484279326)
   await general_channel.send('e')





@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
 await member.kick(reason=reason)
 await ctx.send(f"{member.mention}**KICKED!:thumbsup: https://tenor.com/view/discord-discord-logo-purple-welcome-chat-gif-16615803**")

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
 await member.ban(reason=reason)
 await ctx.send(f"{member.mention}**BANNED! :thumbsup: https://tenor.com/view/discord-discord-logo-purple-welcome-chat-gif-16615803**")

 



    


# Run the client on the server
client.run('ODE4MTI3MTM1ODMwODM1MjMx.YETiRQ.-9W2Z4peJDJM8tto5GgDnV7YBxU')