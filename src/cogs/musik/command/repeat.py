import nextcord
async def slash_repeat(self, Inter):
        player = self.bot.lavalink.player_manager.get(Inter.guild.id)
        emed = nextcord.Embed(color=0xff470b)
        if not player.is_playing:
                                emed.title = 'เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ'
                                return await Inter.send(embed=emed)
        emed.title = '> **🔁 | ลูป :' + ('เปิดใช้งาน' if player.repeat else 'ปิดใช้งาาน') + '**'
        
        
        player.repeat = not player.repeat
        await Inter.send(embed=emed)
async def prefix_repeat(self, ctx):
        player = self.bot.lavalink.player_manager.get(ctx.guild.id)
        emed = nextcord.Embed(color=0xff470b)
        if not player.is_playing:
                                emed.title = 'เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ'
                                return await ctx.send(embed=emed)
        emed.title = '> **🔁 | ลูป :' + ('เปิดใช้งาน' if player.repeat else 'ปิดใช้งาาน') + '**'
        
        
        player.repeat = not player.repeat
        await ctx.send(embed=emed)