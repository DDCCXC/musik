from nextcord.ext import commands
import os,nextcord
from dotenv import load_dotenv
if __name__ == "__main__":
    load_dotenv()
   
    bot = commands.Bot(command_prefix='$', intents=nextcord.Intents.all())

    @bot.event
    async def on_ready():
        print('Ready!')
    bot.load_extension("cogs.music")
    
    # bot.load_extension("cogs.test")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    bot.run(os.getenv("DISCORD_TOKEN"))
