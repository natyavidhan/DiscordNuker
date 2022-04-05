import discord
from discord.ext import commands
from discord_webhook import DiscordWebhook
import json

intents = discord.Intents.all() # Enable all intents except for members and presences
intents.members = True

client = commands.Bot(command_prefix="!", intents=intents)
with open("token.json", "r") as f:
    keys = json.load(f)
    TOKEN = keys['TOKEN']



@client.command()
async def channels_create(ctx, amt,*, name):
    for _ in range(int(amt)):
        await ctx.guild.create_text_channel(name)
    msg_id = ctx.message
    await msg_id.add_reaction('✅')
        
@client.command()
async def destroy_channels(ctx):
    for channel in ctx.guild.channels:
        await channel.delete()
    msg_id = ctx.message
    await msg_id.add_reaction('✅')
        
@client.command()
async def nickto(ctx, name):
    for user in client.get_all_members():
        try:
            await user.edit(nick=name)    
        except:
            pass
    msg_id = ctx.message
    await msg_id.add_reaction('✅')
        
@client.command()
async def dm(ctx, times, *,text):
    for user in client.get_all_members():
        for _ in range(int(times)):
            try:
                await user.send(text)
            except:
                pass
    msg_id = ctx.message
    await msg_id.add_reaction('✅')
                
@client.command()
async def kickall(ctx):
    for user in client.get_all_members():
        try:
            await user.kick()    
        except:
            pass
    msg_id = ctx.message
    await msg_id.add_reaction('✅')
        
@client.command()
async def banall(ctx):
    for user in client.get_all_members():
        try:
            await user.ban()    
        except:
            pass
    msg_id = ctx.message
    await msg_id.add_reaction('✅')
        
@client.command()
async def webhook(ctx, *,name):
    for channel in ctx.guild.channels:
        try:
            hook = await channel.create_webhook(name=name)
        except:
            pass
    msg_id = ctx.message
    await msg_id.add_reaction('✅')
            
@client.command()
async def massping(ctx, amt, *,msg):
    for webhook in await ctx.guild.webhooks():
        for _ in range(int(amt)):
            try:
            # ctx.send(webhook.url)
                DiscordWebhook(url = webhook.url, content = f"||@everyone|| {msg}").execute()
            except:
                pass
    msg_id = ctx.message
    await msg_id.add_reaction('✅')

@client.command()
async def unbanall(ctx):
    for user in client.get_all_members():
        try:
            await user.unban()   
        except:
            pass
    msg_id = ctx.message
    await msg_id.add_reaction('✅')


@client.command()
async def attention(ctx,*, text):
    msg = await ctx.send("@everyone")
    await msg.delete()
    for webhook in await ctx.guild.webhooks():
        try:
        # ctx.send(webhook.url)
            DiscordWebhook(url = webhook.url, content = f"{text}").execute()
        except:
            pass            
    msg_id = ctx.message
    await msg_id.add_reaction('✅')
client.run(TOKEN)
