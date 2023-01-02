import nextcord
async def shuffle(self, Inter):
       
        player = self.bot.lavalink.player_manager.get(Inter.guild.id)
        if not await self.check_join(Inter,player):return 
        emed = nextcord.Embed(color=0xff470b)
        if not player.is_playing:
                                emed.title = 'เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ'
                                return await Inter.send(embed=emed)
        emed.title = f'**🔀 | สุ่มเพลง :' + ('เปิดใช้งาน' if player.shuffle else 'ปิดใช้งาาน'+'**')
        player.shuffle = not player.shuffle
        await Inter.send(embed=emed)