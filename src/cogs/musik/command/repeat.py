import nextcord
# TODO repeat had update
async def repeat(self, Inter,type:int):
        player = self.bot.lavalink.player_manager.get(Inter.guild.id)
        emed = nextcord.Embed(color=0xff470b)
        if player is None:
            emed.title =f'ให้ฉันเข้าก่อนสิ'
            await Inter.send(embed=emed)
            return
        if not player.is_playing:
                                emed.title = 'เฮ้นายน่ะยังไม่ได้เปิดเพลงเลยนะ'
                                return await Inter.send(embed=emed)
        emed.title = '> **🔁 | ลูป :' + ('เปิดใช้งาน' if player.repeat else 'ปิดใช้งาาน') + '**'
        player.repeat = not player.repeat
        await Inter.send(embed=emed)