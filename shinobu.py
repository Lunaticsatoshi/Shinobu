import discord
from discord.ext import commands



shinobu = commands.Bot(command_prefix='$')

@shinobu.event
async def on_ready():
    print("Ara Ara")

@shinobu.event
async def om_message(message):
    print("A User has sent a Message")
    await shinobu.process_commands(message)

@shinobu.command()
async def echo(ctx, args):
    await ctx.send(args)

@shinobu.command(pass_context=True, manage_messages=True)
async def clear(ctx, amount=10):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history():
        messages.append(message)
    await channel.delete_messages(messages) 

shinobu.run(TOKEN)
