from nextcord import Interaction
from nextcord.ext.commands.context import Context
import nextcord,lavalink
async def clear(self, Inter:Interaction|Context,op: str):
        player:lavalink.models.DefaultPlayer = self.bot.lavalink.player_manager.get(Inter.guild.id)
        emed = nextcord.Embed(color=0xff470b)
        emed.title = 'clear แล้วจ้า'
        
        if op=="all":
            await player.clear_filters()
        elif op in player.filters: 
            await player.remove_filter(op)
        else :
            emed.title = 'คุณแม่งโม้วะ'
        
        await Inter.send(embed=emed)