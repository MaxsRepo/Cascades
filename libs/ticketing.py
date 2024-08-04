import nextcord
from libs import buttons
import config

tixchannel = config.ticket_channel
transcripts = config.transcripts

async def create(interaction: nextcord.Interaction):
    msg = await interaction.response.send_message("A ticket is being created.", ephemeral=True)
    thread = await interaction.channel.create_thread(name=f"{interaction.user}'s Ticket", type=nextcord.ChannelType.private_thread, reason="Ticket")
    await msg.edit(f"Channel created successfully! {thread.mention}")
    await thread.send(f"Thank you for opening a ticket, {interaction.user.mention}. A <@&{config.modrole}> will be with you as soon as possible. In the mean time, please provide a brief explanation as to what you need support with. @mention any user to add them to the ticket, but don't add offenders to the ticket, unless we ask for you to, please.", view=buttons.TicketSettings(), allowed_mentions=nextcord.AllowedMentions(roles=True))

async def get_ticket_creator(thread: nextcord.Thread):
    hist = await thread.history(limit=5, around=thread.created_at).flatten()
    for message in hist:
        first = message
    
    return message.mentions[0]

async def close(interaction: nextcord.Interaction):
    thread = interaction.channel
    author = await get_ticket_creator(thread)
    await interaction.response.send_message(f"🎟️ **Ticket Closed** 📭")
    await thread.edit(name=f"{thread.name} [Closed]", archived=True, locked=True)
    await interaction.user.send(f"You closed a ticket in {config.guildname}. Here is the transcript: {thread.mention}")
    await author.send(f"Your ticket in {config.guildname} was closed by {interaction.user.display_name}. Here is the transcript: {thread.mention}")
    logit = interaction.guild.get_channel(transcripts)
    await logit.send(f"# 🎟️ Ticket Closed 📭 #\n**Closed by:** {interaction.user.display_name} ||{interaction.user}, {interaction.user.id}||\n**Transcript:** {thread.mention} ||{thread.name}||\n**Ticket Creator:** {author.display_name} ||{author}, {author.id}||")