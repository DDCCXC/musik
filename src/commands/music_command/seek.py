import nextcord
import lavalink,asyncio
async def seek(self, ctx, seconds: int):
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)
        emed = nextcord.Embed(color=0xff470b)
        
        if player is None:
            emed.title =f'ให้ฉันเข้าก่อนสิ'
            await ctx.send(embed=emed)
            return
        if await self.vote_(ctx):
            emed.title =f'ไม่เอิ้กๆ'
            await emed.send(embed=emed)
            return
        if not player.is_playing:
                                emed.title = 'เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ'
                                return await ctx.send(embed=emed)
        track_time = player.position + (seconds * 1000)
        asyncio.create_task(player.seek(track_time))

      
        emed.title = f"⏩ ทำการขยับเพลงในเวลาไปที่ **{lavalink.utils.format_time(track_time)}"
        await ctx.send(embed=emed)