import nextcord,asyncio
async def stop(self, ctx):
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)
        embed = nextcord.Embed(color=0xff470b)
        if player is None:
            embed.title =f'ให้ฉันเข้าก่อนสิ'
            await ctx.send(embed=embed)
            return
        if not await self.vote_(ctx):
            embed.title =f'ไม่เอิ้กๆ'
            await embed.send(embed=embed)
            return
        if not player.is_playing:
            return await ctx.send('>เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ')
        player.auto_play = False
        player.queue.clear()
        embed.title='⏹ หยุดเพลงแล้วค่ะ>_'
        asyncio.create_task(player.stop())
        await ctx.send(embed=embed)