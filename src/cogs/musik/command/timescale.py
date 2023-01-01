from nextcord import Interaction
from nextcord.ext.commands.context import Context
import nextcord,asyncio,lavalink

async def timescale(self,ctx,speed:float,pitch:float,rate:float):
        player:lavalink.models.DefaultPlayer = self.bot.lavalink.player_manager.get(ctx.guild.id)
        embed = nextcord.Embed(colour=0xdc4700)
        Timescale = lavalink.Timescale()
      
        embed.title =f'คุณได้ปรับระดับtimescaleแล้วจ้า'
        Timescale.update(speed=speed,pitch=pitch,rate=rate)
        await player.set_filter(Timescale)
            
        await ctx.send(embed=embed)