from nextcord import Interaction
from nextcord.ext.commands.context import Context
import nextcord,asyncio,lavalink

async def rotation(self,ctx,r:float):
        player:lavalink.models.DefaultPlayer = self.bot.lavalink.player_manager.get(ctx.guild.id)
        embed = nextcord.Embed(colour=0xdc4700)
        if player is None:
            embed.title =f'ให้ฉันเข้าก่อนสิ'
            await ctx.send(embed=embed)
            return
        if not await self.vote_(ctx):
            embed.title =f'ไม่เอิ้กๆ'
            await embed.send(embed=embed)
        rotation = lavalink.Rotation()
        embed.title =f'คุณได้ปรับระดับtimescaleแล้วจ้า'
        rotation.update(rotation_hz=r)
        asyncio.create_task(player.set_filter(rotation))    
        await ctx.send(embed=embed)