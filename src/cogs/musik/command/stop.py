import nextcord
async def stop(self, ctx):
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)
        embed = nextcord.Embed(color=0xff470b)
        if player is None:
            embed.title =f'ให้ฉันเข้าก่อนสิ'
            await ctx.send(embed=embed)
            return
        if not player.is_playing:
            #เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ
            return await ctx.send('> **เพลงไม่ได้ถูกเล่น กรุณลองใหม่อีกครั้ง**')
        player.auto_play = False
        player.queue.clear()
        embed.title='⏹ หยุดเพลงแล้วค่ะ>_'
        await player.stop()
        await ctx.send(embed=embed)