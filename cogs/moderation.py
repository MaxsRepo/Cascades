import nextcord
from nextcord.ext import commands
from libs import embeds
from logging42 import logger
import config

punish = config.punishments
logs = config.logschannel

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("Moderation cog is ready.")

    @nextcord.slash_command(description= "Warn a user.")
    async def warn(self, interaction: nextcord.Interaction, user: nextcord.Member, reason: str):
        if not interaction.user.guild_permissions.ban_members:
            await interaction.response.send_message(config.nomodperms, ephemeral=True)
        else:
            punishments = self.bot.get_channel(punish)
            await punishments.send(f"**User Warned** \n**User:** {user.mention} \n**Warned by:** {interaction.user.mention} \n**Reason:** {reason}")
            await interaction.response.send_message(embed=embeds.warnembed(warned=user.mention, moderator=interaction.user.mention, reason=reason, icon=interaction.user.display_avatar, dispmod=interaction.user.display_name))

    @nextcord.slash_command(description= "Ban a user.")
    async def ban(self, interaction: nextcord.Interaction, user: nextcord.Member, reason: str):
        if not interaction.user.guild_permissions.ban_members:
            await interaction.response.send_message(config.nomodperms, ephemeral=True)
        else:
            punishments = self.bot.get_channel(punish)
            await punishments.send(f"**User Banned from Guild** \n**User banned:** {user.display_name} \n**Banned by:** {interaction.user.mention} \n**Reason:** {reason}")
            await user.send(f"You have been banned for reason: {reason}. DM a member of staff to appeal.")
            await interaction.response.send_message(embed=embeds.banembed(user.mention, interaction.user.mention, reason, interaction.user.display_avatar, interaction.user.display_name))
            await user.ban(reason=reason)

    @nextcord.slash_command(description="Kick a user.")
    async def kick(self, interaction: nextcord.Interaction, user: nextcord.Member, reason: str):
        if not interaction.user.guild_permissions.kick_members:
            await interaction.send(config.nomodperms, ephemeral=True)
        else:
            punishments = self.bot.get_channel(punish)
            await punishments.send(f"**User Kicked from Guild** \n**User:** {user.display_name} \n**Kicked by:** {interaction.user.mention} \n**Reason:** {reason}")
            await user.send(f"You have been kicked in RedAura by {interaction.user.display_name} for reason: {reason}")
            await interaction.send(embed=embeds.kickembed(user.mention, interaction.user.mention, reason, interaction.user.display_avatar, interaction.user.display_name))
            await user.kick(reason=reason)

    @nextcord.message_command(name="Warn for Message")
    async def warn_message(self, interaction: nextcord.Interaction, message: nextcord.Message):
        punishments = self.bot.get_channel(punish)
        if not interaction.user.guild_permissions.ban_members:
            await interaction.response.send_message(config.nomodperms, ephemeral=True)
        else:
            await interaction.response.send_message(embed=embeds.wfm(message.author.mention, interaction.user.mention, message.content, interaction.user.display_avatar, interaction.user.display_name))
            await punishments.send(f"**User Warned for Message** \n**User:** {message.author.mention} \n**Warned by:** {interaction.user.mention} \n**Message Content:** '{message.content}'")
    
    @nextcord.slash_command(name="purge")
    async def purge(self, interaction: nextcord.Interaction, amount: int):
        logschannel = self.bot.get_channel(logs)
        if interaction.user.guild_permissions.manage_messages:
            if amount <= 0:
                await interaction.response.send_message("Please specify a positive number of messages to purge.")
            else:
                await interaction.channel.purge(limit=amount)
                await interaction.response.send_message(f"Purged {amount} messages.")
                await logschannel.send(f"{interaction.user.display_name} has purged `{amount}` messages in {interaction.channel.mention}")
        else:
            await interaction.response.send_message(config.nomodperms, ephemeral=True)
            await logschannel.send(f"{interaction.user.mention} tried to purge `{amount}` messages, but has no permission.")

def setup(bot):
    bot.add_cog(Moderation(bot))
    logger.info("Added and setup Moderation cog. [moderation.py]")