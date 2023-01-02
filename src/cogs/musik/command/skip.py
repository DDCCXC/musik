import nextcord

async def skip(self, Inter):
    player = self.bot.lavalink.player_manager.get(Inter.guild.id)
    emed = nextcord.Embed(color=0xff470b)
    if player is None:
            emed.title =f'ให้ฉันเข้าก่อนสิ'
            await Inter.send(embed=emed)
            return
    if not player.is_playing:
        emed.title = 'เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ'
        return await Inter.send(embed=emed)
    emed.title = 'ข้ามให้แล้วน้า'
    await player.skip()
    await Inter.send(embed=emed)