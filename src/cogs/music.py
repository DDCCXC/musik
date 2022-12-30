from nextcord import Interaction, slash_command
from nextcord.ext.commands import Bot, Cog
from .musik import Musik
import nextcord
class music_command(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
        self.player =Musik(bot)

    # basic
    @slash_command(force_global=True)
    async def misik(self,inter: nextcord.Interaction):...
    @misik.subcommand()
    async def basic(self,inter: nextcord.Interaction):...
    
    @basic.subcommand(name="join", description="Asdasd")
    async def join(self, inter: Interaction) -> None:
        await self.player.join_to_channel(inter)
        
    @basic.subcommand(name="disconnect", description="Asdasd")
    async def disconnect(self, inter: Interaction) -> None:
        await self.player.disconnect(inter)
        
    @basic.subcommand(name="play", description="Asdasd")
    async def play(self, inter: Interaction,query: str) -> None:
        await self.player.play(inter,query)
        
    @basic.subcommand(name="skip", description="Asdasd")
    async def skip(self, inter: Interaction) -> None:
        await self.player.skip(inter)      
    
    @basic.subcommand(name="stop", description="Asdasd")
    async def stop(self, inter: Interaction) -> None:
        await self.player.stop(inter) 
        
    @basic.subcommand(name="pause", description="Asdasd")
    async def pause(self, inter: Interaction) -> None:
        await self.player.pause(inter) 
        
    @basic.subcommand(name="now", description="Asdasd")
    async def now(self, inter: Interaction) -> None:
        await self.player.now(inter) 
 
    @basic.subcommand(name="queue", description="Asdasd")
    async def queue(self, inter: Interaction) -> None:
        await self.player.queue(inter)     
        
    @basic.subcommand(name="remove", description="Asdasd")
    async def remove(self, inter: Interaction,index:int= nextcord.SlashOption(min_value=1)) -> None:
        await self.player.remove(inter,index)
        
    @basic.subcommand(name="repeat", description="Asdasd")
    async def repeat(self, inter: Interaction) -> None:
        await self.player.repeat(inter)
        
    @basic.subcommand(name="shuffle", description="Asdasd")
    async def shuffle(self, inter: Interaction) -> None:
        await self.player.shuffle(inter) 
        
    @basic.subcommand(name="seek", description="Asdasd")
    async def seek(self, inter: Interaction,sec:int) -> None:
        await self.player.seek(inter,sec)   
      
    @basic.subcommand(name="volume", description="Asdasd")
    async def volume(self, inter: Interaction,volume:int= nextcord.SlashOption(min_value=1,max_value=1000)) -> None:
        await self.player.volume(inter,volume) 
    
    @basic.subcommand(name="info_filters", description="Asdasd")
    async def info_filters(self, inter: Interaction) -> None:
        await self.player.info_filters(inter)      
        
    # filters
    @misik.subcommand()
    async def filters(self,inter: nextcord.Interaction):...
    @filters.subcommand(name="bassboost", description="Asdasd")
    async def bassboost(self, inter: Interaction) -> None:
        ...
    @filters.subcommand(name="bassboost", description="Asdasd")
    async def bassboost(self, inter: Interaction) -> None:
        ...
    @filters.subcommand(name="bassboost", description="Asdasd")
    async def bassboost(self, inter: Interaction) -> None:
        ...
    @filters.subcommand(name="bassboost", description="Asdasd")
    async def bassboost(self, inter: Interaction) -> None:
        ...
    @filters.subcommand(name="bassboost", description="Asdasd")
    async def bassboost(self, inter: Interaction) -> None:
        ...
    @filters.subcommand(name="bassboost", description="Asdasd")
    async def bassboost(self, inter: Interaction) -> None:
        ...
    @filters.subcommand(name="bassboost", description="Asdasd")
    async def bassboost(self, inter: Interaction) -> None:
        ...
    @filters.subcommand(name="bassboost", description="Asdasd")
    async def bassboost(self, inter: Interaction) -> None:
        ...
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def setup(bot: Bot) -> None:
    bot.add_cog(music_command(bot))