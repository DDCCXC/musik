import nextcord
async def pause(self, ctx):
        """ Pauses/Resumes the current track. """
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)
        emed = nextcord.Embed(color=0xff470b)     
        if not await self.check_join(ctx,player):return 
        if not player.is_playing:
            emed.title = 'เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ'
            return await ctx.send(embed=emed)

        if player.paused:
            emed.title = 'เน้เล่นเพลงแล้วนะ'
            await player.set_pause(False)
            await ctx.send(embed=emed)
        else:
            emed.title = 'ปิดเพลงใหเแล้วน้า'
            await player.set_pause(True)
            await ctx.send(embed=emed)