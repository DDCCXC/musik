from nextcord import Interaction
from nextcord.ext.commands.context import Context
import nextcord,lavalink,asyncio
async def clear(self, Inter:Interaction|Context,op: str):
        player:lavalink.models.DefaultPlayer = self.bot.lavalink.player_manager.get(Inter.guild.id)
        embed = nextcord.Embed(color=0xff470b)
        if player is None:
            embed.title =f'ให้ฉันเข้าก่อนสิ'
            return await Inter.send(embed=embed)
        if await self.vote_(Inter):
            embed.title =f'ไม่เอิ้กๆ'
            await embed.send(embed=embed)
        embed.title = 'clear แล้วจ้า'
        if op=="all":
            asyncio.create_task(player.clear_filters())
        elif op in player.filters: 
            asyncio.create_task(player.remove_filter(op))
        else :
            embed.title = 'คุณแม่งโม้วะ'
        
        await Inter.send(embed=embed)