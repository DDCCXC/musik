from nextcord import Interaction
from nextcord.ext.commands.context import Context
import nextcord,asyncio,lavalink
        
async def equalizer(self,ctx,bands:int|str,gain:float):
        player:lavalink.models.DefaultPlayer = self.bot.lavalink.player_manager.get(ctx.guild.id)
        
        equalizer = lavalink.Equalizer()
        embed = nextcord.Embed(colour=0xdc4700,description=f'equaliz')
        if player is None:
            embed.title =f'ให้ฉันเข้าก่อนสิ'
            await ctx.send(embed=embed)
            return
        if not player.is_playing:
                                embed.title = 'เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ'
                                return await ctx.send(embed=embed)
        
        if type(bands)==str:
                embed.title =f'คุณได้ปรับระดับequalizerอยู่ที่{gain}Hz'
                equalizer.update(bands=[(x, float(gain)) for x in range(15)])
        else:
                embed.title =f'คุณได้ปรับระดับequalizer bandที่{bands}เป็น{gain}Hz'
                equalizer.update(band=bands, gain=float(gain))  
        
        asyncio.create_task(player.set_filter(equalizer))
                
        await ctx.send(embed=embed)