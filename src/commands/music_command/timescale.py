from nextcord import Interaction
from nextcord.ext.commands.context import Context
import nextcord,asyncio,lavalink

async def timescale(self,ctx,speed:float,pitch:float,rate:float):
        player:lavalink.models.DefaultPlayer = self.bot.lavalink.player_manager.get(ctx.guild.id)
        embed = nextcord.Embed(colour=0xdc4700)
        if player is None:
            embed.title =f'ให้ฉันเข้าก่อนสิ'
            await ctx.send(embed=embed)
            return
        if not await self.vote_(ctx):
            embed.title =f'ไม่เอิ้กๆ'
            await embed.send(embed=embed)
            return
        Timescale = lavalink.Timescale()
      
        embed.title =f'คุณได้ปรับระดับtimescaleแล้วจ้า'
        Timescale.update(speed=speed,pitch=pitch,rate=rate)
        asyncio.create_task(player.set_filter(Timescale))
            
        await ctx.send(embed=embed)