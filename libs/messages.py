import config

class VoiceActivity:
    def join():
            msg = "# 📞 User Joined VC 📞 #"
            return msg
    
    def leave():
          msg = "# ☎️ User Left VC ☎️ #"
          return msg
    
    def change():
          msg = "# 📲 User Changed VC 📲 #"
          return msg
    
class CogsLogs:
      def load(whichcog: str, admin: str):
            msg = f"# ⚙️ Cog Loaded ⚙️ #\n**Cog:** {whichcog}\n**Loaded by:** {admin}"
            return msg
      
      def unload(whichcog: str, admin: str):
            msg = f"# ⚙️ Cog Unloaded ⚙️ #\n**Cog:** {whichcog}\n**Unloaded by:** {admin}"
            return msg
      
startup_logo = r"""
                r                
               ain
               rai
              nrain
             rainrai
            nrainrain
           ainrainrain
          rainrainrainr
         ainrainrainrain
        rainrainrainrainr
      ainrainrainrainrainra
    inra nrainrainrainrainrai
  nrain  inrainrainrainrainrain
 rain   nrainrainrainrainrainrai
nrai   inrainrainrainrainrainrain
rai   inrainrainrainrainrainrainr
rain   nrainrainrainrainrainrainr
 rainr  nrainrainrainrainrainrai
  nrain ainrainrainrainrainrain
    rainrainrainrainrainrainr
      rainranirainrainrainr
           ainrainrain
      """

def stopmsg(user: str):
      msg = f"# 🛑 Bot Stopped 🛑 #\n**Stopped by:** {user}\n-# To restart me, run the bot.py Python script again wherever I am hosted."
      return msg