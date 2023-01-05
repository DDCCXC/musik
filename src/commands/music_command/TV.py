from nextcord import Interaction
from nextcord.ext.commands.context import Context
import nextcord,asyncio,lavalink

async def Vibrato(self,ctx,depth:float,frequency:float):
        
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
        Vibrato = lavalink.Vibrato()
      
        embed.title =f'คุณได้ปรับระดับtimescaleแล้วจ้า'
        Vibrato.update(depth=depth,frequency=frequency)
        asyncio.create_task(player.set_filter(Vibrato))
            
        await ctx.send(embed=embed)
        
async def depth_(self,ctx,depth:float,yp:str):
        
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
        if yp=="Vibrato":
            Vibrato = lavalink.Vibrato()
            embed.title =f'คุณได้ปรับระดับVibrato-depthแล้วจ้า'
        else:
            Vibrato = lavalink.Tremolo()
            embed.title =f'คุณได้ปรับระดับTremolo-depthแล้วจ้า'
        Vibrato.update(depth=depth)
        asyncio.create_task(player.set_filter(Vibrato))
            
        await ctx.send(embed=embed)
async def frequency_(self,ctx,frequency:float,yp:str):
        
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
        if yp=="Vibrato":
            Vibrato = lavalink.Vibrato()
            embed.title =f'คุณได้ปรับระดับVibrato-frequencyแล้วจ้า'
        else:
            Vibrato = lavalink.Tremolo()
            embed.title =f'คุณได้ปรับระดับTremolo-frequencyแล้วจ้า'
        Vibrato.update(frequency=frequency)
        asyncio.create_task(player.set_filter(Vibrato))
            
        await ctx.send(embed=embed)
        
async def Tremolo(self,ctx,depth:float,frequency:float):
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
        Tremolo = lavalink.Tremolo()
      
        embed.title =f'คุณได้ปรับระดับtimescaleแล้วจ้า'
        Tremolo.update(depth=depth,frequency=frequency)
        asyncio.create_task(player.set_filter(Tremolo))
            
        await ctx.send(embed=embed)