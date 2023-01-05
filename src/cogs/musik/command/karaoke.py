from nextcord import Interaction
from nextcord.ext.commands.context import Context
import nextcord,asyncio,lavalink

async def karaoke(self,ctx,level:float,monoLevel:float,filterBand:float,filterWidth:float):
        player:lavalink.models.DefaultPlayer = self.bot.lavalink.player_manager.get(ctx.guild.id)
        embed = nextcord.Embed(colour=0xdc4700)
        if player is None:
            embed.title =f'ให้ฉันเข้าก่อนสิ'
            await ctx.send(embed=embed)
            return
        
        Timescale = lavalink.Karaoke()
        
        embed.title =f'คุณได้ปรับระดับKaraokeแล้วจ้า'
        Timescale.update(level=level,mono_level=monoLevel,filter_band=filterBand,filter_Width=filterWidth)
        await player.set_filter(Timescale)
            

async def custon_karaoke(self,ctx,type:str,level:float):
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
        embed = nextcord.Embed(colour=0xdc4700)
        Timescale = lavalink.Karaoke()
        
        embed.title =f'คุณได้ปรับระดับKaraoke-{type}แล้วจ้า'
        if type =="level":
                Timescale.update(level=level)
        elif type=="monolevel":
                Timescale.update(mono_level=level)
        elif type=="filterband":
                Timescale.update(filter_band=level)
        elif type=="filterwidth":
                Timescale.update(filter_Width=level)
        await player.set_filter(Timescale)
            
        await ctx.send(embed=embed)