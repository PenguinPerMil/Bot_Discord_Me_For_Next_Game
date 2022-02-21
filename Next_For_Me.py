import discord

import os

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_STR = os.getenv('DISCORD_GUILD')
ROLE_PINGED_STR=os.getenv('DISCORD_ROLE_TO_FIND')
ROLE_TO_PING_STR=os.getenv('DISCORD_ROLE_TO_ATTRIBUTE')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

CHECK_EMOJI_NAME = '\N{THUMBS UP SIGN}'
#CHECK=discord.Reaction()

@client.event
async def on_ready():

    for GUILD_temp in client.guilds:
        if GUILD_temp.name == GUILD_STR:
            GUILD=GUILD_temp
            for role in GUILD_temp.roles:
                if role.name==ROLE_TO_PING_STR:
                    ROLE_TO_PING=role
                if role.name==ROLE_PINGED_STR:
                    ROLE_PINGED=role    
            break
    print(
        f'{client.user} is connected to the following GUILD:\n'
        f'{GUILD.name}(id: {GUILD.id})'
        f'{ROLE_PINGED_STR} to find'
        f'{ROLE_TO_PING_STR} to ping'
        f'{ROLE_TO_PING.name} id to ping'
        f'{ROLE_PINGED.name} id to ping'    
    )


@client.event
async def on_message(message):
    for GUILD_temp in client.guilds:
        if GUILD_temp.name == GUILD_STR:
            GUILD=GUILD_temp
            for role in GUILD_temp.roles:
                if role.name==ROLE_TO_PING_STR:
                    ROLE_TO_PING=role
                if role.name==ROLE_PINGED_STR:
                    ROLE_PINGED=role    
            break
    
    for role_ping in message.role_mentions:
        if role_ping.name==ROLE_PINGED_STR:
            print('role pinged')
            auth=message.author
            print(f'{ROLE_TO_PING.name} added')
            await auth.add_roles(ROLE_TO_PING)
            await message.add_reaction(CHECK_EMOJI_NAME)
            break
        
        if role_ping.name==ROLE_TO_PING_STR:
            print('role to ping')
            auth=message.author
            for memb in GUILD.get_role(ROLE_TO_PING.id).members:
                print(ROLE_TO_PING_STR+ ' removed to '+ memb.name)
                await memb.remove_roles(ROLE_TO_PING)

            await message.add_reaction(CHECK_EMOJI_NAME)
            break



client.run(TOKEN)