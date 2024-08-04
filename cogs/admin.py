import nextcord
from nextcord.ext import commands
import config
from logging42 import logger

logs = config.logschannel

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description="DM a user")
    async def dm(self, interaction: nextcord.Interaction, user: nextcord.Member, message: str):
        logschannel = self.bot.get_channel(logs)
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(config.notadmin)
            await logschannel.send(f"{interaction.user.mention} tried to use /dm, but has no permission.")
        else:
            await user.send(f"{message}")
            await interaction.response.send_message(f"Sent a DM to {user.mention}", ephemeral=True)
            await logschannel.send(f"{interaction.user.display_name} used /dm. \n**User messaged:** {user.display_name} \n**Message:** {message}")

    @nextcord.slash_command(description="Ping!")
    async def ping(self, interaction: nextcord.Interaction):
        if not interaction.user.guild_permissions.administrator:
            await interaction.send(config.notadmin, ephemeral=True)
        else:
            logschannel = self.bot.get_channel(logs)
            latency = round(self.bot.latency * 1000)
            await interaction.response.send_message(f"Pong! Latency: {latency}ms")
            await logschannel.send(f"{interaction.user.display_name} used /ping")

    @nextcord.slash_command(description="say stuff")
    async def echo(self, interaction: nextcord.Interaction, text: str):
        logschannel = self.bot.get_channel(logs)
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(config.notadmin, ephemeral=True)
            await logschannel.send(f"{interaction.user.mention} tried to echo '{text}' in {interaction.channel.mention} but doesn't have permissions.")
        else:
            await interaction.response.send_message(f"{text}")
            await logschannel.send(f"{interaction.user.display_name} echoed '{text}' in {interaction.channel.mention}")

def setup(bot):
    bot.add_cog(Admin(bot))
    logger.info("Added and setup Admin cog. [admin.py]")