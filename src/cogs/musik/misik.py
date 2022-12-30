from nextcord import Interaction, slash_command
from nextcord.ext import commands
from nextcord.ext.commands import Bot, Cog
from . import player as pyer
from .command import *
import lavalink,nextcord,re,time
TESTING_GUILD_ID = 1054648673855868978

URL_RX = re.compile(r'https?://(?:www\.)?.+')
class Musik(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
        bot.lavalink:lavalink.Client
        if not hasattr(bot, 'lavalink'):  
            
            bot.lavalink:lavalink.Client = lavalink.Client(1054981299334549514)
            bot.lavalink.add_node('127.0.0.1', 2333, 'thampomungdoo', 'sg', 'default-node')  # Host, Port, Password, Region, Name

        lavalink.add_event_hook(self.track_hook)
        
    async def track_hook(self, event):
        if isinstance(event, lavalink.events.QueueEndEvent):
            guild_id = event.player.guild_id
            guild = self.bot.get_guild(guild_id)
            await guild.voice_client.disconnect(force=True)
            
    def unload(self):
        self.bot.lavalink._event_hooks.clear()
        
    async def connect_to(self, guild_id: int, channel_id: str):
        ws = self.bot._connection._get_websocket(guild_id)
        await ws.voice_state(str(guild_id), channel_id)
    
    async def join_to_channel(self, Inter:Interaction)->bool:
        await join(self,Inter)
        
    async def disconnect(self, Inter:Interaction):
        await disconnect(self,Inter)

    async def play(self, Inter:Interaction, query: str):
        await play(self,Inter,query)
        
    async def slash_skip(self, Inter:Interaction):
        await slash_skip(self,Inter)
        
    async def prefix_skip(self, ctx:commands.context.Context):
        await prefix_skip(self,ctx)
        
    async def slash_stop(self, Inter:Interaction):
        await slash_stop(self,Inter)
        
    async def prefix_stop(self, ctx:commands.context.Context):
        await prefix_stop(self,ctx)
        
    async def slash_pause(self, Inter:Interaction):
        await slash_pause(self,Inter)
        
    async def prefix_pause(self, ctx:commands.context.Context):
        await prefix_pause(self,ctx)
        
    async def slash_now(self, Inter:Interaction):
        await slash_now(self,Inter)
        
    async def prefix_now(self, ctx:commands.context.Context):
        await prefix_now(self,ctx)
        
    async def remove(self, ctx:commands.context.Context,index:int):
        await remove(self,ctx,index)
        
    async def slash_repeat(self, Inter:Interaction):
        await slash_repeat(self,Inter)
        
    async def prefix_repeat(self, ctx:commands.context.Context):
        await prefix_repeat(self,ctx)
    
    async def slash_shuffle(self, Inter:Interaction):
        await slash_shuffle(self,Inter)
        
    async def prefix_shuffle(self, ctx:commands.context.Context):
        await prefix_shuffle(self,ctx)
    
    async def seek(self, Inter:Interaction,sec:int):
        await seek(self,Inter,sec)
    
    async def volume(self, Inter:Interaction,_volume:int):
        await volume(self,Inter,_volume)
    
    async def queue(self, Inter:Interaction):
        await queue(self,Inter)
        
    async def info_filter(self, Inter:Interaction):
        await check(self,Inter)
def setup(bot: Bot) -> None:
    bot.add_cog(Musik(bot))