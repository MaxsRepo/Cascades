import nextcord
from nextcord.ext import commands
from logging42 import logger
from libs.messages import VoiceActivity as VA
import config

logschannel = config.logschannel

class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        logit = self.bot.get_channel(logschannel)
        attachments = ''
        for attachment in message.attachments:
            if attachments == '':
                attachments += attachment.filename
            else:
                attachments += f', {attachment.filename}'
        if attachments == '':
            attachments = 'None'
        await logit.send(f"# 🗑️ Message Deleted 🗑️ #\n**User:** {message.author.mention} ({message.author}) `{message.author.id}`\n**Channel:** {message.channel.mention}\n**Message Content:** '{message.content}'\n**Attachments:** {attachments}")

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        logit = self.bot.get_channel(logschannel)
        message_link = f"https://discord.com/channels/{before.guild.id}/{before.channel.id}/{before.id}"
        await logit.send(f"# ✏️ Message Edited ✏️\n**Message Author:** {before.author.mention} ||{before.author}, {before.author.id}||\n**Channel:** {before.channel.mention}\n**Message Link:** {message_link}\n**Original Message:** {before.content}\n**Message After Edit:** {after.content}")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel is None and after.channel is not None:
            vc = after.channel
            logit = self.bot.get_channel(logschannel)
            await logit.send(f"{VA.join()}\n**User:** {member.mention} ||{member}, {member.id}||\n**Voice Channel:** {vc.mention}")
        elif before.channel is not None and after.channel is None:
            vc = before.channel
            logit = self.bot.get_channel(logschannel)
            await logit.send(f"{VA.leave()}\n**User:** {member.mention} ||{member}, {member.id}||\n**Voice Channel:** {vc.mention}")
        elif before.channel is not None and after.channel is not None and before.channel != after.channel:
            logit = self.bot.get_channel(logschannel)
            await logit.send(f"{VA.change()}\n**User:** {member.mention} ||{member}, {member.id}||\n**Originally in VC:** {before.channel.mention}\n**Moved to:** {after.channel.mention}")

def setup(bot):
    bot.add_cog(Logs(bot))
    logger.info(f"Added and setup Logs cog. [logs.py]")