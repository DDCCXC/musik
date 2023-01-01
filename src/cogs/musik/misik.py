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
        self.bot.lavalink:lavalink.Client
        if not hasattr(bot, 'lavalink'):  
            
            self.bot.lavalink:lavalink.Client = lavalink.Client(1054981299334549514)
            self.bot.lavalink.add_node('127.0.0.1', 2333, 'thampomungdoo', 'sg', 'default-node')  # Host, Port, Password, Region, Name

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
    
    async def join_to_channel(self, Inter:Interaction|commands.context.Context)->bool:
        await join(self,Inter)
        
    async def disconnect(self, Inter:Interaction|commands.context.Context):
        await disconnect(self,Inter)

    async def play(self, Inter:Interaction|commands.context.Context, query: str):
        await play(self,Inter,query)
        
    async def skip(self, Inter:Interaction|commands.context.Context):
        await skip(self,Inter)
        
    async def stop(self, Inter:Interaction|commands.context.Context):
        await stop(self,Inter)
        
    async def pause(self, Inter:Interaction|commands.context.Context):
        await pause(self,Inter)
        
    async def now(self, Inter:Interaction|commands.context.Context):
        await now(self,Inter)
        
    async def remove(self, ctx:Interaction|commands.context.Context,index:int):
        await remove(self,ctx,index)
        
    async def repeat(self, Inter:Interaction|commands.context.Context):
        await repeat(self,Inter)
    
    async def shuffle(self, Inter:Interaction|commands.context.Context):
        await shuffle(self,Inter)
    
    async def seek(self, Inter:Interaction|commands.context.Context,sec:int):
        await seek(self,Inter,sec)
    
    async def volume(self, Inter:Interaction|commands.context.Context,_volume:int):
        await volume(self,Inter,_volume)
    
    async def queue(self, Inter:Interaction|commands.context.Context):
        await queue(self,Inter)
        
    async def info_filters(self, Inter:Interaction|commands.context.Context):
        await check(self,Inter)
    
    async def bb(self, Inter:Interaction|commands.context.Context,gain: float):
        await equalizer_controller(self,Inter,gain)
def setup(bot: Bot) -> None:
    bot.add_cog(Musik(bot))