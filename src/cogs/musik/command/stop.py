import nextcord
async def stop(self, ctx):
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)
        embed = nextcord.Embed(color=0xff470b)
        if not player.is_playing:
            #เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ
            return await ctx.send('> **เพลงไม่ได้ถูกเล่น กรุณลองใหม่อีกครั้ง**')

        player.queue.clear()
        await player.stop()
        embed.title=\
                              '⏹ หยุดเพลงแล้วค่ะ>_'
        await ctx.send(embed=embed)