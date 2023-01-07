from nextcord import Interaction, slash_command,message_command
from nextcord.ext.commands import Cog,AutoShardedBot
from commands.music_command import Musik
from database import GUILD
import nextcord
class music_commands(Cog):
    def __init__(self, bot: AutoShardedBot) -> None:
        self.bot = bot
        self.player =Musik(bot,GUILD)
        

    # basic
    @slash_command(force_global=True)
    async def misik(self,inter: nextcord.Interaction):...
    @misik.subcommand()
    async def basic(self,inter: nextcord.Interaction):...
    
    @basic.subcommand(name="join", description="Asdasd")
    async def join(self, inter: Interaction) -> None:
        await self.player.join_to_channel(inter,True)
        
    @basic.subcommand(name="disconnect", description="Asdasd")
    async def disconnect(self, inter: Interaction) -> None:
        await self.player.disconnect(inter)
        
    @basic.subcommand(name="play", description="Asdasd")
    async def play(self, inter: Interaction,query: str) -> None:
        await self.player.play(inter,query)
        
    @message_command(name="play", force_global=True)
    async def message_play(self, inter: Interaction, message: nextcord.Message) -> None:
        await self.player.play(inter,message.content)
        
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
        await inter.response.defer()
        await self.player.now(inter) 
 
    @basic.subcommand(name="queue", description="Asdasd")
    async def queue(self, inter: Interaction) -> None:
        await inter.response.defer()
        await self.player.queue(inter)     
        
    @basic.subcommand(name="remove", description="Asdasd")
    async def remove(self, inter: Interaction,index:int= nextcord.SlashOption(min_value=1)) -> None:
        await self.player.remove(inter,index)
        
    @basic.subcommand(name="repeat", description="Asdasd")
    async def repeat(self, inter: Interaction,loop:int=nextcord.SlashOption(name="loop",choices={"None":0,"single":1,"queue":2},default=0)) -> None:
        await self.player.repeat(inter,loop)
        
    @basic.subcommand(name="shuffle", description="Asdasd")
    async def shuffle(self, inter: Interaction) -> None:
        await self.player.shuffle(inter) 
        
    @basic.subcommand(name="seek", description="Asdasd")
    async def seek(self, inter: Interaction,sec:int) -> None:
        await self.player.seek(inter,sec)   
      
    @basic.subcommand(name="volume", description="Asdasd")
    async def volume(self, inter: Interaction,volume:int= nextcord.SlashOption(min_value=1,max_value=1000)) -> None:
        await self.player.volume(inter,volume) 
    
    @basic.subcommand(name="info-filters", description="Asdasd")
    async def info_filters(self, inter: Interaction) -> None:
        await inter.response.defer()
        await self.player.info_filters(inter)  
            
    @basic.subcommand(name="auto-play", description="Asdasd")
    async def auto_play (self, inter: Interaction) -> None:
        await self.player.set_auto_play(inter)
    # filters
    @misik.subcommand()
    async def filters(self,inter: nextcord.Interaction):...
    
    # bass
    @filters.subcommand(name="bassboost", description="Asdasd")
    async def bassboost(self, inter: Interaction
                        ,bands=nextcord.SlashOption(name="bands",choices=[str(x) for x in range(15)],default="all")
                        ,gain:float = nextcord.SlashOption(min_value=-0.25 ,max_value=1.00,default=0) ) -> None:
        await self.player.bb(inter,bands,gain)  
    # Timescale
    @filters.subcommand(name="timescale", description="Asdasd")
    async def timescale(self, inter: Interaction,speed:float = nextcord.SlashOption(min_value=0.1,default=1),pitch:float = nextcord.SlashOption(min_value=0.1,default=1),rate:float = nextcord.SlashOption(min_value=0.1,default=1)) -> None:
        await self.player.timescale(inter,speed,pitch,rate)
    
    # Karaoke
    # {'level': 1.0, 'monoLevel': 1.0, 'filterBand': 220.0, 'filterWidth': 100.0}
    @filters.subcommand(name="karaoke", description="Asdasd")
    async def karaoke(self, inter: Interaction,level:float = nextcord.SlashOption(default=1),monolevel:float = nextcord.SlashOption(default=1),filterband:float = nextcord.SlashOption(default=220.0),filterwidth:float = nextcord.SlashOption(default=100.0)) -> None:
        await self.player.karaoke(inter,level,monolevel,filterband,filterwidth)
        
        
    @filters.subcommand(name="level", description="Asdasd")
    async def level(self, inter: Interaction,level:float = nextcord.SlashOption(min_value=0.1)) -> None:
        await self.player.kalevel(inter,"level",level)
    @filters.subcommand(name="monolevel", description="Asdasd")
    async def monolevel(self, inter: Interaction,monolevel:float = nextcord.SlashOption(min_value=0.1)) -> None:
        await self.player.kalevel(inter,"monolevel",monolevel)
    @filters.subcommand(name="filterband", description="Asdasd")
    async def filterband(self, inter: Interaction,filterband:float = nextcord.SlashOption(min_value=0.1)) -> None:
        await self.player.kalevel(inter,"filterband",filterband)
    @filters.subcommand(name="filterwidth", description="Asdasd")
    async def filterwidth(self, inter: Interaction,filterwidth:float = nextcord.SlashOption(min_value=0.1)) -> None:
        await self.player.kalevel(inter,"filterwidth",filterwidth)
        
    # Tremolo
    @filters.subcommand(name="tremolo", description="Asdasd")
    async def Tremolo(self, inter: Interaction,depth:float = nextcord.SlashOption(default=1),frequency:float = nextcord.SlashOption(default=1))  -> None:
        await self.player.Tremolo(inter,depth,frequency)
    
    @filters.subcommand(name="tremolo-depth", description="Asdasd")
    async def depth(self, inter: Interaction,depth:float = nextcord.SlashOption(default=1)) -> None:
        await self.player.depth(inter,depth,"Tremolo")
    @filters.subcommand(name="tremolo-frequency", description="Asdasd")
    async def frequency(self, inter: Interaction,frequency:float = nextcord.SlashOption(default=1)) -> None:
        await self.player.depth(inter,frequency,"Tremolo")
        
        
    # Vibrato
    @filters.subcommand(name="vibrato", description="Asdasd")
    async def Vibrato(self, inter: Interaction,depth:float = nextcord.SlashOption(default=1),frequency:float = nextcord.SlashOption(default=1)) -> None:
        await self.player.Vibrato(inter,depth,frequency)
    @filters.subcommand(name="vibrato-depth", description="Asdasd")
    async def depth(self, inter: Interaction,depth:float = nextcord.SlashOption(default=1)) -> None:
        await self.player.depth(inter,depth,"Vibrato")
    @filters.subcommand(name="vibrato-frequency", description="Asdasd")
    async def frequency(self, inter: Interaction,frequency:float = nextcord.SlashOption(default=1)) -> None:
        await self.player.frequency(inter,frequency,"Vibrato")
        
        
    # LowPass
    @filters.subcommand(name="smoothing", description="Asdasd")
    async def smoothing(self, inter: Interaction,low:float = nextcord.SlashOption(min_value=1.1)) -> None:
        await self.player.smoothing(inter,low)
        
    # Rotation
    @filters.subcommand(name="rotation", description="Asdasd")
    async def rotationhz (self, inter: Interaction,rotation:float = nextcord.SlashOption(min_value=0)) -> None:
        await self.player.rotation(inter,rotation)
        
    # Clean
    @filters.subcommand(name="clean", description="Asdasd")
    async def clean(self, inter: Interaction,op: str = nextcord.SlashOption(
        name="picker",
        choices={"all": "all", 
                 "equalizer": "equalizer",
                 "timescale": "timescale",
                 "karaoke":"karaoke",
                 "tremolo":"tremolo",
                 "vibrato":"vibrato",
                 "smoothing":"smoothing",
                 "rotation":"rotation",
                 },
    )) -> None:
        await self.player.clean(inter,op)
    
    

    
def setup(bot: AutoShardedBot) -> None:
    bot.add_cog(music_commands(bot))