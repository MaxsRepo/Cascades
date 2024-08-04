import nextcord
from nextcord.ext import commands
from logging42 import logger
from libs import ticketing, buttons
import config

tixchannel = config.ticket_channel

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.button_added = False

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("Tickets has been loaded. [COGS: tickets.py]")
        if not self.button_added:
            self.bot.add_view(buttons.CreateTicket())
            self.bot.add_view(buttons.TicketSettings())
            self.button_added = True

    @nextcord.slash_command(name="ticket")
    async def ticket(self, interaction: nextcord.Interaction):
        pass

    @ticket.subcommand(name="create", description="Create a ticket.")
    async def create(self, interaction: nextcord.Interaction):
        await ticketing.create(interaction)

    @ticket.subcommand(name="setup", description="Create the button in #tickets to setup the tickets feature.")
    async def buttonsetup(self, interaction: nextcord.Interaction):
        tix = self.bot.get_channel(tixchannel)
        if not interaction.user.guild_permissions.administrator:
            await interaction.send(config.notadmin, ephemeral=True)
        else:
            await tix.send("# 🎟️ Create a Ticket 🎟️ #\nPress the button to open a ticket, then go to the ticket thread.", view=buttons.CreateTicket())
            await interaction.send("Setup tickets in current channel.", ephemeral=True)

def setup(bot):
    bot.add_cog(Tickets(bot))
    logger.info("Added and setup Tickets cog. [tickets.py]")