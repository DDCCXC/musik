from nextcord import Interaction
from nextcord.ext.commands.context import Context
import nextcord,asyncio,lavalink

async def equalizer_controller(self,ctx,gain:float):
        player:lavalink.models.DefaultPlayer = self.bot.lavalink.player_manager.get(ctx.guild.id)
        embed = nextcord.Embed(colour=0xdc4700,description=f'equaliz')
        equalizer = lavalink.Equalizer()
      
        embed.title =f'คุณได้ปรับระดับbassอยู่ที่{gain}Hz'
        equalizer.update(bands=[(x, float(gain)) for x in range(15)])
        asyncio.create_task(player.set_filter(equalizer))
            
        a=await ctx.send(embed=embed)