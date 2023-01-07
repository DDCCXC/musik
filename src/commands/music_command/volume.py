import nextcord,asyncio
async def volume(self, ctx, volume: int = None):
        """ Changes the player's volume (0-1000). """
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)
        embed = nextcord.Embed(color=0xff470b)
        if player is None:
            embed.title =f'ให้ฉันเข้าก่อนสิ'
            await ctx.send(embed=embed)
            return
        if await self.vote_(ctx):
            embed.title =f'ไม่เอิ้กๆ'
            await embed.send(embed=embed)
            return
        if not player.is_playing:
                                embed.title = 'เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ'
                                return await ctx.send(embed=embed)
        if volume == None:
            embed.title = f'> 🔈 | ความดังอยู่ในระดับ {player.volume}% คะ'
            return await ctx.send(embed=embed)
        asyncio.create_task(player.set_volume(volume))
        embed.title =f'> 🔈 | คุณได้ปรับระดับควมดังอยู่ที่ {volume}% ค๋ะ'
        await ctx.send(embed=embed)