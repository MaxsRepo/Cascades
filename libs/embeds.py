import nextcord
import config

def warnembed(warned: str, moderator: str, reason: str, icon: str, dispmod: str):
    embed = nextcord.Embed(title="⚠️ Warning ⚠️")
    embed.add_field(name="User:", value=warned)
    embed.add_field(name="Warned By:", value=moderator)
    embed.add_field(name="Reason:", value=reason)
    embed.set_footer(icon_url=icon, text=f"Moderator: {dispmod}")
    return embed

def banembed(banned: str, moderator: str, reason: str, icon: str, dispmod: str):
    embed = nextcord.Embed(title="🛑 User Banned 🛑")
    embed.add_field(name="User:", value=banned)
    embed.add_field(name="Banned by:", value=moderator)
    embed.add_field(name="Reason:", value=reason)
    embed.set_footer(icon_url=icon, text=dispmod)
    return embed

def kickembed(kicked: str, moderator: str, reason: str, icon: str, dispmod: str):
    embed = nextcord.Embed(title="👟 User Kicked 👟")
    embed.add_field(name="User:", value=kicked)
    embed.add_field(name="Kicked by:", value=moderator)
    embed.add_field(name="Reason:", value=reason)
    embed.set_footer(icon_url=icon, text=dispmod)
    return embed

def wfm(warned: str, moderator: str, msgcontent: str, icon: str, dispmod: str):
    embed = nextcord.Embed(title="💬 User Warned for Message ⚠️")
    embed.add_field(name="User:", value=warned)
    embed.add_field(name="Warned by:", value=moderator)
    embed.add_field(name="Message Content:", value=f"||{msgcontent}||")
    embed.set_footer(icon_url=icon, text=dispmod)
    return embed

def guildinfo(name: str):
    mod = f"<@&{config.modrole}>"
    owner = f"<@&{config.ownerrole}>"
    invlnk = config.invite
    embed = nextcord.Embed(title="ℹ️ Guild Information ℹ️")
    embed.set_author(name=config.guildname)
    embed.add_field(name="Guild ID:", value=name)
    embed.add_field(name="Guild Owner:", value=f"<@{config.guildowner}> ||{config.owneruser} (id: {config.guildowner})||")
    embed.add_field(name="Owner Role:", value=owner)
    embed.add_field(name="Moderator Role:", value=mod)
    embed.add_field(name="Invite link:", value=invlnk)
    embed.set_footer(text="Guild Info for this bot.")
    return embed
