from nextcord import Interaction
from nextcord.ext.commands.context import Context
import nextcord,asyncio,lavalink

async def smoothing(self,ctx,smoothing:float):
        player:lavalink.models.DefaultPlayer = self.bot.lavalink.player_manager.get(ctx.guild.id)
        embed = nextcord.Embed(colour=0xdc4700)
        if player is None:
            embed.title =f'ให้ฉันเข้าก่อนสิ'
            await ctx.send(embed=embed)
            return
        LowPass = lavalink.LowPass()
        embed.title =f'คุณได้ปรับระดับtimescaleแล้วจ้า'
        LowPass.update(rotation_hz=smoothing)
        await player.set_filter(LowPass)    
        await ctx.send(embed=embed)