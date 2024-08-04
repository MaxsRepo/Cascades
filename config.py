import yaml
import dotenv
import os

with open('config.yml', 'r') as file:
    cfg = yaml.safe_load(file)

def gettoken():
    dotenv.load_dotenv('cascades.env')
    tkn = os.getenv('TOKEN')
    return tkn 


# DO NOT TAMPER WITH THIS FILE!    

# Guild info
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

botname = cfg['bot_name']

guildname = cfg['guild_name']

modrole = int(cfg['mod_role'])

ownerrole = int(cfg['owner_role'])

sudoers = cfg['sudoers']

logschannel = int(cfg['logschannel'])

punishments = int(cfg['punishments'])

ticket_channel = int(cfg['ticket_channel'])

transcripts = int(cfg['transcripts'])

guildowner = int(cfg['guild_owner'])

owneruser = cfg['owner_username']

invite = cfg['invite_link']

# Permission error messages

notadmin = cfg['noperm_admin']
nomodperms = cfg['noperm_mod']

# Misc

creditmsg = cfg['creditmsg']

# Extensions

allowexts = cfg['extensions']

# ENVS

token = gettoken()

# End of config.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~