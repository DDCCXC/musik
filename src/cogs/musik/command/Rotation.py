from nextcord import Interaction
from nextcord.ext.commands.context import Context
import nextcord,asyncio,lavalink

async def rotation(self,ctx,r:float):
        player:lavalink.models.DefaultPlayer = self.bot.lavalink.player_manager.get(ctx.guild.id)
        embed = nextcord.Embed(colour=0xdc4700)
        rotation = lavalink.Rotation()
        embed.title =f'คุณได้ปรับระดับtimescaleแล้วจ้า'
        rotation.update(rotation_hz=r)
        await player.set_filter(rotation)    
        await ctx.send(embed=embed)