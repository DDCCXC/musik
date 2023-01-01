from nextcord import Interaction
from nextcord.ext.commands.context import Context
import nextcord,asyncio,lavalink

async def karaoke(self,ctx,level:float,monoLevel:float,filterBand:float,filterWidth:float):
        player:lavalink.models.DefaultPlayer = self.bot.lavalink.player_manager.get(ctx.guild.id)
        embed = nextcord.Embed(colour=0xdc4700)
        Timescale = lavalink.Karaoke()
        
        embed.title =f'คุณได้ปรับระดับKaraokeแล้วจ้า'
        Timescale.update(level=level,monoLevel=monoLevel,filterBand=filterBand,filterWidth=filterWidth)
        await player.set_filter(Timescale)
            
        await ctx.send(embed=embed)