import nextcord
import lavalink
async def seek(self, ctx, seconds: int):
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)
        emed = nextcord.Embed(color=0xff470b)
        if not await self.check_join(ctx,player):return 
        if not player.is_playing:
                                emed.title = 'เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ'
                                return await ctx.send(embed=emed)
        track_time = player.position + (seconds * 1000)
        await player.seek(track_time)

      
        emed.title = f"⏩ ทำการขยับเพลงในเวลาไปที่ **{lavalink.utils.format_time(track_time)}"
        await ctx.send(embed=emed)