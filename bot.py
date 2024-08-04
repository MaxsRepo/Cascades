import nextcord
import asyncio
import os
from logging42 import logger
from libs.messages import CogsLogs, stopmsg
from libs import extensions
import config
import sys

intents = nextcord.Intents.all()

from nextcord.ext import commands, tasks
bot = commands.Bot(command_prefix = '!', intents=intents)
logs = config.logschannel
punish = config.punishments

@bot.event
async def on_ready():
    logger.success(f"{config.botname} has started.")

@bot.slash_command(name="cogs")
async def cogs(interaction: nextcord.Interaction):
    pass

@cogs.subcommand(name="load", description="Load a cog.")
async def load(interaction: nextcord.Interaction, cog: str):
    logschannel = bot.get_channel(logs)
    if not interaction.user.guild_permissions.administrator:
        await interaction.send(config.notadmin, ephemeral=True)
    else:
        bot.load_extension(f"cogs.{cog}")
        await interaction.send(f"Loaded {cog} cog.")
        await logschannel.send(f"{CogsLogs.load(whichcog=cog, admin=interaction.user.mention)}")

@cogs.subcommand(name="unload", description="Unload cogs.")
async def unload(interaction: nextcord.Interaction, cog: str):
    logschannel = bot.get_channel(logs)
    if not interaction.user.guild_permissions.administrator:
        await interaction.send(config.notadmin, ephemeral=True)
    else:
        bot.unload_extension(f"cogs.{cog}")
        await interaction.send(f"Unloaded {cog} cog.")
        await logschannel.send(f"{CogsLogs.unload(whichcog=cog, admin=interaction.user.mention)}")

@bot.slash_command(name="force")
async def force(interaction: nextcord.Interaction):
    pass

@force.subcommand(name="syncapps", description="Force sync application commands.")
async def syncapps(interaction: nextcord.Interaction):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message(config.notadmin, ephemeral=True)
    else:
        await bot.sync_all_application_commands(register_new=True)

@force.subcommand(name="stop", description="Stop the bot.")
async def stop(interaction: nextcord.Interaction):
    ownerrole = nextcord.utils.get(interaction.guild.roles, id=config.ownerrole)
    if interaction.user.id in config.sudoers or ownerrole in interaction.user.roles:
        await interaction.send(stopmsg(interaction.user.mention))
        sys.exit()
    else:
        await interaction.send(config.notadmin, ephemeral=True)

extsloaded = []
extresult = extensions.getexts()
if extresult == 'ExtsFalse':
    logger.info("Extensions are set to 'false', they will not be loaded.")
elif extresult == 'NotConfigured':
    logger.warning("Extensions section of the config is not configured properly!")
else:
    for ext in extensions.getexts():
        bot.load_extension(f"ext.{ext}")
        extsloaded.append(ext)
    logger.info(f"Loaded extensions: {extsloaded}")

@bot.slash_command(name="credits", description="Bot credits.")
async def credits(interaction: nextcord.Interaction):
    logschannel = bot.get_channel(logs)
    await interaction.send(config.creditmsg)
    await logschannel.send(f"{interaction.user.display_name} read the credits. [used /credits]")

bot.run(config.token)