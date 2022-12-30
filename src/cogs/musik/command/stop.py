import nextcord
async def prefix_stop(self, ctx):
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
        
async def slash_stop(self, Inter):
        player = self.bot.lavalink.player_manager.get(Inter.guild.id)
        embed = nextcord.Embed(color=0xff470b)
        if not player.is_playing:
            #เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ
            return await Inter.send('> **เพลงไม่ได้ถูกเล่น กรุณลองใหม่อีกครั้ง**')

        player.queue.clear()
        await player.stop()
        embed.title=\
                              '⏹ หยุดเพลงแล้วค่ะ>_'
        await Inter.send(embed=embed)