from nextcord import Interaction
from nextcord.ext.commands.context import Context
import nextcord,asyncio,lavalink

async def Vibrato(self,ctx,depth:float,frequency:float):
        player:lavalink.models.DefaultPlayer = self.bot.lavalink.player_manager.get(ctx.guild.id)
        embed = nextcord.Embed(colour=0xdc4700)
        Vibrato = lavalink.Vibrato()
      
        embed.title =f'คุณได้ปรับระดับtimescaleแล้วจ้า'
        Vibrato.update(depth=depth,frequency=frequency)
        await player.set_filter(Vibrato)
            
        await ctx.send(embed=embed)
        
async def Tremolo(self,ctx,depth:float,frequency:float):
        player:lavalink.models.DefaultPlayer = self.bot.lavalink.player_manager.get(ctx.guild.id)
        embed = nextcord.Embed(colour=0xdc4700)
        Tremolo = lavalink.Tremolo()
      
        embed.title =f'คุณได้ปรับระดับtimescaleแล้วจ้า'
        Tremolo.update(depth=depth,frequency=frequency)
        await player.set_filter(Tremolo)
            
        await ctx.send(embed=embed)