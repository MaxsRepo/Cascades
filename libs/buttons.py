import nextcord
from libs import ticketing

class CreateTicket(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="Create Ticket.", style=nextcord.ButtonStyle.blurple, custom_id="create_ticket", emoji="🎟️")
    async def on_tixcreate(self, button, interaction: nextcord.Interaction):
        await ticketing.create(interaction)

class TicketSettings(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

   
    @nextcord.ui.button(label="Close Ticket", style=nextcord.ButtonStyle.red, custom_id="ticket_settings:red")
    async def on_tixclose(self, button, interaction: nextcord.Interaction):
        await ticketing.close(interaction)