import nextcord
from nextcord.ext import commands
import config
from libs.embeds import guildinfo
from logging42 import logger

logs = config.logschannel

class Community(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description= "Test command.")
    async def test(self, interaction: nextcord.Interaction):
        logschannel = self.bot.get_channel(logs)
        await interaction.response.send_message("Valerie is working, I promise :)")
        await logschannel.send(f"{interaction.user.display_name} used /test.")
    
    @nextcord.slash_command(name="info", description="Get the info of this Guild.")
    async def guildinfo(self, interaction: nextcord.Interaction):
        logschannel = self.bot.get_channel(logs)
        await interaction.response.send_message(embed=guildinfo(name=interaction.guild_id))
        await logschannel.send(f"{interaction.user.display_name} used /info.")

def setup(bot):
    bot.add_cog(Community(bot))
    logger.info("Added and setup Community cog. [community.py]")